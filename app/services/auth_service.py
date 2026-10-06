"""Аутентификация (вход, выход, блокировка попыток)."""

from __future__ import annotations

from app.errors import AppError
from app.permissions import require_permission
from app.session import CurrentUser, session
from app.services.validators import validate_email, validate_password


class AuthService:
    def login(self, email: str, password: str) -> CurrentUser:
        """Вход по email и паролю.

        Аргументы:
            email: почта.
            password: пароль в открытом виде (не логируется).
        Возвращает:
            CurrentUser при успехе.
        Исключения:
            ValidationError, AppError («Неверный логин или пароль» или блокировка).
        Права:
            не требуются.
        После 5 неудач — блокировка на 5 минут (допущение 9).
        """
        validate_email(email)
        if not password:
            raise AppError("Неверный логин или пароль.")
        # TODO(stub): bcrypt.checkpw, счётчик попыток, audit LOGIN
        raise NotImplementedError("AuthService.login: заглушка")

    def logout(self) -> None:
        """Очищает текущую сессию.

        Права: авторизованный пользователь.
        """
        # TODO(stub): audit LOGOUT
        session.clear()

    def change_password(self, old_password: str, new_password: str, confirm: str) -> None:
        """Смена пароля текущего пользователя.

        Права: edit_own_profile.
        """
        validate_password(new_password)
        # TODO(stub): проверить старый пароль, записать bcrypt-хеш
        raise NotImplementedError("AuthService.change_password: заглушка")

    def verify_and_set_session_demo(self) -> CurrentUser:
        """DEMO: открывает сессию администратора без проверки пароля.

        Нужно, чтобы каркас UI работал до реализации входа.
        """
        user = CurrentUser(
            id=1,
            email="admin@example.test",
            full_name="Системный администратор",
            role="admin",
            status="active",
            region_id=1,
            must_change_password=False,
        )
        session.set_user(user)
        return user
