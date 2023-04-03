from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from theme import Theme


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

        create_dir = QLabel("Directions", create_frame)
        create_dir.setObjectName("default_label")
        create_dir.setFont(Theme.CHILLAX_REGULAR_20)
        create_dir.setGeometry(QRect(564, 25, 100, 35))

        self.create_dir_input = QTextEdit(create_frame)
        self.create_dir_input.setObjectName("create_bar")
        self.create_dir_input.setPlaceholderText("How do you make it...")
        self.create_dir_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_dir_input.setGeometry(QRect(564, 56, 278, 354))

        self.setStyleSheet(Theme.get_stylesheet())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = CreateView()
    window.show()
    sys.exit(app.exec())