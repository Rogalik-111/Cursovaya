# login_window.ui
# objectName: edtEmail, edtPassword, btnLogin, lnkRegister, lblLogo, lblError

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton

from app.services.auth_service import AuthService
from app.ui.controllers.base_controller import BaseController, safe_slot


class LoginController(BaseController):
    UI_NAME = "login_window"
    logged_in = pyqtSignal()
    register_requested = pyqtSignal()

    def __init__(self, parent=None) -> None:
        self.auth = AuthService()
        super().__init__(parent)

    def bind_widgets(self) -> None:
        self.edt_email = self._find(QLineEdit, "edtEmail")
        self.edt_password = self._find(QLineEdit, "edtPassword")
        self.btn_login = self._find(QPushButton, "btnLogin")
        self.lnk_register = self._find(QPushButton, "lnkRegister")
        self.lbl_logo = self._find(QLabel, "lblLogo")
        self.lbl_error = self._find(QLabel, "lblError")
        if not self.ui_loaded:
            demo = QPushButton("Демо-вход (заглушка авторизации)", self)
            demo.setObjectName("btnLogin")
            self.btn_login = demo
            if self.layout() is not None:
                self.layout().addWidget(demo)
            to_reg = QPushButton("Регистрация", self)
            self.lnk_register = to_reg
            if self.layout() is not None:
                self.layout().addWidget(to_reg)

    def connect_signals(self) -> None:
        self._connect(self.btn_login, self.on_login)
        self._connect(self.lnk_register, self.on_register_link)

    @safe_slot
    def on_login(self) -> None:
        """Вход. Пока сервис-заглушка: открывает главное окно как admin."""
        self.auth.verify_and_set_session_demo()
        self.logged_in.emit()

    @safe_slot
    def on_register_link(self) -> None:
        self.register_requested.emit()
