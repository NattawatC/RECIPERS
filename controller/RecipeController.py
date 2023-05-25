from functools import partial

from controller.AuthController import AuthController
from model.RecipeModel import RecipeModel, Recipe
from view.RecipeView import *
from view.FavoriteView import *
from view.CreateView import *
from view.RecipeCard import *
from view.DetailView import *

class RecipeController:
    def __init__(self, MainWindow,  imageCache, Controller = None,):
        self.imageCache = imageCache
        self.AuthController = Controller
        self.User = self.AuthController.getCurrentUser()
        self.RecipeModel = RecipeModel()
        self.mainWindow = MainWindow
        self.RecipeView = self.initRecipeView()
        self.FavoriteView = self.initFavoriteView()
        self.views = [self.RecipeView, self.FavoriteView, CreateView(self), DetailView()]



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

                recipe_card.card_detail_btn.clicked.connect(partial(self.handleNavigateToDetail, item.id))
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
    def initRecipeView(self) -> RecipeView:
        self.RecipeView = RecipeView(self, self.initializeCard())
        self.RecipeView.setFavoriteCount(self.getFavoriteCount())
        return self.RecipeView

    def connectFavoriteSignals(self, cards):
        favorites = self.handleGetFavorites()
        recipe_cards = {}

        for card in cards:
            recipe = card.recipe
            recipe_cards[recipe.id] = card

            if recipe.id in [favorite.id for favorite in favorites]:
                card.setFavorite(True)
                card.unStarred.clicked.connect(partial(self.handleUnFavorite, recipe.id, card.unStarred))
                card.updateStar()
            else:
                card.unStarred.clicked.connect(partial(self.handleMakeFavorite, recipe.id, card.unStarred))
                card.updateStar()

    def connectDetailSignals(self, cards):
        for card in cards:
            card.clicked.connect(partial(self.handleNavigateToDetail, card.recipe.id))

    def initializeCard(self) -> list:
        recipes = self.RecipeModel.getAllRecipes()
        cards = self.createCards(recipes)
        self.connectFavoriteSignals(cards)

        return cards


    def handleMakeFavorite(self, recipeId, button):
        self.RecipeModel.makeFavorite(self.User.id, recipeId)
        print(str(recipeId) + " is favorited")
        self.RecipeView.setFavoriteCount(self.getFavoriteCount())
        icon = QIcon("static/asset/img/stared.png")
        button.setIcon(icon)
        button.clicked.disconnect()
        button.clicked.connect(partial(self.handleUnFavorite, recipeId, button))
       

    def handleUnFavorite(self, recipeId, button):
        self.RecipeModel.unFavorite(self.User.id, recipeId)
        print(str(recipeId) + " is unfavorited")
        self.RecipeView.setFavoriteCount(self.getFavoriteCount())
        button.clicked.disconnect()
        button.clicked.connect(partial(self.handleMakeFavorite, recipeId, button))
        icon = QIcon("static/asset/img/unstared.png")
        button.setIcon(icon)
        self.FavoriteView.removeCard(recipeId)



    def handleSearchRecipe(self, keyword):
        recipes = self.RecipeModel.searchRecipe(keyword)
        cards = self.createCards(recipes)
        self.connectFavoriteSignals(cards)
        self.RecipeView.setCards(cards)
    #----------------------------------------------------

    #FavoriteView
    def initFavoriteView(self) -> FavoriteView:
        self.FavoriteView = FavoriteView(self, self.initFavoriteCards())
        return self.FavoriteView

    def initFavoriteCards(self) -> list:
        favorites = self.handleGetFavorites()
        if favorites is None:
            return []
        else:
            cards = self.createCards(favorites)
            self.connectFavoriteSignals(cards)
            return cards

    def getFavoriteCount(self) -> int:
        return len(self.handleGetFavorites())

    def refreshFavoriteView(self):
        self.FavoriteView.setCards(self.initFavoriteCards())

    def handleGetFavorites(self) -> list:
        favorites = []
        for favorite in self.RecipeModel.getFavorites(self.User.id):
            recipe = self.RecipeModel.getRecipeById(favorite.recipe_id)
            favorites.append(recipe)
        return favorites







    #----------------------------------------------------

    #DetailView


    def initDetailView(self, recipeId) -> DetailView:
        recipe = self.handleGetRecipeById(recipeId)
        view = DetailView(self, recipe)
        if recipe.image in self.imageCache:
            view.setRecipeImage(self.imageCache[recipe.image])

        return view

    def handleNavigateToDetail(self, recipeId):
        self.mainWindow.NavigateToDetail(recipeId)






    #----------------------------------------------------

    def handleNavigateToCreate(self):
        self.mainWindow.NavigateToCreate()

    def handleNavigateToRecipe(self):
        self.RecipeView.setCards(self.initializeCard())
        self.RecipeView.setFavoriteCount(self.getFavoriteCount())
        self.mainWindow.NavigateToRecipe()

    def handleNavigateToFavorite(self):
        self.refreshFavoriteView()
        self.mainWindow.NavigateToFavorite()

    def __repr__(self) -> str:
        return self.user.username

