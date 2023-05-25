import sys

from PySide6.QtWidgets import QApplication


class DetailView(QWidget):
    def __init__(self, parent: QWidget = None):
        QWidget.__init__(self, parent)
        self.setFixedSize(1280, 720)

        bg_recipe_img = QLabel(self)
        bg_recipe_img.setObjectName("default_label")
        bg_recipe_img.setGeometry(QRect(0, -352, 1617, 1073))
        bg_recipe_img.setPixmap(QPixmap("../static/asset/img/bg_recipe.png"))

        nav_bar = QFrame(self)
        nav_bar.setObjectName("frame")
        nav_bar.setGeometry(QRect(0, 0, 271, 720))

        label_logo = QLabel(nav_bar)
        label_logo.setObjectName("default_label")
        label_logo.setGeometry(QRect(36, 22, 199, 43))
        label_logo.setPixmap(QPixmap("../static/asset/img/logo_recipe.png"))
        label_logo.setScaledContents(True)

        nav_recipe_logo = QLabel(nav_bar)
        nav_recipe_logo.setObjectName("default_label")
        nav_recipe_logo.setGeometry(QRect(55, 141, 35, 35))
        nav_recipe_logo.setPixmap(QPixmap("../static/asset/img/nav_recipe.png"))
        nav_recipe_logo.setScaledContents(True)

        nav_recipe = QPushButton("Recipes", nav_bar)
        nav_recipe.setObjectName("nav_button")
        nav_recipe.setFont(Theme.CHILLAX_REGULAR_24)
        nav_recipe.setGeometry(QRect(123, 147, 91, 21))

        nav_create_logo = QLabel(nav_bar)
        nav_create_logo.setObjectName("default_label")
        nav_create_logo.setGeometry(QRect(58, 207, 35, 35))
        nav_create_logo.setPixmap(QPixmap("../static/asset/img/nav_create.png"))
        nav_create_logo.setScaledContents(True)

        nav_create = QPushButton("Create", nav_bar)
        nav_create.setObjectName("nav_button")
        nav_create.setFont(Theme.CHILLAX_REGULAR_24)
        nav_create.setGeometry(QRect(123, 214, 91, 21))

        nav_favorite_logo = QLabel(nav_bar)
        nav_favorite_logo.setObjectName("default_label")
        nav_favorite_logo.setGeometry(QRect(54, 273, 40, 40))
        nav_favorite_logo.setPixmap(QPixmap("../static/asset/img/nav_favorite.png"))
        nav_favorite_logo.setScaledContents(True)

        nav_favorite = QPushButton("Favorite", nav_bar)
        nav_favorite.setObjectName("nav_button")
        nav_favorite.setFont(Theme.CHILLAX_REGULAR_24)
        nav_favorite.setGeometry(QRect(123, 283, 101, 21))

        detail_frame = QFrame(self)
        detail_frame.setObjectName("detail_frame")
        detail_frame.setGeometry(QRect(336, 86, 880, 548))

        detail_img = QLabel(detail_frame)
        detail_img.setObjectName("detail_img")
        detail_img.setGeometry(QRect(19, 18, 168, 167))
        detail_img.setPixmap(QPixmap("../static/asset/img/BBQ.png"))

        detail_name = QLabel("Pork BBQ Stick", detail_frame)
        detail_name.setObjectName("default_label")
        detail_name.setGeometry(QRect(212, 13, 300, 50))
        detail_name.setFont(Theme.CHILLAX_BOLD_36)

        detail_cal = QLabel("Calories:", detail_frame)
        detail_cal.setObjectName("default_label")
        detail_cal.setGeometry(QRect(212, 67, 127, 34))
        detail_cal.setFont(Theme.CHILLAX_REGULAR_24)

        detial_cal_num = QLabel("125 Kcal", detail_frame)
        detial_cal_num.setObjectName("default_label")
        detial_cal_num.setGeometry(QRect(315, 67, 127, 34))
        detial_cal_num.setFont(Theme.CHILLAX_REGULAR_24)

        detail_prep_time = QLabel("Prep Time:", detail_frame)
        detail_prep_time.setObjectName("default_label")
        detail_prep_time.setGeometry(QRect(212, 112, 127, 34))
        detail_prep_time.setFont(Theme.CHILLAX_REGULAR_24)

        detail_prep_time_num = QLabel("30 mins", detail_frame)
        detail_prep_time_num.setObjectName("default_label")
        detail_prep_time_num.setGeometry(QRect(337, 112, 127, 34))
        detail_prep_time_num.setFont(Theme.CHILLAX_REGULAR_24)

        detail_cooking_time = QLabel("Cooking time:", detail_frame)
        detail_cooking_time.setObjectName("default_label")
        detail_cooking_time.setGeometry(QRect(212, 157, 164, 34))
        detail_cooking_time.setFont(Theme.CHILLAX_REGULAR_24)

        detail_cooking_time_num = QLabel("30 mins", detail_frame)
        detail_cooking_time_num.setObjectName("default_label")
        detail_cooking_time_num.setGeometry(QRect(380, 157, 127, 34))
        detail_cooking_time_num.setFont(Theme.CHILLAX_REGULAR_24)

        # Ingredients Scroll Area #

        detail_ingredients = QLabel("Ingredients", detail_frame)
        detail_ingredients.setObjectName("default_label")
        detail_ingredients.setGeometry(QRect(45, 205, 111, 28))
        detail_ingredients.setFont(Theme.CHILLAX_REGULAR_20)

        self.ingredients_scrollArea = QScrollArea(detail_frame)
        self.ingredients_scrollArea.setObjectName("default_scrollArea")
        self.ingredients_scrollArea.setGeometry(QRect(45, 235, 378, 301))
        self.ingredients_scrollArea.setWidgetResizable(True)
        self.ingredients_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ingredients_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ingredients_scrollAreaContents = QWidget(self.ingredients_scrollArea)
        self.ingredients_scrollAreaContents.setObjectName(
            "default_scrollAreaContents")
        self.ingredients_scrollAreaContents.setGeometry(QRect(409, 258, 31, 0))

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

        detail_directions = QLabel("Directions", detail_frame)
        detail_directions.setObjectName("default_label")
        detail_directions.setGeometry(QRect(461, 205, 100, 28))
        detail_directions.setFont(Theme.CHILLAX_REGULAR_20)

        self.directions_scrollArea = QScrollArea(detail_frame)
        self.directions_scrollArea.setObjectName("default_scrollArea")
        self.directions_scrollArea.setGeometry(QRect(461, 235, 378, 301))
        self.directions_scrollArea.setWidgetResizable(True)
        self.directions_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.directions_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.directions_scrollAreaContents = QWidget(self.directions_scrollArea)
        self.directions_scrollAreaContents.setObjectName(
            "default_scrollAreaContents")
        self.directions_scrollAreaContents.setGeometry(QRect(409, 258, 31, 0))

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

        self.setStyleSheet(Theme.get_stylesheet())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DetailView()
    window.show()
    sys.exit(app.exec_())