from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CurrentUser:
    id: int
    email: str
    full_name: str
    role: str
    status: str
    region_id: int | None
    must_change_password: bool = False


class Session:
    def __init__(self) -> None:
        self._user: CurrentUser | None = None

    @property
    def user(self) -> CurrentUser | None:
        return self._user

    def set_user(self, user: CurrentUser | None) -> None:
        self._user = user

    def clear(self) -> None:
        self._user = None


session = Session()
