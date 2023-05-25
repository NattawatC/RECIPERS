from static.theme import Theme
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect, Signal, QEvent, Qt
from view.Navbar import NavigationBar
from view.RecipeView import RecipeCardScrollArea

class FavoriteView(NavigationBar):

    def __init__(self, Controller = None, Cards = None):
        super().__init__(Controller)

        self.cards = Cards
        favorite_label = QLabel("Save for the next time!", self)
        favorite_label.setObjectName("default_label")
        favorite_label.setFont(Theme.CHILLAX_REGULAR_40)
        favorite_label.setGeometry(QRect(336, 22, 460, 56))
        # favorite_label.setText(str(self.RecipeController.AuthController.getCurrentUser()) + "'s Favorite")

        total_s_frame = QFrame(self)
        total_s_frame.setObjectName("total_frame")
        total_s_frame.setGeometry(QRect(341, 83, 234, 81))

        save_logo = QLabel(total_s_frame)
        save_logo.setObjectName("create_bg")
        save_logo.setGeometry(QRect(13, 11, 58.8, 58.8))
        save_logo.setPixmap(QPixmap("static/asset/img/save.png"))
        save_logo.setScaledContents(True)

        self.save_num = QLabel("1", total_s_frame)
        self.save_num.setObjectName("default_label")
        self.save_num.setFont(Theme.CHILLAX_REGULAR_24)
        self.save_num.setGeometry(QRect(92, 17, 60, 20))
        self.save_num.setText(str(len(self.cards)))

        save_label = QLabel("Total Saved", total_s_frame)
        save_label.setObjectName("default_label")
        save_label.setFont(Theme.CHILLAX_REGULAR_20)
        save_label.setGeometry(QRect(92, 49, 130, 15))

        self.setStyleSheet(Theme.get_stylesheet())
        self.scrollArea = RecipeCardScrollArea(self.cards)
        self.scrollArea.setParent(self)

    def removeCard(self, card):
        self.save_num.setText(str(int(self.save_num.text()) - 1))
        self.scrollArea.removeCard(card)

    def setCards(self, cards):
        self.save_num.setText(str(len(cards)))
        self.scrollArea.refreshAll(cards)



