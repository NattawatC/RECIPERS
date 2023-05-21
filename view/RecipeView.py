import sys

from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtGui import QPixmap, QFont, Qt
from PySide6.QtWidgets import *

from controller.RecipeController import RecipeController
from static.theme import Theme


class RecipeView(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.RecipeController = RecipeController()
        self.RecipeController.setView(self)

        self.mainWindow = parent
        self.setFixedSize(1280, 720)

        bg_recipe_img = QLabel(self)
        bg_recipe_img.setObjectName("default_label")
        bg_recipe_img.setGeometry(QRect(0, -352, 1617, 1073))
        bg_recipe_img.setPixmap(QPixmap("static/asset/img/bg_recipe.png"))

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
        label_logo.setPixmap(QPixmap("static/asset/img/logo_recipe.png"))
        label_logo.setScaledContents(True)

        nav_recipe_logo = QLabel(nav_bar)
        nav_recipe_logo.setObjectName("default_label")
        nav_recipe_logo.setGeometry(QRect(55, 141, 35, 35))
        nav_recipe_logo.setPixmap(QPixmap("static/asset/img/nav_recipe.png"))
        nav_recipe_logo.setScaledContents(True)

        nav_recipe = QPushButton("Recipes", nav_bar)
        nav_recipe.setObjectName("nav_button")
        nav_recipe.setFont(Theme.CHILLAX_REGULAR_24)
        nav_recipe.setGeometry(QRect(123, 147, 91, 21))
        nav_recipe.clicked.connect(self.mainWindow.NavigateToRecipe)

        nav_create_logo = QLabel(nav_bar)
        nav_create_logo.setObjectName("default_label")
        nav_create_logo.setGeometry(QRect(58, 207, 35, 35))
        nav_create_logo.setPixmap(QPixmap("static/asset/img/nav_create.png"))
        nav_create_logo.setScaledContents(True)

        nav_create = QPushButton("Create", nav_bar)
        nav_create.setObjectName("nav_button")
        nav_create.setFont(Theme.CHILLAX_REGULAR_24)
        nav_create.setGeometry(QRect(123, 214, 91, 21))
        nav_create.clicked.connect(self.mainWindow.NavigateToCreate)

        nav_favorite_logo = QLabel(nav_bar)
        nav_favorite_logo.setObjectName("default_label")
        nav_favorite_logo.setGeometry(QRect(54, 273, 40, 40))
        nav_favorite_logo.setPixmap(QPixmap("static/asset/img/nav_favorite.png"))
        nav_favorite_logo.setScaledContents(True)


        nav_favorite = QPushButton("Favorite", nav_bar)
        nav_favorite.setObjectName("nav_button")
        nav_favorite.setFont(Theme.CHILLAX_REGULAR_24)
        nav_favorite.setGeometry(QRect(123, 283, 101, 21))
        nav_favorite.clicked.connect(self.mainWindow.NavigateToFavorite)

        logout_logo = QLabel(nav_bar)
        logout_logo.setObjectName("create_bg")
        logout_logo.setPixmap(QPixmap("static/asset/img/logout.png"))
        logout_logo.setScaledContents(True)
        logout_logo.setGeometry(QRect(215, 664, 43, 43))

        logout_btn = QPushButton(nav_bar)
        logout_btn.setObjectName("logout_button")
        logout_btn.setGeometry(QRect(215, 664, 43, 43))
        logout_btn.clicked.connect(self.onLogoutButtonClicked)

        search_logo = QLabel(self)
        search_logo.setObjectName("default_label")
        search_logo.setGeometry(QRect(336, 25, 35, 35))
        search_logo.setPixmap(QPixmap("../static/asset/img/search.png"))
        search_logo.setScaledContents(True)

        self.search_bar = QLineEdit(self)
        self.search_bar.setObjectName("input_bar")
        self.search_bar.setPlaceholderText("Search recipe here")
        self.search_bar.setFont(Theme.CHILLAX_REGULAR_16)
        self.search_bar.setGeometry(QRect(381, 17, 520, 50))

        total_c_frame = QFrame(self)
        total_c_frame.setObjectName("total_frame")
        total_c_frame.setGeometry(QRect(341, 168, 234, 81))

        create_logo = QLabel(total_c_frame)
        create_logo.setObjectName("create_bg")
        create_logo.setGeometry(QRect(13, 11, 58.8, 58.8))
        create_logo.setPixmap(QPixmap("static/asset/img/create.png"))
        create_logo.setScaledContents(True)

        create_num = QLabel("120", total_c_frame)
        create_num.setObjectName("default_label")
        create_num.setFont(Theme.CHILLAX_REGULAR_24)
        create_num.setGeometry(QRect(92, 17, 60, 20))

        create_label = QLabel("Total Created", total_c_frame)
        create_label.setObjectName("default_label")
        create_label.setFont(Theme.CHILLAX_REGULAR_20)
        create_label.setGeometry(QRect(92, 49, 130, 15))

        total_s_frame = QFrame(self)
        total_s_frame.setObjectName("total_frame")
        total_s_frame.setGeometry(QRect(610, 168, 234, 81))

        save_logo = QLabel(total_s_frame)
        save_logo.setObjectName("create_bg")
        save_logo.setGeometry(QRect(13, 11, 58.8, 58.8))
        save_logo.setPixmap(QPixmap("static/asset/img/save.png"))
        save_logo.setScaledContents(True)

        save_num = QLabel("120", total_s_frame)
        save_num.setObjectName("default_label")
        save_num.setFont(Theme.CHILLAX_REGULAR_24)
        save_num.setGeometry(QRect(92, 17, 60, 20))

        save_label = QLabel("Total Saved", total_s_frame)
        save_label.setObjectName("default_label")
        save_label.setFont(Theme.CHILLAX_REGULAR_20)
        save_label.setGeometry(QRect(92, 49, 130, 15))

        """Add Card"""
        self.recipe_card = RecipeCard()
        self.recipe_card.setObjectName("recipe_card")
        self.recipe_card.setGeometry(QRect(341, 268, 402, 194))
        self.recipe_card.setParent(self)


    def onLogoutButtonClicked(self):
        self.RecipeController.logout()


    def search_recipe(self):
        pass

    def create_recipe(self):
        pass

    def save_recipe(self):
        pass

    def show_recipe(self):
        pass

    def show_favorite(self):
        pass


class RecipeCard(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(402, 194)

        card_frame = QFrame(self)
        card_frame.setObjectName("total_frame")
        card_frame.setFixedSize(402, 194)

        card_img = QLabel(card_frame)
        card_img.setObjectName("card_img")
        card_img.setGeometry(QRect(16, 13, 168, 168))
        card_img.setPixmap(QPixmap("src/asset/img/BBQ.png"))

        card_name = QLabel("Pork BBQ Stick", card_frame)
        card_name.setObjectName("default_label")
        card_name.setGeometry(QRect(204, 21, 146, 28))
        card_name.setFont(Theme.CHILLAX_REGULAR_20)

        card_prep_time = QLabel("Prep. Time:", card_frame)
        card_prep_time.setObjectName("default_label")
        card_prep_time.setGeometry(QRect(204, 64, 141, 22))
        card_prep_time.setFont(Theme.CHILLAX_REGULAR_16)

        card_prep_time_num = QLabel("30 mins", card_frame)
        card_prep_time_num.setObjectName("default_label")
        card_prep_time_num.setGeometry(QRect(293, 64, 141, 22))
        card_prep_time_num.setFont(Theme.CHILLAX_REGULAR_16)

        card_cooking_time = QLabel("Cooking Time:", card_frame)
        card_cooking_time.setObjectName("default_label")
        card_cooking_time.setGeometry(QRect(204, 96, 141, 22))
        card_cooking_time.setFont(Theme.CHILLAX_REGULAR_16)

        card_cooking_time_num = QLabel("30 mins", card_frame)
        card_cooking_time_num.setObjectName("default_label")
        card_cooking_time_num.setGeometry(QRect(317, 96, 141, 22))
        card_cooking_time_num.setFont(Theme.CHILLAX_REGULAR_16)

        cal_time = QLabel("125 Kcal", card_frame)
        cal_time.setObjectName("default_label")
        cal_time.setGeometry(QRect(204, 155, 141, 22))
        cal_time.setFont(Theme.CHILLAX_REGULAR_20)

        card_detail_btn = QPushButton("Detail", card_frame)
        card_detail_btn.setObjectName("card_detail_btn")
        card_detail_btn.setGeometry(QRect(316, 153, 74, 22))
        card_detail_btn.setFont(Theme.CHILLAX_REGULAR_16)

        arrow = QLabel(card_frame)
        arrow.setObjectName("arrow")
        arrow.setGeometry(QRect(372, 158, 13, 13))
        arrow.setPixmap(QPixmap("src/asset/img/right_arrow.png"))
        arrow.setScaledContents(True)

        self.setStyleSheet(Theme.get_stylesheet())

