import asyncio
import sys

import requests
from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtGui import QPixmap, QFont, Qt, QCursor
from PySide6.QtWidgets import *
import io
from PIL import Image, UnidentifiedImageError
from PIL.ImageQt import ImageQt

from static.theme import Theme
from view.Navbar import NavigationBar

class RecipeView(NavigationBar):
    def __init__(self, parent = None):
        super().__init__(parent)

        recipe_label = QLabel("Welcome to,", self)
        recipe_label.setObjectName("default_label")
        recipe_label.setFont(Theme.CHILLAX_REGULAR_20)
        recipe_label.setGeometry(QRect(336, 92, 121, 16))

        recipe_label2 = QLabel("Recipes", self)
        recipe_label2.setObjectName("default_label")
        recipe_label2.setFont(Theme.CHILLAX_REGULAR_40)
        recipe_label2.setGeometry(QRect(336, 112, 171, 51))

       
        #-------------------------------------------
        logout_logo = QLabel(self)
        logout_logo.setObjectName("create_bg")
        logout_logo.setPixmap(QPixmap("static/asset/img/logout.png"))
        logout_logo.setScaledContents(True)
        logout_logo.setGeometry(QRect(215, 664, 43, 43))

        logout_btn = QPushButton(self)
        logout_btn.setObjectName("logout_button")
        logout_btn.setGeometry(QRect(215, 664, 43, 43))
        logout_btn.clicked.connect(self.onLogoutButtonClicked)

        search_logo = QLabel(self)
        search_logo.setObjectName("default_label")
        search_logo.setGeometry(QRect(336, 25, 35, 35))
        search_logo.setPixmap(QPixmap("static/asset/img/search.png"))
        search_logo.setScaledContents(True)

        self.search_bar = QLineEdit(self)
        self.search_bar.setObjectName("input_bar")
        self.search_bar.setPlaceholderText("Search recipe here")
        self.search_bar.setFont(Theme.CHILLAX_REGULAR_16)
        self.search_bar.setGeometry(QRect(381, 17, 520, 50))

        total_c_frame = QFrame(self)
        total_c_frame.setObjectName("total_frame")
        total_c_frame.setGeometry(QRect(520, 89, 234, 81))

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
        total_s_frame.setGeometry(QRect(789, 89, 234, 81))

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


    def onLogoutButtonClicked(self):
        self.mainWindow.RecipeController.logout()

    def createRecipeCard(self, recipes):
        newline = 0
        for i, recipe in enumerate(recipes):
            recipe_card = RecipeCard(recipe)

            if i % 2 == 0:
                recipe_card.setGeometry(QRect(336, 192 + (230 * newline), 402, 194))

            else:
                recipe_card.setGeometry(QRect(774, 192 + (230 * newline), 402, 194))

            newline += 1
            recipe_card.setParent(self)


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
    def __init__(self, recipe = None):
        super().__init__()
        self.setFixedSize(402, 194)

        self.recipe = recipe

        card_frame = QFrame(self)
        card_frame.setObjectName("total_frame")
        card_frame.setFixedSize(402, 194)

        self.card_img = QLabel(card_frame)
        self.card_img.setObjectName("card_img")
        self.card_img.setGeometry(QRect(16, 13, 168, 168))
        self.loadImageFromURL(recipe.image.strip(), recipe.id)

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
        card_detail_btn.setCursor(QCursor(Qt.PointingHandCursor))
        # card_detail_btn.clicked.connect(self.RecipeController.handleMakeFavorite)

        arrow = QLabel(card_frame)
        arrow.setObjectName("arrow")
        arrow.setGeometry(QRect(372, 158, 13, 13))
        arrow.setPixmap(QPixmap("static/asset/img/right_arrow.png"))
        arrow.setScaledContents(True)

        self.setStyleSheet(Theme.get_stylesheet())

    def loadImageFromURL(self, url, id):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in urls:
                tasks.append(fetch_image(session, url))

            images = await asyncio.gather(*tasks)

        request = requests.get(url)
        try:
            with io.BytesIO(request.content) as img_bytes:
                image = Image.open(img_bytes)
                image = image.resize((170, 170), Image.ANTIALIAS)
                pixmap = QPixmap()
                pixmap.convertFromImage(ImageQt(image))
                self.card_img.setPixmap(pixmap)
        except UnidentifiedImageError:
            print(id, "is not an image file")

