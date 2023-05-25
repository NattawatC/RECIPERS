
from PySide6.QtCore import QRect, QCoreApplication, QSize, Signal
from PySide6.QtGui import QPixmap, QFont, Qt, QCursor, QIcon
from PySide6.QtCore import QRect, QCoreApplication, QUrl
from PySide6.QtGui import QPixmap, QFont, Qt, QCursor
from PySide6.QtWidgets import *
from math import ceil

from static.theme import Theme
from view.Navbar import NavigationBar
from view.RecipeCard import RecipeCard


class RecipeView(NavigationBar):
    def __init__(self, Controller = None, Cards = None):
        super().__init__(Controller)

        self.cards = Cards
        self.recipe_label = QLabel("Welcome to,", self)
        self.recipe_label2 = QLabel("Recipes", self)
        self.logout_btn = QPushButton(self)
        self.search_bar = QLineEdit(self)
        self.search_logo = QLabel(self)
        self.total_c_frame = QFrame(self)
        self.create_logo = QLabel(self.total_c_frame)
        self.create_num = QLabel("120", self.total_c_frame)
        self.create_label = QLabel("Total Created", self.total_c_frame)
        self.total_s_frame = QFrame(self)
        self.save_logo = QLabel(self.total_s_frame)
        self.save_label = QLabel("Total Saved", self.total_s_frame)
        self.save_num = QLabel("120", self.total_s_frame)

        self.logout_btn.clicked.connect(self.RecipeController.handleLogout)
        self.RecipeCardScrollArea = RecipeCardScrollArea(self.cards)
        self.decorateWidgets()



        # self.search_bar.textChanged.connect(self.RecipeController.handleSearch)

    def setFavoriteCount(self, num):
        self.save_num.setText(str(num))

    def setCards(self, cards):
        self.RecipeCardScrollArea.refreshAll(cards)

    def onClickLogoutButton(self, func):
        self.logout_btn.clicked.connect(func)

    def decorateWidgets(self):
        self.recipe_label.setObjectName("default_label")
        self.recipe_label.setFont(Theme.CHILLAX_REGULAR_20)
        self.recipe_label.setGeometry(QRect(336, 92, 121, 16))

        self.recipe_label2.setObjectName("default_label")
        self.recipe_label2.setFont(Theme.CHILLAX_REGULAR_40)
        self.recipe_label2.setGeometry(QRect(336, 112, 171, 51))

        self.logout_btn.setObjectName("logout_button")
        self.logout_btn.setGeometry(QRect(215, 664, 43, 43))
        icon = QIcon("static/asset/img/logout.png")
        icon_size = QSize(25, 25)
        self.logout_btn.setIcon(icon)
        self.logout_btn.setIconSize(icon_size)

        self.search_logo.setObjectName("default_label")
        self.search_logo.setGeometry(QRect(336, 25, 35, 35))
        self.search_logo.setPixmap(QPixmap("static/asset/img/search.png"))
        self.search_logo.setScaledContents(True)

        self.search_bar.setObjectName("input_bar")
        self.search_bar.setPlaceholderText("Search recipe here")
        self.search_bar.setFont(Theme.CHILLAX_REGULAR_16)
        self.search_bar.setGeometry(QRect(381, 17, 520, 50))

        self.total_c_frame.setObjectName("total_frame")
        self.total_c_frame.setGeometry(QRect(520, 89, 234, 81))

        self.create_logo.setObjectName("create_bg")
        self.create_logo.setGeometry(QRect(13, 11, 58, 58))
        self.create_logo.setPixmap(QPixmap("static/asset/img/create.png"))
        self.create_logo.setScaledContents(True)

        self.create_num.setObjectName("default_label")
        self.create_num.setFont(Theme.CHILLAX_REGULAR_24)
        self.create_num.setGeometry(QRect(92, 17, 60, 20))

        self.create_label.setObjectName("default_label")
        self.create_label.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_label.setGeometry(QRect(92, 49, 130, 15))

        self.total_s_frame.setObjectName("total_frame")
        self.total_s_frame.setGeometry(QRect(789, 89, 234, 81))

        self.save_logo.setObjectName("create_bg")
        self.save_logo.setGeometry(QRect(13, 11, 58, 58))
        self.save_logo.setPixmap(QPixmap("static/asset/img/save.png"))
        self.save_logo.setScaledContents(True)

        self.save_num.setObjectName("default_label")
        self.save_num.setFont(Theme.CHILLAX_REGULAR_24)
        self.save_num.setGeometry(QRect(92, 17, 60, 20))


        self.save_label.setObjectName("default_label")
        self.save_label.setFont(Theme.CHILLAX_REGULAR_20)
        self.save_label.setGeometry(QRect(92, 49, 130, 15))

        self.RecipeCardScrollArea.setParent(self)
        self.styleSheet = Theme.get_stylesheet()




class RecipeCardScrollArea(QScrollArea):
    def __init__(self, recipeCards):
        super().__init__()
        self.setObjectName("default_scrollArea")
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setGeometry(QRect(336, 192, 840, 480))
        self.scroll_area_content = QWidget(self)
        self.scroll_area_content.setObjectName("default_scrollArea")
        self.recipeCards= recipeCards
        self.initContent()

        self.setWidget(self.scroll_area_content)


    def initContent(self):
        for recipe in self.recipeCards:
            recipe.setParent(self.scroll_area_content)
        height = (len(self.recipeCards) // 2)* 230
        if len(self.recipeCards) % 2 == 0:
            self.scroll_area_content.setMinimumSize(840, height)
        else:
            self.scroll_area_content.setMinimumSize(840, height + 82)

    def removeCard(self, recipeId):
        for recipeCard in self.recipeCards:
            if recipeCard.getRecipeId() == recipeId:
                recipeCard.setParent(None)
                self.recipeCards.remove(recipeCard)
        self.initContent()
        self.setWidget(self.scroll_area_content)

    def refreshAll(self, recipeCards):
        self.scroll_area_content = QWidget(self)
        self.scroll_area_content.setObjectName("default_scrollArea")
        self.recipeCards = recipeCards
        self.initContent()
        self.setWidget(self.scroll_area_content)


