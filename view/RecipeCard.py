import io
import requests
from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtCore import Signal, QRect, Qt
from PySide6.QtGui import QCursor, QPixmap, QIcon
from PySide6.QtWidgets import QFrame, QWidget, QPushButton, QLabel

from static.theme import Theme


class RecipeCard(QWidget):
    cardStarred = Signal(int)

    def __init__(self, recipe = None, image_cache = None):
        super().__init__()
        self.setFixedSize(402, 194)
        self.isStarred = False
        self.recipe = recipe
        self.recipeId = recipe.id
        self.image_cache = image_cache

        self.card_frame = QFrame(self)
        self.card_img = QLabel(self.card_frame)
        # self.loadImageFromURL(recipe.image.strip())
        self.card_name = QLabel(self.card_frame)
        self.card_prep_time = QLabel("Prep. Time:", self.card_frame)
        self.card_prep_time_num = QLabel("30 mins", self.card_frame)
        self.card_cooking_time = QLabel("Cooking Time:", self.card_frame)
        self.card_cooking_time_num = QLabel("30 mins", self.card_frame)
        self.cal_time = QLabel("125 Kcal", self.card_frame)
        self.card_detail_btn = QPushButton("Detail", self.card_frame)
        # card_detail_btn.clicked.connect(self.RecipeController.handleMakeFavorite)
        self.arrow = QLabel(self.card_frame)
        self.unStarred = QPushButton(self.card_frame)
        self.icon = QIcon("static/asset/img/unstared.png")
        
        # self.unStarred.clicked.connect(self.emitFavoriteSignal)

        self.decorateRecipeCard()

    def decorateRecipeCard(self):
        self.card_frame.setObjectName("total_frame")
        self.card_frame.setFixedSize(402, 194)
        
        self.card_img.setObjectName("card_img")
        self.card_img.setGeometry(QRect(16, 13, 168, 168))
        
        self.card_name.setObjectName("default_label")
        self.card_name.setGeometry(QRect(204, 21, 146, 28))
        self.card_name.setFont(Theme.CHILLAX_REGULAR_20)
        self.card_name.setText(self.recipe.name)
        self.card_name.setWordWrap(True)
    
        self.card_prep_time.setObjectName("default_label")
        self.card_prep_time.setGeometry(QRect(204, 64, 141, 22))
        self.card_prep_time.setFont(Theme.CHILLAX_REGULAR_16)
        
        self.card_prep_time_num.setObjectName("default_label")
        self.card_prep_time_num.setGeometry(QRect(293, 64, 141, 22))
        self.card_prep_time_num.setFont(Theme.CHILLAX_REGULAR_16)
        
        self.card_cooking_time.setObjectName("default_label")
        self.card_cooking_time.setGeometry(QRect(204, 96, 141, 22))
        self.card_cooking_time.setFont(Theme.CHILLAX_REGULAR_16)
        
        self.card_cooking_time_num.setObjectName("default_label")
        self.card_cooking_time_num.setGeometry(QRect(317, 96, 141, 22))
        self.card_cooking_time_num.setFont(Theme.CHILLAX_REGULAR_16)
        
        self.cal_time.setObjectName("default_label")
        self.cal_time.setGeometry(QRect(204, 155, 141, 22))
        self.cal_time.setFont(Theme.CHILLAX_REGULAR_20)
        
        self.card_detail_btn.setObjectName("card_detail_btn")
        self.card_detail_btn.setGeometry(QRect(316, 153, 74, 22))
        self.card_detail_btn.setFont(Theme.CHILLAX_REGULAR_16)
        self.card_detail_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.arrow.setObjectName("arrow")
        self.arrow.setGeometry(QRect(372, 158, 13, 13))
        self.arrow.setPixmap(QPixmap("static/asset/img/right_arrow.png"))
        self.arrow.setScaledContents(True)
        
        self.unStarred.setObjectName("unstared")
        self.unStarred.setGeometry(QRect(372, 13, 17, 17))
        
        self.unStarred.setIcon(self.icon)
        self.unStarred.setIconSize(self.unStarred.size())
        self.unStarred.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.setStyleSheet(Theme.get_stylesheet())
        
    def getRecipeId(self):
        return self.recipeId

    def setFavorite(self, isFavorite):
        self.isStarred = isFavorite

    def loadImageFromURL(self, url):
        if self.image_cache is not None and url in self.image_cache:
            pixmap = self.image_cache[url]
            self.card_img.setPixmap(pixmap)

        else:
            request = requests.get(url)
            try:
                with io.BytesIO(request.content) as img_bytes:
                    image = Image.open(img_bytes)
                    image = image.resize((170, 170), Image.ANTIALIAS)
                    pixmap = QPixmap.fromImage(ImageQt(image))

                    # Cache the image for future use
                    self.image_cache[url] = pixmap
                    self.card_img.setPixmap(pixmap)
            except Exception as e:
                print(id, "is not an image file")

    def toggleStar(self):
        self.isStarred = not self.isStarred
        self.updateStar()

    def updateStar(self):
        if self.isStarred:
            icon = QIcon("static/asset/img/stared.png")
            self.unStarred.setIcon(icon)
            self.unStarred.setIconSize(self.unStarred.size())
        else:
            icon = QIcon("static/asset/img/unstared.png")
            self.unStarred.setIcon(icon)
            self.unStarred.setIconSize(self.unStarred.size())

        self.unStarred.repaint()
    