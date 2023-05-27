from model.AuthModel import AuthModel
from view.AuthView import AuthView
import time
from view.RegisterView import RegisterView
from functools import partial
from PySide6.QtCore import Qt

class AuthController:
    def __init__(self, MainWindow):
        self.mainWindow = MainWindow
        self.model = AuthModel()
        self.AuthView = AuthView(self)
        self.RegisterView = RegisterView(self)
        self.RegisterView.start_button.clicked.connect(self.handleRegister)
        # self.handleRegister()
        self.__currentUser = None
        self.isLoginSuccess = False
        self.isRegisterValid = False
        self.__currentUserLog = None


    def authenticate(self,username, password):
        if self.model.validate(username, password):
            self.__currentUser = self.model.getUser(username)
            self.isLoginSuccess = True
        else:
            self.isLoginSuccess = False
        return self.isLoginSuccess

    def registerAuthenticate(self, userInformation):
        for i in range(self.AuthView):
            if userInformation[i] == "":
                self.RegisterView.showError("Please fill in all the blanks")
                return False

            
    def handleLogin(self):
        self.authenticate(self.AuthView.lineEdit_username.text(), self.AuthView.lineEdit_password.text())
        if self.isLoginSuccess:
            return self.__currentUser
        else:
            self.AuthView.showError("Invalid username or password")

    def handleRegister(self):
        self.checkUsernameValid = self.checkUsername(self.RegisterView.lineEdit_regUsername.text())
        self.checkFnameValid = self.checkFname(self.RegisterView.lineEdit_fname.text())
        self.checkLnameValid = self.checkLname(self.RegisterView.lineEdit_lname.text())
        self.checkRegPasswordValid = self.checkPassword(self.RegisterView.lineEdit_regPassword.text())
        self.checkConfirmPasswordValid = self.checkConfirmPassword(self.RegisterView.lineEdit_regConPassword.text(), self.RegisterView.lineEdit_regPassword.text())
        if self.checkUsernameValid == True and self.checkFnameValid == True and self.checkLnameValid == True and self.checkRegPasswordValid == True and self.checkConfirmPasswordValid == True:
            self.RegisterView.start_button.clicked.connect(self.mainWindow.returnToAuth)
        else:
            print(self.checkUsernameValid, self.checkFnameValid, self.checkLnameValid, self.checkRegPasswordValid, self.checkConfirmPasswordValid)
            self.setFocus()

    def setFocus(self):
        if self.checkUsernameValid == False:
            self.RegisterView.lineEdit_regUsername.setFocus()
            self.RegisterView.lineEdit_regUsername.clear()
            self.RegisterView.showUserError("Username is already have.")
            self.checkUsernameValid = True
        if self.checkFnameValid == False:
            self.checkFnameValid = True
            self.RegisterView.lineEdit_fname.setFocus()
            self.RegisterView.lineEdit_fname.clear()
            self.RegisterView.showFnameError("Invalid First name.")
        if self.checkLnameValid == False:
            self.checkLnameValid = True
            self.RegisterView.lineEdit_lname.setFocus()
            self.RegisterView.lineEdit_lname.clear()
            self.RegisterView.showLnameError("Invalid Last name.")
        if self.checkRegPasswordValid == False:
            self.checkRegPasswordValid = True
            self.checkPassword(self.RegisterView.lineEdit_regPassword.text())
            self.RegisterView.lineEdit_regPassword.setFocus()
            self.RegisterView.lineEdit_regPassword.clear()
        if self.checkConfirmPasswordValid == False:
            self.checkConfirmPasswordValid = True
            self.RegisterView.lineEdit_regConPassword.setFocus()
            self.RegisterView.lineEdit_regConPassword.clear()
            self.RegisterView.showConPasswordError("Password is not match.")
            
    def checkUsername(self, username):
        dataUser = self.model.getAllUsername()
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
        if len(password) < 8:
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
            return True

    def checkConfirmPassword(self, confirmPassword, password):
        if confirmPassword != password:
            return False
        return True

    def handleLogout(self, user=None):
        self.model.logout(self.getCurrentUser())
        self.setCurrentUser(None)
        print("log out!")

    def getCurrentUser(self):
        return self.__currentUser

    def setCurrentUser(self, user):
        self.__currentUser = user

    def getCurrentUserLog(self):
        self.__currentUserLog = self.model.getUserLogTime(time.strftime('%Y-%m-%d %H:%M:%S'))
        return self.__currentUserLog

    def handleNavigateToRegister(self):
        self.mainWindow.NavigateToRegister()
    
    def handleNavigateToLogin(self):
        self.mainWindow.NavigateToAuth()
    # def NavigateToRegister(self):
    #     print(self.AuthView)
    #     self.mainWindow.setCentralWidget(self.RegisterView)
        
    
    # def NavigateToLogin(self, view):
    #     print(view)
    #     self.mainWindow.setCentralWidget(view)
