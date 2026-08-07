"""Tests for ai_core.main."""

from __future__ import annotations

import pytest

from ai_core.main import AppConfig, create_app, run


class TestAppConfig:
    """Tests for the AppConfig class."""

    def test_default_config(self) -> None:
        config = AppConfig()
        assert config.name == "ai-core"
        assert config.version == "0.1.0"
        assert config.debug is False

    def test_custom_config(self) -> None:
        config = AppConfig(name="custom-app", version="2.0.0", debug=True)
        assert config.name == "custom-app"
        assert config.version == "2.0.0"
        assert config.debug is True

    def test_repr(self) -> None:
        config = AppConfig(name="test", version="1.0.0")
        assert "name='test'" in repr(config)
        assert "version='1.0.0'" in repr(config)

    def test_strips_whitespace(self) -> None:
        config = AppConfig(name="  spaced  ", version="  1.0.0  ")
        assert config.name == "spaced"
        assert config.version == "1.0.0"

    def test_empty_name_raises(self) -> None:
        with pytest.raises(ValueError, match="name must not be empty"):
            AppConfig(name="")

    def test_whitespace_only_name_raises(self) -> None:
        with pytest.raises(ValueError, match="name must not be empty"):
            AppConfig(name="   ")

    def test_empty_version_raises(self) -> None:
        with pytest.raises(ValueError, match="version must not be empty"):
            AppConfig(version="")

    def test_whitespace_only_version_raises(self) -> None:
        with pytest.raises(ValueError, match="version must not be empty"):
            AppConfig(version="    ")

    def test_to_dict(self) -> None:
        config = AppConfig(name="test", version="1.0.0", debug=True)
        result = config.to_dict()
        assert result == {"name": "test", "version": "1.0.0", "debug": True}


class TestCreateApp:
    """Tests for the create_app function."""

    def test_create_default_app(self) -> None:
        config = create_app()
        assert isinstance(config, AppConfig)
        assert config.name == "ai-core"

    def test_create_app_with_config(self) -> None:
        custom = AppConfig(name="custom", version="3.0.0")
        config = create_app(custom)
        assert config is custom


class TestRun:
    """Tests for the run function."""

    def test_run_returns_ok_status(self) -> None:
        result = run()
        assert result["status"] == "ok"

    def test_run_returns_config_info(self) -> None:
        result = run()
        assert "config" in result
        assert result["config"]["name"] == "ai-core"
        assert result["config"]["version"] == "0.1.0"

    def test_run_with_custom_config(self) -> None:
        custom = AppConfig(name="custom-run", version="5.0.0", debug=True)
        result = run(custom)
        assert result["config"]["name"] == "custom-run"
        assert result["config"]["debug"] is True

    def test_run_uses_to_dict(self) -> None:
        """Ensure run() uses to_dict() for the config output."""
        custom = AppConfig(name="dict-test", version="9.9.9")
        result = run(custom)
        assert result["config"] == custom.to_dict()