from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from theme import Theme
from card_widget import CardWidget


"""
Log In page
"""


class LoginView(QWidget):
    switch_to_recipe = Signal()
    
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
        self.login_button.clicked.connect(self.switch_to_recipe)
        self.login_button.setFont(Theme.CHILLAX_REGULAR_20)
        self.login_button.setGeometry(QRect(59, 557, 520, 50))
        
        self.setStyleSheet(Theme.get_stylesheet())

    def get_username(self) -> str:
        return self.lineEdit_username.text()
    
    def get_password(self) -> str:
        return self.lineEdit_password.text()
    
    def set_login_button_listener(self, function) -> None:
        self.login_button.clicked.connect(function)


"""
Recipe page
"""


class RecipeView(QWidget):
    switch_to_favorite = Signal()
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
        nav_favorite.clicked.connect(self.switch_to_favorite)
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
        save_logo.setPixmap(QPixmap("src/asset/img/save.png"))
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

        self.setStyleSheet(Theme.get_stylesheet())

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


"""
Recipe Card
"""


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


"""
Detail Recipe Page
"""


class DetailView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1280, 720)

        bg_recipe_img = QLabel(self)
        bg_recipe_img.setObjectName("default_label")
        bg_recipe_img.setGeometry(QRect(0, -352, 1617, 1073))
        bg_recipe_img.setPixmap(QPixmap("src/asset/img/bg_recipe.png"))

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

        detail_frame = QFrame(self)
        detail_frame.setObjectName("detail_frame")
        detail_frame.setGeometry(QRect(336, 86, 880, 548))

        detail_img = QLabel(detail_frame)
        detail_img.setObjectName("detail_img")
        detail_img.setGeometry(QRect(19, 18, 168, 167))
        detail_img.setPixmap(QPixmap("src/asset/img/BBQ.png"))

        detail_name = QLabel("Pork BBQ Stick", detail_frame)
        detail_name.setObjectName("default_label")
        detail_name.setGeometry(QRect(212, 13, 300, 50))
        detail_name.setFont(Theme.CHILLAX_BOLD_36)

        detail_cal = QLabel("Calories:", detail_frame)
        detail_cal.setObjectName("default_label")
        detail_cal.setGeometry(QRect(212, 67, 127, 34))
        detail_cal.setFont(Theme.CHILLAX_REGULAR_24)

        detial_cal_num = QLabel("125 Kcal", detail_frame)
        detial_cal_num.setObjectName("default_label")
        detial_cal_num.setGeometry(QRect(315, 67, 127, 34))
        detial_cal_num.setFont(Theme.CHILLAX_REGULAR_24)

        detail_prep_time = QLabel("Prep Time:", detail_frame)
        detail_prep_time.setObjectName("default_label")
        detail_prep_time.setGeometry(QRect(212, 112, 127, 34))
        detail_prep_time.setFont(Theme.CHILLAX_REGULAR_24)

        detail_prep_time_num = QLabel("30 mins", detail_frame)
        detail_prep_time_num.setObjectName("default_label")
        detail_prep_time_num.setGeometry(QRect(337, 112, 127, 34))
        detail_prep_time_num.setFont(Theme.CHILLAX_REGULAR_24)

        detail_cooking_time = QLabel("Cooking time:", detail_frame)
        detail_cooking_time.setObjectName("default_label")
        detail_cooking_time.setGeometry(QRect(212, 157, 164, 34))
        detail_cooking_time.setFont(Theme.CHILLAX_REGULAR_24)

        detail_cooking_time_num = QLabel("30 mins", detail_frame)
        detail_cooking_time_num.setObjectName("default_label")
        detail_cooking_time_num.setGeometry(QRect(380, 157, 127, 34))
        detail_cooking_time_num.setFont(Theme.CHILLAX_REGULAR_24)

        # Ingredients Scroll Area #

        detail_ingredients = QLabel("Ingredients", detail_frame)
        detail_ingredients.setObjectName("default_label")
        detail_ingredients.setGeometry(QRect(45, 205, 111, 28))
        detail_ingredients.setFont(Theme.CHILLAX_REGULAR_20)

        self.ingredients_scrollArea = QScrollArea(detail_frame)
        self.ingredients_scrollArea.setObjectName("default_scrollArea")
        self.ingredients_scrollArea.setGeometry(QRect(45, 235, 378, 301))
        self.ingredients_scrollArea.setWidgetResizable(True)
        self.ingredients_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ingredients_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.ingredients_scrollAreaContents = QWidget(self.ingredients_scrollArea)
        self.ingredients_scrollAreaContents.setObjectName(
            "default_scrollAreaContents")
        self.ingredients_scrollAreaContents.setGeometry(QRect(409, 258, 31, 0))

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignTop)
        self.ingredients_scrollAreaContents.setLayout(self.vBox)
        self.ingredients_scrollArea.setWidget(self.ingredients_scrollAreaContents)

        for i in range(1,50):
            detail_ingredients = QLabel("Ingredients")
            detail_ingredients.setFont(Theme.CHILLAX_REGULAR_14)
            detail_ingredients.setObjectName("default_label")
            self.vBox.addWidget(detail_ingredients)

        self.ingredients_scrollAreaContents.setLayout(self.vBox)


        # Directions Scroll Area #

        detail_directions = QLabel("Directions", detail_frame)
        detail_directions.setObjectName("default_label")
        detail_directions.setGeometry(QRect(461, 205, 100, 28))
        detail_directions.setFont(Theme.CHILLAX_REGULAR_20)

        self.directions_scrollArea = QScrollArea(detail_frame)
        self.directions_scrollArea.setObjectName("default_scrollArea")
        self.directions_scrollArea.setGeometry(QRect(461, 235, 378, 301))
        self.directions_scrollArea.setWidgetResizable(True)
        self.directions_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.directions_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.directions_scrollAreaContents = QWidget(self.directions_scrollArea)
        self.directions_scrollAreaContents.setObjectName(
            "default_scrollAreaContents")
        self.directions_scrollAreaContents.setGeometry(QRect(409, 258, 31, 0))

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignTop)
        self.directions_scrollAreaContents.setLayout(self.vBox)
        self.directions_scrollArea.setWidget(self.directions_scrollAreaContents)

        for i in range(1,50):
            detail_directions = QLabel("Directions")
            detail_directions.setFont(Theme.CHILLAX_REGULAR_14)
            detail_directions.setObjectName("default_label")
            self.vBox.addWidget(detail_directions)

        self.directions_scrollAreaContents.setLayout(self.vBox)

        self.setStyleSheet(Theme.get_stylesheet())


