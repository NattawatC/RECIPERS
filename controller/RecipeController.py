from functools import partial

from controller.AuthController import AuthController
from model.RecipeModel import RecipeModel, Recipe
from view.RecipeView import *
from view.FavoriteView import *
from view.CreateView import *
from view.RecipeCard import *

class RecipeController:
    def __init__(self, MainWindow, Controller = None):
        self.AuthController = Controller
        self.User = self.AuthController.getCurrentUser()
        self.RecipeModel = RecipeModel()
        self.mainWindow = MainWindow
        self.RecipeView = self.initRecipeView()
        self.FavoriteView = self.initFavoriteView()
        self.views = [self.RecipeView, self.FavoriteView, CreateView(self)]

    def addView(self, view):
        self.views.append(view)

    def handleLogout(self):
        self.AuthController.handleLogout()
        self.mainWindow.showAuthView()
        self.views.clear()

    #RecipeView
    def initRecipeView(self):
        self.RecipeView = RecipeView(self, self.initializeCard())
        return self.RecipeView

    def initializeCard(self):
        cards = []
        recipes = self.RecipeModel.getAllRecipes()

        newline = 0

        if type(recipes) == Recipe:
            recipe_card = RecipeCard(recipes)
            recipe_card.setGeometry(QRect(0, 0, 402, 194))
            cards.append(recipe_card)

        else:
            for i, recipe in enumerate(recipes):
                recipe_card = RecipeCard(recipe)

                x = 0 if i % 2 == 0 else 436
                y = 230 * newline

                if i % 2 != 0:
                    newline += 1

                recipe_card.setGeometry(QRect(x, y, 402, 194))

                cards.append(recipe_card)
                # recipe_card.unStarred.clicked.connect(lambda: self.handleMakeFavorite(recipe.id))
        for card in cards:
            card.unStarred.clicked.connect(partial(self.handleMakeFavorite, card.recipe.id, card.unStarred))

        favorites = self.handleGetFavorites()
        for favorite in favorites:
            for card in cards:
                if favorite.id == card.recipe.id:
                    card.setFavorite(True)
                    card.unStarred.clicked.disconnect()
                    card.unStarred.clicked.connect(
                        partial(self.handleUnFavorite, card.recipe.id, card.unStarred))
        return cards


    def handleMakeFavorite(self, recipeId, button):
        self.RecipeModel.makeFavorite(self.User.id, recipeId)
        print(str(recipeId) + " is favorited")
        button.clicked.disconnect()
        button.clicked.connect(partial(self.handleUnFavorite, recipeId, button))


    def handleUnFavorite(self, recipeId, button):
        self.RecipeModel.unFavorite(self.User.id, recipeId)
        print(str(recipeId) + " is unfavorited")
        button.clicked.disconnect()
        button.clicked.connect(partial(self.handleMakeFavorite, recipeId, button))

    # def handleSearchRecipe(self, keyword):
    #     pass

    #FavoriteView
    def initFavoriteView(self):
        self.FavoriteView = FavoriteView(self, self.initFavoriteCards())
        return self.FavoriteView

    def initFavoriteCards(self):
        if self.handleGetFavorites() is None:
            return
        else:
            favorites = self.handleGetFavorites()
            cards = []
            newline = 0

            if len(favorites) == 1:
                recipe_card = RecipeCard(favorites[0])
                recipe_card.setGeometry(QRect(0, 0, 402, 194))
                cards.append(recipe_card)

            else:
                for i, recipe in enumerate(favorites):
                    recipe_card = RecipeCard(recipe)
                    x = 0 if i % 2 == 0 else 436
                    y = 230 * newline

                    if i % 2 != 0:
                        newline += 1

                    recipe_card.setGeometry(QRect(x, y, 402, 194))
                    cards.append(recipe_card)
            return cards




    def handleGetFavorites(self):
        favorites = []
        for favorite in self.RecipeModel.getFavorites(self.User.id):
            recipe = self.RecipeModel.getRecipeById(favorite.recipe_id)
            favorites.append(recipe)
        return favorites


    #----------------------------------------------------

    def handleNavigateToCreate(self):
        self.mainWindow.NavigateToCreate()

    def handleNavigateToRecipe(self):
        # self.handleCreateRecipeCard()
        self.mainWindow.NavigateToRecipe()

    def handleNavigateToFavorite(self):
        self.views[1].setCards(self.initFavoriteCards())
        self.mainWindow.NavigateToFavorite()

    def __repr__(self):
        return self.user.username

