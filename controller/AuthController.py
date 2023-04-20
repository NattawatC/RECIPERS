from model.AuthModel import AuthModel
from controller.RecipeController import RecipeController

class AuthController:
    def __init__(self):
        self.RecipeController = RecipeController()
        self.model = AuthModel()
        self.isSuccess = False

    def authenticate(self,username, password):
        if self.model.validate(username, password):
            self.isSuccess = True
            return self.model.getUser(username)

    def isLoginSuccess(self):
        return self.isSuccess

    def logout(self):
        self.model.logout(self.model.getCurrentUser())
        print("log out!")

    def getCurrentUser(self):
        return self.model.getCurrentUser()



