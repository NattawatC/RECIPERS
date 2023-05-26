import sys

from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication, QHBoxLayout, QStackedWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect, Signal, QEvent, Qt
from static.theme import Theme

class RegisterView(QWidget):
    def __init__(self, Controller = None):
        super().__init__()

        self.AuthController = Controller

        self.setFixedSize(1280, 720)
        self.setObjectName("reg_view")
        self.label_logo = QLabel(self)
        self.pic_login = QLabel(self)
        self.text_label2 = QLabel("Be a Part of Our Team!", self)
        self.start_button = QPushButton("Start!", self)


        self.decorateRegView()
        # self.lineEdit_regUsername.textChanged.connect(self.AuthController.checkUsername)
        # self.lineEdit_regPassword.textChanged.connect(self.AuthController.checkPassword)

    def decorateRegView(self):
        self.userError = QLabel(self)
        self.userError.setObjectName("error_label")
        self.userError.setGeometry(QRect(701, 195, 218, 20))
        self.userError.setFont(Theme.CHILLAX_REGULAR_14)

        self.fnameError = QLabel(self)
        self.fnameError.setObjectName("error_label")
        self.fnameError.setGeometry(QRect(701, 306, 218, 20))
        self.fnameError.setFont(Theme.CHILLAX_REGULAR_14)

        self.lnameError = QLabel(self)
        self.lnameError.setObjectName("error_label")
        self.lnameError.setGeometry(QRect(981, 306, 218, 20))
        self.lnameError.setFont(Theme.CHILLAX_REGULAR_14)

        self.passwordError = QLabel(self)
        self.passwordError.setObjectName("error_label")
        self.passwordError.setGeometry(QRect(701, 416, 520, 20))
        self.passwordError.setFont(Theme.CHILLAX_REGULAR_14)

        self.confirmPasswordError = QLabel(self)
        self.confirmPasswordError.setObjectName("error_label")
        self.confirmPasswordError.setGeometry(QRect(701, 525, 520, 20))
        self.confirmPasswordError.setFont(Theme.CHILLAX_REGULAR_14)

        self.text_lable1 = QLabel("Let's Cook!", self)
        self.text_lable1.setObjectName("default_label")
        self.text_lable1.setFont(Theme.CHILLAX_REGULAR_36)
        self.text_lable1.setGeometry(QRect(865, 36, 275, 48))
        
        self.label_regUsername = QLabel("Username", self)
        self.label_regUsername.setObjectName("default_label")
        self.label_regUsername.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        self.label_regUsername.setGeometry(QRect(701, 101, 171, 31))
        
        self.lineEdit_regUsername = QLineEdit(self)
        self.lineEdit_regUsername.setObjectName("logIn_bar")
        self.lineEdit_regUsername.setPlaceholderText("Enter your name")
        self.lineEdit_regUsername.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_regUsername.setGeometry(QRect(701, 146, 520, 50))
        self.lineEdit_regUsername.installEventFilter(self)

        self.label_fname = QLabel("First Name", self)
        self.label_fname.setObjectName("default_label")
        self.label_fname.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        self.label_fname.setGeometry(QRect(701, 211, 190, 31))

        self.lineEdit_fname = QLineEdit(self)
        self.lineEdit_fname.setObjectName("logIn_bar")
        self.lineEdit_fname.setPlaceholderText("Firstname")
        self.lineEdit_fname.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_fname.setGeometry(QRect(701, 256, 240, 50))
        self.lineEdit_fname.installEventFilter(self)

        self.label_lname = QLabel("Last Name", self)
        self.label_lname.setObjectName("default_label")
        self.label_lname.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        self.label_lname.setGeometry(QRect(981, 211, 190, 31))

        self.lineEdit_lname = QLineEdit(self)
        self.lineEdit_lname.setObjectName("logIn_bar")
        self.lineEdit_lname.setPlaceholderText("Lastname")
        self.lineEdit_lname.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_lname.setGeometry(QRect(981, 256, 240, 50))
        self.lineEdit_lname.installEventFilter(self)
        
        self.label_regPassword = QLabel("Password", self)
        self.label_regPassword.setObjectName("default_label")
        self.label_regPassword.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        self.label_regPassword.setGeometry(QRect(701, 321, 171, 31))
        
        self.lineEdit_regPassword = QLineEdit(self)
        self.lineEdit_regPassword.setObjectName("logIn_bar")
        self.lineEdit_regPassword.setPlaceholderText("**********")
        self.lineEdit_regPassword.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_regPassword.setEchoMode(QLineEdit.Password)
        self.lineEdit_regPassword.installEventFilter(self)
        self.lineEdit_regPassword.setGeometry(QRect(701, 366, 520, 50))

        self.label_regConPassword = QLabel("Confirm Password", self)
        self.label_regConPassword.setObjectName("default_label")
        self.label_regConPassword.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        self.label_regConPassword.setGeometry(QRect(701, 431, 287, 31))
        
        self.lineEdit_regConPassword = QLineEdit(self)
        self.lineEdit_regConPassword.setObjectName("logIn_bar")
        self.lineEdit_regConPassword.setPlaceholderText("**********")
        self.lineEdit_regConPassword.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_regConPassword.setEchoMode(QLineEdit.Password)
        self.lineEdit_regConPassword.installEventFilter(self)
        self.lineEdit_regConPassword.setGeometry(QRect(701, 476, 520, 50))
        
        self.pic_register = QLabel(self)
        self.pic_register.setGeometry(QRect(0, 0, 649, 720))
        self.pic_register.setPixmap(QPixmap("static/asset/img/register_bg.png"))
        self.pic_register.setScaledContents(True)
        
        self.text_label2.setObjectName("default_label")
        self.text_label2.setFont(Theme.CHILLAX_REGULAR_16)
        self.text_label2.setGeometry(QRect(873, 569, 231, 20))
        
        self.start_button.setObjectName("logIn_button")
        self.start_button.setFont(Theme.CHILLAX_REGULAR_20)
        self.start_button.setGeometry(QRect(701, 634, 520, 50))
        self.start_button.setDefault(True)
        self.start_button.setAutoDefault(True)

        self.setStyleSheet(Theme.get_stylesheet())


    def eventFilter(self, obj, event):
        if obj == self.lineEdit_regUsername and event.type() == QEvent.FocusIn:
            self.lineEdit_regUsername.setStyleSheet("border: 2px solid #D9A32B;")

        elif obj == self.lineEdit_fname and event.type() == QEvent.FocusIn:
            self.lineEdit_fname.setStyleSheet("border: 2px solid #D9A32B;")

        elif obj == self.lineEdit_lname and event.type() == QEvent.FocusIn:
            self.lineEdit_lname.setStyleSheet("border: 2px solid #D9A32B;")

        elif obj == self.lineEdit_regPassword and event.type() == QEvent.FocusIn:
            self.lineEdit_regPassword.setStyleSheet("border: 2px solid #D9A32B;")

        elif obj == self.lineEdit_regConPassword and event.type() == QEvent.FocusIn:
            self.lineEdit_regConPassword.setStyleSheet("border: 2px solid #D9A32B;")

        if obj == self.lineEdit_regUsername and event.type() == QEvent.FocusOut:
            self.lineEdit_regUsername.setStyleSheet(Theme.get_stylesheet())

        elif obj == self.lineEdit_fname and event.type() == QEvent.FocusOut:
            self.lineEdit_fname.setStyleSheet(Theme.get_stylesheet())

        elif obj == self.lineEdit_lname and event.type() == QEvent.FocusOut:
            self.lineEdit_lname.setStyleSheet(Theme.get_stylesheet())

        elif obj == self.lineEdit_regPassword and event.type() == QEvent.FocusOut:
            self.lineEdit_regPassword.setStyleSheet(Theme.get_stylesheet())

        elif obj == self.lineEdit_regConPassword and event.type() == QEvent.FocusOut:
            self.lineEdit_regConPassword.setStyleSheet(Theme.get_stylesheet())
            
        if obj == self.lineEdit_regUsername and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.lineEdit_fname.setFocus()
                return True
            
        elif obj == self.lineEdit_fname and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.lineEdit_lname.setFocus()
                return True
            
        elif obj == self.lineEdit_lname and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.lineEdit_regPassword.setFocus()
                return True
            
        elif obj == self.lineEdit_regPassword and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.lineEdit_regConPassword.setFocus()
                return True

        elif obj == self.lineEdit_regConPassword and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.start_button.click()
                return True
            
        return super().eventFilter(obj, event)

    def get_regUsername(self) -> str:
        return self.lineEdit_regUsername.text()
    
    def get_fname(self) -> str:
        return self.lineEdit_fname.text()
    
    def get_lname(self) -> str:
        return self.lineEdit_lname.text()
    
    def get_regPassword(self) -> str:
        return self.lineEdit_regPassword.text()

    def get_regConPassword(self) -> str:
        return self.lineEdit_regConPassword.text()

    def showError(self, message: str) -> None:
        # self.userError.setText(message)
        # self.userError.show()

        # self.fnameError.setText(message)
        # self.fnameError.show()

        # self.lnameError.setText(message)
        # self.lnameError.show()

        # self.confirmPasswordError.setText(message)
        # self.confirmPasswordError.show()

        self.passwordError.setText(message)
        self.passwordError.show()

    def reset(self) -> None:
        self.userError.hide()
        self.lineEdit_regUsername.clear()
        self.lineEdit_regPassword.clear()
        self.lineEdit_regConPassword.clear()
        self.lineEdit_regUsername.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = RegisterView()
    window.show()
    sys.exit(app.exec_())