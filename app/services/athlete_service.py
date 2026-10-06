"""Спортсмены: списки, карточка, деактивация."""

from __future__ import annotations

from typing import Any

from app.permissions import require_permission
from app.services._demo_data import DEMO_ATHLETES


class AthleteService:
    @require_permission("view_athletes", "region")
    def list_athletes(
        self,
        search: str | None = None,
        discipline_id: int | None = None,
        rank_id: int | None = None,
    ) -> list[dict[str, Any]]:
        """Возвращает список спортсменов для таблицы.

        Права: view_athletes.
        # DEMO — пока без БД.
        """
        # DEMO
        rows = DEMO_ATHLETES
        if search:
            needle = search.lower()
            rows = [r for r in rows if needle in r["full_name"].lower() or needle in str(r["id"])]
        return rows

    def get_profile(self, user_id: int) -> dict[str, Any]:
        """Карточка спортсмена.

        Права: view_athletes или own.
        # TODO(stub): репозиторий профиля
        """
        # DEMO
        for row in DEMO_ATHLETES:
            if row["id"] == user_id:
                return row
        return DEMO_ATHLETES[0]

    @require_permission("edit_athlete", "region")
    def save_athlete(self, data: dict[str, Any]) -> int:
        """Создаёт или обновляет спортсмена.

        Права: edit_athlete.
        """
        # TODO(stub): валидация + репозиторий
        raise NotImplementedError("AthleteService.save_athlete: заглушка")

    @require_permission("deactivate_athlete", "all")
    def deactivate(self, user_id: int) -> None:
        """Мягкая блокировка: status=blocked, результаты сохраняются.

        Права: deactivate_athlete.
        """
        # TODO(stub): update status
        raise NotImplementedError("AthleteService.deactivate: заглушка")

    @require_permission("activate_minor", "region")
    def confirm_minor(self, user_id: int) -> None:
        """Подтверждение согласия родителя и активация несовершеннолетнего.

        Права: activate_minor.
        """
        # TODO(stub): consents + status active
        raise NotImplementedError("AthleteService.confirm_minor: заглушка")
