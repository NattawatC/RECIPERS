from model.AuthModel import AuthModel


class AuthController:
    def __init__(self, view=None):
        self.model = AuthModel()
        self.view = view
        self.currentUser = None
        self.isLoginSuccess = False

    def authenticate(self,username, password):
        if self.model.validate(username, password):
            self.currentUser = self.model.getUser(username)
            self.isLoginSuccess = True
        else:
            self.isLoginSuccess = False
        return self.isLoginSuccess

    def handleLogin(self):
        self.authenticate(self.view.lineEdit_username.text(), self.view.lineEdit_password.text())
        if self.isLoginSuccess:
            self.view.close()
            self.view.mainWindow.showRecipeView()
        else:
            self.view.showError("Invalid username or password")

    def handleLogout(self, user=None):
        self.model.logout(self.getCurrentUser())
        self.setCurrentUser(None)
        self.view.mainWindow.showAuthView()
        print("log out!")

    def getCurrentUser(self):
        return self.currentUser



