# page_home.ui
# objectName: lblAthletesCount, tblRecentCompetitions, lblAbout, cmbYear

from PyQt5.QtWidgets import QComboBox, QLabel, QTableWidget

from app.services.statistics_service import StatisticsService
from app.ui.controllers.base_controller import BaseController
from app.ui.table_utils import fill_table


class HomeController(BaseController):
    UI_NAME = "page_home"

    def __init__(self, parent=None) -> None:
        self.stats = StatisticsService()
        super().__init__(parent)

    def bind_widgets(self) -> None:
        self.lbl_athletes_count = self._find(QLabel, "lblAthletesCount")
        self.tbl_recent = self._find(QTableWidget, "tblRecentCompetitions")
        self.lbl_about = self._find(QLabel, "lblAbout")
        self.cmb_year = self._find(QComboBox, "cmbYear")

    def on_show(self) -> None:
        try:
            data = self.stats.home_summary(2026)
        except Exception:
            return
        if self.lbl_athletes_count is not None:
            self.lbl_athletes_count.setText(str(data["athletes_count"]))
        if self.lbl_about is not None:
            self.lbl_about.setText(data["about"])
        fill_table(
            self.tbl_recent,
            ["Название", "Дата", "Город", "Статус"],
            [[c["name"], c["event_date"], c["city"], c["status"]] for c in data.get("recent", [])],
        )
