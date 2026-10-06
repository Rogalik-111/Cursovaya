"""Создание схемы, сидов и первого администратора."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import bcrypt
import psycopg2
from psycopg2 import sql

from app.config import ROOT_DIR, get_settings
from app.logging_setup import setup_logging

logger = logging.getLogger(__name__)
SQL_DIR = Path(__file__).resolve().parent


def _connect(dbname: str | None = None):
    settings = get_settings()
    return psycopg2.connect(
        host=settings.db_host,
        port=settings.db_port,
        dbname=dbname or settings.db_name,
        user=settings.db_user,
        password=settings.db_password,
    )


def _apply_sql(conn, path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    with conn.cursor() as cur:
        cur.execute(text)


def _ensure_admin(conn) -> None:
    settings = get_settings()
    password_hash = bcrypt.hashpw(
        settings.first_admin_password.encode("utf-8"),
        bcrypt.gensalt(),
    ).decode("utf-8")
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO users (email, full_name, password_hash, role, status, must_change_password)
            VALUES (%s, %s, %s, 'admin', 'active', TRUE)
            ON CONFLICT (lower(email)) DO NOTHING
            """,
            (settings.first_admin_email.lower(), "Системный администратор", password_hash),
        )
        # ON CONFLICT по выражению lower(email) требует constraint. Используем индекс уникальности:
        # PostgreSQL unique index on expression isn't a named constraint for ON CONFLICT
        # unless created as constraint. Fallback: проверить наличие.


def _ensure_admin_safe(conn) -> None:
    settings = get_settings()
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id FROM users WHERE lower(email) = lower(%s)",
            (settings.first_admin_email,),
        )
        if cur.fetchone():
            logger.info("Администратор уже существует, пропуск.")
            return
        password_hash = bcrypt.hashpw(
            settings.first_admin_password.encode("utf-8"),
            bcrypt.gensalt(),
        ).decode("utf-8")
        cur.execute(
            """
            INSERT INTO users (email, full_name, password_hash, role, status, must_change_password)
            VALUES (%s, %s, %s, 'admin', 'active', TRUE)
            """,
            (settings.first_admin_email.lower(), "Системный администратор", password_hash),
        )
        logger.info("Создан первый администратор: %s", settings.first_admin_email)


def init_schema(reset: bool = False) -> None:
    settings = get_settings()
    if reset:
        logger.warning("Пересоздание базы %s", settings.db_name)
        admin_conn = _connect(dbname="postgres")
        admin_conn.autocommit = True
        with admin_conn.cursor() as cur:
            cur.execute(
                sql.SQL("DROP DATABASE IF EXISTS {}").format(
                    sql.Identifier(settings.db_name)
                )
            )
            cur.execute(
                sql.SQL("CREATE DATABASE {} OWNER {}").format(
                    sql.Identifier(settings.db_name),
                    sql.Identifier(settings.db_user),
                )
            )
        admin_conn.close()

    conn = _connect()
    try:
        _apply_sql(conn, SQL_DIR / "schema.sql")
        _apply_sql(conn, SQL_DIR / "seed.sql")
        _ensure_admin_safe(conn)
        conn.commit()
        logger.info("Инициализация БД завершена.")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def main(argv: list[str] | None = None) -> int:
    setup_logging()
    parser = argparse.ArgumentParser(description="Инициализация БД sportstat")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Удалить и создать БД заново (требует подтверждения)",
    )
    args = parser.parse_args(argv)
    if args.reset:
        answer = input("Это удалит все данные. Введите YES для подтверждения: ")
        if answer.strip() != "YES":
            print("Отменено.")
            return 1
    try:
        init_schema(reset=args.reset)
    except psycopg2.Error as exc:
        logger.exception("Ошибка PostgreSQL")
        print("Не удалось инициализировать БД. Проверьте .env и права пользователя.")
        print(str(exc))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
