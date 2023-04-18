from PySide6.QtWidgets import QStackedWidget
from model.AuthModel import User
from view.AuthView import AuthView

class PageController:
    def __init__(self, parent=None):
        self.model = User()
        self.AuthView = AuthView()
        self.view = QStackedWidget()
        # self.Authview.login_button.clicked.connect(self.login)
        self.view.show()

    def setPage(self,page):
        self.view.setCurrentIndex(page)

