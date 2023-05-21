from controller.AuthController import AuthController

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

    def logout(self):
        self.view.close()
        self.AuthController.handleLogout()

    def handleCreateRecipeCard(self):
        self.view.createRecipeCard()


    def __repr__(self):
        return self.user.username

