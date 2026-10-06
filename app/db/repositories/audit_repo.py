"""Журнал действий. Запись в БД реализована."""

from __future__ import annotations

import json
from typing import Any

from psycopg2.extensions import connection as PgConnection


class AuditRepo:
    def add(
        self,
        conn: PgConnection,
        user_id: int | None,
        action: str,
        entity: str | None,
        entity_id: str | None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Пишет строку в audit_log. Не логирует пароли.

        Аргументы:
            conn: соединение в открытой транзакции.
            user_id: кто выполнил действие.
            action: код (LOGIN, CREATE_TRAINER, ...).
            entity: имя сущности.
            entity_id: идентификатор.
            details: JSON без секретов.
        """
        payload = json.dumps(details or {}, ensure_ascii=False)
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO audit_log (user_id, action, entity, entity_id, details)
                VALUES (%s, %s, %s, %s, %s::jsonb)
                """,
                (user_id, action, entity, entity_id, payload),
            )

    def list_recent(self, conn: PgConnection, limit: int = 100) -> list[dict[str, Any]]:
        """Последние записи журнала для админа.

        # TODO(stub): выборка для UI пока может использовать демо при отсутствии БД
        """
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, user_id, action, entity, entity_id, details, created_at
                FROM audit_log
                ORDER BY created_at DESC
                LIMIT %s
                """,
                (limit,),
            )
            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in cur.fetchall()]
