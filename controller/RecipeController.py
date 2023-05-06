from controller.AuthController import AuthController
from model.RecipeModel import RecipeModel

class RecipeController:
    def __init__(self, view=None):
        self.AuthController = None
        self.RecipeModel = RecipeModel()
        self.view = view
        self.user = None


    def setController(self, c):
        self.AuthController = c
        self.user = self.AuthController.getCurrentUser()

    def logout(self):
        self.view.close()
        self.AuthController.handleLogout()

    def handleCreateRecipeCard(self):
        self.view.createRecipeCard()


    def __repr__(self):
        return self.user.username

