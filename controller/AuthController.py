from model.AuthModel import AuthModel
from view.AuthView import AuthView
import time
from view.RegisterView import RegisterView
from PySide6.QtCore import Qt

class AuthController:
    def __init__(self, MainWindow):
        self.model = AuthModel()
        self.AuthView = AuthView(self)
        self.RegisterView = RegisterView(self)
        self.mainWindow = MainWindow
        self.__currentUser = None
        self.isLoginSuccess = False
        self.__currentUserLog = None

    def authenticate(self,username, password):
        if self.model.validate(username, password):
            self.__currentUser = self.model.getUser(username)
            self.isLoginSuccess = True
        else:
            self.isLoginSuccess = False
        return self.isLoginSuccess

    def checkpassword(self, password):
        pass

    def handleLogin(self):
        self.authenticate(self.AuthView.lineEdit_username.text(), self.AuthView.lineEdit_password.text())
        if self.isLoginSuccess:
            return self.__currentUser
        else:
            self.AuthView.showError("Invalid username or password")

    def handleRegister(self):
        pass

    def handleLogout(self, user=None):
        self.model.logout(self.getCurrentUser())
        self.setCurrentUser(None)
        print("log out!")

    def getCurrentUser(self):
        return self.__currentUser

    def setCurrentUser(self, user):
        self.__currentUser = user

    def getCurrentUserLog(self):
        self.__currentUserLog = self.model.getUserLogTime(time.strftime('%Y-%m-%d %H:%M:%S'))
        return self.__currentUserLog


    # def NavigateToRegister(self):
    #     print(self.AuthView)
    #     self.mainWindow.setCentralWidget(self.RegisterView)
        
    
    # def NavigateToLogin(self, view):
    #     print(view)
    #     self.mainWindow.setCentralWidget(view)
