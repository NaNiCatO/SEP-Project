from Python_ui_file import login as login
from Python_ui_file import register as register
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from validate_email import validate_email 
# pip install validate_email

# ******************************  Connect to database  ********************************
import ZODB , ZODB.FileStorage
import transaction
mystorage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(mystorage)
connection = db.open()
root = connection.root()


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = login.Ui_Form()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.createAccountButton.clicked.connect(self.register)

    def login(self):
        print("Login")

    def register(self):
        print("Register")
        self.registerWindow = RegisterWindow()
        self.registerWindow.show()
        self.close()

class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = register.Ui_Form()
        self.ui.setupUi(self)
        self.ui.createAccountButton.clicked.connect(self.create_account)
        self.ui.loginButton.clicked.connect(self.login)

    def create_account(self):
        email_is_valid = validate_email(self.ui.emailLineEdit.text(), verify=True)
        if email_is_valid:
            print("Email is valid")
        else:
            print("Email is invalid")

    def login(self):
        print("Login")
        self.loginWindow = LoginWindow()
        self.loginWindow.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())