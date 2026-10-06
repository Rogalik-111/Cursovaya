"""Запись в журнал действий — рабочий код поверх AuditRepo."""

from __future__ import annotations

import logging
from typing import Any

from app.db.connection import transaction
from app.db.repositories.audit_repo import AuditRepo
from app.session import session

logger = logging.getLogger(__name__)


class AuditService:
    def __init__(self) -> None:
        self._repo = AuditRepo()

    def log(
        self,
        action: str,
        entity: str | None = None,
        entity_id: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        """Пишет событие в audit_log. При недоступной БД — только WARNING в лог, без падения."""
        user_id = session.user.id if session.user else None
        safe_details = dict(details or {})
        for key in list(safe_details):
            if "password" in key.lower() or "hash" in key.lower():
                safe_details.pop(key)
        try:
            with transaction() as conn:
                self._repo.add(conn, user_id, action, entity, entity_id, safe_details)
        except Exception:
            logger.warning("Не удалось записать audit_log action=%s", action)
