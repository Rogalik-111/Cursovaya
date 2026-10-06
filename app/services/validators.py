from __future__ import annotations

import re
from datetime import date, datetime

from app.errors import ValidationError

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$")
_NAME_RE = re.compile(r"^[A-Za-zА-Яа-яЁё][A-Za-zА-Яа-яЁё'\- ]{1,148}[A-Za-zА-Яа-яЁё]$")
_PHONE_RE = re.compile(r"^(?:\+7|8)\d{10}$")


def validate_email(value: str) -> str:
    """Проверяет адрес почты и возвращает его в нижнем регистре.

    Аргументы:
        value: строка email.
    Возвращает:
        нормализованный email.
    Исключения:
        ValidationError, если формат неверен.
    """
    email = (value or "").strip().lower()
    if not _EMAIL_RE.fullmatch(email):
        raise ValidationError("Некорректный адрес электронной почты", field="email")
    return email


def validate_password(password: str) -> None:
    """Проверяет пароль: не менее 8 символов, есть буква и цифра.

    Исключения:
        ValidationError.
    """
    if len(password or "") < 8 or not re.search(r"[A-Za-zА-Яа-яЁё]", password) or not re.search(r"\d", password):
        raise ValidationError(
            "Пароль должен содержать не менее 8 символов, включая букву и цифру",
            field="password",
        )


def validate_password_confirm(password: str, confirm: str) -> None:
    """Проверяет совпадение пароля и подтверждения."""
    if password != confirm:
        raise ValidationError("Пароли не совпадают", field="password_confirm")


def validate_full_name(value: str) -> str:
    """Проверяет ФИО: 2–3 слова, буквы, дефис, апостроф, пробел, 3–150 символов."""
    name = " ".join((value or "").split())
    parts = name.split(" ")
    if not (3 <= len(name) <= 150) or not (2 <= len(parts) <= 3) or not _NAME_RE.fullmatch(name):
        raise ValidationError(
            "Введите ФИО (например, Иванов Иван Иванович)",
            field="full_name",
        )
    return name


def validate_birth_date(value: date, today: date | None = None) -> date:
    """Проверяет дату рождения: возраст от 5 до 100 лет."""
    today = today or date.today()
    if not isinstance(value, date):
        raise ValidationError("Проверьте дату рождения", field="birth_date")
    try:
        years = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    except Exception as exc:  # noqa: BLE001
        raise ValidationError("Проверьте дату рождения", field="birth_date") from exc
    if years < 5 or years > 100:
        raise ValidationError("Проверьте дату рождения", field="birth_date")
    return value


def is_minor(birth_date: date, today: date | None = None) -> bool:
    """Возвращает True, если возраст меньше 18 лет."""
    today = today or date.today()
    years = today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )
    return years < 18


def validate_phone(value: str | None) -> str | None:
    """Проверяет телефон в формате +7XXXXXXXXXX или 8XXXXXXXXXX. Пустое значение допустимо."""
    if value is None or value.strip() == "":
        return None
    phone = value.strip()
    if not _PHONE_RE.fullmatch(phone):
        raise ValidationError("Некорректный номер телефона", field="phone")
    return phone


def validate_non_negative_number(value: float | int, field: str = "value") -> float:
    """Проверяет, что число неотрицательное."""
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValidationError("Введите неотрицательное число", field=field) from exc
    if number < 0:
        raise ValidationError("Значение не может быть отрицательным", field=field)
    return number


def parse_ui_date(value: str) -> date:
    """Разбирает дату из интерфейса в формате ДД.ММ.ГГГГ."""
    try:
        return datetime.strptime(value.strip(), "%d.%m.%Y").date()
    except ValueError as exc:
        raise ValidationError("Дата должна быть в формате ДД.ММ.ГГГГ", field="date") from exc
