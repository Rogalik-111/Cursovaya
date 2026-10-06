"""Репозиторий справочников."""

from __future__ import annotations

from typing import Any


class DictionariesRepo:
    def list_regions(self) -> list[dict[str, Any]]:
        """Список регионов.

        # TODO(stub): SELECT regions
        """
        # TODO(stub): реализовать
        raise NotImplementedError("DictionariesRepo.list_regions: заглушка")

    def list_disciplines(self) -> list[dict[str, Any]]:
        """Список дисциплин и форматов расчёта.

        # TODO(stub): SELECT disciplines
        """
        # TODO(stub): реализовать
        raise NotImplementedError("DictionariesRepo.list_disciplines: заглушка")

    def list_ranks(self) -> list[dict[str, Any]]:
        """Список разрядов.

        # TODO(stub): SELECT ranks ORDER BY sort_order
        """
        # TODO(stub): реализовать
        raise NotImplementedError("DictionariesRepo.list_ranks: заглушка")

    def get_calc_param(self, key: str) -> float:
        """Числовой параметр расчёта (например penalty_minutes).

        # TODO(stub): SELECT value FROM calc_params
        """
        # TODO(stub): реализовать
        raise NotImplementedError("DictionariesRepo.get_calc_param: заглушка")

    def upsert_dictionary_row(self, table: str, data: dict[str, Any]) -> int:
        """Добавляет или меняет строку справочника (только белый список таблиц).

        Права: manage_dictionaries.
        # TODO(stub): INSERT/UPDATE
        """
        # TODO(stub): реализовать
        raise NotImplementedError("DictionariesRepo.upsert_dictionary_row: заглушка")
