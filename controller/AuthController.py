from model.AuthModel import AuthModel
from view.AuthView import AuthView
import time
from view.RegisterView import RegisterView
from functools import partial
from PySide6.QtCore import Qt

class AuthController:
    def __init__(self, MainWindow):
        self.mainWindow = MainWindow
        self.AuthModel = AuthModel()
        self.AuthView = AuthView(self)
        self.RegisterView = RegisterView(self)
        self.RegisterView.start_button.clicked.connect(self.handleRegister)
        self.__currentUser = None
        self.isLoginSuccess = False
        self.isRegisterValid = False
        self.__currentUserLog = None


    def authenticate(self,username, password):
        if self.AuthModel.validate(username, password):
            self.__currentUser = self.AuthModel.getUser(username)
            self.isLoginSuccess = True
        else:
            self.isLoginSuccess = False
        return self.isLoginSuccess
            
    def handleLogin(self):
        self.authenticate(self.AuthView.lineEdit_username.text(), self.AuthView.lineEdit_password.text())
        if self.isLoginSuccess:
            return self.__currentUser
        else:
            self.AuthView.showError("Invalid username or password")

    def handleRegister(self):
        checkUsernameValid = self.checkUsername(self.RegisterView.lineEdit_regUsername.text())
        checkFirstnameValid = self.checkFname(self.RegisterView.lineEdit_fname.text())
        checkLastnameValid = self.checkLname(self.RegisterView.lineEdit_lname.text())
        checkRegPasswordValid = self.checkPassword(self.RegisterView.lineEdit_regPassword.text())
        checkConfirmPasswordValid = self.checkConfirmPassword(self.RegisterView.lineEdit_regConPassword.text(), self.RegisterView.lineEdit_regPassword.text())
        if checkUsernameValid == True and checkFirstnameValid == True and checkLastnameValid == True and checkRegPasswordValid == True and checkConfirmPasswordValid == True:
            self.RegisterView.start_button.clicked.connect(self.mainWindow.returnToAuth)
            self.AuthModel.register(self.RegisterView.lineEdit_regUsername.text(), self.RegisterView.lineEdit_regPassword.text(), self.RegisterView.lineEdit_fname.text(), self.RegisterView.lineEdit_lname.text())
        else:
            self.setFocus(checkUsernameValid, checkFirstnameValid, checkLastnameValid, checkRegPasswordValid, checkConfirmPasswordValid)

    def setFocus(self, checkUsernameValid, checkFirstnameValid, checkLastnameValid, checkRegPasswordValid, checkConfirmPasswordValid):
        if not checkUsernameValid:
            self.RegisterView.lineEdit_regUsername.setFocus()
            self.RegisterView.lineEdit_regUsername.clear()
            self.RegisterView.showUserError("Username is already have.")
            return
        if not checkFirstnameValid:
            self.RegisterView.lineEdit_fname.setFocus()
            self.RegisterView.lineEdit_fname.clear()
            self.RegisterView.showFnameError("Invalid First name.")
            return
        if not checkLastnameValid:
            self.RegisterView.lineEdit_lname.setFocus()
            self.RegisterView.lineEdit_lname.clear()
            self.RegisterView.showLnameError("Invalid Last name.")
            return
        if not checkRegPasswordValid:
            self.checkPassword(self.RegisterView.lineEdit_regPassword.text())
            self.RegisterView.lineEdit_regPassword.setFocus()
            self.RegisterView.lineEdit_regPassword.clear()
            return
        if not checkConfirmPasswordValid:
            self.RegisterView.lineEdit_regConPassword.setFocus()
            self.RegisterView.lineEdit_regConPassword.clear()
            self.RegisterView.showConPasswordError("Password is not match.")
            return
            
    def checkUsername(self, username):
        dataUser = self.AuthModel.getAllUsername()
        for i in range(len(dataUser)):
            if username == dataUser[i][0]:
                return False
        return True

    def checkFname(self, firstName):
        for i in range(len(firstName)):
            if firstName[i].isdigit():
                return False
        return True
            
    def checkLname(self, lastname):
        for i in range(len(lastname)):
            if lastname[i].isdigit():
                return False
        return True

    def checkPassword(self, password):
        if len(password) == 0:
            self.RegisterView.showPasswordError("Please fill in a password.")
            return False
        elif len(password) < 8:
            self.RegisterView.showPasswordError("Please fill in a password with at least 8 characters.")
            return False
        elif not any(char.isdigit() for char in password):
            self.RegisterView.showPasswordError("Please fill in a password with at least 1 number.")
            return False
        elif not any(char.isupper() for char in password):
            self.RegisterView.showPasswordError("Please fill in a password with at least 1 uppercase letter.")
            return False
        elif not any(char.islower() for char in password):
            self.RegisterView.showPasswordError("Please fill in a password with at least 1 lowercase letter.")
            return False
        else:
            self.RegisterView.showPasswordError("Password is valid.")
            return True

    def checkConfirmPassword(self, confirmPassword, password):
        if confirmPassword != password:
            return False
        return True

    def handleLogout(self, user=None):
        self.AuthModel.logout(self.getCurrentUser())
        self.setCurrentUser(None)
        print("log out!")

    def getCurrentUser(self):
        return self.__currentUser

    def setCurrentUser(self, user):
        self.__currentUser = user

    def getCurrentUserLog(self):
        self.__currentUserLog = self.AuthModel.getUserLogTime(self.getCurrentUser().id)
        return self.__currentUserLog

    def handleNavigateToRegister(self):
        self.RegisterView.reset()
        self.mainWindow.NavigateToRegister()
    
    def handleNavigateToLogin(self):
        self.mainWindow.NavigateToAuth()
