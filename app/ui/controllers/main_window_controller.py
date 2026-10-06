# main_window.ui
# objectName: btnNavHome, btnNavAthletes, btnNavCompetitions, btnNavResults,
# btnNavStatistics, btnNavSettings, btnNavAdmin, btnProfile, lblAppTitle,
# lblSectionTitle, lblSectionDescription, stackPages

from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, QStackedWidget, QVBoxLayout, QWidget

from app.ui.navigation import Navigation
from app.ui.ui_loader import connect_safe, find, load_ui


class MainWindowController(QMainWindow):
    UI_NAME = "main_window"

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Учёт статистики спортсменов")
        self.resize(1280, 720)
        self.ui_loaded = load_ui(self.UI_NAME, self)
        self._ensure_shell()
        self.navigation = Navigation(self)
        profile = find(self, QPushButton, "btnProfile")
        connect_safe(profile, "clicked", self.on_profile)

    def _ensure_shell(self) -> None:
        if find(self, QStackedWidget, "stackPages") is not None:
            return
        central = self.centralWidget()
        if central is None:
            central = QWidget()
            self.setCentralWidget(central)
        layout = central.layout()
        if layout is None:
            layout = QVBoxLayout(central)
        title = find(self, QLabel, "lblAppTitle")
        if title is None:
            title = QLabel("ИС учёта статистики спортсменов")
            title.setObjectName("lblAppTitle")
            layout.addWidget(title)
        stack = QStackedWidget()
        stack.setObjectName("stackPages")
        layout.addWidget(stack)

    def on_profile(self) -> None:
        from PyQt5.QtWidgets import QMessageBox

        QMessageBox.information(self, "Сообщение", "Функция «Личный профиль» ещё не реализована")
