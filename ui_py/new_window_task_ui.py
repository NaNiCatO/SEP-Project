# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow_viewtask.ui'
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
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_view_task_frame = QFrame(self.centralwidget)
        self.main_view_task_frame.setObjectName(u"main_view_task_frame")
        self.main_view_task_frame.setStyleSheet(u"*{\n"
"color: #000;\n"
"border : none;\n"
"}\n"
"\n"
"#main_view_task_frame{\n"
"background-color: #F5FAFE;\n"
"}\n"
"\n"
"\n"
"\n"
"#create_Button, #delete_Button, #edit_Button {\n"
"    padding: 5px 10px;\n"
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
"#create_Button:hover , #delete_Button:hover , #edit_Button:hover {\n"
"    background-color: #ff6347; \n"
"}\n"
"\n"
"#scrollAreaWidgetContents_2{\n"
"background-color: transparent;\n"
"}\n"
"")
        self.main_view_task_frame.setFrameShape(QFrame.StyledPanel)
        self.main_view_task_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.main_view_task_frame)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.main_view_task_frame)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMaximumSize(QSize(16777215, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_15)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.scrollArea_4 = QScrollArea(self.frame_15)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 776, 424))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_12.addWidget(self.scrollArea_4, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_15, 1, 0, 1, 1)

        self.frame_17 = QFrame(self.main_view_task_frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_17)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.delete_Button = QPushButton(self.frame_17)
        self.delete_Button.setObjectName(u"delete_Button")

        self.gridLayout_13.addWidget(self.delete_Button, 0, 0, 1, 1)

        self.edit_Button = QPushButton(self.frame_17)
        self.edit_Button.setObjectName(u"edit_Button")

        self.gridLayout_13.addWidget(self.edit_Button, 0, 1, 1, 1)

        self.create_Button = QPushButton(self.frame_17)
        self.create_Button.setObjectName(u"create_Button")

        self.gridLayout_13.addWidget(self.create_Button, 0, 2, 1, 1)


        self.gridLayout_11.addWidget(self.frame_17, 2, 0, 1, 1, Qt.AlignRight)

        self.frame_20 = QFrame(self.main_view_task_frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 50))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_20)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainMenuButton_4 = QWidget(self.frame_20)
        self.mainMenuButton_4.setObjectName(u"mainMenuButton_4")
        self.horizontalLayout_35 = QHBoxLayout(self.mainMenuButton_4)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.homeHeader_5 = QLabel(self.mainMenuButton_4)
        self.homeHeader_5.setObjectName(u"homeHeader_5")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.homeHeader_5.setFont(font)

        self.horizontalLayout_35.addWidget(self.homeHeader_5)


        self.horizontalLayout.addWidget(self.mainMenuButton_4, 0, Qt.AlignLeft)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_21)


        self.gridLayout_11.addWidget(self.frame_20, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.main_view_task_frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.delete_Button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.edit_Button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.create_Button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.homeHeader_5.setText(QCoreApplication.translate("MainWindow", u"View Task", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    