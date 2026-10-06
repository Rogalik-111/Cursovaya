"""Базовый контроллер окон и страниц.

Ожидаемые атрибуты наследника: UI_NAME — имя .ui без расширения.
"""

from __future__ import annotations

import functools
import logging
from typing import Callable, TypeVar

from PyQt5.QtWidgets import QMessageBox, QWidget

from app.errors import AppError
from app.ui.ui_loader import connect_safe, find, load_ui

logger = logging.getLogger(__name__)
F = TypeVar("F", bound=Callable)


def safe_slot(method: F) -> F:
    """Ловит AppError (сообщение пользователю) и прочие исключения (лог + общее сообщение)."""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except AppError as exc:
            self.show_error(str(exc))
        except Exception:
            logger.exception("Необработанная ошибка в обработчике %s", method.__name__)
            self.show_error("Произошла ошибка. Действие отменено.")

    return wrapper  # type: ignore[return-value]


class BaseController(QWidget):
    UI_NAME: str = ""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.ui_loaded = load_ui(self.UI_NAME, self)
        self.bind_widgets()
        self.connect_signals()

    def bind_widgets(self) -> None:
        """Сохраняет ссылки на виджеты из .ui. Не падает, если виджет отсутствует."""

    def connect_signals(self) -> None:
        """Подключает сигналы через connect_safe."""

    def on_show(self) -> None:
        """Вызывается при показе страницы — перезагрузка данных."""

    def show_error(self, msg: str) -> None:
        QMessageBox.critical(self, "Ошибка", msg)

    def show_info(self, msg: str) -> None:
        QMessageBox.information(self, "Сообщение", msg)

    def _find(self, widget_type, object_name: str):
        return find(self, widget_type, object_name)

    def _connect(self, widget, slot, signal_name: str = "clicked") -> None:
        connect_safe(widget, signal_name, slot)