"""
Favorite Page
"""


class FavoriteView(QWidget):
    
    
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1280, 720)
        
        bg_favorite = QLabel(self)
        bg_favorite.setObjectName("default_label")
        bg_favorite.setGeometry(QRect(0, -352, 1617, 1073))
        bg_favorite.setPixmap(QPixmap("src/asset/img/bg_recipe.png"))
        
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
        
        favorite_label = QLabel("Save for the next time!", self)
        favorite_label.setObjectName("default_label")
        favorite_label.setFont(Theme.CHILLAX_REGULAR_40)
        favorite_label.setGeometry(QRect(336, 22, 460, 56))
        
        total_s_frame = QFrame(self)
        total_s_frame.setObjectName("total_frame")
        total_s_frame.setGeometry(QRect(341, 83, 234, 81))

        save_logo = QLabel(total_s_frame)
        save_logo.setObjectName("create_bg")
        save_logo.setGeometry(QRect(13, 11, 58.8, 58.8))
        save_logo.setPixmap(QPixmap("src/asset/img/save.png"))
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


"""
Create Page
"""


class CreateView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1280, 720)

        bg_recipe_img = QLabel(self)
        bg_recipe_img.setObjectName("default_label")
        bg_recipe_img.setGeometry(QRect(0, -352, 1617, 1073))
        bg_recipe_img.setPixmap(QPixmap("src/asset/img/bg_recipe.png"))

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

        create_txt = QLabel("Create Your Masterpiece!", self)
        create_txt.setObjectName("default_label")
        create_txt.setFont(Theme.CHILLAX_REGULAR_40)
        create_txt.setGeometry(QRect(341, 15, 681, 61))

        total_c_frame = QFrame(self)
        total_c_frame.setObjectName("total_frame")
        total_c_frame.setGeometry(QRect(341, 83, 234, 81))

        create_logo = QLabel(total_c_frame)
        create_logo.setObjectName("create_bg")
        create_logo.setGeometry(QRect(13, 11, 58.8, 58.8))
        create_logo.setPixmap(QPixmap("src/asset/img/create.png"))
        create_logo.setScaledContents(True)

        create_num = QLabel("120", total_c_frame)
        create_num.setObjectName("default_label")
        create_num.setFont(Theme.CHILLAX_REGULAR_24)
        create_num.setGeometry(QRect(92, 17, 60, 20))

        create_label = QLabel("Total Created", total_c_frame)
        create_label.setObjectName("default_label")
        create_label.setFont(Theme.CHILLAX_REGULAR_20)
        create_label.setGeometry(QRect(92, 49, 130, 15))

        create_frame = QFrame(self)
        create_frame.setObjectName("create_frame")
        create_frame.setGeometry(QRect(341, 189, 875, 445))
        
        create_menu_name = QLabel("Menu Name", create_frame)
        create_menu_name.setObjectName("default_label")
        create_menu_name.setFont(Theme.CHILLAX_REGULAR_20)
        create_menu_name.setGeometry(QRect(33, 25, 119, 31))

        self.create_menu_name_input = QLineEdit(create_frame)
        self.create_menu_name_input.setObjectName("create_bar")
        self.create_menu_name_input.setPlaceholderText("Menu name")
        self.create_menu_name_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_menu_name_input.setGeometry(QRect(33, 56, 227, 33))

        create_cal = QLabel("Calories", create_frame)
        create_cal.setObjectName("default_label")
        create_cal.setFont(Theme.CHILLAX_REGULAR_20)
        create_cal.setGeometry(QRect(33, 132, 78, 31))

        self.create_cal_input = QLineEdit(create_frame)
        self.create_cal_input.setObjectName("create_bar")
        self.create_cal_input.setPlaceholderText("Calories")
        self.create_cal_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_cal_input.setGeometry(QRect(33, 163, 227, 33))

        create_prep_time = QLabel("Preparation Time", create_frame)
        create_prep_time.setObjectName("default_label")
        create_prep_time.setFont(Theme.CHILLAX_REGULAR_20)
        create_prep_time.setGeometry(QRect(33, 239, 170, 33))

        self.create_prep_time_input = QLineEdit(create_frame)
        self.create_prep_time_input.setObjectName("create_bar")
        self.create_prep_time_input.setPlaceholderText("hrs. or mins.")
        self.create_prep_time_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_prep_time_input.setGeometry(QRect(33, 270, 227, 33))

        create_cook_time = QLabel("Cooking Time", create_frame)
        create_cook_time.setObjectName("default_label")
        create_cook_time.setFont(Theme.CHILLAX_REGULAR_20)
        create_cook_time.setGeometry(QRect(33, 346, 134, 31))

        self.create_cook_time_input = QLineEdit(create_frame)
        self.create_cook_time_input.setObjectName("create_bar")
        self.create_cook_time_input.setPlaceholderText("hrs. or mins.")
        self.create_cook_time_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_cook_time_input.setGeometry(QRect(33, 377, 227, 33))

        create_ing = QLabel("Ingredients", create_frame)
        create_ing.setObjectName("default_label")
        create_ing.setFont(Theme.CHILLAX_REGULAR_20)
        create_ing.setGeometry(QRect(290, 25, 111, 35))

        self.create_ing_input = QTextEdit(create_frame)
        self.create_ing_input.setObjectName("create_bar")
        self.create_ing_input.setPlaceholderText("What do you need...")
        self.create_ing_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_ing_input.setGeometry(QRect(290, 56, 244, 354))
        self.create_ing_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.create_ing_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        create_dir = QLabel("Directions", create_frame)
        create_dir.setObjectName("default_label")
        create_dir.setFont(Theme.CHILLAX_REGULAR_20)
        create_dir.setGeometry(QRect(564, 25, 100, 35))

        self.create_dir_input = QTextEdit(create_frame)
        self.create_dir_input.setObjectName("create_bar")
        self.create_dir_input.setPlaceholderText("How do you make it...")
        self.create_dir_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_dir_input.setGeometry(QRect(564, 56, 278, 354))
        self.create_dir_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.create_dir_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setStyleSheet(Theme.get_stylesheet())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    
    login = LoginView()
    recipe = RecipeView()
    fav = FavoriteView()
    
    stacked_widget = QStackedWidget()
    stacked_widget.addWidget(login)
    stacked_widget.addWidget(recipe)
    stacked_widget.addWidget(fav)
    
    login.switch_to_recipe.connect(lambda: stacked_widget.setCurrentIndex(1))
    recipe.switch_to_favorite.connect(lambda: stacked_widget.setCurrentIndex(2))
    
    window = QWidget()
    window.setLayout(QVBoxLayout())
    window.layout().addWidget(stacked_widget)
    
    # window = LoginView()
    window.show()
    sys.exit(app.exec())