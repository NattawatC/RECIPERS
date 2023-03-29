from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from theme import Theme

"""
Log In page
"""

class Login_page(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1280, 720)

        label_logo = QLabel(self)
        label_logo.setObjectName("default_label")
        label_logo.setGeometry(QRect(23, 19, 181, 41))
        label_logo.setPixmap(QPixmap("src/asset/img/logo.png"))
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
        self.lineEdit_username.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_username.setGeometry(QRect(59, 256, 520, 50))

        label_password = QLabel("Password", self)
        label_password.setObjectName("default_label")
        label_password.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        label_password.setGeometry(QRect(59, 354, 171, 31))

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setObjectName("logIn_bar")
        self.lineEdit_password.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setGeometry(QRect(59, 399, 520, 50))

        pic_login = QLabel(self)
        pic_login.setGeometry(QRect(642, 0, 649, 720))
        pic_login.setPixmap(QPixmap("src/asset/img/login_pic.png"))
        pic_login.setScaledContents(True)

        text_label2 = QLabel("Let's create your Masterpiece!", self)
        text_label2.setObjectName("default_label")
        text_label2.setFont(Theme.CHILLAX_REGULAR_16)
        text_label2.setGeometry(QRect(201, 492, 231, 20))

        self.login_button = QPushButton("Ready", self)
        self.login_button.setObjectName("logIn_button")
        self.login_button.setFont(Theme.CHILLAX_REGULAR_20)
        self.login_button.setGeometry(QRect(59, 557, 520, 50))
        
        self.setStyleSheet(Theme.get_stylesheet())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Login_page()
    window.show()
    sys.exit(app.exec())