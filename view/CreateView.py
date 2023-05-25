from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtGui import QPixmap, QFont, Qt, QCursor
from PySide6.QtWidgets import *

from static.theme import Theme
from view.Navbar import NavigationBar
class CreateView(NavigationBar):
    def __init__(self, Controller = None):
        super().__init__(Controller)
#------------------------------------------------------------------
        self.create_txt = QLabel("Create Your Masterpiece!", self)
        self.total_c_frame = QFrame(self)
        self.create_logo = QLabel(self.total_c_frame)
        self.create_num = QLabel("120", self.total_c_frame)
        self.create_label = QLabel("Total Created", self.total_c_frame)
        self.create_frame = QFrame(self)
        self.create_menu_name = QLabel("Menu Name", self.create_frame)
        self.create_menu_name_input = QLineEdit(self.create_frame)
        self.create_cal = QLabel("Calories", self.create_frame)
        self.create_cal_input = QLineEdit(self.create_frame)
        self.create_prep_time = QLabel("Preparation Time", self.create_frame)
        self.create_prep_time_input = QLineEdit(self.create_frame)
        self.create_cook_time = QLabel("Cooking Time", self.create_frame)
        self.create_cook_time_input = QLineEdit(self.create_frame)
        self.create_ing = QLabel("Ingredients", self.create_frame)
        self.create_ing_input = QTextEdit(self.create_frame)
        self.create_dir = QLabel("Directions", self.create_frame)
        self.create_dir_input = QTextEdit(self.create_frame)
       
        self.decorateCreateView()

    def decorateCreateView(self):
        self.create_txt.setObjectName("default_label")
        self.create_txt.setFont(Theme.CHILLAX_REGULAR_40)
        self.create_txt.setGeometry(QRect(341, 15, 681, 61))

        self.total_c_frame.setObjectName("total_frame")
        self.total_c_frame.setGeometry(QRect(341, 83, 234, 81))
        
        self.create_logo.setObjectName("create_bg")
        self.create_logo.setGeometry(QRect(13, 11, 58.8, 58.8))
        self.create_logo.setPixmap(QPixmap("static/asset/img/create.png"))
        self.create_logo.setScaledContents(True)
        
        self.create_num.setObjectName("default_label")
        self.create_num.setFont(Theme.CHILLAX_REGULAR_24)
        self.create_num.setGeometry(QRect(92, 17, 60, 20))
        
        self.create_label.setObjectName("default_label")
        self.create_label.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_label.setGeometry(QRect(92, 49, 130, 15))

        self.create_frame.setObjectName("create_frame")
        self.create_frame.setGeometry(QRect(341, 189, 875, 445))

        self.create_menu_name.setObjectName("default_label")
        self.create_menu_name.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_menu_name.setGeometry(QRect(33, 25, 119, 31))

        self.create_menu_name_input.setObjectName("create_bar")
        self.create_menu_name_input.setPlaceholderText("Menu name")
        self.create_menu_name_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_menu_name_input.setGeometry(QRect(33, 56, 227, 33))
        
        self.create_cal.setObjectName("default_label")
        self.create_cal.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_cal.setGeometry(QRect(33, 132, 78, 31))
        
        self.create_cal_input.setObjectName("create_bar")
        self.create_cal_input.setPlaceholderText("Calories")
        self.create_cal_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_cal_input.setGeometry(QRect(33, 163, 227, 33))
        
        self.create_prep_time.setObjectName("default_label")
        self.create_prep_time.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_prep_time.setGeometry(QRect(33, 239, 170, 33))
        
        self.create_prep_time_input.setObjectName("create_bar")
        self.create_prep_time_input.setPlaceholderText("hrs. or mins.")
        self.create_prep_time_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_prep_time_input.setGeometry(QRect(33, 270, 227, 33))
        
        self.create_cook_time.setObjectName("default_label")
        self.create_cook_time.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_cook_time.setGeometry(QRect(33, 346, 134, 31))
        
        self.create_cook_time_input.setObjectName("create_bar")
        self.create_cook_time_input.setPlaceholderText("hrs. or mins.")
        self.create_cook_time_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_cook_time_input.setGeometry(QRect(33, 377, 227, 33))
        
        self.create_ing.setObjectName("default_label")
        self.create_ing.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_ing.setGeometry(QRect(290, 25, 111, 35))

        self.create_ing_input.setObjectName("create_bar")
        self.create_ing_input.setPlaceholderText("What do you need...")
        self.create_ing_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_ing_input.setGeometry(QRect(290, 56, 244, 354))
        self.create_ing_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.create_ing_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.create_dir.setObjectName("default_label")
        self.create_dir.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_dir.setGeometry(QRect(564, 25, 100, 35))
        
        self.create_dir_input.setObjectName("create_bar")
        self.create_dir_input.setPlaceholderText("How do you make it...")
        self.create_dir_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_dir_input.setGeometry(QRect(564, 56, 278, 354))
        self.create_dir_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.create_dir_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.submit_btn = QPushButton("Submit", self)
        self.submit_btn.setObjectName("submit_button")
        self.submit_btn.setGeometry(QRect(1118, 647, 98, 27))
        self.submit_btn.setFont(Theme.CHILLAX_REGULAR_20)
        self.submit_btn.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.setStyleSheet(Theme.get_stylesheet())