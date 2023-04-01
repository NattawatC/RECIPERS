from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class CardWidget(QWidget):
        def __init__(self):
                super().__init__()
                self.setObjectName(u"card_widget")
                self.setGeometry(QRect(342, 280, 402, 194))
                self.setAttribute(Qt.WA_StyledBackground, True)
                self.setStyleSheet(u"background-color: #f6f6f6;\n"
"border: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px\n"
"")
                self.font3 = QFont()
                self.font3.setFamilies([u"Chillax"])
                self.font3.setPointSize(20)
              
                self.font2 = QFont()
                self.font2.setFamilies([u"Chillax"])
                self.font2.setPointSize(16)
                self.setObjectName(u"card_widget")
                self.setGeometry(QRect(342, 280, 402, 194))
               
                card_img = QLabel(self)
                card_img.setObjectName(u"card_img")
                card_img.setGeometry(QRect(16, 13, 168, 168))
                card_img.setPixmap(QPixmap(u"src/asset/img/Recipe_page_assets/BBQ.png"))

                card_info_widget = QWidget(self)
                card_info_widget.setParent(self)
                card_info_widget.setObjectName(u"card_info_widget")
                card_info_widget.setGeometry(QRect(200, 10, 191, 171))
                card_info_widget.setStyleSheet(u"border: none;\n"
        "background-color: transparent;")
                

                
                card_name = QLabel(card_info_widget)
                card_name.setObjectName(u"card_name")
                card_name.setGeometry(QRect(-1, 10, 150, 16))
                card_name.setFont(self.font3)
                card_name.setStyleSheet(u"color: #343454")
 
                cal_label = QLabel(card_info_widget)
                cal_label.setObjectName(u"cal_label")
                cal_label.setGeometry(QRect(63, 140, 41, 21))
                cal_label.setFont(self.font3)
                cal_label.setStyleSheet(u"color: #343454;")

                card_prep_time = QLabel(card_info_widget)
                card_prep_time.setObjectName(u"card_prep_time")
                card_prep_time.setGeometry(QRect(90, 50, 61, 21))
                card_prep_time.setFont(self.font2)
                card_prep_time.setStyleSheet(u"color: #343454;")

                card_cooking_time = QLabel(card_info_widget)
                card_cooking_time.setObjectName(u"card_cooking_time")
                card_cooking_time.setGeometry(QRect(115, 94, 61, 21))
                card_cooking_time.setFont(self.font2)
                card_cooking_time.setStyleSheet(u"color: #343454;")

                card_calories = QLabel(card_info_widget)
                card_calories.setObjectName(u"card_calories")
                card_calories.setGeometry(QRect(0, 140, 61, 21))
                card_calories.setFont(self.font3)
                card_calories.setStyleSheet(u"color: #343454;")

                prep_time_label = QLabel(card_info_widget)
                prep_time_label.setObjectName(u"prep_time_label")
                prep_time_label.setGeometry(QRect(0, 50, 91, 21))
                prep_time_label.setFont(self.font2)
                prep_time_label.setStyleSheet(u"color: #343454;")

                cooking_time_label = QLabel(card_info_widget)
                cooking_time_label.setObjectName(u"cooking_time_label")
                cooking_time_label.setGeometry(QRect(0, 94, 111, 21))
                cooking_time_label.setFont(self.font2)
                cooking_time_label.setStyleSheet(u"color: #343454;")


                card_name.setText(QCoreApplication.translate("Form", u"Pork BBQ Stick", None))
                prep_time_label.setText(QCoreApplication.translate("Form", u"Prep. Time: ", None))
                cooking_time_label.setText(QCoreApplication.translate("Form", u"Cooking Time: ", None))
                cal_label.setText(QCoreApplication.translate("Form", u"Kcal", None))
                card_prep_time.setText(QCoreApplication.translate("Form", u"25 mins", None))
                card_cooking_time.setText(QCoreApplication.translate("Form", u"10 mins", None))
                card_calories.setText(QCoreApplication.translate("Form", u"10000", None))

