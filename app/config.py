from pathlib import Path

from dotenv import load_dotenv
import os

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")


def _get(name: str, default: str | None = None) -> str:
    value = os.getenv(name, default)
    if value is None or value == "":
        raise RuntimeError(f"Не задана переменная окружения {name}")
    return value


class Settings:
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str
    first_admin_email: str
    first_admin_password: str
    log_level: str
    pool_min: int = 1
    pool_max: int = 8
    login_max_attempts: int = 5
    login_lock_minutes: int = 5
    consent_document_version: str = "pd-1.0"

    def __init__(self) -> None:
        self.db_host = os.getenv("DB_HOST", "localhost")
        self.db_port = int(os.getenv("DB_PORT", "5432"))
        self.db_name = os.getenv("DB_NAME", "sportstat")
        self.db_user = os.getenv("DB_USER", "sportstat_user")
        self.db_password = os.getenv("DB_PASSWORD", "change_me")
        self.first_admin_email = os.getenv("FIRST_ADMIN_EMAIL", "admin@example.test")
        self.first_admin_password = os.getenv("FIRST_ADMIN_PASSWORD", "ChangeMe123!")
        self.log_level = os.getenv("APP_LOG_LEVEL", "INFO")


def get_settings() -> Settings:
    return Settings()
