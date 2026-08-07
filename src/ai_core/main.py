"""Main entry point for the AI Core application."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


class AppConfig:
    """Application configuration container.

    Attributes:
        name: Human-readable application name.
        version: Semantic version string.
        debug: Whether debug mode is enabled.

    Raises:
        ValueError: If name is empty or version is empty.
    """

    def __init__(
        self, name: str = "ai-core", version: str = "0.1.0", debug: bool = False
    ) -> None:
        if not name or not name.strip():
            raise ValueError("name must not be empty")
        if not version or not version.strip():
            raise ValueError("version must not be empty")
        self.name = name.strip()
        self.version = version.strip()
        self.debug = debug

    def __repr__(self) -> str:
        return f"AppConfig(name={self.name!r}, version={self.version!r}, debug={self.debug})"

    def to_dict(self) -> dict[str, Any]:
        """Return a dictionary representation of the config.

        Returns:
            A dictionary with keys ``name``, ``version``, and ``debug``.
        """
        return {"name": self.name, "version": self.version, "debug": self.debug}


def create_app(config: AppConfig | None = None) -> AppConfig:
    """Create and return an application config instance.

    Args:
        config: Optional pre-built config. If None, a default config is created.

    Returns:
        The resolved AppConfig instance.
    """
    if config is None:
        config = AppConfig()
    logger.info("Application initialised: %s v%s", config.name, config.version)
    return config


def run(config: AppConfig | None = None) -> dict[str, Any]:
    """Run the application and return a status dict.

    Args:
        config: Optional config override.

    Returns:
        A dictionary with keys ``status`` and ``config``.
    """
    cfg = create_app(config)
    return {
        "status": "ok",
        "config": cfg.to_dict(),
    }