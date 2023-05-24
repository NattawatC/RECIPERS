import sys

from PySide6.QtCore import QRect, QCoreApplication, QSize, Signal
from PySide6.QtGui import QPixmap, QFont, Qt, QCursor, QIcon
from PySide6.QtCore import QRect, QCoreApplication, QUrl
from PySide6.QtGui import QPixmap, QFont, Qt, QCursor
from PySide6.QtWidgets import *
from math import ceil


from static.theme import Theme
from view.Navbar import NavigationBar

class RecipeView(NavigationBar):
    def __init__(self, Controller = None):
        super().__init__(Controller)

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
        self.RecipeCardScrollArea = RecipeCardScrollArea(self.RecipeController.handleCreateRecipeCard())

        self.decorateWidgets()
        self.logout_btn.clicked.connect(self.RecipeController.handleLogout)
        self.RecipeCardScrollArea.connectFavoriteSignal(self.MarkAsFavorite)

        # self.search_bar.textChanged.connect(self.RecipeController.handleSearch)



    def MarkAsFavorite(self, recipe_id):
        self.RecipeController.handleMakeFavorite(recipe_id)

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
    def __init__(self, recipes = []):
        super().__init__()
        self.RecipeCardList = []
        self.setObjectName("default_scrollArea")
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setGeometry(QRect(336, 192, 840, 480))
        self.scroll_area_content = QWidget(self)
        self.scroll_area_content.setObjectName("default_scrollArea")
        self.recipes = recipes

        """Add Card"""

        if self.recipes is not None:
            self.createRecipeCard(self.recipes)
            if len(self.recipes) > 4:
                height = ceil((len(self.recipes) / 2)) * 230
                if len(self.recipes) % 2 == 0:
                    self.scroll_area_content.setMinimumSize(840, height)
                else:
                    self.scroll_area_content.setMinimumSize(840, height + 82)

        self.setWidget(self.scroll_area_content)

    def createRecipeCard(self,recipes):
        if len(recipes) > 1:
            newline = 0
            for i, recipe in enumerate(recipes):
                recipe_card = RecipeCard(recipe)
                if i % 2 == 0:
                    recipe_card.setGeometry(QRect(0, 0 + (230 * newline), 402, 194))

                else:
                    recipe_card.setGeometry(QRect(436, 0 + (230 * newline), 402, 194))
                    newline += 1
                recipe_card.setParent(self.scroll_area_content)
                self.RecipeCardList.append(recipe_card)
        else:
            recipe_card = RecipeCard(recipes[0])
            recipe_card.setGeometry(QRect(0, 0, 402, 194))
            recipe_card.setParent(self.scroll_area_content)
            self.RecipeCardList.append(recipe_card)

    def connectFavoriteSignal(self, func):
        for recipe_card in self.RecipeCardList:
            recipe_card.cardStarred.connect(func)



class RecipeCard(QWidget):
    cardStarred = Signal(int)

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
        # self.loadImageFromURL(recipe.image.strip(), recipe.id)

        card_name = QLabel(card_frame)
        card_name.setObjectName("default_label")
        card_name.setGeometry(QRect(204, 21, 146, 28))
        card_name.setFont(Theme.CHILLAX_REGULAR_20)
        card_name.setText(recipe.name)

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

        self.unStarred = QPushButton(card_frame)
        self.unStarred.setObjectName("unstared")
        self.unStarred.setGeometry(QRect(372, 13, 17, 17))
        icon = QIcon("static/asset/img/unstared.png")
        self.unStarred.setIcon(icon)
        self.unStarred.setIconSize(self.unStarred.size())
        self.unStarred.setCursor(QCursor(Qt.PointingHandCursor))
        self.unStarred.clicked.connect(self.MarkAsFavorite)

        self.setStyleSheet(Theme.get_stylesheet())

    def MarkAsFavorite(self):
        self.cardStarred.emit(self.recipe.id)



    # def loadImageFromURL(self, url, id):
    #     async with aiohttp.ClientSession() as session:
    #         tasks = []
    #         for url in urls:
    #             tasks.append(fetch_image(session, url))

    #         images = await asyncio.gather(*tasks)

    #     request = requests.get(url)
    #     try:
    #         with io.BytesIO(request.content) as img_bytes:
    #             image = Image.open(img_bytes)
    #             image = image.resize((170, 170), Image.ANTIALIAS)
    #             pixmap = QPixmap()
    #             pixmap.convertFromImage(ImageQt(image))
    #             self.card_img.setPixmap(pixmap)
    #     except UnidentifiedImageError:
    #         print(id, "is not an image file")
        # async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        #     async with session.get(url) as response:
        #         image_data = await response.read()
        # try:
        #     with io.BytesIO(image_data) as img_bytes:
        #         image = Image.open(img_bytes)
        #         image = image.resize((170, 170), Image.ANTIALIAS)
        #         pixmap = QPixmap()
        #         pixmap.convertFromImage(ImageQt(image))
        #         self.card_img.setPixmap(pixmap)
        # except UnidentifiedImageError:
        #     print(id, "is not an image file")
        # manager =  QNetworkAccessManager()
        # request = QNetworkRequest(QUrl(url))
        # reply = manager.get(request)
        # manager.get(reply)


        # request = requests.get(url)
        # image_data = io.BytesIO(request.content)
        # image = Image.open(image_data)
        # image = image.resize((170, 170), Image.ANTIALIAS)
        # pixmap = QPixmap()
        # pixmap.convertFromImage(ImageQt(image))
        # self.card_img.setPixmap(pixmap)
