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
        self.user_btn = QPushButton(self)
        self.user_message_box = QMessageBox(self)
      
        self.decorateNavbar()
    def onClickedNavToRecipe(self):
        self.RecipeController.handleNavigateToRecipe()
    
    def onClickedNavToCreate(self):
        self.RecipeController.handleNavigateToCreate()
    
    def onClickedNavToFavorite(self):
        self.RecipeController.handleNavigateToFavorite()

    @staticmethod
    def createMessageBoxWithInput(title, message, icon):
        box = QMessageBox()
        box.setIcon(icon)
        box.setText(message)
        box.setWindowTitle(title)
        box.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        box.setButtonText(QMessageBox.Ok, "Confirm")
        if box.exec() == QMessageBox.Ok:
            return True

    @staticmethod
    def createMessageBox(title, message, icon):
        box = QMessageBox()
        box.setIcon(icon)
        box.setText(message)
        box.setWindowTitle(title)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec()

    def showMessageBox(self):
        self.user_message_box.exec()
    
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
        
        self.user_btn.setObjectName("user_button")
        self.user_btn.setGeometry(QRect(1166, 17, 50, 50))
        self.user_icon = QIcon("static/asset/img/user.png")
        self.icon_size = QSize(28, 28)
        self.user_btn.setIcon(self.user_icon)
        self.user_btn.setIconSize(self.icon_size)
        self.user_btn.setCursor(Qt.PointingHandCursor)
        self.user_btn.clicked.connect(self.showMessageBox)
        
        
        self.user_message_box.setObjectName("user_message_box")
        self.user_message_box.setWindowTitle("User")
        self.setUserMessageBox()
        self.user_message_box.setFont(Theme.CHILLAX_REGULAR_16)
        
        self.setStyleSheet(Theme.get_stylesheet())

    def setUserMessageBox(self):
        create_time = self.RecipeController.getUserCreateTime()
        create_time = create_time[-3:]
        recipe_names = []
        for item in create_time:
            recipe_names.append(self.RecipeController.getRecipeName(item.recipe_id))
        create_timestamps = []
        if create_time is not None:
            if len(create_time) > 3:
                create_time = create_time[-3:]
            for i, item in enumerate(create_time):
                if i > 0:
                    create_timestamps.append(
                        " " * 31  + recipe_names[i] + " - " + str(item.add_timestamp))
                else:
                    create_timestamps.append(recipe_names[i] + " - " + str(item.add_timestamp))

        login_time = self.RecipeController.getUserLoginTime()
        if login_time is not None:
            login_timestamps = []
            for i, item in enumerate(login_time[:3]):
                if i > 0:
                    login_timestamps.append(" " * 23 + str(item.logged_in_at))

                else:
                    login_timestamps.append(str(item.logged_in_at))



        message = f"User_name: {self.RecipeController.getUser()}\n"
        message += "Created recipe at: " + "\n".join(create_timestamps) + "\n"
        message += "Logged in at: " + "\n".join(login_timestamps)

        self.user_message_box.setText(message)


