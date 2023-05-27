from PySide6.QtWidgets import QStackedWidget
from PySide6.QtWidgets import QMainWindow
from controller.AuthController import AuthController
from static.theme import Theme
from controller.RecipeController import RecipeController
from functools import partial
from view.RegisterView import RegisterView

class Application(QMainWindow):

    def __init__(self):
        super().__init__()
        self.AuthController = AuthController(self)
        self.RecipeController = None
        self.stack = None
        self.setFixedSize(1280, 720)
        self.imageCache = {}
        self.setWindowTitle("RECIPER")
        self.showAuthView()
        
        self.setStyleSheet(Theme.get_stylesheet())


    def handleLogin(self):
        if self.AuthController.handleLogin():
            self.stack = QStackedWidget()
            self.RecipeController = RecipeController(self, self.imageCache, self.AuthController)
            for i in self.RecipeController.views:
                self.stack.addWidget(i)
            self.setCentralWidget(self.stack)
            self.NavigateToRecipe()

    def showAuthView(self):
        self.stack = QStackedWidget()
        self.AuthController = AuthController(self)
        self.stack.addWidget(self.AuthController.AuthView)
        self.stack.addWidget(self.AuthController.RegisterView)
        self.setCentralWidget(self.stack)
        self.AuthController.AuthView.login_button.clicked.connect(self.handleLogin)
        self.AuthController.AuthView.register_button.clicked.connect(self.NavigateToRegister)

        #Vega------------------------------------
    def passwordIsValid(self):
        if self.AuthController.isRegisterValid == True: 
            self.AuthController.RegisterView.start_button.clicked.connect(self.handleRegister)
        #Vega------------------------------------

    def returnToAuth(self):
        self.AuthController.handleRegister()
        self.stack.setCurrentIndex(0)

    def NavigateToRegister(self):
        self.stack.setCurrentIndex(1)
    
    def NavigateToAuth(self):
        self.stack.setCurrentIndex(0)

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

    def NavigateToDetail(self):
        self.stack.setCurrentIndex(3)

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