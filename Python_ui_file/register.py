# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(910, 525)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(780, 500))
        self.widget.setMaximumSize(QSize(1500, 1500))
        self.widget.setStyleSheet(u"#widget{\n"
"background-color: #ffffff;\n"
"border-radius: 25px 25px 25px 25px;\n"
"}\n"
"\n"
"*{\n"
"border: none;\n"
"}")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.passwordInput = QLineEdit(self.frame_2)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMinimumSize(QSize(400, 0))
        font = QFont()
        font.setBold(True)
        self.passwordInput.setFont(font)
        self.passwordInput.setStyleSheet(u"#passwordInput{\n"
"background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid #1e1e1e;\n"
"padding-bottom: 7px;\n"
"color: #1e1e1e;\n"
"}")
        self.passwordInput.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout.addWidget(self.passwordInput)


        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.emailInput = QLineEdit(self.frame_7)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setMinimumSize(QSize(400, 0))
        self.emailInput.setFont(font)
        self.emailInput.setStyleSheet(u"#emailInput{\n"
"background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid #1e1e1e;\n"
"padding-bottom: 7px;\n"
"color: #1e1e1e;\n"
"}")
        self.emailInput.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_5.addWidget(self.emailInput)


        self.gridLayout.addWidget(self.frame_7, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.confirmPassword = QLineEdit(self.frame_3)
        self.confirmPassword.setObjectName(u"confirmPassword")
        self.confirmPassword.setFont(font)
        self.confirmPassword.setStyleSheet(u"#confirmPassword{\n"
"background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid #1e1e1e;\n"
"padding-bottom: 7px;\n"
"color: #1e1e1e;\n"
"}")

        self.verticalLayout_2.addWidget(self.confirmPassword)


        self.gridLayout.addWidget(self.frame_3, 4, 0, 1, 1)

        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.CreateButton = QPushButton(self.frame_6)
        self.CreateButton.setObjectName(u"CreateButton")
        self.CreateButton.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.CreateButton, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.haveAccountHeader = QLabel(self.frame_8)
        self.haveAccountHeader.setObjectName(u"haveAccountHeader")
        self.haveAccountHeader.setStyleSheet(u"#haveAccountHeader{\n"
"   color: #1e1e1e;\n"
"}")

        self.gridLayout_6.addWidget(self.haveAccountHeader, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_8, 0, Qt.AlignRight)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.signInButton = QPushButton(self.frame_9)
        self.signInButton.setObjectName(u"signInButton")
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(True)
        self.signInButton.setFont(font1)
        self.signInButton.setStyleSheet(u"#signInButton {\n"
"    color: #1e1e1e;\n"
"}\n"
"\n"
"#signInButton:hover {\n"
"/*    background-color: #F5FAFE;*/\n"
"    color: #1F95EF;\n"
"    font-weight: bold; \n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.signInButton, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_9, 0, Qt.AlignLeft)


        self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_6, 5, 0, 1, 1)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.userInput = QLineEdit(self.frame_5)
        self.userInput.setObjectName(u"userInput")
        self.userInput.setMinimumSize(QSize(400, 0))
        self.userInput.setFont(font)
        self.userInput.setStyleSheet(u"#userInput{\n"
"background-color:rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid #1e1e1e;\n"
"padding-bottom: 7px;\n"
"color: #1e1e1e;\n"
"}")

        self.horizontalLayout_2.addWidget(self.userInput)


        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 1)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.loginHeader = QLabel(self.frame)
        self.loginHeader.setObjectName(u"loginHeader")
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        font2.setItalic(False)
        self.loginHeader.setFont(font2)
        self.loginHeader.setStyleSheet(u"#loginHeader{\n"
"color : #1e1e1e;\n"
"}")

        self.gridLayout_2.addWidget(self.loginHeader, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.emailInput.setText("")
        self.emailInput.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.confirmPassword.setPlaceholderText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.CreateButton.setText(QCoreApplication.translate("Form", u"Create Account", None))
        self.haveAccountHeader.setText(QCoreApplication.translate("Form", u"Already have account? ", None))
        self.signInButton.setText(QCoreApplication.translate("Form", u"Sign in.", None))
        self.userInput.setText("")
        self.userInput.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.loginHeader.setText(QCoreApplication.translate("Form", u"Register", None))
    # retranslateUi

