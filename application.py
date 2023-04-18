from PySide6.QtWidgets import QStackedWidget
from PySide6.QtWidgets import QMainWindow
from controller.AuthController import AuthController
from static.theme import Theme
from view.AuthView import AuthView
from view.RecipeView import RecipeView


#
# from models import *
# from views import *
# # from controllers import *
#
#
class Application(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(1280, 720)
        self.setWindowTitle("RECIPER")
        self.AuthView = AuthView(self)
        self.RecipeView = RecipeView(self)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.addWidget(self.AuthView)
        self.stack.addWidget(self.RecipeView)
        self.setStyleSheet(Theme.get_stylesheet())


    def showAuthView(self):
        self.stack.setCurrentIndex(0)

    def showRecipeView(self):
        self.stack.setCurrentIndex(1)

        # self.current_user = None
#
#         # Login Page
#         # home Page
#         self.recipe_page = RecipeView(self)
#
        # start page

        # self.detail_page = DetailView(self)

        # self.stack.addWidget(self.page)
        self.setStyleSheet(Theme.get_stylesheet())

    # def initialize_page(self) -> None:
    #     "set up method for user."
    #     if self.current_user is None:
    #         return
    #
    #     self.recipe_page = RecipeView(
    #         self, RecipeView(), RecipeModel(), self.current_user)
    #
    #     # self.order_page = OrderPage(OrderView(), OrderModel())
    #
    #     # replace widget if already exist
    #     self.insertWidget(1, self.recipe_page.view)
    #     self.move_to_home()

#     # def set_current_user(self, user: User) -> None:
#     #     self.current_user = user
#
#     def move_to_login(self):
#         self.current_user = None
#         self.login_page.clear_input_field()
#         self.setCurrentIndex(0)
#
#     def move_to_home(self):
#         self.setCurrentIndex(1)
#
#     def start(self) -> None:
#         "driver method."
#         self.showFullScreen()
#         self.show()

