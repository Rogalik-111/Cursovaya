"""Репозиторий соревнований."""

from __future__ import annotations

from typing import Any, Optional


class CompetitionsRepo:
    def list_competitions(
        self,
        region_id: int | None,
        search: str | None = None,
        discipline_id: int | None = None,
        status: str | None = None,
    ) -> list[dict[str, Any]]:
        """Список соревнований с фильтрами.

        # TODO(stub): SELECT competitions
        """
        # TODO(stub): реализовать
        raise NotImplementedError("CompetitionsRepo.list_competitions: заглушка")

    def get(self, competition_id: int) -> Optional[dict[str, Any]]:
        """Одно соревнование по id.

        # TODO(stub): SELECT
        """
        # TODO(stub): реализовать
        raise NotImplementedError("CompetitionsRepo.get: заглушка")

    def insert(self, data: dict[str, Any]) -> int:
        """Создаёт соревнование.

        # TODO(stub): INSERT
        """
        # TODO(stub): реализовать
        raise NotImplementedError("CompetitionsRepo.insert: заглушка")

    def update(self, competition_id: int, data: dict[str, Any]) -> None:
        """Обновляет соревнование.

        # TODO(stub): UPDATE
        """
        # TODO(stub): реализовать
        raise NotImplementedError("CompetitionsRepo.update: заглушка")

    def delete(self, competition_id: int) -> None:
        """Удаляет соревнование без результатов.

        # TODO(stub): DELETE, проверка results
        """
        # TODO(stub): реализовать
        raise NotImplementedError("CompetitionsRepo.delete: заглушка")

    def list_criteria(self, competition_id: int) -> list[dict[str, Any]]:
        """Критерии формата Б.

        # TODO(stub): SELECT competition_criteria
        """
        # TODO(stub): реализовать
        raise NotImplementedError("CompetitionsRepo.list_criteria: заглушка")
