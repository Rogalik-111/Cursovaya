from __future__ import annotations

from dataclasses import dataclass

from PyQt5.QtWidgets import QLabel, QPushButton, QStackedWidget

from app.session import session
from app.ui.controllers.admin_controller import AdminController
from app.ui.controllers.athlete_profile_controller import AthleteProfileController
from app.ui.controllers.athletes_controller import AthletesController
from app.ui.controllers.competitions_controller import CompetitionsController
from app.ui.controllers.home_controller import HomeController
from app.ui.controllers.results_controller import ResultsController
from app.ui.controllers.settings_controller import SettingsController
from app.ui.controllers.statistics_controller import StatisticsController
from app.ui.ui_loader import connect_safe, find


@dataclass(frozen=True)
class NavItem:
    key: str
    button_name: str
    title: str
    description: str
    hidden_for_roles: tuple[str, ...] = ()


NAV_ITEMS = (
    NavItem("home", "btnNavHome", "Главная", "Сводка по региону и последние соревнования"),
    NavItem(
        "athletes",
        "btnNavAthletes",
        "Спортсмены",
        "Список спортсменов региона",
        hidden_for_roles=("athlete",),
    ),
    NavItem("competitions", "btnNavCompetitions", "Соревнования", "Календарь и статусы соревнований"),
    NavItem("results", "btnNavResults", "Результаты", "Протоколы и показатели"),
    NavItem("statistics", "btnNavStatistics", "Статистика", "Рейтинг, динамика и сводки"),
    NavItem("settings", "btnNavSettings", "Настройки", "Пароль, профиль и параметры"),
    NavItem(
        "admin",
        "btnNavAdmin",
        "Администрирование",
        "Пользователи, справочники и журнал",
        hidden_for_roles=("athlete", "trainer"),
    ),
)


class Navigation:
    """Страницы в QStackedWidget и видимость кнопок по роли."""

    def __init__(self, main_window) -> None:
        self.main = main_window
        self.stack: QStackedWidget | None = find(main_window, QStackedWidget, "stackPages")
        if self.stack is None:
            self.stack = QStackedWidget(main_window)
            layout = main_window.layout()
            if layout is not None:
                layout.addWidget(self.stack)
        self.pages = {
            "home": HomeController(),
            "athletes": AthletesController(),
            "athlete_profile": AthleteProfileController(),
            "competitions": CompetitionsController(),
            "results": ResultsController(),
            "statistics": StatisticsController(),
            "settings": SettingsController(),
            "admin": AdminController(),
        }
        self._index: dict[str, int] = {}
        for key, page in self.pages.items():
            self._index[key] = self.stack.addWidget(page)
        self._bind_nav_buttons()
        self.apply_role_visibility()
        self.show_page("home")

    def _bind_nav_buttons(self) -> None:
        for item in NAV_ITEMS:
            btn = find(self.main, QPushButton, item.button_name)
            connect_safe(btn, "clicked", lambda _checked=False, k=item.key: self.show_page(k))

    def apply_role_visibility(self) -> None:
        role = session.user.role if session.user else "athlete"
        for item in NAV_ITEMS:
            btn = find(self.main, QPushButton, item.button_name)
            if btn is None:
                continue
            btn.setVisible(role not in item.hidden_for_roles)

    def show_page(self, key: str) -> None:
        if key not in self._index:
            return
        self.stack.setCurrentIndex(self._index[key])
        page = self.pages[key]
        item = next((i for i in NAV_ITEMS if i.key == key), None)
        lbl_title = find(self.main, QLabel, "lblSectionTitle")
        lbl_desc = find(self.main, QLabel, "lblSectionDescription")
        if item and lbl_title is not None:
            lbl_title.setText(item.title)
        if item and lbl_desc is not None:
            lbl_desc.setText(item.description)
        page.on_show()
