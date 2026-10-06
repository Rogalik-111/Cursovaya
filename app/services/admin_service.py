"""Администрирование пользователей и справочников."""

from __future__ import annotations

from typing import Any

from app.permissions import require_permission
from app.services._demo_data import DEMO_AUDIT, DEMO_USERS


class AdminService:
    @require_permission("manage_accounts", "all")
    def list_users(self, search: str | None = None) -> list[dict[str, Any]]:
        """Список учёток.

        # DEMO
        """
        rows = DEMO_USERS
        if search:
            needle = search.lower()
            rows = [r for r in rows if needle in r["full_name"].lower() or needle in r["email"]]
        return rows

    @require_permission("create_trainer", "all")
    def create_trainer(self, full_name: str, email: str, region_id: int, temp_password: str) -> int:
        """Создаёт тренера с временным паролем и must_change_password.

        Права: create_trainer.
        """
        # TODO(stub): INSERT user role=trainer
        raise NotImplementedError("AdminService.create_trainer: заглушка")

    @require_permission("manage_accounts", "all")
    def block_user(self, user_id: int) -> None:
        """Блокирует учётную запись."""
        # TODO(stub): status=blocked + audit
        raise NotImplementedError("AdminService.block_user: заглушка")

    @require_permission("manage_accounts", "all")
    def reset_password(self, user_id: int) -> str:
        """Сбрасывает пароль и возвращает временный (показать один раз)."""
        # TODO(stub): генерация + bcrypt + audit
        raise NotImplementedError("AdminService.reset_password: заглушка")

    @require_permission("manage_accounts", "all")
    def change_role(self, user_id: int, role: str) -> None:
        """Меняет роль."""
        # TODO(stub): UPDATE role + audit
        raise NotImplementedError("AdminService.change_role: заглушка")

    @require_permission("manage_dictionaries", "all")
    def list_dictionary(self, name: str) -> list[dict[str, Any]]:
        """Строки справочника."""
        # TODO(stub): dictionaries_repo
        raise NotImplementedError("AdminService.list_dictionary: заглушка")

    @require_permission("view_audit_log", "all")
    def list_audit(self) -> list[dict[str, Any]]:
        """Журнал. # DEMO, если БД недоступна."""
        return list(DEMO_AUDIT)
