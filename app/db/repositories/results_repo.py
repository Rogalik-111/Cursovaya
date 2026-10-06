"""Репозиторий результатов."""

from __future__ import annotations

from typing import Any, Optional


class ResultsRepo:
    def list_results(
        self,
        region_id: int | None,
        competition_id: int | None = None,
        athlete_id: int | None = None,
        year: int | None = None,
    ) -> list[dict[str, Any]]:
        """Список результатов с фильтрами.

        # TODO(stub): SELECT results JOIN competitions
        """
        # TODO(stub): реализовать
        raise NotImplementedError("ResultsRepo.list_results: заглушка")

    def get(self, result_id: int) -> Optional[dict[str, Any]]:
        """Один результат.

        # TODO(stub): SELECT
        """
        # TODO(stub): реализовать
        raise NotImplementedError("ResultsRepo.get: заглушка")

    def insert(self, data: dict[str, Any]) -> int:
        """Создаёт результат. Вызывать внутри транзакции вместе с попытками/оценками.

        # TODO(stub): INSERT results
        """
        # TODO(stub): реализовать
        raise NotImplementedError("ResultsRepo.insert: заглушка")

    def update(self, result_id: int, data: dict[str, Any]) -> None:
        """Обновляет результат.

        # TODO(stub): UPDATE
        """
        # TODO(stub): реализовать
        raise NotImplementedError("ResultsRepo.update: заглушка")

    def delete(self, result_id: int) -> None:
        """Удаляет результат и связанные попытки/оценки (CASCADE).

        # TODO(stub): DELETE
        """
        # TODO(stub): реализовать
        raise NotImplementedError("ResultsRepo.delete: заглушка")

    def update_places(self, competition_id: int, places: list[tuple[int, int, float]]) -> None:
        """Сохраняет место и процентиль пакетом.

        # TODO(stub): UPDATE place, percentile, r_n
        """
        # TODO(stub): реализовать
        raise NotImplementedError("ResultsRepo.update_places: заглушка")
