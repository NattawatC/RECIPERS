from controller.AuthController import AuthController
from model.RecipeModel import RecipeModel



class RecipeController:
    def __init__(self):
        self.AuthController = None
        self.RecipeModel = RecipeModel()
        self.views = []
        self.user = None

    def addView(self, view):
        self.views.append(view)

    def setController(self, c):
        self.AuthController = c
        self.user = self.AuthController.getCurrentUser()

    def logout(self):
        self.AuthController.handleLogout()
        self.user = None
        self.views[0].mainWindow.showAuthView()
        self.views.clear()

    # def CreateRecipe(self, recipe):
    #     self.RecipeModel.createRecipe(recipe)

    def handleMakeFavorite(self, recipe):
        self.RecipeModel.makeFavorite(self.user.id, recipe.id)

    def handleGetFavorites(self):
        return self.RecipeModel.getFavorites(self.user.id)


    def __repr__(self):
        return self.user.username

