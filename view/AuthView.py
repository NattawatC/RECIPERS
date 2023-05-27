from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication, QHBoxLayout, QStackedWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect, QEvent, Qt
from static.theme import Theme


class AuthView(QWidget):
    def __init__(self, Controller = None):
        super().__init__()

        self.AuthController = Controller

        self.setFixedSize(1280, 720)
        self.setObjectName("auth_view")

        self.errorLabel = QLabel(self)
        self.label_logo = QLabel(self)
        self.text_lable1 = QLabel("First thing, first!", self)
        self.label_username = QLabel("Username", self)
        self.lineEdit_username = QLineEdit(self)
        self.label_password = QLabel("Password", self)
        self.lineEdit_password = QLineEdit(self)
        self.pic_login = QLabel(self)
        self.text_label2 = QLabel("Let's create your Masterpiece!", self)
        self.login_button = QPushButton("Ready", self)
        

        self.decorateAuthView()

    def decorateAuthView(self):
        self.errorLabel.setObjectName("error_label")
        self.errorLabel.setGeometry(QRect(59, 420, 249, 22))
        self.errorLabel.setFont(Theme.CHILLAX_REGULAR_16)
        self.errorLabel.setStyleSheet("color: #FF0000")
        
        self.label_logo.setObjectName("default_label")
        self.label_logo.setGeometry(QRect(23, 19, 181, 41))
        self.label_logo.setPixmap(QPixmap("static/asset/img/logo.png"))
        self.label_logo.setScaledContents(True)
        
        self.text_lable1.setObjectName("default_label")
        self.text_lable1.setFont(Theme.CHILLAX_REGULAR_36)
        self.text_lable1.setGeometry(QRect(181, 80, 275, 48))
        
        self.label_username.setObjectName("default_label")
        self.label_username.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        self.label_username.setGeometry(QRect(59, 178, 171, 31))
        
        self.lineEdit_username.setObjectName("logIn_bar")
        self.lineEdit_username.setPlaceholderText("Enter your name")
        self.lineEdit_username.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_username.setGeometry(QRect(59, 223, 520, 50))
        self.lineEdit_username.installEventFilter(self)
        
        self.label_password.setObjectName("default_label")
        self.label_password.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        self.label_password.setGeometry(QRect(59, 321, 171, 31))
        
        self.lineEdit_password.setObjectName("logIn_bar")
        self.lineEdit_password.setPlaceholderText("**********")
        self.lineEdit_password.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.installEventFilter(self)
        self.lineEdit_password.setGeometry(QRect(59, 366, 520, 50))
        
        self.pic_login.setGeometry(QRect(642, 0, 649, 720))
        self.pic_login.setPixmap(QPixmap("static/asset/img/login_pic.png"))
        self.pic_login.setScaledContents(True)
        
        self.text_label2.setObjectName("default_label")
        self.text_label2.setFont(Theme.CHILLAX_REGULAR_16)
        self.text_label2.setGeometry(QRect(201, 459, 231, 20))
        
        self.login_button.setObjectName("logIn_button")
        self.login_button.setFont(Theme.CHILLAX_REGULAR_20)
        self.login_button.setGeometry(QRect(59, 589, 520, 50))
        self.login_button.setDefault(True)
        self.login_button.setAutoDefault(True)
        
        self.register_button = QPushButton("Register", self)
        self.register_button.setObjectName("logIn_button")
        self.register_button.setFont(Theme.CHILLAX_REGULAR_20)
        self.register_button.setGeometry(QRect(59, 524, 520, 50))
        self.register_button.setDefault(True)
        self.register_button.setAutoDefault(True)
        
        self.setStyleSheet(Theme.get_stylesheet())


    def eventFilter(self, obj, event):
        if obj == self.lineEdit_username and event.type() == QEvent.FocusIn:
            self.lineEdit_username.setStyleSheet("border: 2px solid #D9A32B;")

        elif obj == self.lineEdit_password and event.type() == QEvent.FocusIn:
            self.lineEdit_password.setStyleSheet("border: 2px solid #D9A32B;")

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