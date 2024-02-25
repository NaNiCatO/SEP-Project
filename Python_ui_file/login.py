# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(909, 503)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 900, 500))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(900, 500))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u"#widget{\n"
"background-color: #ffffff;\n"
"border-radius: 25px 25px 25px 25px;\n"
"}\n"
"\n"
"*{\n"
"border: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.loginHeader = QLabel(self.frame)
        self.loginHeader.setObjectName(u"loginHeader")
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        self.loginHeader.setFont(font)
        self.loginHeader.setStyleSheet(u"#loginHeader{\n"
"color : #1e1e1e;\n"
"}")

        self.verticalLayout_3.addWidget(self.loginHeader, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.userInput = QLineEdit(self.frame_5)
        self.userInput.setObjectName(u"userInput")
        self.userInput.setMinimumSize(QSize(400, 0))
        font1 = QFont()
        font1.setBold(True)
        self.userInput.setFont(font1)
        self.userInput.setStyleSheet(u"#userInput{\n"
"background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid #1e1e1e;\n"
"padding-bottom: 7px;\n"
"color: #1e1e1e;\n"
"}")

        self.horizontalLayout_2.addWidget(self.userInput)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.passwordInput = QLineEdit(self.frame_2)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMinimumSize(QSize(400, 0))
        self.passwordInput.setFont(font1)
        self.passwordInput.setStyleSheet(u"#passwordInput{\n"
"background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid #1e1e1e;\n"
"padding-bottom: 7px;\n"
"color: #1e1e1e;\n"
"}")
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.passwordInput)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.loginButton = QPushButton(self.frame_3)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setStyleSheet(u"QPushButton {\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    /*background: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #f0792b, stop:0.5 #ffa163, stop:1 #edb28c);*/\n"
"	background-color: #f0792b;\n"
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ff6347; \n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.loginButton)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.createAccountButton = QPushButton(self.frame_6)
        self.createAccountButton.setObjectName(u"createAccountButton")
        self.createAccountButton.setMinimumSize(QSize(120, 0))
        font2 = QFont()
        font2.setBold(True)
        font2.setUnderline(True)
        self.createAccountButton.setFont(font2)
        self.createAccountButton.setStyleSheet(u"#createAccountButton{\n"
"border: none;\n"
"color: #1e1e1e;\n"
"}")

        self.verticalLayout_4.addWidget(self.createAccountButton, 0, Qt.AlignRight)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 30))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setUnderline(True)
        self.label.setFont(font3)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.loginHeader.setText(QCoreApplication.translate("Form", u"Login", None))
        self.userInput.setText("")
        self.userInput.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.createAccountButton.setText(QCoreApplication.translate("Form", u"Create account", None))
        self.label.setText("")
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())