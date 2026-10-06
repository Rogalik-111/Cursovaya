"""Рейтинг: среднее Rₙ за год."""

from __future__ import annotations

from typing import Any

from app.permissions import require_permission
from app.services._demo_data import DEMO_RATING


class RatingService:
    @require_permission("view_rating", "own")
    def build_rating(
        self,
        year: int,
        discipline_id: int | None,
        region_scope: str,
    ) -> list[dict[str, Any]]:
        """Строит рейтинг.

        Рейтинг = среднее Rₙ по результатам за год (дисциплина или все).
        Места по убыванию среднего, ничьи как в calc_service.assign_places.

        Аргументы:
            year: календарный год.
            discipline_id: фильтр или None.
            region_scope: own / region / all.
        Права:
            view_rating.
        # DEMO
        """
        _ = (year, discipline_id, region_scope)
        return list(DEMO_RATING)
