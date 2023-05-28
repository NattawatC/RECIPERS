import time
from functools import partial

import sqlalchemy
from sqlalchemy.exc import IntegrityError

from controller.AuthController import AuthController
from model.RecipeModel import RecipeModel, AddedRecipes
from view.RecipeView import *
from view.FavoriteView import *
from view.CreateView import *
from view.RecipeCard import *
from view.DetailView import *


class RecipeController:
    def __init__(self, MainWindow,  imageCache, Controller = None,):
        self.imageCache = imageCache
        self.AuthController = Controller
        self.UserLogIn = self.AuthController.getCurrentUserLog()
        self.User = self.AuthController.getCurrentUser()
        self.RecipeModel = RecipeModel()
        self.mainWindow = MainWindow
        self.RecipeView = self.initRecipeView()
        self.FavoriteView = self.initFavoriteView()
        self.DetailView = DetailView(self)
        self.CreateView = CreateView(self)
        self.views = [self.RecipeView, self.FavoriteView, self.CreateView, self.DetailView]


    def createCards(self,items) -> list:
        cards = []
        newline = 0

        if len(items) == 1:
            recipe_card = RecipeCard(items[0], self.imageCache)

            if items[0].id in [addedRecipe.id for addedRecipe in self.handleGetAddedRecipe()]:
                recipe_card.delete_btn.clicked.connect(partial(self.handleDeleteRecipe, items[0].id))
                recipe_card.delete_btn.show()

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

                if item.id in [addedRecipe.id for addedRecipe in self.handleGetAddedRecipe()]:
                    recipe_card.delete_btn.clicked.connect(partial(self.handleDeleteRecipe, item.id))
                    recipe_card.delete_btn.show()

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
        self.mainWindow.stack = None
        self.mainWindow.showAuthView()
        self.mainWindow.imageCache = self.imageCache
        self.views.clear()

    def handleGetAddedRecipe(self):
        addedRecipes = []
        addedRecipe = self.RecipeModel.getAddedRecipes(self.User.id)
        for recipe in addedRecipe:
            addedRecipes.append(self.RecipeModel.getRecipeById(recipe.recipe_id))
        return addedRecipes


    #-------------------------------------------------

    #RecipeView
    def initRecipeView(self) -> RecipeView:
        self.RecipeView = RecipeView(self, self.initializeCard())
        self.RecipeView.setCreateCount(self.RecipeModel.getAddedCount(self.User.id))
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
            card.card_detail_btn.clicked.connect(partial(self.handleNavigateToDetail, card.recipe.id))

    def initializeCard(self) -> list:
        # recipes = [self.RecipeModel.getRecipeById(16), self.RecipeModel.getRecipeById(716342), self.RecipeModel.getRecipeById(662744), self.RecipeModel.getRecipeById(19), self.RecipeModel.getRecipeById(48)]
        recipes = self.RecipeModel.getAllRecipes()
        # recipes = [self.RecipeModel.getRecipeById(16), self.RecipeModel.getRecipeById(716342), self.RecipeModel.getRecipeById(662744), self.RecipeModel.getRecipeById(19), self.RecipeModel.getRecipeById(48)]
        cards = self.createCards(recipes)
        self.connectFavoriteSignals(cards)
        self.connectDetailSignals(cards)

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
        recipes = self.RecipeModel.searchRecipe(keyword, self.User.id)
        cards = self.createCards(recipes)
        self.connectFavoriteSignals(cards)
        self.connectDetailSignals(cards)
        self.RecipeView.setCards(cards)
        
    def handleFilterRecipe(self):
        tag = None
        type = ("breakfast", "lunch", "dinner")
        ingredient = ("meat", "seafood", "vegetable")
        serving = ("1", "2", "3", "4", 5)
        if self.RecipeView.breakfast_checkbox.isChecked() == True:
            tag = type[0]
            if self.RecipeView.lunch_checkbox.isChecked() == True:
                tag = type[:2]
                if self.RecipeView.dinner_checkbox.isChecked() == True:
                    tag = type[:3]
                elif self.RecipeView.meat_checkbox.isChecked() == True:
                    tag = type[:2], ingredient[0]
                elif self.RecipeView.seafood_checkbox.isChecked() == True:
                    tag = type[:2], ingredient[1]
                elif self.RecipeView.vegetable_checkbox.isChecked() == True:
                    tag = type[:2], ingredient[2]
            elif self.RecipeView.dinner_checkbox.isChecked() == True:
                tag = ("breakfast", "dinner")
                if self.RecipeView.meat_checkbox.isChecked() == True:
                    tag = ("breakfast", "dinner", "meat")
                elif self.RecipeView.seafood_checkbox.isChecked() == True:
                    tag = ("breakfast", "dinner", "seafood")
                elif self.RecipeView.vegetable_checkbox.isChecked() == True:
                    tag = ("breakfast", "dinner", "vegetable")
                elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("breakfast", "dinner", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("breakfast", "dinner", "5")
            elif self.RecipeView.meat_checkbox.isChecked() == True:
                tag = ("breakfast", "meat")
                if self.RecipeView.seafood_checkbox.isChecked() == True:
                    tag = ("breakfast", "meat", "seafood")
                elif self.RecipeView.vegetable_checkbox.isChecked() == True:
                    tag = ("breakfast", "meat", "vegetable")
                elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("breakfast", "meat", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("breakfast", "meat", "5")
            elif self.RecipeView.seafood_checkbox.isChecked() == True:
                tag = ("breakfast", "seafood")
                if self.RecipeView.vegetable_checkbox.isChecked() == True:
                    tag = ("breakfast", "seafood", "vegetable")
                elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("breakfast", "seafood", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("breakfast", "seafood", "5")
            elif self.RecipeView.vegetable_checkbox.isChecked() == True:
                tag = ("breakfast", "vegetable")
            elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                tag = ("breakfast", "1","2","3","4")
            elif self.RecipeView.morethan5_checkbox.isChecked():
                tag = ("breakfast", 5)
        elif self.RecipeView.lunch_checkbox.isChecked() == True:
            tag = "lunch"
            if self.RecipeView.dinner_checkbox.isChecked() == True:
                tag = ("lunch", "dinner")
                if self.RecipeView.meat_checkbox.isChecked() == True:
                    tag = ("lunch", "dinner", "meat")
                elif self.RecipeView.seafood_checkbox.isChecked() == True:
                    tag = ("lunch", "dinner", "seafood")
                elif self.RecipeView.vegetable_checkbox.isChecked() == True:
                    tag = ("lunch", "dinner", "vegetable")
                elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("lunch", "dinner", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("lunch", "dinner", "5")
            elif self.RecipeView.meat_checkbox.isChecked() == True:
                tag = ("lunch", "meat")
                if self.RecipeView.seafood_checkbox.isChecked() == True:
                    tag = ("lunch", "meat", "seafood")
                elif self.RecipeView.vegetable_checkbox.isChecked() == True:
                    tag = ("lunch", "meat", "vegetable")
                elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("lunch", "meat", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("lunch", "meat", "5")
            elif self.RecipeView.seafood_checkbox.isChecked() == True:
                tag = ("lunch", "seafood")
                if self.RecipeView.vegetable_checkbox.isChecked() == True:
                    tag = ("lunch", "seafood", "vegetable")
                elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("lunch", "seafood", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("lunch", "seafood", "5")
            elif self.RecipeView.vegetable_checkbox.isChecked() == True:
                tag = ("lunch", "vegetable")
                if self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("lunch", "vegetable", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("lunch", "vegetable", "5")
            elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                tag = ("lunch", "1","2","3","4")
            elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                tag = ("lunch", 5)
        elif self.RecipeView.dinner_checkbox.isChecked() == True:
            tag = "dinner"
            if self.RecipeView.meat_checkbox.isChecked() == True:
                tag = ("dinner", "meat")
                if self.RecipeView.seafood_checkbox.isChecked() == True:
                    tag = ("dinner", "meat", "seafood")
                elif self.RecipeView.vegetable_checkbox.isChecked() == True:
                    tag = ("dinner", "meat", "vegetable")
                elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("dinner", "meat", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("dinner", "meat", "5")
            elif self.RecipeView.seafood_checkbox.isChecked() == True:
                tag = ("dinner", "seafood")
                if self.RecipeView.vegetable_checkbox.isChecked() == True:
                    tag = ("dinner", "seafood", "vegetable")
                elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("dinner", "seafood", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("dinner", "seafood", "5")
            elif self.RecipeView.vegetable_checkbox.isChecked() == True:
                tag = ("dinner", "vegetable")
                if self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("dinner", "vegetable", "1","2","3","4")
                if self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("dinner", "vegetable", "5")
            elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                tag = ("dinner", "1","2","3","4")
            elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                tag = ("dinner", 5)
        elif self.RecipeView.meat_checkbox.isChecked() == True:
            tag = "meat"
            if self.RecipeView.seafood_checkbox.isChecked() == True:
                tag = ("meat", "seafood")
                if self.RecipeView.vegetable_checkbox.isChecked() == True:
                    tag = ("meat", "seafood", "vegetable")
                elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("meat", "seafood", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("meat", "seafood", "5")
            elif self.RecipeView.vegetable_checkbox.isChecked() == True:
                tag = ("meat", "vegetable")
                if self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("meat", "vegetable", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("meat", "vegetable", "5")
            elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                tag = ("meat", "1","2","3","4")
            elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                tag = ("meat", 5)
        elif self.RecipeView.seafood_checkbox.isChecked() == True:
            tag = "seafood"
            if self.RecipeView.vegetable_checkbox.isChecked() == True:
                tag = ("seafood", "vegetable")
                if self.RecipeView.lessthan5_checkbox.isChecked() == True:
                    tag = ("seafood", "vegetable", "1","2","3","4")
                elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                    tag = ("seafood", "vegetable", "5")
            elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
                tag = ("seafood", "1","2","3","4")
            elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                tag = ("seafood", 5)
        elif self.RecipeView.vegetable_checkbox.isChecked() == True:
            tag = "vegetable"
            if self.RecipeView.lessthan5_checkbox.isChecked() == True:
                tag = ("vegetable", "1","2","3","4")
            elif self.RecipeView.morethan5_checkbox.isChecked() == True:
                tag = ("vegetable", 5)
        elif self.RecipeView.lessthan5_checkbox.isChecked() == True:
            tag = ("1", "2", "3", "4")
        elif self.RecipeView.morethan5_checkbox.isChecked() == True:
            tag = 5
        
        
        
        recipes = self.RecipeModel.filterRecipe(tag)
        cards = self.createCards(recipes)
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
            self.connectDetailSignals(cards)
            return cards

    def getFavoriteCount(self) -> int:
        return len(self.handleGetFavorites())

    def refreshFavoriteView(self):
        self.FavoriteView.setCards(self.initFavoriteCards())

    def handleGetFavorites(self) -> list:
        return self.RecipeModel.getFavorites(self.User.id)


    #----------------------------------------------------

    #DetailView

    def handleNavigateToDetail(self, recipeId):
        if self.imageCache is not None:
            self.DetailView.setImage(self.imageCache[self.RecipeModel.getRecipeById(recipeId).image])
        self.DetailView.setRecipe(self.RecipeModel.getRecipeById(recipeId))
        self.DetailView.setIngredients(self.RecipeModel.getIngredients(recipeId))
        self.DetailView.setDirections(self.RecipeModel.getInstructions(recipeId))
        self.DetailView.update()
        self.mainWindow.NavigateToDetail()

    #----------------------------------------------------

    #CreateView
    def handleCreateRecipe(self):
        recipeInfo = self.CreateView.recipeSubmitted()
        if recipeInfo["detail"]["name"] == self.RecipeModel.getRecipeById(recipeInfo["detail"]["id"]).name:
            self.CreateView.showAlert("Recipe already exists")

        elif recipeInfo is not None and recipeInfo["detail"]["image"] == "":
            recipeInfo['detail']['image'] = 'https://media.istockphoto.com/' \
                                            'id/1443601388/th/รูปถ่าย/อาหารอินเดียใต้นานาชนิด-' \
                                            'เนื้อแกะสมองมาซาลา-ไก่ตังดี-ไก่-reshmi-tikka-' \
                                            'ไก่คาราฮี-เนื้อเนฮาริ.jpg?s=612x612&w=0&k=20&c=jJsdVGAk5efw' \
                                            'wnwWCfCU9tFvRpfWhCcp9SDRw_z7Pl0='
            self.RecipeModel.createRecipe(recipeInfo, self.User.id)
            self.CreateView.createMessageBox("inform", "Recipe created successfully", QMessageBox.Information)
            self.CreateView.setCreateCount(self.RecipeModel.getAddedCount(self.User.id))
            self.CreateView.clearForm()

        elif recipeInfo is not None:
            self.RecipeModel.createRecipe(recipeInfo, self.User.id)
            self.CreateView.createMessageBox("inform", "Recipe created successfully", QMessageBox.Information)
            self.CreateView.setCreateCount(self.RecipeModel.getAddedCount(self.User.id))
            self.CreateView.clearForm()


    def handleDeleteRecipe(self, recipeId):
        box = self.RecipeView.createMessageBoxWithInput("inform", "Are you sure to delete?", QMessageBox.Warning)
        if box:
            if self.RecipeModel.deleteRecipe(recipeId):
                self.RecipeView.setCards(self.initializeCard())
                self.RecipeView.setCreateCount(self.RecipeModel.getAddedCount(self.User.id))
                self.RecipeView.createMessageBox("inform", "Recipe deleted successfully", QMessageBox.Information)
                self.RecipeView.setCards(self.initializeCard())
                self.RecipeView.setFavoriteCount(self.getFavoriteCount())




    #----------------------------------------------------

    def handleNavigateToCreate(self):
        self.CreateView.setCreateCount(self.RecipeModel.getAddedCount(self.User.id))
        self.mainWindow.NavigateToCreate()

    def handleNavigateToRecipe(self):
        self.RecipeView.setCards(self.initializeCard())
        self.RecipeView.setFavoriteCount(self.getFavoriteCount())
        self.RecipeView.setCreateCount(self.RecipeModel.getAddedCount(self.User.id))
        self.mainWindow.NavigateToRecipe()

    def handleNavigateToFavorite(self):
        self.refreshFavoriteView()
        self.mainWindow.NavigateToFavorite()

    def __repr__(self) -> str:
        return self.user.username

    def getUser(self):
        return self.User.username
    
    def getUserLoginTime(self):
        return self.UserLogIn

    def getUserCreateTime(self):
        return self.RecipeModel.getCreatedRecipeTime(self.User.id)

    def getRecipeName(self, recipeId):
        return self.RecipeModel.getRecipeById(recipeId).name