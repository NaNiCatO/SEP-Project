from PySide6.QtGui import QCloseEvent
from Python_ui_file import login as login
from Python_ui_file import register as register
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from class_module import *
from main import *

# ******************************  Connect to database  ********************************
import ZODB, ZODB.FileStorage
import transaction

class LoginWindow(QWidget):
    def __init__(self,connection):
        super().__init__()
        self.connection = connection
        self.root = self.connection.root()
        self.ui = login.Ui_Form()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)

    def login(self):
        user_data = self.root.user
        for user in user_data:
            if user == self.ui.userInput.text():
                if user_data[user].login(self.ui.passwordInput.text()):
                    print("Login success")
                    self.username = user
                    self.sidebar = Sidebar(user_data[user],self.connection)
                    self.sidebar.show()
                    self.close()
        return None

class RegisterWindow(QWidget):
    def __init__(self,connection):
        super().__init__()
        self.ui = register.Ui_Form()
        self.connection = connection
        self.root = self.connection.root()
        self.ui.setupUi(self)
        # self.ui.CreateAccountButton.clicked.connect(self.create_account)

    def create_account(self):
        # check if the input is empty
        if self.check_input():
            print("Account created")
            user = User(self.ui.userInput.text(), self.ui.passwordInput.text(), self.ui.emailInput.text())
            self.root.user[self.ui.userInput.text()] = user
            transaction.commit()
            return True         
        return False
    
    def check_input(self):
        if not self.ui.userInput.text() or not self.ui.passwordInput.text() or not self.ui.emailInput.text():
            print("Input is empty")
            return False
        elif self.ui.passwordInput.text() != self.ui.confirmPassword.text():
            print("Password does not match")
            return False
        else:
            return self.check_duplicate()
    
    def check_duplicate(self):
        user_data = self.root.user
        for user in user_data:
            if user == self.ui.userInput.text():
                print("Username already exists")
                return False
            elif user_data[user].email == self.ui.emailInput.text():
                print("Email already exists")
                return False
        return True


    

class SignInWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mystorage = ZODB.FileStorage.FileStorage('mydata.fs')
        self.db = ZODB.DB(self.mystorage)
        self.connection = self.db.open()
        self.root = self.connection.root()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.login_window = LoginWindow(self.connection)
        self.register_window = RegisterWindow(self.connection)

        self.layout.addWidget(self.login_window)
        self.layout.addWidget(self.register_window)

        self.register_window.hide()

        self.login_window.ui.createAccountButton.clicked.connect(self.show_register)
        self.register_window.ui.signInButton.clicked.connect(self.show_login)
        self.register_window.ui.CreateButton.clicked.connect(self.check_create_success)

    def check_create_success(self):
        if self.register_window.create_account():
            self.show_login()

    def show_login(self):
        self.login_window.show()
        self.register_window.hide()

    def show_register(self):
        self.login_window.hide()
        self.register_window.show()
    
    def closeEvent(self, event):
        self.root.user[self.login_window.username]._p_changed = True
        print("Closing")
        transaction.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignInWindow()
    window.show()
    sys.exit(app.exec())
