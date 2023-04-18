from model.AuthModel import UserModel

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.isSuccess = False

    def authenticate(self,username, password):
        if self.model.login(username, password):
            self.isSuccess = True

        else:
            self.isSuccess = False

    def isLoginSuccess(self):
        return self.isSuccess



