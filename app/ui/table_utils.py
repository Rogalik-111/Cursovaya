"""Заполнение таблиц демо-данными."""

from __future__ import annotations

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


def fill_table(table: QTableWidget | None, headers: list[str], rows: list[list[object]]) -> None:
    if table is None:
        return
    table.clear()
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)
    table.setRowCount(len(rows))
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            table.setItem(i, j, QTableWidgetItem(str(value)))
