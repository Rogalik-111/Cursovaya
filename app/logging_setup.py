from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.config import ROOT_DIR, get_settings

LOG_DIR = ROOT_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"
_PASSWORD_KEYS = ("password", "password_hash", "passwd", "secret")


class _RedactFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        lowered = message.lower()
        if any(key in lowered for key in _PASSWORD_KEYS):
            record.msg = "[сообщение скрыто: содержит чувствительные данные]"
            record.args = ()
        return True


def setup_logging() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    settings = get_settings()
    level = getattr(logging, settings.log_level.upper(), logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=1_000_000, backupCount=5, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    root = logging.getLogger()
    root.setLevel(level)
    root.handlers.clear()
    root.addHandler(file_handler)
    root.addHandler(console)
    root.addFilter(_RedactFilter())
