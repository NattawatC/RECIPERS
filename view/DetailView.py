import sys

from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtGui import QPixmap, QFont, Qt
from PySide6.QtWidgets import *
from Navbar import NavigationBar
from static.theme import Theme


class DetailView(NavigationBar):
    def __init__(self, parent: QWidget = None):
        super.__init__(self, parent)
        
#--------------------------------------------------------------
        self.detail_frame = QFrame(self)
        self.detail_img = QLabel(self.detail_frame)
        self.detail_name = QLabel("Pork BBQ Stick", self.detail_frame)
        self.detail_cal = QLabel("Calories:", self.detail_frame)
        self.detial_cal_num = QLabel("125 Kcal", self.detail_frame)
        self.detail_prep_time = QLabel("Prep Time:", self.detail_frame)
        self.detail_prep_time_num = QLabel("30 mins", self.detail_frame)
        self.detail_cooking_time = QLabel("Cooking time:", self.detail_frame)
        self.detail_cooking_time_num = QLabel("30 mins", self.detail_frame)

        # Ingredients Scroll Area #

        self.detail_ingredients = QLabel("Ingredients", self.detail_frame)
        self.ingredients_scrollArea = QScrollArea(self.detail_frame)
        self.ingredients_scrollAreaContents = QWidget(self.ingredients_scrollArea)
        
        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignTop)
        
        self.ingredients_scrollAreaContents.setLayout(self.vBox)
        self.ingredients_scrollArea.setWidget(self.ingredients_scrollAreaContents)

        for i in range(1, 50):
            detail_ingredients = QLabel("Ingredients")
            detail_ingredients.setFont(Theme.CHILLAX_REGULAR_14)
            detail_ingredients.setObjectName("default_label")
            self.vBox.addWidget(detail_ingredients)

        self.ingredients_scrollAreaContents.setLayout(self.vBox)

        # Directions Scroll Area #

        self.detail_directions = QLabel("Directions", self.detail_frame)
        self.directions_scrollArea = QScrollArea(self.detail_frame)
        self.directions_scrollAreaContents = QWidget(self.directions_scrollArea)
       

        self.vBox = QVBoxLayout()
        self.vBox.setAlignment(Qt.AlignTop)
        self.directions_scrollAreaContents.setLayout(self.vBox)
        self.directions_scrollArea.setWidget(self.directions_scrollAreaContents)

        for i in range(1, 50):
            detail_directions = QLabel("Directions")
            detail_directions.setFont(Theme.CHILLAX_REGULAR_14)
            detail_directions.setObjectName("default_label")
            self.vBox.addWidget(detail_directions)

        self.directions_scrollAreaContents.setLayout(self.vBox)

        self.decorateDetailView()
        
    def decorateDetailView(self):
        self.detail_frame.setObjectName("detail_frame")
        self.detail_frame.setGeometry(QRect(336, 86, 880, 548))
        
        self.detail_img.setObjectName("detail_img")
        self.detail_img.setGeometry(QRect(19, 18, 168, 167))
        self.detail_img.setPixmap(QPixmap("../static/asset/img/BBQ.png"))

        self.detail_name.setObjectName("default_label")
        self.detail_name.setGeometry(QRect(212, 13, 300, 50))
        self.detail_name.setFont(Theme.CHILLAX_BOLD_36)
        
        self.detail_cal.setObjectName("default_label")
        self.detail_cal.setGeometry(QRect(212, 67, 127, 34))
        self.detail_cal.setFont(Theme.CHILLAX_REGULAR_24)
        
        self.detial_cal_num.setObjectName("default_label")
        self.detial_cal_num.setGeometry(QRect(315, 67, 127, 34))
        self.detial_cal_num.setFont(Theme.CHILLAX_REGULAR_24)
        
        self.detail_prep_time.setObjectName("default_label")
        self.detail_prep_time.setGeometry(QRect(212, 112, 127, 34))
        self.detail_prep_time.setFont(Theme.CHILLAX_REGULAR_24)
        
        self.detail_prep_time_num.setObjectName("default_label")
        self.detail_prep_time_num.setGeometry(QRect(337, 112, 127, 34))
        self.detail_prep_time_num.setFont(Theme.CHILLAX_REGULAR_24)

        self.detail_cooking_time.setObjectName("default_label")
        self.detail_cooking_time.setGeometry(QRect(212, 157, 164, 34))
        self.detail_cooking_time.setFont(Theme.CHILLAX_REGULAR_24)

        self.detail_cooking_time_num.setObjectName("default_label")
        self.detail_cooking_time_num.setGeometry(QRect(380, 157, 127, 34))
        self.detail_cooking_time_num.setFont(Theme.CHILLAX_REGULAR_24)
        
        self.detail_ingredients.setObjectName("default_label")
        self.detail_ingredients.setGeometry(QRect(45, 205, 111, 28))
        self.detail_ingredients.setFont(Theme.CHILLAX_REGULAR_20)
        
        self.ingredients_scrollArea.setObjectName("default_scrollArea")
        self.ingredients_scrollArea.setGeometry(QRect(45, 235, 378, 301))
        self.ingredients_scrollArea.setWidgetResizable(True)
        self.ingredients_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ingredients_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ingredients_scrollAreaContents.setObjectName("default_scrollAreaContents")
        self.ingredients_scrollAreaContents.setGeometry(QRect(409, 258, 31, 0))
        
        self.detail_directions.setObjectName("default_label")
        self.detail_directions.setGeometry(QRect(461, 205, 100, 28))
        self.detail_directions.setFont(Theme.CHILLAX_REGULAR_20)
        
        self.directions_scrollArea.setObjectName("default_scrollArea")
        self.directions_scrollArea.setGeometry(QRect(461, 235, 378, 301))
        self.directions_scrollArea.setWidgetResizable(True)
        self.directions_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.directions_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.directions_scrollAreaContents.setObjectName("default_scrollAreaContents")
        self.directions_scrollAreaContents.setGeometry(QRect(409, 258, 31, 0))
        
        self.setStyleSheet(Theme.get_stylesheet())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DetailView()
    window.show()
    sys.exit(app.exec_())