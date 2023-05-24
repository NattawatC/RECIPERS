from static.theme import Theme
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class NavigationBar(QWidget):
    def __init__(self, Controller =None):
        super().__init__()
        self.RecipeController = Controller
        
        self.setFixedSize(1280, 720)

        self.bg_favorite = QLabel(self)
        self.nav_bar = QFrame(self)
        self.label_logo = QLabel(self.nav_bar)
        self.nav_recipe_logo = QLabel(self.nav_bar)
        self.nav_recipe = QPushButton("Recipes", self.nav_bar)
        self.nav_create_logo = QLabel(self.nav_bar)
        self.nav_create = QPushButton("Create", self.nav_bar)
        self.nav_favorite_logo = QLabel(self.nav_bar)
        self.nav_favorite = QPushButton("Favorite", self.nav_bar)
      
        self.decorateNavbar()
    def onClickedNavToRecipe(self):
        self.RecipeController.handleNavigateToRecipe()
    
    def onClickedNavToCreate(self):
        self.RecipeController.handleNavigateToCreate()
    
    def onClickedNavToFavorite(self):
        self.RecipeController.handleNavigateToFavorite()
    
    def decorateNavbar(self):
        self.bg_favorite.setObjectName("default_label")
        self.bg_favorite.setGeometry(QRect(0, -352, 1617, 1073))
        self.bg_favorite.setPixmap(QPixmap("static/asset/img/bg_recipe.png"))
        
        self.nav_bar.setObjectName("frame")
        self.nav_bar.setGeometry(QRect(0, 0, 271, 720))
        
        self.label_logo.setObjectName("default_label")
        self.label_logo.setGeometry(QRect(36, 22, 199, 43))
        self.label_logo.setPixmap(QPixmap("static/asset/img/logo_recipe.png"))
        self.label_logo.setScaledContents(True)

        self.nav_recipe_logo.setObjectName("default_label")
        self.nav_recipe_logo.setGeometry(QRect(55, 141, 35, 35))
        self.nav_recipe_logo.setPixmap(QPixmap("static/asset/img/nav_recipe.png"))
        self.nav_recipe_logo.setScaledContents(True)
        
        self.nav_recipe.setObjectName("nav_button")
        self.nav_recipe.setFont(Theme.CHILLAX_REGULAR_24)
        self.nav_recipe.setGeometry(QRect(123, 147, 91, 21))
        self.nav_recipe.clicked.connect(self.onClickedNavToRecipe)    
        
        self.nav_create_logo.setObjectName("default_label")
        self.nav_create_logo.setGeometry(QRect(58, 207, 35, 35))
        self.nav_create_logo.setPixmap(QPixmap("static/asset/img/nav_create.png"))
        self.nav_create_logo.setScaledContents(True)
    
        self.nav_create.setObjectName("nav_button")
        self.nav_create.setFont(Theme.CHILLAX_REGULAR_24)
        self.nav_create.setGeometry(QRect(123, 214, 91, 21))
        self.nav_create.clicked.connect(self.onClickedNavToCreate)

        self.nav_favorite_logo.setObjectName("default_label")
        self.nav_favorite_logo.setGeometry(QRect(54, 273, 40, 40))
        self.nav_favorite_logo.setPixmap(QPixmap("static/asset/img/nav_favorite.png"))
        self.nav_favorite_logo.setScaledContents(True)
        
        self.nav_favorite.setObjectName("nav_button")
        self.nav_favorite.setFont(Theme.CHILLAX_REGULAR_24)
        self.nav_favorite.setGeometry(QRect(123, 283, 101, 21))
        self.nav_favorite.clicked.connect(self.onClickedNavToFavorite)
        
        self.styleSheet = Theme.get_stylesheet()