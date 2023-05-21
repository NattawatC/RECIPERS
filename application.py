from PySide6.QtWidgets import QStackedWidget
from PySide6.QtWidgets import QMainWindow
from controller.AuthController import AuthController
from static.theme import Theme
from view.AuthView import AuthView
from view.RecipeView import RecipeView
from view.FavoriteView import FavoriteView
from view.CreateView import CreateView

class Application(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(1280, 720)
        self.setWindowTitle("RECIPER")
        self.AuthView = AuthView(self)
        self.RecipeView = RecipeView(self)
        self.FavoriteView = FavoriteView(self)
        self.CreateView = CreateView(self)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.addWidget(self.AuthView)
        self.stack.addWidget(self.RecipeView)
        self.stack.addWidget(self.FavoriteView)
        self.stack.addWidget(self.CreateView)
        self.setStyleSheet(Theme.get_stylesheet())


    def showAuthView(self):
        self.AuthView.reset()
        self.stack.setCurrentIndex(0)


    def showRecipeView(self):
        self.stack.setCurrentIndex(1)
        self.RecipeView.RecipeController.setController(self.AuthView.AuthController)
        # self.setStyleSheet(Theme.get_stylesheet())

    def closeEvent(self, event):
        if self.AuthView.AuthController.getCurrentUser() is not None:
            self.AuthView.handleUserLogout()
            self.showAuthView()
        event.accept()

    def NavigateToFavorite(self):
        self.stack.setCurrentIndex(2)
        # self.FavoriteView.FavoriteController.setController(self.AuthView.AuthController)
        self.setStyleSheet(Theme.get_stylesheet())

    def NavigateToRecipe(self):
        self.stack.setCurrentIndex(1)
        self.RecipeView.RecipeController.setController(self.AuthView.AuthController)
        self.setStyleSheet(Theme.get_stylesheet())

    def NavigateToCreate(self):
        self.stack.setCurrentIndex(3)
        self.CreateView.CreateController.setController(self.AuthView.AuthController)
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

    # # def set_current_user(self, user: User) -> None:
    # #     self.current_user = user
    #
    # def move_to_login(self):
    #     self.current_user = None
    #     self.login_page.clear_input_field()
    #     self.setCurrentIndex(0)
    #
    # def move_to_home(self):
    #     self.setCurrentIndex(1)
    #
    # def start(self) -> None:
    #     "driver method."
    #     self.showFullScreen()
    #     self.show()