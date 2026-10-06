# register_window.ui
# objectName: edtFullName, edtEmail, dteBirthDate, edtPassword, edtPasswordConfirm,
# cmbRegion, chkConsent, lnkConsentText, btnRegister, lnkLogin, lblLogo, lblError

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QCheckBox, QComboBox, QDateEdit, QLabel, QLineEdit, QPushButton

from app.ui.controllers.base_controller import BaseController, safe_slot


class RegisterController(BaseController):
    UI_NAME = "register_window"
    login_requested = pyqtSignal()
    registered = pyqtSignal()

    def bind_widgets(self) -> None:
        self.edt_full_name = self._find(QLineEdit, "edtFullName")
        self.edt_email = self._find(QLineEdit, "edtEmail")
        self.dte_birth = self._find(QDateEdit, "dteBirthDate")
        self.edt_password = self._find(QLineEdit, "edtPassword")
        self.edt_password_confirm = self._find(QLineEdit, "edtPasswordConfirm")
        self.cmb_region = self._find(QComboBox, "cmbRegion")
        self.chk_consent = self._find(QCheckBox, "chkConsent")
        self.lnk_consent = self._find(QPushButton, "lnkConsentText")
        self.btn_register = self._find(QPushButton, "btnRegister")
        self.lnk_login = self._find(QPushButton, "lnkLogin")
        self.lbl_logo = self._find(QLabel, "lblLogo")
        self.lbl_error = self._find(QLabel, "lblError")
        if not self.ui_loaded:
            back = QPushButton("Назад ко входу", self)
            self.lnk_login = back
            if self.layout() is not None:
                self.layout().addWidget(back)

    def connect_signals(self) -> None:
        self._connect(self.btn_register, self.on_register)
        self._connect(self.lnk_login, self.on_login_link)
        self._connect(self.lnk_consent, self.on_consent_text)

    @safe_slot
    def on_register(self) -> None:
        self.show_info("Функция «Регистрация» ещё не реализована")

    @safe_slot
    def on_login_link(self) -> None:
        self.login_requested.emit()

    @safe_slot
    def on_consent_text(self) -> None:
        self.show_info("Текст согласия на обработку персональных данных будет добавлен в следующей версии.")
