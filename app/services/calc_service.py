"""Формулы форматов А/Б/В/Г, нормированный балл, место и процентиль.

Все числовые константы штрафа берутся из calc_params (ключ penalty_minutes), не из кода.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Attempt:
    points: float
    penalty: float
    time_min: float | None = None


@dataclass(frozen=True)
class CriterionScore:
    weight: float
    avg_score: float
    max_value: float


class CalcService:
    def calc_format_a(self, solved: int, penalty_time: int, ioi_style: bool = False, score_sum: float = 0.0) -> float:
        """Формат А: Rᵢ = Z (число решённых задач).

        Штрафное время T = Σ(tₖ + penalty_minutes·fₖ) считается только по решённым задачам.
        При равенстве Rᵢ выше место у меньшего T.
        Для IOI-стиля Rᵢ = сумма баллов, T не применяется. Rₘₐₓ = число задач (или сумма max баллов).

        Аргументы:
            solved: Z.
            penalty_time: T в минутах (для тай-брейка, на Rᵢ не влияет).
            ioi_style: если True, вернуть score_sum.
            score_sum: сумма баллов IOI.
        Возвращает:
            Rᵢ.
        Исключения:
            ValidationError при отрицательных значениях.
        """
        # TODO(stub): реализовать
        raise NotImplementedError("calc_format_a: заглушка")

    def calc_format_b(self, scores: list[CriterionScore], penalty: float) -> float:
        """Формат Б: Rᵢ = max(0; 100·Σ wₖ·(cₖ/cₘₐₓ,ₖ) − P), Σwₖ=1, Rₘₐₓ=100.

        Ничья → больше оценка по критерию с наибольшим весом.

        Аргументы:
            scores: оценки критериев.
            penalty: P.
        Возвращает:
            Rᵢ.
        """
        # TODO(stub): реализовать
        raise NotImplementedError("calc_format_b: заглушка")

    def calc_format_v(self, attempts: list[Attempt]) -> float:
        """Формат В: Rₐ = max(0; Bₐ − Pₐ); Rᵢ = max Rₐ.

        Ничья → меньше время tₐ лучшей попытки.
        Rₘₐₓ = сумма максимальных баллов за задания.

        Аргументы:
            attempts: попытки.
        Возвращает:
            Rᵢ.
        """
        # TODO(stub): реализовать
        raise NotImplementedError("calc_format_v: заглушка")

    def calc_format_g(self, task_scores: list[float], penalty: float) -> float:
        """Формат Г: Rᵢ = max(0; Σ sₖ − P).

        Ничья → раньше принявший последнюю сдачу.
        Rₘₐₓ = сумма стоимостей задач.
        Компоненты атака/защита хранятся в details.

        Аргументы:
            task_scores: баллы за задания sₖ.
            penalty: P.
        Возвращает:
            Rᵢ.
        """
        # TODO(stub): реализовать
        raise NotImplementedError("calc_format_g: заглушка")

    def normalize(self, r_i: float, r_max: float) -> float:
        """Rₙ = 100·Rᵢ/Rₘₐₓ, диапазон 0..100, округление до 0,01.

        При Rₘₐₓ ≤ 0 — ValidationError.
        """
        # TODO(stub): реализовать
        raise NotImplementedError("normalize: заглушка")

    def assign_places(self, items: list[tuple[int, float]]) -> dict[int, int]:
        """Место m по убыванию Rᵢ; при полном равенстве места общие, следующее пропускается (1, 2, 2, 4).

        Аргументы:
            items: пары (id, Rᵢ).
        Возвращает:
            словарь id → место.
        """
        # TODO(stub): реализовать
        raise NotImplementedError("assign_places: заглушка")

    def percentile(self, place: int, n: int) -> float:
        """Pct = 100·(N−m)/(N−1); при N=1 равен 100.

        Аргументы:
            place: m.
            n: N.
        Возвращает:
            процентиль.
        """
        # TODO(stub): реализовать
        raise NotImplementedError("percentile: заглушка")
