# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipes_page.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 720)
        Form.setStyleSheet(u"background-color: #f6f6f6")
        self.bg_nav = QLabel(Form)
        self.bg_nav.setObjectName(u"bg_nav")
        self.bg_nav.setGeometry(QRect(0, 0, 271, 720))
        self.bg_nav.setStyleSheet(u"background-color: #343454;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px")
        self.logo_recipe = QLabel(Form)
        self.logo_recipe.setObjectName(u"logo_recipe")
        self.logo_recipe.setGeometry(QRect(36, 22, 199, 43))
        self.logo_recipe.setStyleSheet(u"background-image: url(:/newPrefix/Recipe_page_assets/logo_recipe.png);")
        self.logo_recipe.setPixmap(QPixmap(u"img/Recipe_page_assets/logo_recipe.png"))
        self.bg_recipes_page = QLabel(Form)
        self.bg_recipes_page.setObjectName(u"bg_recipes_page")
        self.bg_recipes_page.setGeometry(QRect(0, -352, 1617, 1073))
        font = QFont()
        font.setFamilies([u"Chillax"])
        self.bg_recipes_page.setFont(font)
        self.bg_recipes_page.setStyleSheet(u"background-image: url(:/newPrefix/bg_recipe.png);")
        self.bg_recipes_page.setPixmap(QPixmap(u"img/Recipe_page_assets/bg_recipe.png"))
        self.bg_recipes_page.setScaledContents(False)
        self.nav_recipe = QLabel(Form)
        self.nav_recipe.setObjectName(u"nav_recipe")
        self.nav_recipe.setGeometry(QRect(123, 147, 91, 21))
        self.font1 = QFont()
        self.font1.setFamilies([u"Chillax"])
        self.font1.setPointSize(24)
        self.font1.setBold(False)
        
        #Initialize the card widget
        self.card_widget = QWidget(Form)
        
        self.nav_recipe.setFont(self.font1)
        self.nav_recipe.setStyleSheet(u"font-weight: medium;\n"
"color: #FFFFFF;\n"
"background-color: transparent;")
        self.nav_recipe.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nav_recipe_logo = QLabel(Form)
        self.nav_recipe_logo.setObjectName(u"nav_recipe_logo")
        self.nav_recipe_logo.setGeometry(QRect(55, 141, 35, 35))
        self.nav_recipe_logo.setStyleSheet(u"background-image: url(:/newPrefix/Desktop/Recipe_page_assets/recipe-book.png);\n"
"background-color: transparent;")
        self.nav_recipe_logo.setPixmap(QPixmap(u"img/Recipe_page_assets/recipe-book.png"))
        self.nav_recipe_logo.setScaledContents(True)
        self.nav_create = QLabel(Form)
        self.nav_create.setObjectName(u"nav_create")
        self.nav_create.setGeometry(QRect(123, 214, 91, 21))
        self.nav_create.setFont(self.font1)
        self.nav_create.setStyleSheet(u"font-weight: medium;\n"
"color: #FFFFFF;\n"
"background-color: transparent;")
        self.nav_create.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nav_bake_logo = QLabel(Form)
        self.nav_bake_logo.setObjectName(u"nav_bake_logo")
        self.nav_bake_logo.setGeometry(QRect(58, 207, 35, 35))
        self.nav_bake_logo.setStyleSheet(u"background-image: url(:/newPrefix/Recipe_page_assets/bake.png);\n"
"background-color: transparent;")
        self.nav_bake_logo.setPixmap(QPixmap(u"img/Recipe_page_assets/bake.png"))
        self.nav_bake_logo.setScaledContents(True)
        self.nav_favorite = QLabel(Form)
        self.nav_favorite.setObjectName(u"nav_favorite")
        self.nav_favorite.setGeometry(QRect(123, 283, 101, 21))
        self.nav_favorite.setFont(self.font1)
        self.nav_favorite.setStyleSheet(u"font-weight: medium;\n"
"color: #FFFFFF;\n"
"background-color: transparent;")
        self.nav_favorite.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nav_fav_logo = QLabel(Form)
        self.nav_fav_logo.setObjectName(u"nav_fav_logo")
        self.nav_fav_logo.setGeometry(QRect(54, 273, 40, 40))
        self.nav_fav_logo.setStyleSheet(u"background-image: url(:/newPrefix/favorite.png);\n"
"background-color: transparent;")
        self.nav_fav_logo.setPixmap(QPixmap(u"img/Recipe_page_assets/favorite.png"))
        self.nav_fav_logo.setScaledContents(True)
        self.search = QLineEdit(Form)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(381, 17, 639, 50))
        self.font2 = QFont()
        self.font2.setFamilies([u"Chillax"])
        self.font2.setPointSize(16)
        self.search.setFont(self.font2)
        self.search.setStyleSheet(u"border: solid;\n"
"border-radius: 25px; \n"
"border-width: 1px;\n"
"color: #343454;\n"
"background-color: #f6f6f6")
        self.search_logo = QLabel(Form)
        self.search_logo.setObjectName(u"search_logo")
        self.search_logo.setGeometry(QRect(336, 25, 35, 35))
        self.search_logo.setStyleSheet(u"background-image: url(:/newPrefix/loupe.png);\n"
"background-color: transparent;")
        self.search_logo.setPixmap(QPixmap(u"img/Recipe_page_assets/loupe.png"))
        self.search_logo.setScaledContents(True)
        self.welcome_to = QLabel(Form)
        self.welcome_to.setObjectName(u"welcome_to")
        self.welcome_to.setGeometry(QRect(336, 81, 121, 16))
        self.font3 = QFont()
        self.font3.setFamilies([u"Chillax"])
        self.font3.setPointSize(20)
        self.welcome_to.setFont(self.font3)
        self.welcome_to.setStyleSheet(u"color: #343454;\n"
"background-color: transparent;")
        self.RECIPE = QLabel(Form)
        self.RECIPE.setObjectName(u"RECIPE")
        self.RECIPE.setGeometry(QRect(336, 104, 171, 51))
        self.font4 = QFont()
        self.font4.setFamilies([u"Chillax"])
        self.font4.setPointSize(40)
        self.font4.setBold(True)
        self.font4.setItalic(False)
        self.RECIPE.setFont(self.font4)
        self.RECIPE.setStyleSheet(u"font-style: medium;\n"
"color: #343454;\n"
"background-color: transparent;")
       
        self.create_widget = QWidget(Form)
        self.create_widget.setObjectName(u"create_widget")
        self.create_widget.setGeometry(QRect(341, 170, 234, 81))
        self.create_widget.setStyleSheet(u"background-color: #F6F6F6;\n"
"border:solid;\n"
"border-width: 1px;\n"
"border-radius: 10px")
        self.create_info_widget = QWidget(self.create_widget)
        self.create_info_widget.setObjectName(u"create_info_widget")
        self.create_info_widget.setGeometry(QRect(87, 6, 131, 61))
        self.create_info_widget.setStyleSheet(u"border: none")
        self.create_num = QLabel(self.create_info_widget)
        self.create_num.setObjectName(u"create_num")
        self.create_num.setGeometry(QRect(10, 10, 60, 21))
        self.create_num.setFont(self.font1)
        self.create_num.setStyleSheet(u"color: #343454;")
        self.total_create_label = QLabel(self.create_info_widget)
        self.total_create_label.setObjectName(u"total_create_label")
        self.total_create_label.setGeometry(QRect(10, 42, 121, 21))
        self.total_create_label.setFont(self.font3)
        self.total_create_label.setStyleSheet(u"color: #343454;")
        self.bg_yellow_create = QLabel(self.create_widget)
        self.bg_yellow_create.setObjectName(u"bg_yellow_create")
        self.bg_yellow_create.setGeometry(QRect(15, 12, 58, 58))
        self.bg_yellow_create.setStyleSheet(u"background-color: #D9A32B;\n"
"border: none")
        self.create_logo = QLabel(self.create_widget)
        self.create_logo.setObjectName(u"create_logo")
        self.create_logo.setGeometry(QRect(26, 23, 37, 37))
        self.create_logo.setStyleSheet(u"background-image: url(:/newPrefix/grill.png);\n"
"background-color: transparent;\n"
"border: none")
        self.create_logo.setPixmap(QPixmap(u"img/Recipe_page_assets/grill.png"))
        self.create_logo.setScaledContents(True)
        self.saved_widget = QWidget(Form)
        self.saved_widget.setObjectName(u"saved_widget")
        self.saved_widget.setGeometry(QRect(610, 170, 234, 81))
        self.saved_widget.setStyleSheet(u"background-color: #F6F6F6;\n"
"border:solid;\n"
"border-width: 1px;\n"
"border-radius: 10px")
        self.create_info_widget_2 = QWidget(self.saved_widget)
        self.create_info_widget_2.setObjectName(u"create_info_widget_2")
        self.create_info_widget_2.setGeometry(QRect(87, 6, 131, 61))
        self.create_info_widget_2.setStyleSheet(u"border: none")
        self.create_num_2 = QLabel(self.create_info_widget_2)
        self.create_num_2.setObjectName(u"create_num_2")
        self.create_num_2.setGeometry(QRect(10, 10, 60, 21))
        self.create_num_2.setFont(self.font1)
        self.create_num_2.setStyleSheet(u"color: #343454;")
        self.total_create_label_2 = QLabel(self.create_info_widget_2)
        self.total_create_label_2.setObjectName(u"total_create_label_2")
        self.total_create_label_2.setGeometry(QRect(10, 42, 121, 21))
        self.total_create_label_2.setFont(self.font3)
        self.total_create_label_2.setStyleSheet(u"color: #343454;")
        self.bg_yellow_create_2 = QLabel(self.saved_widget)
        self.bg_yellow_create_2.setObjectName(u"bg_yellow_create_2")
        self.bg_yellow_create_2.setGeometry(QRect(15, 12, 58, 58))
        self.bg_yellow_create_2.setStyleSheet(u"background-color: #D9A32B;\n"
"border: none")
        self.create_logo_2 = QLabel(self.saved_widget)
        self.create_logo_2.setObjectName(u"create_logo_2")
        self.create_logo_2.setGeometry(QRect(26, 23, 37, 37))
        self.create_logo_2.setStyleSheet(u"background-image: url(:/newPrefix/Recipe_page_assets/favorite2.png);\n"
"background-color: transparent;\n"
"border: none")
        self.create_logo_2.setPixmap(QPixmap(u"img/Recipe_page_assets/favorite2.png"))
        self.create_logo_2.setScaledContents(True)
        self.bg_recipes_page.raise_()
        self.bg_nav.raise_()
        self.logo_recipe.raise_()
        self.nav_recipe.raise_()
        self.nav_recipe_logo.raise_()
        self.nav_create.raise_()
        self.nav_bake_logo.raise_()
        self.nav_favorite.raise_()
        self.nav_fav_logo.raise_()
        self.search.raise_()
        self.search_logo.raise_()
        self.welcome_to.raise_()
        self.RECIPE.raise_()
        self.card_widget.raise_()
        self.create_widget.raise_()
        self.saved_widget.raise_()

        # self.retranslateUi(Form)
        self.createCard(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi
    def createCard(self, Form):
        self.card_widget.setObjectName(u"card_widget")
        self.card_widget.setGeometry(QRect(342, 280, 402, 194))
        self.card_widget.setStyleSheet(u"background-color: #f6f6f6;\n"
"border: solid;\n"
"border-width: 1px;\n"
"border-radius: 10px\n"
"")
        self.card_img = QLabel(self.card_widget)
        self.card_img.setObjectName(u"card_img")
        self.card_img.setGeometry(QRect(16, 13, 168, 168))
        self.card_img.setStyleSheet(u"background-image: url(:/newPrefix/BBQ.png);")
        self.card_img.setPixmap(QPixmap(u"img/Recipe_page_assets/BBQ.png"))
        self.card_img.setScaledContents(True)
        self.card_info_widget = QWidget(self.card_widget)
        self.card_info_widget.setObjectName(u"card_info_widget")
        self.card_info_widget.setGeometry(QRect(200, 10, 191, 171))
        self.card_info_widget.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        self.card_name = QLabel(self.card_info_widget)
        self.card_name.setObjectName(u"card_name")
        self.card_name.setGeometry(QRect(-1, 10, 150, 16))
        self.card_name.setFont(self.font3)
        self.card_name.setStyleSheet(u"color: #343454")

        self.cal_label = QLabel(self.card_info_widget)
        self.cal_label.setObjectName(u"cal_label")
        self.cal_label.setGeometry(QRect(63, 140, 41, 21))
        self.cal_label.setFont(self.font3)
        self.cal_label.setStyleSheet(u"color: #343454;")

        self.card_prep_time = QLabel(self.card_info_widget)
        self.card_prep_time.setObjectName(u"card_prep_time")
        self.card_prep_time.setGeometry(QRect(90, 50, 61, 21))
        self.card_prep_time.setFont(self.font2)
        self.card_prep_time.setStyleSheet(u"color: #343454;")
        self.card_cooking_time = QLabel(self.card_info_widget)
        self.card_cooking_time.setObjectName(u"card_cooking_time")
        self.card_cooking_time.setGeometry(QRect(115, 94, 61, 21))
        self.card_cooking_time.setFont(self.font2)
        self.card_cooking_time.setStyleSheet(u"color: #343454;")
        self.card_calories = QLabel(self.card_info_widget)
        self.card_calories.setObjectName(u"card_calories")
        self.card_calories.setGeometry(QRect(0, 140, 61, 21))
        self.card_calories.setFont(self.font3)
        self.card_calories.setStyleSheet(u"color: #343454;")

        self.prep_time_label = QLabel(self.card_info_widget)
        self.prep_time_label.setObjectName(u"prep_time_label")
        self.prep_time_label.setGeometry(QRect(0, 50, 91, 21))
        self.prep_time_label.setFont(self.font2)
        self.prep_time_label.setStyleSheet(u"color: #343454;")
        self.cooking_time_label = QLabel(self.card_info_widget)
        self.cooking_time_label.setObjectName(u"cooking_time_label")
        self.cooking_time_label.setGeometry(QRect(0, 94, 111, 21))
        self.cooking_time_label.setFont(self.font2)
        self.cooking_time_label.setStyleSheet(u"color: #343454;")


        self.card_name.setText(QCoreApplication.translate("Form", u"Pork BBQ Stick", None))
        self.prep_time_label.setText(QCoreApplication.translate("Form", u"Prep. Time: ", None))
        self.cooking_time_label.setText(QCoreApplication.translate("Form", u"Cooking Time: ", None))
        self.cal_label.setText(QCoreApplication.translate("Form", u"Kcal", None))
        self.card_prep_time.setText(QCoreApplication.translate("Form", u"25 mins", None))
        self.card_cooking_time.setText(QCoreApplication.translate("Form", u"10 mins", None))
        self.card_calories.setText(QCoreApplication.translate("Form", u"10000", None))

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bg_nav.setText("")
        self.logo_recipe.setText("")
        self.bg_recipes_page.setText("")
        self.nav_recipe.setText(QCoreApplication.translate("Form", u"Recipes", None))
        self.nav_recipe_logo.setText("")
        self.nav_create.setText(QCoreApplication.translate("Form", u"Create", None))
        self.nav_bake_logo.setText("")
        self.nav_favorite.setText(QCoreApplication.translate("Form", u"Favorite", None))
        self.nav_fav_logo.setText("")
        self.search.setPlaceholderText(QCoreApplication.translate("Form", u"Search recipe here", None))
        self.search_logo.setText("")
        self.welcome_to.setText(QCoreApplication.translate("Form", u"Welcome to,", None))
        self.RECIPE.setText(QCoreApplication.translate("Form", u"RECIPES", None))
      
        self.create_num.setText(QCoreApplication.translate("Form", u"0", None))
        self.total_create_label.setText(QCoreApplication.translate("Form", u"Total Create", None))
        self.bg_yellow_create.setText("")
        self.create_logo.setText("")
        self.create_num_2.setText(QCoreApplication.translate("Form", u"0", None))
        self.total_create_label_2.setText(QCoreApplication.translate("Form", u"Total Saved", None))
        self.bg_yellow_create_2.setText("")
        self.create_logo_2.setText("")
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())