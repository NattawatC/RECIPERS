from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtGui import QPixmap, QFont, Qt
from PySide6.QtWidgets import *

from static.theme import Theme
from view.Navbar import NavigationBar
class CreateView(NavigationBar):
    def __init__(self, Controller = None):
        super().__init__(Controller)
        
#------------------------------------------------------------------
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
        create_logo.setPixmap(QPixmap("static/asset/img/create.png"))
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