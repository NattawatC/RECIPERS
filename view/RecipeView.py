import sys

from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *

from controller.RecipeController import RecipeController
from static.theme import Theme


class RecipeView(QWidget):
    def __init__(self, parent):
        super().__init__()


        self.RecipeController = RecipeController(self)
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

        nav_create_logo = QLabel(nav_bar)
        nav_create_logo.setObjectName("default_label")
        nav_create_logo.setGeometry(QRect(58, 207, 35, 35))
        nav_create_logo.setPixmap(QPixmap("static/asset/img/nav_create.png"))
        nav_create_logo.setScaledContents(True)

        nav_create = QPushButton("Create", nav_bar)
        nav_create.setObjectName("nav_button")
        nav_create.setFont(Theme.CHILLAX_REGULAR_24)
        nav_create.setGeometry(QRect(123, 214, 91, 21))

        nav_favorite_logo = QLabel(nav_bar)
        nav_favorite_logo.setObjectName("default_label")
        nav_favorite_logo.setGeometry(QRect(54, 273, 40, 40))
        nav_favorite_logo.setPixmap(QPixmap("static/asset/img/nav_favorite.png"))
        nav_favorite_logo.setScaledContents(True)

        nav_favorite = QPushButton("Favorite", nav_bar)
        nav_favorite.setObjectName("nav_button")
        nav_favorite.setFont(Theme.CHILLAX_REGULAR_24)
        nav_favorite.setGeometry(QRect(123, 283, 101, 21))

        logout_logo = QLabel(nav_bar)
        logout_logo.setObjectName("create_bg")
        logout_logo.setPixmap(QPixmap("src/asset/img/logout.png"))
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
        # self.recipe_card = RecipeCard(self)
        # self.recipe_card.setObjectName("recipe_card")
        # self.recipe_card.setGeometry(QRect(341, 268, 402, 194))

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



# def main() -> int:
#     root = QApplication(sys.argv)
#     app = RecipeView()
#     app.show()
#     return root.exec()
#
# if __name__ == "__main__":
#     sys.exit(main())
