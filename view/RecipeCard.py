import io
import requests
from PIL import Image
from PIL.ImageQt import ImageQt
from PySide6.QtCore import Signal, QRect, Qt, QPoint, QMimeData, QSize
from PySide6.QtGui import QCursor, QPixmap, QIcon, QPainter, QDrag, QMouseEvent
from PySide6.QtWidgets import QFrame, QWidget, QPushButton, QLabel
import random

from static.theme import Theme

class RecipeCard(QWidget):
    cardStarred = Signal(int)

    def __init__(self, recipe = None, imageCache = None):
        super().__init__()
        self.setFixedSize(402, 194)
        self.isStarred = False
        self.recipe = recipe
        self.imageCache = imageCache

        self.card_frame = QFrame(self)
        self.card_img = QLabel(self.card_frame)
        self.loadImageFromUrl(recipe.image.strip(), self.recipe.id)
        self.card_name = QLabel(self.card_frame)
        self.card_serving = QLabel("Serving:", self.card_frame)
        self.card_serving_num = QLabel(str(self.recipe.serving), self.card_frame)
        self.card_cooking_time = QLabel("Cooking Time:", self.card_frame)
        self.card_cooking_time_num = QLabel("30 mins", self.card_frame)
        self.cal_time = QLabel(f"{random.randint(100,1000)} Kcal", self.card_frame)
        self.card_detail_btn = QPushButton("Detail", self.card_frame)
        self.arrow = QLabel(self.card_frame)
        self.unStarred = QPushButton(self.card_frame)
        self.starIcon = QIcon("static/asset/img/unstared.png")
        self.delete_btn = QPushButton(self.card_frame)
        self.deleteIcon = QIcon("static/asset/img/delete.png")
        self.decorateRecipeCard()

    def decorateRecipeCard(self):
        self.card_frame.setObjectName("total_frame")
        self.card_frame.setFixedSize(402, 194)
        
        self.card_img.setObjectName("card_img")
        self.card_img.setGeometry(QRect(16, 13, 168, 168))
        
        self.card_name.setObjectName("default_label")
        self.card_name.setGeometry(QRect(204, 21, 164, 55))
        self.card_name.setFont(Theme.CHILLAX_REGULAR_20)
        self.card_name.setText(self.recipe.name)
        self.card_name.setWordWrap(True)
    
        self.card_serving.setObjectName("default_label")
        self.card_serving.setGeometry(QRect(204, 87, 141, 22))
        self.card_serving.setFont(Theme.CHILLAX_REGULAR_16)
        
        self.card_serving_num.setObjectName("default_label")
        self.card_serving_num.setGeometry(QRect(293, 87, 141, 22))
        self.card_serving_num.setFont(Theme.CHILLAX_REGULAR_16)
        
        self.card_cooking_time.setObjectName("default_label")
        self.card_cooking_time.setGeometry(QRect(204, 119, 141, 22))
        self.card_cooking_time.setFont(Theme.CHILLAX_REGULAR_16)
        
        self.card_cooking_time_num.setObjectName("default_label")
        self.card_cooking_time_num.setGeometry(QRect(317, 119, 141, 22))
        self.card_cooking_time_num.setFont(Theme.CHILLAX_REGULAR_16)
        self.card_cooking_time_num.setText(f"{self.recipe.duration_minute} mins")
        
        self.cal_time.setObjectName("default_label")
        self.cal_time.setGeometry(QRect(204, 155, 141, 22))
        self.cal_time.setFont(Theme.CHILLAX_REGULAR_20)

        self.card_detail_btn.setObjectName("card_detail_btn")
        self.card_detail_btn.setGeometry(QRect(290, 153, 74, 22))
        self.card_detail_btn.setFont(Theme.CHILLAX_REGULAR_16)
        self.card_detail_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.arrow.setObjectName("arrow")
        self.arrow.setGeometry(QRect(345, 158, 13, 13))
        self.arrow.setPixmap(QPixmap("static/asset/img/right_arrow.png"))
        self.arrow.setScaledContents(True)

        self.delete_btn.setObjectName("delete_button")
        self.delete_btn.setGeometry(QRect(372, 153, 22, 22))
        self.delete_btn.setIcon(self.deleteIcon)
        deleteSize = QSize(15, 15)
        self.delete_btn.setIconSize(deleteSize)
        self.delete_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_btn.hide()
        
        self.unStarred.setObjectName("unstared")
        self.unStarred.setGeometry(QRect(372, 13, 17, 17))
        self.unStarred.setIcon(self.starIcon)
        self.unStarred.setIconSize(self.unStarred.size())
        self.unStarred.setCursor(QCursor(Qt.PointingHandCursor))

        self.setStyleSheet(Theme.get_stylesheet())

    # def mousePressEvent(self, event: QMouseEvent):
    #     if event.button() == Qt.LeftButton:
    #         self.startDrag()

    # def startDrag(self):
    #     self.deleteLater()
    #     # Create a custom mime data object to hold the pixmap data
    #     mime_data = QMimeData()
    #     mime_data.setData(self.recipe.name, str(self.recipe.id).encode())
    #
    #     # Create a drag object and set the custom mime data
    #     drag = QDrag(self)
    #     drag.setMimeData(mime_data)
    #
    #
    #     # Execute the drag operation and track the result
    #     result = drag.exec_(Qt.MoveAction)
    #     if result == Qt.MoveAction:  # Widget was moved within the program
    #         self.show()  # Show the widget again

    def getRecipeId(self):
        return self.recipe.id

    def setFavorite(self, isFavorite):
        self.isStarred = isFavorite

    def loadImageFromUrl(self, url, recipe_id = None):
        if self.imageCache is not None and url in self.imageCache:
            pixmap = self.imageCache[url]
            self.card_img.setPixmap(pixmap)

        else:
            try:
                request = requests.get(url)
                with io.BytesIO(request.content) as img_bytes:
                    image = Image.open(img_bytes)
                    image = image.resize((170, 170), Image.ANTIALIAS)
                    pixmap = QPixmap.fromImage(ImageQt(image))

                    # Cache the image for future use
                    self.imageCache[url] = pixmap
                    self.card_img.setPixmap(pixmap)
            except Exception as e:
                print(recipe_id, "is not an image file")

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
    