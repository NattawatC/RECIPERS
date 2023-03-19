# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_Page.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    Qt)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet(u"background-color: #F6F6F6")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(23, 19, 181, 41))
        self.label.setStyleSheet(u"background-image: url(:/newPrefix/logo.png);")
        self.label.setPixmap(QPixmap(u"img/logo.png"))
        self.label.setScaledContents(True)
        self.username = QLabel(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(59, 211, 171, 31))
        font = QFont()
        font.setFamilies([u"Chillax"])
        font.setPointSize(32)
        font.setBold(True)
        self.username.setFont(font)
        self.username.setStyleSheet(u"color: #343454")
        self.username_edit = QLineEdit(self.centralwidget)
        self.username_edit.setObjectName(u"username_edit")
        self.username_edit.setGeometry(QRect(59, 256, 520, 50))
        font1 = QFont()
        font1.setFamilies([u"Chillax"])
        font1.setPointSize(20)
        self.username_edit.setFont(font1)
        self.username_edit.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"color: #343454")
        self.username_edit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.username_edit_2 = QLineEdit(self.centralwidget)
        self.username_edit_2.setObjectName(u"username_edit_2")
        self.username_edit_2.setGeometry(QRect(59, 399, 520, 50))
        self.username_edit_2.setFont(font1)
        self.username_edit_2.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"color: #343454")
        self.username_edit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_ready = QPushButton(self.centralwidget)
        self.btn_ready.setObjectName(u"btn_ready")
        self.btn_ready.setEnabled(False)
        self.btn_ready.setGeometry(QRect(59, 557, 520, 50))
        font2 = QFont()
        font2.setFamilies([u"Chillax"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.btn_ready.setFont(font2)
        self.btn_ready.setStyleSheet(u"background-color: #D9A32B;\n"
"color: white;\n"
"border: none")
        self.username_2 = QLabel(self.centralwidget)
        self.username_2.setObjectName(u"username_2")
        self.username_2.setGeometry(QRect(59, 354, 171, 31))
        self.username_2.setFont(font)
        self.username_2.setStyleSheet(u"color: #343454")
        self.title_msg_2 = QLabel(self.centralwidget)
        self.title_msg_2.setObjectName(u"title_msg_2")
        self.title_msg_2.setGeometry(QRect(201, 492, 231, 20))
        font3 = QFont()
        font3.setFamilies([u"Chillax"])
        font3.setPointSize(16)
        self.title_msg_2.setFont(font3)
        self.title_msg_2.setStyleSheet(u"color: #343454")
        self.title_msg_2.setAlignment(Qt.AlignCenter)
        self.pic_login = QLabel(self.centralwidget)
        self.pic_login.setObjectName(u"pic_login")
        self.pic_login.setGeometry(QRect(642, 0, 649, 720))
        self.pic_login.setStyleSheet(u"background-image: url(:/newPrefix/Login_pic.png);")
        self.pic_login.setPixmap(QPixmap(u"img/Login_pic.png"))
        self.pic_login.setScaledContents(True)
        self.title_msg_1 = QLabel(self.centralwidget)
        self.title_msg_1.setObjectName(u"title_msg_1")
        self.title_msg_1.setEnabled(True)
        self.title_msg_1.setGeometry(QRect(181, 113, 275, 48))
        font4 = QFont()
        font4.setFamilies([u"Chillax"])
        font4.setPointSize(36)
        self.title_msg_1.setFont(font4)
        self.title_msg_1.setStyleSheet(u"color: #343454")
        self.title_msg_1.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.username_edit.setText("")
        self.username_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Your Name", None))
        self.username_edit_2.setText("")
        self.username_edit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"**********", None))
        self.btn_ready.setText(QCoreApplication.translate("MainWindow", u"READY", None))
        self.username_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.title_msg_2.setText(QCoreApplication.translate("MainWindow", u"Let\u2019s create your Masterpiece!", None))
        self.pic_login.setText("")
        self.title_msg_1.setText(QCoreApplication.translate("MainWindow", u"First thing, first!", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())