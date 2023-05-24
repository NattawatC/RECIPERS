from controller.AuthController import AuthController
from model.RecipeModel import RecipeModel
from view.RecipeView import *
from view.FavoriteView import *
from view.CreateView import *

class RecipeController:
    def __init__(self, MainWindow, Controller = None):
        self.AuthController = Controller
        self.User = self.AuthController.getCurrentUser()
        self.RecipeModel = RecipeModel()
        self.mainWindow = MainWindow
        self.views = [RecipeView(self), FavoriteView(self), CreateView(self)]


    def addView(self, view):
        self.views.append(view)

    def handleLogout(self):
        self.AuthController.handleLogout()
        self.mainWindow.showAuthView()
        self.views.clear()

    #RecipeView
    def handleCreateRecipeCard(self):
        recipes = self.RecipeModel.getAllRecipes()
        return recipes

    # def handleSearchRecipe(self, keyword):
    #     pass

    #FavoriteView
    def handleMakeFavorite(self, recipeId):
        self.RecipeModel.makeFavorite(self.User.id , recipeId)

    def handleGetFavorites(self):
        print(self.RecipeModel.getFavorites(self.User.id))
        # return self.RecipeModel.getFavorites(self.user.id)



    #----------------------------------------------------

    def handleNavigateToCreate(self):
        self.mainWindow.NavigateToCreate()

    def handleNavigateToRecipe(self):
        # self.handleCreateRecipeCard()
        self.mainWindow.NavigateToRecipe()

    def handleNavigateToFavorite(self):

        self.mainWindow.NavigateToFavorite()

    def __repr__(self):
        return self.user.username

