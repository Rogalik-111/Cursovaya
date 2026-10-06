"""Репозиторий профилей спортсменов."""

from __future__ import annotations

from typing import Any, Optional


class AthletesRepo:
    def list_by_region(self, region_id: int | None, search: str | None = None) -> list[dict[str, Any]]:
        """Список спортсменов региона с поиском по ФИО.

        # TODO(stub): JOIN users, ranks, disciplines
        """
        # TODO(stub): реализовать
        raise NotImplementedError("AthletesRepo.list_by_region: заглушка")

    def get_profile(self, user_id: int) -> Optional[dict[str, Any]]:
        """Карточка спортсмена.

        # TODO(stub): SELECT athlete_profiles
        """
        # TODO(stub): реализовать
        raise NotImplementedError("AthletesRepo.get_profile: заглушка")

    def upsert_profile(self, user_id: int, data: dict[str, Any]) -> None:
        """Создаёт или обновляет профиль.

        # TODO(stub): INSERT/UPDATE athlete_profiles
        """
        # TODO(stub): реализовать
        raise NotImplementedError("AthletesRepo.upsert_profile: заглушка")

    def set_disciplines(self, user_id: int, discipline_ids: list[int]) -> None:
        """Заменяет набор дисциплин спортсмена.

        # TODO(stub): DELETE + INSERT athlete_disciplines
        """
        # TODO(stub): реализовать
        raise NotImplementedError("AthletesRepo.set_disciplines: заглушка")
