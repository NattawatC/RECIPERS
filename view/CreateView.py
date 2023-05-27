import sys
from xml import etree

from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap, Qt, QCursor, QIntValidator
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
        self.create_cook_time = QLabel("Cooking Time (min)", self.create_frame)
        self.create_cook_time_input = QLineEdit(self.create_frame)
        self.create_serving = QLabel("Servings", self.create_frame)
        self.create_serving_input = QLineEdit(self.create_frame)
        self.create_category = QLabel("Category", self.create_frame)
        self.create_category_input = QLineEdit(self.create_frame)
        self.create_ing = QLabel("Ingredients", self.create_frame)
        self.create_ing_input = QTextEdit(self.create_frame)
        self.create_dir = QLabel("Directions", self.create_frame)
        self.create_dir_input = QTextEdit(self.create_frame)
        self.create_URL = QLabel("Image / URL", self.create_frame)
        self.create_URL_input = QLineEdit(self.create_frame)

        self.submit_btn = QPushButton("Submit", self)

        
       
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

        #Create Area
        self.create_menu_name.setObjectName("default_label")
        self.create_menu_name.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_menu_name.setGeometry(QRect(33, 25, 119, 31))

        self.create_menu_name_input.setObjectName("create_bar")
        self.create_menu_name_input.setPlaceholderText("Menu name")
        self.create_menu_name_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_menu_name_input.setGeometry(QRect(33, 56, 227, 33))
        self.create_menu_name_input.setMaxLength(50)
        self.create_menu_name_input.setClearButtonEnabled(True)
        
        self.create_cal.setObjectName("default_label")
        self.create_cal.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_cal.setGeometry(QRect(33, 105, 78, 31))
        self.create_cal.setWordWrap(True)


        self.create_cal_input.setObjectName("create_bar")
        self.create_cal_input.setPlaceholderText("Calories")
        self.create_cal_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_cal_input.setGeometry(QRect(33, 136, 227, 33))
        self.create_cal_input.setMaxLength(50)
        self.create_cal_input.setValidator(QIntValidator(0, 10000, self))
        self.create_cal_input.setClearButtonEnabled(True)
        
        self.create_cook_time.setObjectName("default_label")
        self.create_cook_time.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_cook_time.setGeometry(QRect(33, 185, 200, 31))


        self.create_cook_time_input.setObjectName("create_bar")
        self.create_cook_time_input.setPlaceholderText("hrs. or mins.")
        self.create_cook_time_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_cook_time_input.setGeometry(QRect(33, 216, 227, 33))
        self.create_cook_time_input.setMaxLength(50)
        self.create_cook_time_input.setClearButtonEnabled(True)
        self.create_cook_time_input.setValidator(QIntValidator(0, 1000, self))


        self.create_serving.setObjectName("default_label")
        self.create_serving.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_serving.setGeometry(QRect(33, 265, 170, 33))
        
        self.create_serving_input.setObjectName("create_bar")
        self.create_serving_input.setPlaceholderText("hrs. or mins.")
        self.create_serving_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_serving_input.setGeometry(QRect(33, 296, 227, 33))
        self.create_serving_input.setMaxLength(50)
        self.create_serving_input.setClearButtonEnabled(True)
        self.create_serving_input.setValidator(QIntValidator(0, 1000, self))
        
        self.create_category.setObjectName("default_label")
        self.create_category.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_category.setGeometry(QRect(33, 345, 134, 31))

        self.create_category_input.setObjectName("create_bar")
        self.create_category_input.setPlaceholderText("ie. Breakfast,Lunch, ...")
        self.create_category_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_category_input.setGeometry(QRect(33, 376, 227, 33))
        self.create_category_input.setClearButtonEnabled(True)
        
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
        self.create_dir_input.setGeometry(QRect(564, 56, 278, 284))
        self.create_dir_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.create_dir_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        self.create_URL.setObjectName("default_label")
        self.create_URL.setFont(Theme.CHILLAX_REGULAR_20)
        self.create_URL.setGeometry(QRect(564, 345, 164, 35))

        self.create_URL_input.setObjectName("create_bar")
        self.create_URL_input.setPlaceholderText("Image / URL")
        self.create_URL_input.setFont(Theme.CHILLAX_REGULAR_16)
        self.create_URL_input.setGeometry(QRect(564, 376, 278, 33))


        self.submit_btn.setObjectName("submit_button")
        self.submit_btn.setGeometry(QRect(1118, 647, 98, 27))
        self.submit_btn.setFont(Theme.CHILLAX_REGULAR_20)
        self.submit_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.submit_btn.clicked.connect(self.RecipeController.handleCreateRecipe)

        self.setStyleSheet(Theme.get_stylesheet())

    def recipeSubmitted(self):
        try:
            data = {"detail": self.getRecipeDetail(), "categories": self.getCategories(),
              "ingredients": self.getIngredients()
                , "instructions": self.getInstructions()}
            return data
        except Exception as e:
            self.createMessageBox("Error",str(e), QMessageBox.Critical)





    def getRecipeDetail(self) -> Exception | dict[str, str]:
        if self.validateInput(self.create_menu_name_input):
            self.create_menu_name_input.setFocus()
            self.create_menu_name_input.clear()
            raise Exception("Please enter a name")

        for i in range(len(self.create_menu_name_input.text())):
            if self.create_menu_name_input.text()[i].isdigit():
                self.create_menu_name_input.setFocus()
                self.create_menu_name_input.clear()
                raise Exception("Please enter a valid name")

        if self.validateInput(self.create_cal_input):
            self.create_cal_input.setFocus()
            self.create_cal_input.clear()
            raise Exception("Please enter a calorie amount")

        if self.validateInput(self.create_cook_time_input):
            self.create_cook_time_input.setFocus()
            self.create_cooke_time_input.clear()
            raise Exception("Please enter a cooking time")

        if self.validateInput(self.create_serving_input):
            self.create_serving_input.setFocus()
            self.create_serving_input.clear()
            raise Exception("Please enter a serving amount")

        if not self.isHTML(self.create_URL_input.text()):
            self.create_URL_input.setFocus()
            self.create_URL_input.clear()
            raise Exception("Please enter a valid URL")


        detail = {"name": self.create_menu_name_input.text(), "calories": self.create_cal_input.text(),
                  "duration_minute": self.create_cook_time_input.text(), "serving": self.create_serving_input.text(),
                  "image": self.create_URL_input.text().strip()}

        return detail

    @staticmethod
    def isHTML(text):
        if text == "":
            return True
        try:
            parser = etree.HTMLParser()
            etree.HTML(text, parser)
            return True
        except Exception:
            return False

    @staticmethod
    def validateInput(inputField):
        if type(inputField) == QTextEdit:
            return True
        else:
            if inputField.text() == "":
                return True
        return False

    @staticmethod
    def showWarningMessage(message):
        message_box = QMessageBox()
        # message_box.setIcon(QMessageBox.Warning)
        message_box.setObjectName("user_message_box")
        message_box.setWindowTitle("Warning")
        message_box.setText(message)
        message_box.exec()
        message_box.setStyleSheet(Theme.get_stylesheet())

    @staticmethod
    def showMessageBox(message):
        message_box = QMessageBox()
        # message_box.setIcon(QMessageBox.Information)
        message_box.setObjectName("user_message_box")
        message_box.setWindowTitle("Success")
        message_box.setText(message)
        message_box.exec()
        message_box.setStyleSheet(Theme.get_stylesheet())
        

    def getCategories(self) -> list[str] | None:

        if self.validateInput(self.create_category_input):
            self.create_category_input.setFocus()
            raise Exception("Please enter a category")

        if "," in self.create_category_input.text():
            categories = self.create_category_input.text().split(",")
        else:
            categories = [self.create_category_input.text()]
        return categories

    def getIngredients(self) -> list:
        ingredients = []

        input_text = self.create_ing_input.toPlainText()

        if "\n" in input_text:
            lines = input_text.strip().split("\n") if "\n" in input_text else [input_text]
            try:
                for line in lines:
                    if line != "":
                        parts = line.split(" ")

                    if len(parts) == 3 or (len(parts) == 2 and parts[2] == ""):
                        ingredients.append(parts)

                    elif parts[1].isnumeric():
                        self.create_ing_input.setFocus()
                        raise Exception("Amount must be a number")

                    else:
                        self.create_ing_input.setFocus()
                        raise Exception("Please enter ingredients in the format: 'name amount unit'")

            except Exception:
                self.create_ing_input.setFocus()
                raise Exception("Please enter ingredients in the format: 'name amount unit'")

        else:
            parts = input_text.split(" ")
            if len(parts) == 3 or (len(parts) == 2 and parts[2] == ""):
                ingredients.append(parts)

            elif parts[1].isnumeric():
                self.create_ing_input.setFocus()
                raise Exception("Amount must be a number")

            else:
                self.create_ing_input.setFocus()
                raise Exception("Please enter ingredients in the format: 'name amount unit'")

            return ingredients

        return ingredients

    def getInstructions(self) -> list:
        directions = []
        try:
            if self.create_dir_input.toPlainText() != "":
                if "\n" not in self.create_dir_input.toPlainText():
                    each = [self.create_dir_input.toPlainText()]
                    directions.append(each[0].split(".",1))
                else:
                    each = self.create_dir_input.toPlainText().split("\n")
                    for e in each:
                        if e != "" and "." in e and e[0] in "1234567890":
                            directions.append(e.split(".",1))
        except Exception:
            self.create_dir_input.setFocus()
            raise Exception("Please enter directions in the format: 'number. direction'")

        return directions

    def clearForm(self):
        self.create_menu_name_input.clear()
        self.create_cal_input.clear()
        self.create_cook_time_input.clear()
        self.create_serving_input.clear()
        self.create_category_input.clear()
        self.create_ing_input.clear()
        self.create_dir_input.clear()
        self.create_URL_input.clear()

    def setCreateCount(self, count):
        self.create_num.setText(str(count))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateView()
    window.show()
    sys.exit(app.exec_())