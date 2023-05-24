from static.theme import Theme
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect, Signal, QEvent, Qt
from view.Navbar import NavigationBar

class FavoriteView(NavigationBar):

    def __init__(self, Controller = None):
        super().__init__(Controller)

        favorite_label = QLabel("Save for the next time!", self)
        favorite_label.setObjectName("default_label")
        favorite_label.setFont(Theme.CHILLAX_REGULAR_40)
        favorite_label.setGeometry(QRect(336, 22, 460, 56))
        favorite_label.setText(str(self.RecipeController.AuthController.getCurrentUser()) + "'s Favorite")

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



