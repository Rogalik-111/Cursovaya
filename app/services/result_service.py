"""Результаты соревнований."""

from __future__ import annotations

from typing import Any

from app.permissions import require_permission
from app.services._demo_data import DEMO_RESULTS


class ResultService:
    @require_permission("view_competitions", "region")
    def list_results(self, **filters: Any) -> list[dict[str, Any]]:
        """Список результатов.

        Права: view_competitions / view_own_results (сервис сузит выборку при реализации).
        # DEMO
        """
        return list(DEMO_RESULTS)

    @require_permission("edit_results", "region")
    def save_result(self, data: dict[str, Any]) -> int:
        """Сохраняет результат и связанные попытки/оценки в одной транзакции.

        Допущение 8: только для статуса finished.
        Права: edit_results.
        """
        # TODO(stub): calc_service + INSERT
        raise NotImplementedError("ResultService.save_result: заглушка")

    @require_permission("delete_results", "region")
    def delete_result(self, result_id: int) -> None:
        """Удаляет результат.

        Права: delete_results.
        """
        # TODO(stub): DELETE + пересчёт мест
        raise NotImplementedError("ResultService.delete_result: заглушка")
