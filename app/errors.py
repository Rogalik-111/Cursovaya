class AppError(Exception):
    """Базовая ошибка приложения с текстом для пользователя."""


class ValidationError(AppError):
    def __init__(self, message: str, field: str | None = None) -> None:
        super().__init__(message)
        self.field = field


class PermissionDenied(AppError):
    def __init__(self, message: str = "Недостаточно прав для этого действия.") -> None:
        super().__init__(message)


class NotFoundError(AppError):
    def __init__(self, message: str = "Запись не найдена.") -> None:
        super().__init__(message)
