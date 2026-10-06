from __future__ import annotations

from functools import wraps
from typing import Any, Callable, TypeVar

from app.errors import PermissionDenied
from app.session import session

F = TypeVar("F", bound=Callable[..., Any])

SCOPE_RANK = {"own": 1, "region": 2, "all": 3}

# Матрица: действие → роль → область (own/region/all) или False
MATRIX: dict[str, dict[str, str | bool]] = {
    "self_register": {"athlete": True, "trainer": False, "admin": False},
    "create_trainer": {"athlete": False, "trainer": False, "admin": "all"},
    "manage_accounts": {"athlete": False, "trainer": False, "admin": "all"},
    "activate_minor": {"athlete": False, "trainer": "region", "admin": "all"},
    "edit_own_profile": {"athlete": "own", "trainer": "own", "admin": "all"},
    "view_athletes": {"athlete": False, "trainer": "region", "admin": "all"},
    "edit_athlete": {"athlete": "own", "trainer": "region", "admin": "all"},
    "deactivate_athlete": {"athlete": False, "trainer": False, "admin": "all"},
    "view_competitions": {"athlete": "region", "trainer": "region", "admin": "all"},
    "edit_competition": {"athlete": False, "trainer": "region", "admin": "all"},
    "delete_competition": {"athlete": False, "trainer": False, "admin": "all"},
    "edit_results": {"athlete": False, "trainer": "region", "admin": "all"},
    "delete_results": {"athlete": False, "trainer": "region", "admin": "all"},
    "view_own_results": {"athlete": "own", "trainer": False, "admin": False},
    "view_rating": {"athlete": "own", "trainer": "region", "admin": "all"},
    "view_statistics": {"athlete": "region", "trainer": "region", "admin": "all"},
    "manage_dictionaries": {"athlete": False, "trainer": False, "admin": "all"},
    "view_audit_log": {"athlete": False, "trainer": False, "admin": "all"},
}


def can(role: str, action: str, scope: str = "own") -> bool:
    """Проверяет, разрешено ли роли действие в запрошенной области."""
    allowed = MATRIX.get(action, {}).get(role, False)
    if allowed is False:
        return False
    if allowed is True:
        return True
    if scope not in SCOPE_RANK or allowed not in SCOPE_RANK:
        return False
    return SCOPE_RANK[str(allowed)] >= SCOPE_RANK[scope]


def require_permission(action: str, scope: str = "own") -> Callable[[F], F]:
    """Декоратор сервисного слоя: требует авторизацию и право."""

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            user = session.user
            if user is None:
                raise PermissionDenied("Необходима авторизация.")
            if not can(user.role, action, scope):
                raise PermissionDenied()
            return func(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorator
