from functools import partial

from controller.AuthController import AuthController
from model.RecipeModel import RecipeModel, Recipe
from view.RecipeView import *
from view.FavoriteView import *
from view.CreateView import *
from view.RecipeCard import *

class RecipeController:
    def __init__(self, MainWindow,  imageCache, Controller = None,):
        self.imageCache = imageCache
        self.AuthController = Controller
        self.User = self.AuthController.getCurrentUser()
        self.RecipeModel = RecipeModel()
        self.mainWindow = MainWindow
        self.RecipeView = self.initRecipeView()
        self.FavoriteView = self.initFavoriteView()
        self.views = [self.RecipeView, self.FavoriteView, CreateView(self)]


    def createCards(self,items) -> list:
        cards = []
        newline = 0

        if len(items) == 1:
            recipe_card = RecipeCard(items[0], self.imageCache)
            if self.imageCache is None:
                self.imageCache = {}
            self.imageCache[items[0].image] = recipe_card.card_img.pixmap()
            recipe_card.setGeometry(QRect(0, 0, 402, 194))
            cards.append(recipe_card)
        else:
            for i, item in enumerate(items):
                if self.imageCache is None:
                    self.imageCache = {}
                recipe_card = RecipeCard(item, self.imageCache)
                self.imageCache[item.image] = recipe_card.card_img.pixmap()
                x = 0 if i % 2 == 0 else 436
                y = 230 * newline

                if i % 2 != 0:
                    newline += 1

                recipe_card.setGeometry(QRect(x, y, 402, 194))
                cards.append(recipe_card)
        return cards

    def addView(self, view):
        self.views.append(view)

    def handleLogout(self):
        self.AuthController.handleLogout()
        self.mainWindow.showAuthView()
        self.mainWindow.stack = None
        self.mainWindow.imageCache = self.imageCache
        self.views.clear()

    #RecipeView
    def initRecipeView(self):
        self.RecipeView = RecipeView(self, self.initializeCard())
        return self.RecipeView

    def connectFavoriteSignals(self, cards):
        favorites = self.handleGetFavorites()
        recipe_cards = {}

        for card in cards:
            card_id = card.recipe.id
            recipe_cards[card_id] = card

            if card_id in [favorite.id for favorite in favorites]:
                card.setFavorite(True)
                card.unStarred.clicked.connect(partial(self.handleUnFavorite, card_id, card.unStarred))
            else:
                card.unStarred.clicked.connect(partial(self.handleMakeFavorite, card_id, card.unStarred))

    def initializeCard(self):
        recipes = self.RecipeModel.getAllRecipes()
        cards = self.createCards(recipes)
        self.connectFavoriteSignals(cards)

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
        favorites = self.handleGetFavorites()
        if favorites is None:
            return []
        else:
            cards = self.createCards(favorites)
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

