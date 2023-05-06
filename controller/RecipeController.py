from controller.AuthController import AuthController

class RecipeController:
    def __init__(self, view=None):
        self.AuthController = None
        self.view = view

    def setController(self, c):
        self.AuthController = c

    def logout(self):
        self.view.close()
        self.AuthController.handleLogout()

    def __repr__(self):
        return self.user.username

