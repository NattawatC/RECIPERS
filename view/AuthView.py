import sys

from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication, QHBoxLayout, QStackedWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect, Signal, QEvent, Qt
from controller.AuthController import AuthController
from static.theme import Theme


class AuthView(QWidget):
    def __init__(self, parent):

        QWidget.__init__(self)

        self.AuthController = AuthController(self)
        self.mainWindow = parent

        self.setFixedSize(1280, 720)
        self.setObjectName("auth_view")

        self.errorLabel = QLabel(self)
        self.errorLabel.setObjectName("error_label")
        self.errorLabel.setGeometry(QRect(59, 450, 520, 50))
        self.errorLabel.setFont(Theme.CHILLAX_REGULAR_20)
        self.errorLabel.setStyleSheet("color: #FF0000")

        label_logo = QLabel(self)
        label_logo.setObjectName("default_label")
        label_logo.setGeometry(QRect(23, 19, 181, 41))
        label_logo.setPixmap(QPixmap("static/asset/img/logo.png"))
        label_logo.setScaledContents(True)

        text_lable1 = QLabel("First thing, first!", self)
        text_lable1.setObjectName("default_label")
        text_lable1.setFont(Theme.CHILLAX_REGULAR_36)
        text_lable1.setGeometry(QRect(181, 113, 275, 48))

        label_username = QLabel("Username", self)
        label_username.setObjectName("default_label")
        label_username.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        label_username.setGeometry(QRect(59, 211, 171, 31))

        self.lineEdit_username = QLineEdit(self)
        self.lineEdit_username.setObjectName("logIn_bar")
        self.lineEdit_username.setPlaceholderText("Enter your name")
        self.lineEdit_username.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_username.setGeometry(QRect(59, 256, 520, 50))
        self.lineEdit_username.installEventFilter(self)

        label_password = QLabel("Password", self)
        label_password.setObjectName("default_label")
        label_password.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        label_password.setGeometry(QRect(59, 354, 171, 31))

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setObjectName("logIn_bar")
        self.lineEdit_password.setPlaceholderText("**********")
        self.lineEdit_password.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.installEventFilter(self)

        self.lineEdit_password.setGeometry(QRect(59, 399, 520, 50))

        pic_login = QLabel(self)
        pic_login.setGeometry(QRect(642, 0, 649, 720))
        pic_login.setPixmap(QPixmap("static/asset/img/login_pic.png"))
        pic_login.setScaledContents(True)

        text_label2 = QLabel("Let's create your Masterpiece!", self)
        text_label2.setObjectName("default_label")
        text_label2.setFont(Theme.CHILLAX_REGULAR_16)
        text_label2.setGeometry(QRect(201, 492, 231, 20))

        self.login_button = QPushButton("Ready", self)
        self.login_button.setObjectName("logIn_button")
        self.login_button.setFont(Theme.CHILLAX_REGULAR_20)
        self.login_button.setGeometry(QRect(59, 557, 520, 50))
        self.login_button.setDefault(True)
        self.login_button.setAutoDefault(True)



    def eventFilter(self, obj, event):
        if obj == self.lineEdit_username and event.type() == QEvent.FocusIn:
            self.lineEdit_username.setStyleSheet("border: 2px solid gray;")

        elif obj == self.lineEdit_password and event.type() == QEvent.FocusIn:
            self.lineEdit_password.setStyleSheet("border: 2px solid gray;")

        if obj == self.lineEdit_username and event.type() == QEvent.FocusOut:
            self.lineEdit_username.setStyleSheet(Theme.get_stylesheet())

        elif obj == self.lineEdit_password and event.type() == QEvent.FocusOut:
            self.lineEdit_password.setStyleSheet(Theme.get_stylesheet())
            
        if obj == self.lineEdit_username and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.lineEdit_password.setFocus()
                return True

        elif obj == self.lineEdit_password and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.login_button.click()
                return True
        return super().eventFilter(obj, event)


    def get_username(self) -> str:
        return self.lineEdit_username.text()

    def get_password(self) -> str:
        return self.lineEdit_password.text()

    def handleUserLogout(self) -> None:
        self.AuthController.handleLogout()

    def showError(self, message: str) -> None:
        self.errorLabel.setText(message)
        self.errorLabel.show()

    def reset(self) -> None:
        self.errorLabel.hide()
        self.lineEdit_username.clear()
        self.lineEdit_password.clear()
        self.lineEdit_username.setFocus()


