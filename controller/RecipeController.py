from controller.AuthController import AuthController
from model.RecipeModel import RecipeModel
from view.RecipeView import *
from view.FavoriteView import *
from view.CreateView import *

class RecipeController:
    def __init__(self, MainWindow, AuthController=None):
        self.AuthController = AuthController
        self.RecipeModel = RecipeModel()
        self.mainWindow = MainWindow
        self.views = [RecipeView(self), FavoriteView(self), CreateView(self)]
        self.views[0].onClickLogoutButton(self.handleLogout)
        self.user = None

    def addView(self, view):
        self.views.append(view)

    def setController(self, c):
        self.AuthController = c
        self.user = self.AuthController.getCurrentUser()

    def handleLogout(self):
        self.AuthController.handleLogout()
        self.user = None
        self.mainWindow.showAuthView()
        self.views.clear()

    def handleNavigateToCreate(self):
        self.mainWindow.NavigateToCreate()

    def handleNavigateToRecipe(self):
        self.mainWindow.NavigateToRecipe()

    def handleNavigateToFavorite(self):
        self.mainWindow.NavigateToFavorite()

    def handleCreateRecipeCard(self):
        recipes = self.RecipeModel.getAllRecipes()
        self.views[0].createRecipeCard(recipes)

    def handleMakeFavorite(self, recipe):
        self.RecipeModel.makeFavorite(self.user.id, recipe.id)
        self.views[1].makeFavorite(recipe)

    def handleGetFavorites(self):
        return self.RecipeModel.getFavorites(self.user.id)


    def __repr__(self):
        return self.user.username

