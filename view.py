from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from theme import Theme
from card_widget import CardWidget


"""
Log In page
"""


class LoginView(QWidget):
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
        self.lineEdit_username.setPlaceholderText("Enter your name")
        self.lineEdit_username.setFont(Theme.CHILLAX_REGULAR_20)
        self.lineEdit_username.setGeometry(QRect(59, 256, 520, 50))

        label_password = QLabel("Password", self)
        label_password.setObjectName("default_label")
        label_password.setFont(Theme.CHILLAX_SEMI_BOLD_32)
        label_password.setGeometry(QRect(59, 354, 171, 31))

        self.lineEdit_password = QLineEdit(self)
        self.lineEdit_password.setObjectName("logIn_bar")
        self.lineEdit_password.setPlaceholderText("**********")
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


"""
Recipe page
"""


class RecipeView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1280, 720)

        bg_recipe_img = QLabel(self)
        bg_recipe_img.setObjectName("default_label")
        bg_recipe_img.setGeometry(QRect(0, -352, 1617, 1073))
        bg_recipe_img.setPixmap(QPixmap("src/asset/img/bg_recipe.png"))

        recipe_label = QLabel("Welcome to,", self)
        recipe_label.setObjectName("default_label")
        recipe_label.setFont(Theme.CHILLAX_REGULAR_20)
        recipe_label.setGeometry(QRect(336, 81, 121, 16))

        recipe_label2 = QLabel("Recipes", self)
        recipe_label2.setObjectName("default_label")
        recipe_label2.setFont(Theme.CHILLAX_REGULAR_40)
        recipe_label2.setGeometry(QRect(336, 104, 171, 51))

        nav_bar = QFrame(self)
        nav_bar.setObjectName("frame")
        nav_bar.setGeometry(QRect(0, 0, 271, 720))

        label_logo = QLabel(nav_bar)
        label_logo.setObjectName("default_label")
        label_logo.setGeometry(QRect(36, 22, 199, 43))
        label_logo.setPixmap(QPixmap("src/asset/img/logo_recipe.png"))
        label_logo.setScaledContents(True)

        nav_recipe_logo = QLabel(nav_bar)
        nav_recipe_logo.setObjectName("default_label")
        nav_recipe_logo.setGeometry(QRect(55, 141, 35, 35))
        nav_recipe_logo.setPixmap(QPixmap("src/asset/img/nav_recipe.png"))
        nav_recipe_logo.setScaledContents(True)

        nav_recipe = QPushButton("Recipes", nav_bar)
        nav_recipe.setObjectName("nav_button")
        nav_recipe.setFont(Theme.CHILLAX_REGULAR_24)
        nav_recipe.setGeometry(QRect(123, 147, 91, 21))

        nav_create_logo = QLabel(nav_bar)
        nav_create_logo.setObjectName("default_label")
        nav_create_logo.setGeometry(QRect(58, 207, 35, 35))
        nav_create_logo.setPixmap(QPixmap("src/asset/img/nav_create.png"))
        nav_create_logo.setScaledContents(True)

        nav_create = QPushButton("Create", nav_bar)
        nav_create.setObjectName("nav_button")
        nav_create.setFont(Theme.CHILLAX_REGULAR_24)
        nav_create.setGeometry(QRect(123, 214, 91, 21))

        nav_favorite_logo = QLabel(nav_bar)
        nav_favorite_logo.setObjectName("default_label")
        nav_favorite_logo.setGeometry(QRect(54, 273, 40, 40))
        nav_favorite_logo.setPixmap(QPixmap("src/asset/img/nav_favorite.png"))
        nav_favorite_logo.setScaledContents(True)

        nav_favorite = QPushButton("Favorite", nav_bar)
        nav_favorite.setObjectName("nav_button")
        nav_favorite.setFont(Theme.CHILLAX_REGULAR_24)
        nav_favorite.setGeometry(QRect(123, 283, 101, 21))

        search_logo = QLabel(self)
        search_logo.setObjectName("default_label")
        search_logo.setGeometry(QRect(336, 25, 35, 35))
        search_logo.setPixmap(QPixmap("src/asset/img/search.png"))
        search_logo.setScaledContents(True)

        self.seaerch_bar = QLineEdit(self)
        self.seaerch_bar.setObjectName("input_bar")
        self.seaerch_bar.setPlaceholderText("Search recipe here")
        self.seaerch_bar.setFont(Theme.CHILLAX_REGULAR_16)
        self.seaerch_bar.setGeometry(QRect(381, 17, 520, 50))

        total_c_frame = QFrame(self)
        total_c_frame.setObjectName("total_frame")
        total_c_frame.setGeometry(QRect(341, 168, 234, 81))

        create_logo = QLabel(total_c_frame)
        create_logo.setObjectName("create_bg")
        create_logo.setGeometry(QRect(13, 11, 58.8, 58.8))
        create_logo.setPixmap(QPixmap("src/asset/img/create.png"))
        create_logo.setScaledContents(True)

        create_num = QLabel("120", total_c_frame)
        create_num.setObjectName("textbox")
        create_num.setFont(Theme.CHILLAX_REGULAR_24)
        create_num.setGeometry(QRect(92, 17, 60, 20))

        create_label = QLabel("Total Created", total_c_frame)
        create_label.setObjectName("textbox")
        create_label.setFont(Theme.CHILLAX_REGULAR_20)
        create_label.setGeometry(QRect(92, 49, 130, 15))

        total_s_frame = QFrame(self)
        total_s_frame.setObjectName("total_frame")
        total_s_frame.setGeometry(QRect(610, 168, 234, 81))

        save_logo = QLabel(total_s_frame)
        save_logo.setObjectName("create_bg")
        save_logo.setGeometry(QRect(13, 11, 58.8, 58.8))
        save_logo.setPixmap(QPixmap("src/asset/img/save.png"))
        save_logo.setScaledContents(True)

        save_num = QLabel("120", total_s_frame)
        save_num.setObjectName("textbox")
        save_num.setFont(Theme.CHILLAX_REGULAR_24)
        save_num.setGeometry(QRect(92, 17, 60, 20))

        save_label = QLabel("Total Saved", total_s_frame)
        save_label.setObjectName("textbox")
        save_label.setFont(Theme.CHILLAX_REGULAR_20)
        save_label.setGeometry(QRect(92, 49, 130, 15))

        self.setStyleSheet(Theme.get_stylesheet())

        # self.card = CardWidget()
        # self.card.setParent(self)


