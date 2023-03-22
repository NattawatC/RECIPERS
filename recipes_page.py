# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipes_page.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from card_widget import CardWidget

class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1280,720)
        self.setStyleSheet("background-color: white;")
        self.setStyleSheet(u"background-color: #f6f6f6;")
          
       
        self.bg_nav = QLabel(self)
        self.bg_nav.setObjectName(u"bg_nav")
        self.bg_nav.setGeometry(QRect(0, 0, 271, 720))
        self.bg_nav.setStyleSheet(u"background-color: #343454;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px")
        self.logo_recipe = QLabel(self)
        self.logo_recipe.setObjectName(u"logo_recipe")
        self.logo_recipe.setGeometry(QRect(36, 22, 199, 43))
        self.logo_recipe.setPixmap(QPixmap(u"img/Recipe_page_assets/logo_recipe.png"))
        self.bg_recipes_page = QLabel(self)
        self.bg_recipes_page.setObjectName(u"bg_recipes_page")
        self.bg_recipes_page.setGeometry(QRect(0, -352, 1617, 1073))
        font = QFont()
        font.setFamilies([u"Chillax"])
        self.bg_recipes_page.setFont(font)
        self.bg_recipes_page.setPixmap(QPixmap(u"img/Recipe_page_assets/bg_recipe.png"))
        self.bg_recipes_page.setScaledContents(False)
        self.nav_recipe = QLabel(self)
        self.nav_recipe.setObjectName(u"nav_recipe")
        self.nav_recipe.setGeometry(QRect(123, 147, 91, 21))
        self.font1 = QFont()
        self.font1.setFamilies([u"Chillax"])
        self.font1.setPointSize(24)
        self.font1.setBold(False)

       
        self.nav_recipe.setFont(self.font1)
        self.nav_recipe.setStyleSheet(u"font-weight: medium;\n"
"color: #FFFFFF;\n"
"background-color: transparent;")
        self.nav_recipe.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nav_recipe_logo = QLabel(self)
        self.nav_recipe_logo.setObjectName(u"nav_recipe_logo")
        self.nav_recipe_logo.setGeometry(QRect(55, 141, 35, 35))
        self.nav_recipe_logo.setStyleSheet(u"background-color: transparent;")
        self.nav_recipe_logo.setPixmap(QPixmap(u"img/Recipe_page_assets/recipe-book.png"))
        self.nav_recipe_logo.setScaledContents(True)
        self.nav_create = QLabel(self)
        self.nav_create.setObjectName(u"nav_create")
        self.nav_create.setGeometry(QRect(123, 214, 91, 21))
        self.nav_create.setFont(self.font1)
        self.nav_create.setStyleSheet(u"font-weight: medium;\n"
"color: #FFFFFF;\n"
"background-color: transparent;")
        self.nav_create.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nav_bake_logo = QLabel(self)
        self.nav_bake_logo.setObjectName(u"nav_bake_logo")
        self.nav_bake_logo.setGeometry(QRect(58, 207, 35, 35))
        self.nav_bake_logo.setStyleSheet(u"background-color: transparent;")
        self.nav_bake_logo.setPixmap(QPixmap(u"img/Recipe_page_assets/bake.png"))
        self.nav_bake_logo.setScaledContents(True)
        self.nav_favorite = QLabel(self)
        self.nav_favorite.setObjectName(u"nav_favorite")
        self.nav_favorite.setGeometry(QRect(123, 283, 101, 21))
        self.nav_favorite.setFont(self.font1)
        self.nav_favorite.setStyleSheet(u"font-weight: medium;\n"
"color: #FFFFFF;\n"
"background-color: transparent;")
        self.nav_favorite.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nav_fav_logo = QLabel(self)
        self.nav_fav_logo.setObjectName(u"nav_fav_logo")
        self.nav_fav_logo.setGeometry(QRect(54, 273, 40, 40))
        self.nav_fav_logo.setStyleSheet(u"background-color: transparent;")
        self.nav_fav_logo.setPixmap(QPixmap(u"img/Recipe_page_assets/favorite.png"))
        self.nav_fav_logo.setScaledContents(True)
        self.search = QLineEdit(self)
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
        self.search_logo = QLabel(self)
        self.search_logo.setObjectName(u"search_logo")
        self.search_logo.setGeometry(QRect(336, 25, 35, 35))
        self.search_logo.setStyleSheet(u"background-color: transparent;")
        self.search_logo.setPixmap(QPixmap(u"img/Recipe_page_assets/loupe.png"))
        self.search_logo.setScaledContents(True)
        self.welcome_to = QLabel(self)
        self.welcome_to.setObjectName(u"welcome_to")
        self.welcome_to.setGeometry(QRect(336, 81, 121, 16))
        self.font3 = QFont()
        self.font3.setFamilies([u"Chillax"])
        self.font3.setPointSize(20)
        self.welcome_to.setFont(self.font3)
        self.welcome_to.setStyleSheet(u"color: #343454;\n"
"background-color: transparent;")
        self.RECIPE = QLabel(self)
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
       
        self.create_widget = QWidget(self)
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
        self.create_logo.setStyleSheet(u"background-color: transparent;\n"
"border: none")
        self.create_logo.setPixmap(QPixmap(u"img/Recipe_page_assets/grill.png"))
        self.create_logo.setScaledContents(True)
        self.saved_widget = QWidget(self)
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
        self.create_logo_2.setStyleSheet(u"background-color: transparent;\n" "border: none")
        self.create_logo_2.setPixmap(QPixmap(u"img/Recipe_page_assets/favorite2.png"))
        self.create_logo_2.setScaledContents(True)
        self.bg_recipes_page.lower()
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
        self.create_widget.raise_()
        self.saved_widget.raise_() 
        

        self.card_widget = CardWidget()
        self.card_widget.setParent(self)
      
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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec_())