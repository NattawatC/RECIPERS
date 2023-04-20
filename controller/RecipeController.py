class RecipeController:
    def __init__(self):
        self.user = None

    def setUser(self, user):
        self.user = user

    def __repr__(self):
        return self.user.username

