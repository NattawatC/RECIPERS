from static.theme import Theme
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect, Signal, QEvent, Qt

class FavoriteView(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.mainWindow = parent

        self.setFixedSize(1280, 720)

        bg_favorite = QLabel(self)
        bg_favorite.setObjectName("default_label")
        bg_favorite.setGeometry(QRect(0, -352, 1617, 1073))
        bg_favorite.setPixmap(QPixmap("static/asset/img/bg_recipe.png"))

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

        favorite_label = QLabel("Save for the next time!", self)
        favorite_label.setObjectName("default_label")
        favorite_label.setFont(Theme.CHILLAX_REGULAR_40)
        favorite_label.setGeometry(QRect(336, 22, 460, 56))
        favorite_label.setText(str(self.mainWindow.AuthController.getCurrentUser()) + "'s Favorite")

        total_s_frame = QFrame(self)
        total_s_frame.setObjectName("total_frame")
        total_s_frame.setGeometry(QRect(341, 83, 234, 81))

        save_logo = QLabel(total_s_frame)
        save_logo.setObjectName("create_bg")
        save_logo.setGeometry(QRect(13, 11, 58.8, 58.8))
        save_logo.setPixmap(QPixmap("static/asset/img/save.png"))
        save_logo.setScaledContents(True)

        save_num = QLabel("1", total_s_frame)
        save_num.setObjectName("default_label")
        save_num.setFont(Theme.CHILLAX_REGULAR_24)
        save_num.setGeometry(QRect(92, 17, 60, 20))

        save_label = QLabel("Total Saved", total_s_frame)
        save_label.setObjectName("default_label")
        save_label.setFont(Theme.CHILLAX_REGULAR_20)
        save_label.setGeometry(QRect(92, 49, 130, 15))

        self.setStyleSheet(Theme.get_stylesheet())

