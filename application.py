from PySide6.QtWidgets import QStackedWidget
from PySide6.QtWidgets import QMainWindow
from controller.AuthController import AuthController
from static.theme import Theme
from controller.RecipeController import RecipeController

class Application(QMainWindow):

    def __init__(self):
        super().__init__()
        self.AuthController = None
        self.RecipeController = None
        self.stack = None
        self.setFixedSize(1280, 720)
        self.setWindowTitle("RECIPER")
        self.showAuthView()
        self.setStyleSheet(Theme.get_stylesheet())

    def handleLogin(self):
        if self.AuthController.handleLogin():
            self.stack = QStackedWidget()
            self.RecipeController = RecipeController(self, self.AuthController)
            for i in self.RecipeController.views:
                self.stack.addWidget(i)
            self.setCentralWidget(self.stack)
            self.NavigateToRecipe()
    def showAuthView(self):
        self.AuthController = AuthController(self)
        self.setCentralWidget(self.AuthController.AuthView)
        self.AuthController.AuthView.login_button.clicked.connect(self.handleLogin)

    def closeEvent(self, event):
        if self.AuthController.getCurrentUser() is not None:
            self.AuthController.handleLogout()
        event.accept()

    def NavigateToFavorite(self):
        self.stack.setCurrentIndex(1)

    def NavigateToRecipe(self):
        self.stack.setCurrentIndex(0)

    def NavigateToCreate(self):
        self.stack.setCurrentIndex(2)

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