"""
Recipe Card
"""


# class RecipeCard(QWidget):
class RecipeCard(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(402, 194)

        card_img = QLabel(self)
        card_img.setObjectName("card_img")
        card_img.setGeometry(QRect(16, 13, 168, 168))
        card_img.setPixmap(QPixmap("src/asset/img/BBQ.png"))

        card_name = QLabel("Pork BBQ Stick", self)
        card_name.setObjectName("textbox")
        card_name.setGeometry(QRect(204, 21, 146, 28))
        card_name.setFont(Theme.CHILLAX_REGULAR_20)

        card_prep_time = QLabel("Prep. Time:", self)
        card_prep_time.setObjectName("textbox")
        card_prep_time.setGeometry(QRect(204, 64, 141, 22))
        card_prep_time.setFont(Theme.CHILLAX_REGULAR_16)

        card_prep_time_num = QLabel("30 mins", self)
        card_prep_time_num.setObjectName("textbox")
        card_prep_time_num.setGeometry(QRect(293, 64, 141, 22))
        card_prep_time_num.setFont(Theme.CHILLAX_REGULAR_16)
        
        card_cooking_time = QLabel("Cooking Time:", self)
        card_cooking_time.setObjectName("textbox")
        card_cooking_time.setGeometry(QRect(204, 96, 141, 22))
        card_cooking_time.setFont(Theme.CHILLAX_REGULAR_16)

        card_cooking_time_num = QLabel("30 mins", self)
        card_cooking_time_num.setObjectName("textbox")
        card_cooking_time_num.setGeometry(QRect(317, 96, 141, 22))
        card_cooking_time_num.setFont(Theme.CHILLAX_REGULAR_16)

        cal_time = QLabel("125 Kcal", self)
        cal_time.setObjectName("textbox")
        cal_time.setGeometry(QRect(204, 155, 141, 22))
        cal_time.setFont(Theme.CHILLAX_REGULAR_20)

        detail_btn = QPushButton("Detail", self)
        detail_btn.setObjectName("detail_btn")
        detail_btn.setGeometry(QRect(316, 153, 74, 22))
        detail_btn.setFont(Theme.CHILLAX_REGULAR_16)

        arrow = QLabel(self)
        arrow.setObjectName("arrow")
        arrow.setGeometry(QRect(372, 158, 13, 13))
        arrow.setPixmap(QPixmap("src/asset/img/right_arrow.png"))
        arrow.setScaledContents(True)

        self.setStyleSheet(Theme.get_stylesheet())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = RecipeCard()
    window.show()
    sys.exit(app.exec())