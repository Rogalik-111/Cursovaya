"""Самостоятельная регистрация спортсмена."""

from __future__ import annotations

from datetime import date

from app.errors import AppError
from app.permissions import require_permission
from app.services.validators import (
    is_minor,
    validate_birth_date,
    validate_email,
    validate_full_name,
    validate_password,
    validate_password_confirm,
)


class RegistrationService:
    def register(
        self,
        full_name: str,
        email: str,
        birth_date: date,
        password: str,
        password_confirm: str,
        region_id: int,
        consent: bool,
    ) -> int:
        """Создаёт учётную запись с ролью athlete.

        Аргументы:
            full_name, email, birth_date, password, password_confirm, region_id, consent.
        Возвращает:
            id пользователя.
        Исключения:
            ValidationError, AppError (нет согласия, занятый email).
        Права:
            self_register (роль ещё не задана — проверка после создания не применяется;
            метод доступен без сессии).
        Если возраст < 18, статус pending до activate_minor.
        """
        validate_full_name(full_name)
        validate_email(email)
        validate_birth_date(birth_date)
        validate_password(password)
        validate_password_confirm(password, password_confirm)
        if not consent:
            raise AppError("Без согласия регистрация невозможна")
        _ = is_minor(birth_date)
        _ = region_id
        # TODO(stub): INSERT users + athlete_profiles + consents в одной транзакции
        raise NotImplementedError("RegistrationService.register: заглушка")
