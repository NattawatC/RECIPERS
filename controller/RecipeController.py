from controller.AuthController import AuthController
from model.RecipeModel import RecipeModel

class RecipeController:
    def __init__(self):
        self.AuthController = None
        self.RecipeModel = RecipeModel()
        self.view = None
        self.user = None

    def setView(self, view):
        self.view = view

    def setController(self, c):
        self.AuthController = c
        self.user = self.AuthController.getCurrentUser()

    def logout(self):
        self.view.close()
        self.AuthController.handleLogout()

    def CreateRecipe(self, recipe):
        self.RecipeModel.createRecipe(recipe)

    def makeFavorite(self, recipe):
        self.RecipeModel.makeFavorite(self.user.id, recipe.id)


    def __repr__(self):
        return self.user.username

