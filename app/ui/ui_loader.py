"""Загрузка окон Qt Designer в рантайме и безопасный поиск виджетов."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional, Type, TypeVar

from PyQt5 import uic
from PyQt5.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget

logger = logging.getLogger(__name__)

UI_DIR = Path(__file__).resolve().parent / "designer"
ASSETS_DIR = Path(__file__).resolve().parent / "assets"
STYLES_PATH = Path(__file__).resolve().parent / "styles" / "app.qss"

_missing_widgets: set[tuple[int, str]] = set()

T = TypeVar("T", bound=QWidget)


def load_ui(name: str, base_widget: QWidget) -> bool:
    """Загружает `name`.ui в виджет. Если файла нет — рисует плейсхолдер.

    Возвращает True, если файл найден и загружен.
    """
    path = UI_DIR / f"{name}.ui"
    if path.is_file():
        uic.loadUi(str(path), base_widget)
        return True
    logger.warning("Файл интерфейса не найден: %s", path)
    if isinstance(base_widget, QMainWindow):
        holder = QWidget()
        _build_placeholder(holder, name)
        base_widget.setCentralWidget(holder)
    else:
        _build_placeholder(base_widget, name)
    return False


def _build_placeholder(base_widget: QWidget, name: str) -> None:
    layout = base_widget.layout()
    if layout is None:
        layout = QVBoxLayout(base_widget)
    label = QLabel(
        f"Заглушка: файл «{name}.ui» не найден в app/ui/designer/"
    )
    label.setWordWrap(True)
    label.setObjectName("lblPlaceholder")
    layout.addWidget(label)


def find(root: QWidget, widget_type: Type[T], object_name: str) -> Optional[T]:
    """Ищет дочерний виджет по objectName. Если нет — WARNING один раз и None."""
    widget = root.findChild(widget_type, object_name)
    if widget is None:
        key = (id(root), object_name)
        if key not in _missing_widgets:
            _missing_widgets.add(key)
            logger.warning(
                "Виджет objectName='%s' (%s) не найден",
                object_name,
                widget_type.__name__,
            )
    return widget


def connect_safe(widget: Optional[QWidget], signal_name: str, slot) -> None:
    """Подключает сигнал, только если виджет существует."""
    if widget is None:
        return
    signal = getattr(widget, signal_name, None)
    if signal is None:
        logger.warning("Нет сигнала %s у виджета %s", signal_name, widget.objectName())
        return
    signal.connect(slot)


def load_stylesheet(app) -> None:
    """Подключает app.qss, если файл не пустой."""
    if not STYLES_PATH.is_file():
        return
    text = STYLES_PATH.read_text(encoding="utf-8").strip()
    if text:
        app.setStyleSheet(text)


def asset_path(relative: str) -> Path:
    """Путь к ресурсу относительно app/ui/assets/."""
    return ASSETS_DIR / relative
