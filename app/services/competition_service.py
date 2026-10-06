"""Соревнования."""

from __future__ import annotations

from typing import Any

from app.permissions import require_permission
from app.services._demo_data import DEMO_COMPETITIONS


class CompetitionService:
    @require_permission("view_competitions", "region")
    def list_competitions(
        self,
        search: str | None = None,
        discipline_id: int | None = None,
        status: str | None = None,
    ) -> list[dict[str, Any]]:
        """Список соревнований.

        Права: view_competitions.
        # DEMO
        """
        rows = DEMO_COMPETITIONS
        if search:
            needle = search.lower()
            rows = [r for r in rows if needle in r["name"].lower()]
        if status:
            rows = [r for r in rows if r["status"] == status]
        return rows

    def get(self, competition_id: int) -> dict[str, Any]:
        """Карточка соревнования.

        # DEMO
        """
        for row in DEMO_COMPETITIONS:
            if row["id"] == competition_id:
                return row
        return DEMO_COMPETITIONS[0]

    @require_permission("edit_competition", "region")
    def save(self, data: dict[str, Any]) -> int:
        """Создаёт или обновляет соревнование своего региона.

        Права: edit_competition.
        """
        # TODO(stub): INSERT/UPDATE + критерии формата Б
        raise NotImplementedError("CompetitionService.save: заглушка")

    @require_permission("delete_competition", "all")
    def delete(self, competition_id: int) -> None:
        """Удаляет соревнование только без результатов.

        Права: delete_competition.
        """
        # TODO(stub): проверка results и DELETE
        raise NotImplementedError("CompetitionService.delete: заглушка")
