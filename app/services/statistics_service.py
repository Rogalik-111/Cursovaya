"""Сводки и данные для графиков."""

from __future__ import annotations

from typing import Any

from app.permissions import require_permission
from app.services._demo_data import DEMO_COMPETITIONS, DEMO_HOME, DEMO_RESULTS


class StatisticsService:
    @require_permission("view_statistics", "region")
    def home_summary(self, year: int) -> dict[str, Any]:
        """Сводка для главной: число спортсменов, последние соревнования.

        # DEMO
        """
        data = dict(DEMO_HOME)
        data["year"] = year
        data["recent"] = DEMO_COMPETITIONS[:5]
        return data

    @require_permission("view_statistics", "region")
    def competition_stats(self, competition_id: int) -> dict[str, Any]:
        """Сводка по соревнованию.

        # DEMO
        """
        _ = competition_id
        return {
            "participants": 6,
            "avg_rn": 78.4,
            "max_rn": 91.25,
            "winner": "Северный Артём Тестович",
        }

    @require_permission("view_statistics", "region")
    def dynamics(self, athlete_id: int, year: int) -> list[dict[str, Any]]:
        """Точки графика динамики спортсмена.

        # DEMO
        """
        _ = (athlete_id, year)
        return [
            {"date": "12.03.2026", "place": 1, "r_n": 91.25},
            {"date": "01.03.2026", "place": 3, "r_n": 76.00},
            {"date": "10.10.2025", "place": 4, "r_n": 65.00},
        ]
