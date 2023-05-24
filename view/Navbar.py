from static.theme import Theme
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class NavigationBar(QWidget):
    def __init__(self, Controller =None):
        super().__init__()
        self.RecipeController = Controller
        
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
        nav_recipe.clicked.connect(self.onClickedNavToRecipe)
        
        nav_create_logo = QLabel(nav_bar)
        nav_create_logo.setObjectName("default_label")
        nav_create_logo.setGeometry(QRect(58, 207, 35, 35))
        nav_create_logo.setPixmap(QPixmap("static/asset/img/nav_create.png"))
        nav_create_logo.setScaledContents(True)

        nav_create = QPushButton("Create", nav_bar)
        nav_create.setObjectName("nav_button")
        nav_create.setFont(Theme.CHILLAX_REGULAR_24)
        nav_create.setGeometry(QRect(123, 214, 91, 21))
        nav_create.clicked.connect(self.onClickedNavToCreate)

        nav_favorite_logo = QLabel(nav_bar)
        nav_favorite_logo.setObjectName("default_label")
        nav_favorite_logo.setGeometry(QRect(54, 273, 40, 40))
        nav_favorite_logo.setPixmap(QPixmap("static/asset/img/nav_favorite.png"))
        nav_favorite_logo.setScaledContents(True)

        nav_favorite = QPushButton("Favorite", nav_bar)
        nav_favorite.setObjectName("nav_button")
        nav_favorite.setFont(Theme.CHILLAX_REGULAR_24)
        nav_favorite.setGeometry(QRect(123, 283, 101, 21))
        nav_favorite.clicked.connect(self.onClickedNavToFavorite)

    def onClickedNavToRecipe(self):
        self.RecipeController.handleNavigateToRecipe()
    
    def onClickedNavToCreate(self):
        self.RecipeController.handleNavigateToCreate()
    
    def onClickedNavToFavorite(self):
        self.RecipeController.handleNavigateToFavorite()
            
            
            