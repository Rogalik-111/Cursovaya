from __future__ import annotations

import logging
from contextlib import contextmanager
from typing import Iterator

import psycopg2
from psycopg2.extensions import connection as PgConnection
from psycopg2.pool import ThreadedConnectionPool

from app.config import get_settings
from app.errors import AppError

logger = logging.getLogger(__name__)

_pool: ThreadedConnectionPool | None = None


def init_pool() -> ThreadedConnectionPool:
    global _pool
    if _pool is not None:
        return _pool
    settings = get_settings()
    try:
        _pool = ThreadedConnectionPool(
            minconn=settings.pool_min,
            maxconn=settings.pool_max,
            host=settings.db_host,
            port=settings.db_port,
            dbname=settings.db_name,
            user=settings.db_user,
            password=settings.db_password,
        )
    except psycopg2.Error as exc:
        raise AppError(
            "Не удалось подключиться к базе данных. "
            "Проверьте хост, порт, имя БД, пользователя и пароль в файле .env."
        ) from exc
    return _pool


def close_pool() -> None:
    global _pool
    if _pool is not None:
        _pool.closeall()
        _pool = None


def check_connection() -> bool:
    """Проверяет, что PostgreSQL доступен. Возвращает True при успехе."""
    conn = None
    try:
        pool = init_pool()
        conn = pool.getconn()
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            cur.fetchone()
        return True
    except Exception as exc:  # noqa: BLE001 — сообщение для пользователя
        logger.warning("Проверка подключения не удалась: %s", type(exc).__name__)
        return False
    finally:
        if conn is not None and _pool is not None:
            _pool.putconn(conn)


@contextmanager
def get_connection() -> Iterator[PgConnection]:
    pool = init_pool()
    conn = pool.getconn()
    try:
        yield conn
    finally:
        pool.putconn(conn)


@contextmanager
def transaction() -> Iterator[PgConnection]:
    """Транзакция: commit при успехе, rollback при ошибке."""
    with get_connection() as conn:
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
