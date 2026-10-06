"""Репозиторий пользователей.

Заглушки CRUD. Исключения: NotFoundError. SQL не вызывается, кроме будущей реализации.
"""

from __future__ import annotations

from typing import Any, Optional


class UsersRepo:
    def get_by_email(self, email: str) -> Optional[dict[str, Any]]:
        """Находит пользователя по email (без учёта регистра).

        Возвращает словарь без password_hash-отображения наружу после реализации.
        # TODO(stub): SELECT по lower(email)
        """
        # TODO(stub): реализовать выборку пользователя
        raise NotImplementedError("UsersRepo.get_by_email: заглушка")

    def get_by_id(self, user_id: int) -> Optional[dict[str, Any]]:
        """Возвращает пользователя по id.

        # TODO(stub): SELECT * FROM users WHERE id = %s
        """
        # TODO(stub): реализовать
        raise NotImplementedError("UsersRepo.get_by_id: заглушка")

    def insert(self, data: dict[str, Any]) -> int:
        """Создаёт пользователя. Возвращает id.

        Права: self_register / create_trainer / manage_accounts — на уровне сервиса.
        # TODO(stub): INSERT INTO users
        """
        # TODO(stub): реализовать
        raise NotImplementedError("UsersRepo.insert: заглушка")

    def update_status(self, user_id: int, status: str) -> None:
        """Меняет статус (active/pending/blocked).

        # TODO(stub): UPDATE users SET status
        """
        # TODO(stub): реализовать
        raise NotImplementedError("UsersRepo.update_status: заглушка")

    def update_role(self, user_id: int, role: str) -> None:
        """Меняет роль пользователя.

        # TODO(stub): UPDATE users SET role
        """
        # TODO(stub): реализовать
        raise NotImplementedError("UsersRepo.update_role: заглушка")

    def update_password(self, user_id: int, password_hash: str) -> None:
        """Сохраняет bcrypt-хеш пароля.

        # TODO(stub): UPDATE users SET password_hash, must_change_password
        """
        # TODO(stub): реализовать
        raise NotImplementedError("UsersRepo.update_password: заглушка")

    def list_users(self, role: str | None = None, status: str | None = None, search: str | None = None) -> list[dict[str, Any]]:
        """Список пользователей с фильтрами.

        # TODO(stub): SELECT с WHERE
        """
        # TODO(stub): реализовать
        raise NotImplementedError("UsersRepo.list_users: заглушка")
