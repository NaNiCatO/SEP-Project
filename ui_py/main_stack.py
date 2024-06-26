# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface31Mar.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import ui_py.resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1052, 641)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"color: #000;\n"
"border : none;\n"
"\n"
"}\n"
"#mainBody{\n"
"background-color:#f6f6f6;\n"
"\n"
"}\n"
"#leftMenu{\n"
"background-color:#f26e56;\n"
"}\n"
"\n"
"#frame_10{\n"
"background-color:#FAC898;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#searchFrame,#searchFrame_2,#searchFrame_3,#searchFrame_4,#searchFrame_5,#searchFrame_6{\n"
"background-color: none;\n"
"border-radius: 10px;\n"
"border : 2px solid #1e1e1e;\n"
"}\n"
"\n"
"#homeHeader{\n"
"color : #1e1e1e;\n"
"}\n"
"\n"
"#allTaskCard, #todayCard, #urgentCard, #cancleCard{\n"
"background-color:;\n"
"border : 2px solid #2596be;\n"
"border-radius:15px 15px 15px 15px;\n"
"}\n"
"\n"
"#todayButton, #urgentButton, #completedButton{\n"
"background-color:#f26e56;\n"
"color:#ffffff;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"#homeButton{\n"
"background-color:;\n"
"/*padding: 10px 5px; \n"
"border-top-left-radius: 20px;*/\n"
"text-align: left;\n"
"}\n"
"\n"
"#analysisButton, #calendarButton, #historyButton, #taskButton,#logo"
                        "utButton{\n"
"text-align: left;\n"
"\n"
"}\n"
"\n"
"#frame10{\n"
"background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"/*F5FAFE*/\n"
"background-color: #F5FAFE;\n"
"color: #1F95EF;\n"
"padding: 5px;\n"
"border-radius: 5px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"#analysisMain{\n"
"background-color: #F5FAFE;\n"
"}\n"
"\n"
"\n"
"\n"
"#main_calendar_frame{\n"
"background-color: #F5FAFE;\n"
"\n"
"}\n"
"\n"
"")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.homeMain = QWidget(self.centralwidget)
        self.homeMain.setObjectName(u"homeMain")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.homeMain.sizePolicy().hasHeightForWidth())
        self.homeMain.setSizePolicy(sizePolicy)
        self.homeMain.setMinimumSize(QSize(845, 0))
        self.verticalLayout = QVBoxLayout(self.homeMain)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.homeMain)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.a_homePage = QWidget()
        self.a_homePage.setObjectName(u"a_homePage")
        sizePolicy.setHeightForWidth(self.a_homePage.sizePolicy().hasHeightForWidth())
        self.a_homePage.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.a_homePage)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.a_homePage)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainBody = QWidget(self.frame)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        self.mainBody.setMinimumSize(QSize(500, 500))
        self.verticalLayout_2 = QVBoxLayout(self.mainBody)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QWidget(self.mainBody)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setStyleSheet(u"background-color:#FAC898;")
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.mainMenuButton = QWidget(self.headerFrame)
        self.mainMenuButton.setObjectName(u"mainMenuButton")
        self.mainMenuButton.setMinimumSize(QSize(295, 0))
        self.menuButton = QPushButton(self.mainMenuButton)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setGeometry(QRect(12, 14, 30, 30))
        self.menuButton.setMinimumSize(QSize(30, 30))
        self.menuButton.setMaximumSize(QSize(30, 30))
        self.menuButton.setSizeIncrement(QSize(10, 10))
        self.menuButton.setStyleSheet(u"image: url(:/icons/assets/icons/align-justify.svg);\n"
"")
        self.menuButton.setIconSize(QSize(18, 18))
        self.menuButton.setCheckable(True)
        self.homeHeader = QLabel(self.mainMenuButton)
        self.homeHeader.setObjectName(u"homeHeader")
        self.homeHeader.setGeometry(QRect(50, 20, 110, 19))
        self.homeHeader.setMinimumSize(QSize(110, 0))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.homeHeader.setFont(font)

        self.horizontalLayout_2.addWidget(self.mainMenuButton)

        self.mainSearchFrame = QWidget(self.headerFrame)
        self.mainSearchFrame.setObjectName(u"mainSearchFrame")
        self.mainSearchFrame.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.mainSearchFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.searchFrame = QFrame(self.mainSearchFrame)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(240, 0))
        self.searchFrame.setStyleSheet(u"background-color:#ffffff;\n"
"")
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.pushButton = QPushButton(self.searchFrame)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons_v2/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(self.searchFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons_v2/mic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.horizontalLayout_4.addWidget(self.searchFrame, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.mainSearchFrame, 0, Qt.AlignHCenter)

        self.mainAccountFrame = QWidget(self.headerFrame)
        self.mainAccountFrame.setObjectName(u"mainAccountFrame")
        self.horizontalLayout_6 = QHBoxLayout(self.mainAccountFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.mainAccountFrame)


        self.verticalLayout_2.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.cardFrame = QWidget(self.mainBody)
        self.cardFrame.setObjectName(u"cardFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.cardFrame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 0, 0)
        self.todayCard = QFrame(self.cardFrame)
        self.todayCard.setObjectName(u"todayCard")
        self.todayCard.setMinimumSize(QSize(180, 80))
        self.todayCard.setMaximumSize(QSize(160, 90))
        self.todayCard.setStyleSheet(u"#todayCard{\n"
"background-color: #ffc148;\n"
"}")
        self.todayCard.setFrameShape(QFrame.StyledPanel)
        self.todayCard.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.todayCard)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.todayTaskBG = QLabel(self.todayCard)
        self.todayTaskBG.setObjectName(u"todayTaskBG")
        self.todayTaskBG.setMinimumSize(QSize(0, 0))
        self.todayTaskBG.setMaximumSize(QSize(40, 40))
        self.todayTaskBG.setStyleSheet(u"#todayTaskBG {\n"
"/*background-color: #d89c25;\n"
"border-radius:15px;*/\n"
" \n"
"}")
        self.todayTaskBG.setPixmap(QPixmap(u":/icons_v2/last-24-hours-svgrepo-com.svg"))
        self.todayTaskBG.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.todayTaskBG)

        self.frame_2 = QFrame(self.todayCard)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.todayHeader = QLabel(self.frame_2)
        self.todayHeader.setObjectName(u"todayHeader")
        self.todayHeader.setFont(font)

        self.verticalLayout_3.addWidget(self.todayHeader, 0, Qt.AlignLeft)

        self.todayTask = QLabel(self.frame_2)
        self.todayTask.setObjectName(u"todayTask")

        self.verticalLayout_3.addWidget(self.todayTask, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.frame_2, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.todayCard)

        self.urgentCard = QFrame(self.cardFrame)
        self.urgentCard.setObjectName(u"urgentCard")
        self.urgentCard.setMinimumSize(QSize(180, 80))
        self.urgentCard.setMaximumSize(QSize(160, 90))
        self.urgentCard.setStyleSheet(u"#urgentCard{\n"
"background-color: #f26e56;\n"
"}")
        self.urgentCard.setFrameShape(QFrame.StyledPanel)
        self.urgentCard.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.urgentCard)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.todayTaskBG_4 = QLabel(self.urgentCard)
        self.todayTaskBG_4.setObjectName(u"todayTaskBG_4")
        self.todayTaskBG_4.setMinimumSize(QSize(0, 0))
        self.todayTaskBG_4.setMaximumSize(QSize(40, 40))
        self.todayTaskBG_4.setStyleSheet(u"#todayTaskBG {\n"
"background-color: #d89c25;\n"
"border-radius:15px;\n"
"}")
        self.todayTaskBG_4.setPixmap(QPixmap(u":/icons/important-dates-svgrepo-com.svg"))
        self.todayTaskBG_4.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.todayTaskBG_4)

        self.frame_4 = QFrame(self.urgentCard)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.urgentHeader = QLabel(self.frame_4)
        self.urgentHeader.setObjectName(u"urgentHeader")
        self.urgentHeader.setFont(font)

        self.verticalLayout_5.addWidget(self.urgentHeader)

        self.urgentTask = QLabel(self.frame_4)
        self.urgentTask.setObjectName(u"urgentTask")

        self.verticalLayout_5.addWidget(self.urgentTask, 0, Qt.AlignHCenter)


        self.horizontalLayout_9.addWidget(self.frame_4, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.urgentCard)

        self.allTaskCard = QFrame(self.cardFrame)
        self.allTaskCard.setObjectName(u"allTaskCard")
        self.allTaskCard.setMinimumSize(QSize(180, 80))
        self.allTaskCard.setMaximumSize(QSize(160, 90))
        self.allTaskCard.setStyleSheet(u"#allTaskCard{\n"
"background-color: #4e82d3;\n"
"}")
        self.allTaskCard.setFrameShape(QFrame.StyledPanel)
        self.allTaskCard.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.allTaskCard)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.todayTaskBG_3 = QLabel(self.allTaskCard)
        self.todayTaskBG_3.setObjectName(u"todayTaskBG_3")
        self.todayTaskBG_3.setMinimumSize(QSize(0, 0))
        self.todayTaskBG_3.setMaximumSize(QSize(40, 40))
        self.todayTaskBG_3.setStyleSheet(u"#todayTaskBG {\n"
"background-color: #d89c25;\n"
"border-radius:15px;\n"
" \n"
"}")
        self.todayTaskBG_3.setPixmap(QPixmap(u":/icons_v2/refresh-cw.svg"))
        self.todayTaskBG_3.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.todayTaskBG_3)

        self.frame_3 = QFrame(self.allTaskCard)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.allTaskHeader = QLabel(self.frame_3)
        self.allTaskHeader.setObjectName(u"allTaskHeader")
        self.allTaskHeader.setFont(font)

        self.verticalLayout_4.addWidget(self.allTaskHeader, 0, Qt.AlignHCenter)

        self.allTask = QLabel(self.frame_3)
        self.allTask.setObjectName(u"allTask")

        self.verticalLayout_4.addWidget(self.allTask, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.frame_3)


        self.horizontalLayout_7.addWidget(self.allTaskCard)

        self.cancleCard = QFrame(self.cardFrame)
        self.cancleCard.setObjectName(u"cancleCard")
        self.cancleCard.setMinimumSize(QSize(180, 80))
        self.cancleCard.setMaximumSize(QSize(160, 90))
        self.cancleCard.setStyleSheet(u"#cancleCard{\n"
"background-color: #52c1c4;\n"
"}")
        self.cancleCard.setFrameShape(QFrame.StyledPanel)
        self.cancleCard.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.cancleCard)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.todayTaskBG_2 = QLabel(self.cancleCard)
        self.todayTaskBG_2.setObjectName(u"todayTaskBG_2")
        self.todayTaskBG_2.setMinimumSize(QSize(0, 0))
        self.todayTaskBG_2.setMaximumSize(QSize(40, 40))
        self.todayTaskBG_2.setStyleSheet(u"#todayTaskBG {\n"
"background-color: #d89c25;\n"
"border-radius:15px;\n"
" \n"
"}")
        self.todayTaskBG_2.setPixmap(QPixmap(u":/icons_v2/urgent-svgrepo-com.svg"))
        self.todayTaskBG_2.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.todayTaskBG_2)

        self.frame_8 = QFrame(self.cancleCard)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.cancleHeader = QLabel(self.frame_8)
        self.cancleHeader.setObjectName(u"cancleHeader")
        self.cancleHeader.setFont(font)

        self.verticalLayout_14.addWidget(self.cancleHeader, 0, Qt.AlignHCenter)

        self.cancelTask = QLabel(self.frame_8)
        self.cancelTask.setObjectName(u"cancelTask")

        self.verticalLayout_14.addWidget(self.cancelTask, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_11.addWidget(self.frame_8)


        self.horizontalLayout_7.addWidget(self.cancleCard)


        self.verticalLayout_2.addWidget(self.cardFrame)

        self.subcardFrame = QWidget(self.mainBody)
        self.subcardFrame.setObjectName(u"subcardFrame")
        sizePolicy.setHeightForWidth(self.subcardFrame.sizePolicy().hasHeightForWidth())
        self.subcardFrame.setSizePolicy(sizePolicy)
        self.subcardFrame.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.subcardFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget = QWidget(self.subcardFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(240, 0))
        self.widget.setStyleSheet(u"#widget{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 0, 10, 10)
        self.frame_9 = QFrame(self.widget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(40, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.todayHeader_2 = QLabel(self.frame_9)
        self.todayHeader_2.setObjectName(u"todayHeader_2")
        self.todayHeader_2.setFont(font)

        self.horizontalLayout_14.addWidget(self.todayHeader_2)

        self.todayButton = QPushButton(self.frame_9)
        self.todayButton.setObjectName(u"todayButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons_v2/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.todayButton.setIcon(icon2)
        self.todayButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.todayButton)


        self.gridLayout_2.addWidget(self.frame_9, 0, 0, 1, 1, Qt.AlignTop)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(228, 0))
        self.scrollArea.setStyleSheet(u"\n"
"#scrollArea QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#scrollArea QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollArea QWidget::item {\n"
"    border-bottom: 1px solid #cccccc; /* Add a border bottom to create a line break */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cccccc;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #b3b3b3;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #999999;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
""
                        "    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 262, 367))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.todayMainTask = QFrame(self.scrollAreaWidgetContents)
        self.todayMainTask.setObjectName(u"todayMainTask")
        self.todayMainTask.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.todayMainTask.sizePolicy().hasHeightForWidth())
        self.todayMainTask.setSizePolicy(sizePolicy1)
        self.todayMainTask.setMinimumSize(QSize(0, 0))
        self.todayMainTask.setStyleSheet(u"#todayMainTask{ \n"
"background-color:#ffffff; \n"
"\n"
"border : 2px solid #f26e56; \n"
"border-radius:15px 15px 15px 15px; \n"
"\n"
"\n"
"} ")
        self.todayMainTask.setFrameShape(QFrame.StyledPanel)
        self.todayMainTask.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.todayMainTask, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.widget)

        self.widget_2 = QWidget(self.subcardFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(240, 0))
        self.widget_2.setStyleSheet(u"#widget_2{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.frame_11 = QFrame(self.widget_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(240, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 7)
        self.urgentHeader_2 = QLabel(self.frame_11)
        self.urgentHeader_2.setObjectName(u"urgentHeader_2")
        self.urgentHeader_2.setFont(font)

        self.horizontalLayout_15.addWidget(self.urgentHeader_2)

        self.urgentButton = QPushButton(self.frame_11)
        self.urgentButton.setObjectName(u"urgentButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.urgentButton.setIcon(icon3)
        self.urgentButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.urgentButton)


        self.gridLayout_3.addWidget(self.frame_11, 0, 0, 1, 1, Qt.AlignTop)

        self.scrollArea_2 = QScrollArea(self.widget_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(228, 0))
        self.scrollArea_2.setStyleSheet(u"\n"
"#scrollArea_2 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#scrollArea QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollArea QWidget::item {\n"
"    border-bottom: 1px solid #cccccc; /* Add a border bottom to create a line break */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cccccc;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #b3b3b3;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #999999;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
""
                        "    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 263, 362))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.urgentMainTask = QFrame(self.scrollAreaWidgetContents_3)
        self.urgentMainTask.setObjectName(u"urgentMainTask")
        self.urgentMainTask.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.urgentMainTask.sizePolicy().hasHeightForWidth())
        self.urgentMainTask.setSizePolicy(sizePolicy1)
        self.urgentMainTask.setMinimumSize(QSize(0, 0))
        self.urgentMainTask.setStyleSheet(u"#urgentMainTask{ \n"
"background-color:#ffffff; \n"
"border : 2px solid #f26e56; \n"
"border-radius:15px 15px 15px 15px; \n"
"} ")
        self.urgentMainTask.setFrameShape(QFrame.StyledPanel)
        self.urgentMainTask.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.urgentMainTask, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.scrollArea_2, 1, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.subcardFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(240, 0))
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}")
        self.gridLayout_7 = QGridLayout(self.widget_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(6)
        self.gridLayout_7.setVerticalSpacing(5)
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.frame_18 = QFrame(self.widget_3)
        self.frame_18.setObjectName(u"frame_18")
        font1 = QFont()
        font1.setPointSize(14)
        self.frame_18.setFont(font1)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 7)
        self.completedHeader = QLabel(self.frame_18)
        self.completedHeader.setObjectName(u"completedHeader")
        self.completedHeader.setFont(font)

        self.horizontalLayout_16.addWidget(self.completedHeader)

        self.completedButton = QPushButton(self.frame_18)
        self.completedButton.setObjectName(u"completedButton")
        self.completedButton.setIcon(icon2)
        self.completedButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.completedButton)


        self.gridLayout_7.addWidget(self.frame_18, 0, 0, 1, 1)

        self.scrollArea_3 = QScrollArea(self.widget_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(228, 0))
        self.scrollArea_3.setStyleSheet(u"\n"
"#scrollArea_3 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#scrollArea QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollArea QWidget::item {\n"
"    border-bottom: 1px solid #cccccc; /* Add a border bottom to create a line break */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cccccc;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #b3b3b3;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #999999;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
""
                        "    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 262, 362))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.completedMainTask = QFrame(self.scrollAreaWidgetContents_4)
        self.completedMainTask.setObjectName(u"completedMainTask")
        self.completedMainTask.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.completedMainTask.sizePolicy().hasHeightForWidth())
        self.completedMainTask.setSizePolicy(sizePolicy1)
        self.completedMainTask.setMinimumSize(QSize(0, 0))
        self.completedMainTask.setMaximumSize(QSize(16777215, 16777215))
        self.completedMainTask.setStyleSheet(u"#completedMainTask{ \n"
"background-color:#ffffff; \n"
"border : 2px solid #f26e56; \n"
"border-radius:15px 15px 15px 15px; \n"
"} \n"
"\n"
"#scrollArea QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"QScrollArea {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cccccc;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #b3b3b3;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #999999;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: "
                        "margin;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.completedMainTask.setFrameShape(QFrame.StyledPanel)
        self.completedMainTask.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.completedMainTask)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_7.addWidget(self.scrollArea_3, 1, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.subcardFrame)


        self.gridLayout_8.addWidget(self.mainBody, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.a_homePage)
        self.c_calendar = QWidget()
        self.c_calendar.setObjectName(u"c_calendar")
        self.gridLayout_33 = QGridLayout(self.c_calendar)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.main_calendar_frame = QFrame(self.c_calendar)
        self.main_calendar_frame.setObjectName(u"main_calendar_frame")
        self.main_calendar_frame.setStyleSheet(u"*{\n"
"color: #000;\n"
"border : none;\n"
"}\n"
"\n"
"#main_view_task_frame{\n"
"background-color: #d9d9d9;\n"
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
"    \n"
"    \n"
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
        self.main_calendar_frame.setFrameShape(QFrame.StyledPanel)
        self.main_calendar_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.main_calendar_frame)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.main_calendar_frame)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy2)
        self.frame_50.setMaximumSize(QSize(16777215, 16777215))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_50)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.frame_50)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 354, 199))
        self.gridLayout_36 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.view_frame_3 = QFrame(self.scrollAreaWidgetContents_6)
        self.view_frame_3.setObjectName(u"view_frame_3")
        self.view_frame_3.setFrameShape(QFrame.StyledPanel)
        self.view_frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.view_frame_3)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget = QCalendarWidget(self.view_frame_3)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"\n"
"#calendarWidget QWidget{\n"
"alternate-background-color: #fec89a;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"#qt_calendar_navigationbar{\n"
"background-color: #f8edeb;\n"
"border: 2px solid #f8edeb;\n"
"border-bottom: 0px;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border : 2px solid #1e1e1e; \n"
"\n"
"}\n"
"\n"
"#qt_calendar_prevmonth, #qt_calendar_nextmonth{\n"
"border: none;\n"
"qproperty-icon: none;\n"
"min-width: 13px;\n"
"max-width: 13px;\n"
"min-height: 13px;\n"
"max-height: 13px;\n"
"border-radius: 5px;\n"
"background-color: transparent;\n"
"padding: 5px;\n"
"\n"
"\n"
"}\n"
"\n"
"#qt_calendar_prevmonth{\n"
"\n"
"	image: url(:/icons/assets/icons/arrow-left.svg);\n"
"\n"
"}\n"
"\n"
"#qt_calendar_nextmonth{\n"
"\n"
"	\n"
"	image: url(:/icons/assets/icons/arrow-right.svg);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth:hover,#qt_calendar_prevmonth:hover{\n"
"background-color: #f8edeb;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_nextmonth:pressd,#qt_calendar_prevmonth:pressd{\n"
"background-color: #fcd5ce;\n"
""
                        "}\n"
"\n"
"#qt_calendar_yearbutton{\n"
"color: #000;\n"
"margin: 5px;\n"
"border-radius: 5px;\n"
"font-size: 13px;\n"
"padding: 0 10px;\n"
"}\n"
"\n"
"#qt_calendar_monthbutton{\n"
"width: 110px;\n"
"color: #000;\n"
"font-size: 13px;\n"
"margin: 5px 10px;\n"
"border-radius: 5px;\n"
"padding: 0px 0px;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:hover,#qt_calendar_nextmonth:hover,#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover{\n"
"background-color: #55aaff;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed{\n"
"background-color: rgba(235,235,235,100);\n"
"}\n"
"\n"
"#qt_calendar_yearedit{\n"
"min-width: 53px;\n"
"color: #1e1e1e;\n"
"background: transparent;\n"
"font-size: 13px;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button{\n"
"	image: url(:/icons/assets/icons/arrow-down.svg);\n"
"subcontrol-position:left;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::up-button{\n"
"	image: url(:/icons/assets/icons/arrow-up.svg);\n"
"subcontrol-position:right;\n"
"}\n"
"\n"
"#qt_calen"
                        "dar_yearedit::down-button,#qt_calendar_yearedit::up-button{\n"
"width:10px;\n"
"padding: 0px 5px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button,#qt_calendar_yearedit::up-button{\n"
"background-color: #55aaff;\n"
"}\n"
"\n"
"#calendarWidgetQToolButton QMenu{\n"
"background-color: #ffffff;\n"
"}\n"
"\n"
"#calendarWidgetQToolButton QMenu::item{\n"
"\n"
"}\n"
"\n"
"#calendarWidgetQToolButton QMenu::item:selected:enable{\n"
"background-color: #55aaff;\n"
"}\n"
"\n"
"#calendarWidgetQToolButton QToolButtin::menu-indicator{\n"
"nosubcontrol-origin: margin;\n"
"subcontrol-position:right center;\n"
"margin-top: 10px;\n"
"width:20px;\n"
"\n"
"\n"
"}\n"
"\n"
"#qt_calendar_calendarview{\n"
"border: 2px solid #fcd5ce;\n"
"border-top:0px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border : 2px solid #1e1e1e; \n"
"\n"
"\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover{\n"
"border-radius: 5px;\n"
"background-color: #cdd1d1;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_calen"
                        "darview::item:selected{\n"
"border-radius: 5px;\n"
"color:#1e1e1e;\n"
"background-color: #ffddd2;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.calendarWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_37.addWidget(self.calendarWidget, 0, 0, 1, 1)


        self.gridLayout_36.addWidget(self.view_frame_3, 0, 0, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_31.addWidget(self.scrollArea_6, 0, 0, 1, 1)


        self.gridLayout_30.addWidget(self.frame_50, 1, 0, 1, 1)

        self.frame_51 = QFrame(self.main_calendar_frame)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_51)
        self.gridLayout_32.setObjectName(u"gridLayout_32")

        self.gridLayout_30.addWidget(self.frame_51, 2, 0, 1, 1, Qt.AlignRight)

        self.frame_52 = QFrame(self.main_calendar_frame)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 50))
        self.frame_52.setStyleSheet(u"background-color:#FAC898;\n"
"")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 12)
        self.frame_45 = QFrame(self.frame_52)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(320, 0))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.menuButton_8 = QPushButton(self.frame_45)
        self.menuButton_8.setObjectName(u"menuButton_8")
        self.menuButton_8.setMinimumSize(QSize(30, 30))
        self.menuButton_8.setMaximumSize(QSize(30, 30))
        self.menuButton_8.setSizeIncrement(QSize(10, 10))
        self.menuButton_8.setStyleSheet(u"image: url(:/icons/assets/icons/align-justify.svg);\n"
"")
        self.menuButton_8.setIconSize(QSize(18, 18))
        self.menuButton_8.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.menuButton_8)

        self.homeHeader_8 = QLabel(self.frame_45)
        self.homeHeader_8.setObjectName(u"homeHeader_8")
        self.homeHeader_8.setFont(font)

        self.horizontalLayout_21.addWidget(self.homeHeader_8)


        self.horizontalLayout_23.addWidget(self.frame_45)

        self.frame_41 = QFrame(self.frame_52)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"background-color:none;")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_41)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.searchFrame_6 = QFrame(self.frame_41)
        self.searchFrame_6.setObjectName(u"searchFrame_6")
        self.searchFrame_6.setMinimumSize(QSize(240, 0))
        self.searchFrame_6.setStyleSheet(u"#searchFrame_6{\n"
"background-color: #ffffff;\n"
"border-radius: 10px;\n"
"border : 2px solid #1e1e1e;\n"
"}")
        self.searchFrame_6.setFrameShape(QFrame.StyledPanel)
        self.searchFrame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_52 = QGridLayout(self.searchFrame_6)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.gridLayout_52.setContentsMargins(5, 5, 5, 5)
        self.calendar_search_button = QPushButton(self.searchFrame_6)
        self.calendar_search_button.setObjectName(u"calendar_search_button")
        self.calendar_search_button.setIcon(icon)
        self.calendar_search_button.setIconSize(QSize(24, 24))

        self.gridLayout_52.addWidget(self.calendar_search_button, 0, 0, 1, 1)

        self.calendar_line_edit = QLineEdit(self.searchFrame_6)
        self.calendar_line_edit.setObjectName(u"calendar_line_edit")
        self.calendar_line_edit.setStyleSheet(u"")

        self.gridLayout_52.addWidget(self.calendar_line_edit, 0, 1, 1, 1)

        self.calendar_mic_button = QPushButton(self.searchFrame_6)
        self.calendar_mic_button.setObjectName(u"calendar_mic_button")
        self.calendar_mic_button.setIcon(icon1)
        self.calendar_mic_button.setIconSize(QSize(24, 24))

        self.gridLayout_52.addWidget(self.calendar_mic_button, 0, 2, 1, 1)


        self.verticalLayout_19.addWidget(self.searchFrame_6)


        self.horizontalLayout_23.addWidget(self.frame_41)

        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(320, 0))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.frame_53)


        self.gridLayout_30.addWidget(self.frame_52, 0, 0, 1, 1)


        self.gridLayout_33.addWidget(self.main_calendar_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.c_calendar)
        self.d_historyPage = QWidget()
        self.d_historyPage.setObjectName(u"d_historyPage")
        self.gridLayout_26 = QGridLayout(self.d_historyPage)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.main_create_task_frame = QFrame(self.d_historyPage)
        self.main_create_task_frame.setObjectName(u"main_create_task_frame")
        self.main_create_task_frame.setStyleSheet(u"*{\n"
"color: #000;\n"
"/*border : none;*/\n"
"}\n"
"\n"
"#main_create_task_frame{\n"
"background-color: #F5FAFE;\n"
"}\n"
"\n"
"\n"
"\n"
"#confirm_Button {\n"
"    padding: 5px 10px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #fff;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    /*background: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #f0792b, stop:0.5 #ffa163, stop:1 #edb28c);*/\n"
"	background-color: #f0792b;\n"
"   \n"
"}\n"
"\n"
"#create_Button:hover , #delete_Button:hover , #edit_Button:hover {\n"
"    background-color: #ff6347; \n"
"}\n"
"\n"
"*{\n"
"color: #000;\n"
"/*border : none;*/\n"
"\n"
"}\n"
"#frame{\n"
"background-color:#f6f6f6;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#detail_lineEdit, #topic_lineEdit{\n"
"border-radius: 10px;\n"
"margin: 5px;\n"
"border : 2px solid #f26e56;\n"
"}\n"
"\n"
"#detailHeadline{\n"
"margin-right: 35px;\n"
"}\n"
"\n"
"#topicNameHeadline{\n"
"margin-right: 3px;\n"
"}\n"
"")
        self.main_create_task_frame.setFrameShape(QFrame.StyledPanel)
        self.main_create_task_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.main_create_task_frame)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.viewTaskHeafer = QFrame(self.main_create_task_frame)
        self.viewTaskHeafer.setObjectName(u"viewTaskHeafer")
        self.viewTaskHeafer.setMinimumSize(QSize(0, 50))
        self.viewTaskHeafer.setStyleSheet(u"background-color:#FAC898;\n"
"")
        self.viewTaskHeafer.setFrameShape(QFrame.StyledPanel)
        self.viewTaskHeafer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.viewTaskHeafer)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 10)
        self.mainMenuButton_5 = QWidget(self.viewTaskHeafer)
        self.mainMenuButton_5.setObjectName(u"mainMenuButton_5")
        self.horizontalLayout_36 = QHBoxLayout(self.mainMenuButton_5)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.menuButton_6 = QPushButton(self.mainMenuButton_5)
        self.menuButton_6.setObjectName(u"menuButton_6")
        self.menuButton_6.setMinimumSize(QSize(30, 30))
        self.menuButton_6.setMaximumSize(QSize(30, 30))
        self.menuButton_6.setSizeIncrement(QSize(10, 10))
        self.menuButton_6.setStyleSheet(u"image: url(:/icons/assets/icons/align-justify.svg);\n"
"")
        self.menuButton_6.setIconSize(QSize(18, 18))
        self.menuButton_6.setCheckable(True)

        self.horizontalLayout_36.addWidget(self.menuButton_6, 0, Qt.AlignHCenter)

        self.homeHeader_6 = QLabel(self.mainMenuButton_5)
        self.homeHeader_6.setObjectName(u"homeHeader_6")
        self.homeHeader_6.setFont(font)

        self.horizontalLayout_36.addWidget(self.homeHeader_6)


        self.horizontalLayout_13.addWidget(self.mainMenuButton_5, 0, Qt.AlignLeft)

        self.frame_42 = QFrame(self.viewTaskHeafer)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_42)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.searchFrame_3 = QFrame(self.frame_42)
        self.searchFrame_3.setObjectName(u"searchFrame_3")
        self.searchFrame_3.setMinimumSize(QSize(240, 0))
        self.searchFrame_3.setStyleSheet(u"background-color:#fff;\n"
"")
        self.searchFrame_3.setFrameShape(QFrame.StyledPanel)
        self.searchFrame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.searchFrame_3)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(5, 5, 5, 5)
        self.history_search_button = QPushButton(self.searchFrame_3)
        self.history_search_button.setObjectName(u"history_search_button")
        self.history_search_button.setIcon(icon)
        self.history_search_button.setIconSize(QSize(24, 24))

        self.gridLayout_48.addWidget(self.history_search_button, 0, 0, 1, 1)

        self.history_line_edit_ = QLineEdit(self.searchFrame_3)
        self.history_line_edit_.setObjectName(u"history_line_edit_")
        self.history_line_edit_.setStyleSheet(u"")

        self.gridLayout_48.addWidget(self.history_line_edit_, 0, 1, 1, 1)

        self.history_mic_button = QPushButton(self.searchFrame_3)
        self.history_mic_button.setObjectName(u"history_mic_button")
        self.history_mic_button.setIcon(icon1)
        self.history_mic_button.setIconSize(QSize(24, 24))

        self.gridLayout_48.addWidget(self.history_mic_button, 0, 2, 1, 1)


        self.verticalLayout_18.addWidget(self.searchFrame_3)


        self.horizontalLayout_13.addWidget(self.frame_42, 0, Qt.AlignHCenter)

        self.frame_43 = QFrame(self.viewTaskHeafer)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_43)


        self.gridLayout_15.addWidget(self.viewTaskHeafer, 0, 0, 1, 1)

        self.frame_22 = QFrame(self.main_create_task_frame)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy2.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy2)
        self.frame_22.setMaximumSize(QSize(16777215, 16777215))
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_22)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(6, 12, 6, 12)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_23)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.frame_23)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"\n"
"#scrollArea_5 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#scrollArea QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollArea QWidget::item {\n"
"    border-bottom: 1px solid #cccccc; /* Add a border bottom to create a line break */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cccccc;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #b3b3b3;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #999999;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
""
                        "    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 98, 28))
        self.gridLayout_25 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.history_frame = QFrame(self.scrollAreaWidgetContents_5)
        self.history_frame.setObjectName(u"history_frame")
        self.history_frame.setFrameShape(QFrame.StyledPanel)
        self.history_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_25.addWidget(self.history_frame, 0, 0, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_24.addWidget(self.scrollArea_5, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.frame_23, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_22, 1, 0, 1, 1)


        self.gridLayout_26.addWidget(self.main_create_task_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.d_historyPage)
        self.e_viewTask = QWidget()
        self.e_viewTask.setObjectName(u"e_viewTask")
        self.gridLayout_14 = QGridLayout(self.e_viewTask)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.main_view_task_frame = QFrame(self.e_viewTask)
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
"    \n"
"}\n"
"\n"
"#create_Button:hover , #delete_Button:hover , #edit_Button:hover {\n"
"    background-color: #A8A8A8; \n"
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
        self.frame_20 = QFrame(self.main_view_task_frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 50))
        self.frame_20.setStyleSheet(u"background-color:#FAC898;\n"
"")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_20)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 10)
        self.mainMenuButton_4 = QWidget(self.frame_20)
        self.mainMenuButton_4.setObjectName(u"mainMenuButton_4")
        self.horizontalLayout_35 = QHBoxLayout(self.mainMenuButton_4)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.menuButton_5 = QPushButton(self.mainMenuButton_4)
        self.menuButton_5.setObjectName(u"menuButton_5")
        self.menuButton_5.setMinimumSize(QSize(30, 30))
        self.menuButton_5.setMaximumSize(QSize(30, 30))
        self.menuButton_5.setSizeIncrement(QSize(10, 10))
        self.menuButton_5.setStyleSheet(u"image: url(:/icons/assets/icons/align-justify.svg);\n"
"")
        self.menuButton_5.setIconSize(QSize(18, 18))
        self.menuButton_5.setCheckable(True)

        self.horizontalLayout_35.addWidget(self.menuButton_5, 0, Qt.AlignHCenter)

        self.homeHeader_5 = QLabel(self.mainMenuButton_4)
        self.homeHeader_5.setObjectName(u"homeHeader_5")
        self.homeHeader_5.setFont(font)

        self.horizontalLayout_35.addWidget(self.homeHeader_5)


        self.horizontalLayout.addWidget(self.mainMenuButton_4, 0, Qt.AlignLeft)

        self.frame_44 = QFrame(self.frame_20)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"background-color:none;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_50 = QGridLayout(self.frame_44)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.searchFrame_4 = QFrame(self.frame_44)
        self.searchFrame_4.setObjectName(u"searchFrame_4")
        self.searchFrame_4.setMinimumSize(QSize(240, 0))
        self.searchFrame_4.setStyleSheet(u"#searchFrame_4{\n"
"background-color: #ffffff;\n"
"border-radius: 10px;\n"
"border : 2px solid #1e1e1e;\n"
"}")
        self.searchFrame_4.setFrameShape(QFrame.StyledPanel)
        self.searchFrame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.searchFrame_4)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(5, 5, 5, 5)
        self.view_search_button = QPushButton(self.searchFrame_4)
        self.view_search_button.setObjectName(u"view_search_button")
        self.view_search_button.setIcon(icon)
        self.view_search_button.setIconSize(QSize(24, 24))

        self.gridLayout_49.addWidget(self.view_search_button, 0, 0, 1, 1)

        self.view_line_edit = QLineEdit(self.searchFrame_4)
        self.view_line_edit.setObjectName(u"view_line_edit")
        self.view_line_edit.setStyleSheet(u"")

        self.gridLayout_49.addWidget(self.view_line_edit, 0, 1, 1, 1)

        self.view_mic_button = QPushButton(self.searchFrame_4)
        self.view_mic_button.setObjectName(u"view_mic_button")
        self.view_mic_button.setIcon(icon1)
        self.view_mic_button.setIconSize(QSize(24, 24))

        self.gridLayout_49.addWidget(self.view_mic_button, 0, 2, 1, 1)


        self.gridLayout_50.addWidget(self.searchFrame_4, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_44, 0, Qt.AlignHCenter)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_21)


        self.gridLayout_11.addWidget(self.frame_20, 0, 0, 1, 1)

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

        self.frame_15 = QFrame(self.main_view_task_frame)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy2.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy2)
        self.frame_15.setMaximumSize(QSize(16777215, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_15)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"#ongoing_Task_Button,#complete_Task_Button,#late_Task_Button{\n"
"    padding: 5px 0px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    color: #1e1e1e;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    /*background: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #f0792b, stop:0.5 #ffa163, stop:1 #edb28c);*/\n"
"	background-color: #f0792b;\n"
"\n"
"	\n"
"}\n"
"\n"
"\n"
"#ongoing_Task_Button::hover ,\n"
"#complete_Task_Button::hover ,\n"
"#late_Task_Button::hover {\n"
"\n"
"    background-color: #ff6347; \n"
"	background-color: #A8A8A8;\n"
"\n"
"}")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 12, 0, 0)
        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"padding: 5px;\n"
"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_19.setSpacing(6)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.ongoing_Task_Button = QPushButton(self.frame_40)
        self.ongoing_Task_Button.setObjectName(u"ongoing_Task_Button")
        icon4 = QIcon()
        icon4.addFile(u":/icons_v2/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ongoing_Task_Button.setIcon(icon4)

        self.horizontalLayout_19.addWidget(self.ongoing_Task_Button)

        self.complete_Task_Button = QPushButton(self.frame_40)
        self.complete_Task_Button.setObjectName(u"complete_Task_Button")
        icon5 = QIcon()
        icon5.addFile(u":/icons_v2/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.complete_Task_Button.setIcon(icon5)

        self.horizontalLayout_19.addWidget(self.complete_Task_Button)

        self.late_Task_Button = QPushButton(self.frame_40)
        self.late_Task_Button.setObjectName(u"late_Task_Button")
        icon6 = QIcon()
        icon6.addFile(u":/icons_v2/late.png", QSize(), QIcon.Normal, QIcon.Off)
        self.late_Task_Button.setIcon(icon6)

        self.horizontalLayout_19.addWidget(self.late_Task_Button)


        self.horizontalLayout_18.addWidget(self.frame_40, 0, Qt.AlignLeft)

        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_39)
        self.gridLayout_43.setObjectName(u"gridLayout_43")

        self.horizontalLayout_18.addWidget(self.frame_39)


        self.verticalLayout_17.addWidget(self.frame_38)

        self.frame_37 = QFrame(self.frame_15)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_37)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.frame_37)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"\n"
"#scrollArea_4 QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#scrollArea QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollArea QWidget::item {\n"
"    border-bottom: 1px solid #cccccc; /* Add a border bottom to create a line break */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #cccccc;\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #b3b3b3;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background: #999999;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
""
                        "    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 98, 28))
        self.gridLayout_28 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.taskList_frame = QFrame(self.scrollAreaWidgetContents_2)
        self.taskList_frame.setObjectName(u"taskList_frame")
        self.taskList_frame.setFrameShape(QFrame.StyledPanel)
        self.taskList_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.taskList_frame)
        self.gridLayout_35.setSpacing(4)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(4, 4, 4, 4)
        self.stackedWidget_2 = QStackedWidget(self.taskList_frame)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.ongoingStack = QWidget()
        self.ongoingStack.setObjectName(u"ongoingStack")
        self.gridLayout_46 = QGridLayout(self.ongoingStack)
        self.gridLayout_46.setSpacing(0)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.ongoing_Task_Frame = QFrame(self.ongoingStack)
        self.ongoing_Task_Frame.setObjectName(u"ongoing_Task_Frame")
        self.ongoing_Task_Frame.setFrameShape(QFrame.StyledPanel)
        self.ongoing_Task_Frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_46.addWidget(self.ongoing_Task_Frame, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.ongoingStack)
        self.lateStack = QWidget()
        self.lateStack.setObjectName(u"lateStack")
        self.gridLayout_45 = QGridLayout(self.lateStack)
        self.gridLayout_45.setSpacing(0)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.late_Task_Frame = QFrame(self.lateStack)
        self.late_Task_Frame.setObjectName(u"late_Task_Frame")
        self.late_Task_Frame.setFrameShape(QFrame.StyledPanel)
        self.late_Task_Frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_45.addWidget(self.late_Task_Frame, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.lateStack)
        self.completeStack = QWidget()
        self.completeStack.setObjectName(u"completeStack")
        self.gridLayout_44 = QGridLayout(self.completeStack)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.complete_Task_Frame = QFrame(self.completeStack)
        self.complete_Task_Frame.setObjectName(u"complete_Task_Frame")
        self.complete_Task_Frame.setFrameShape(QFrame.StyledPanel)
        self.complete_Task_Frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_44.addWidget(self.complete_Task_Frame, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.completeStack)

        self.gridLayout_35.addWidget(self.stackedWidget_2, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.taskList_frame, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_12.addWidget(self.scrollArea_4, 0, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_37)


        self.gridLayout_11.addWidget(self.frame_15, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.main_view_task_frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.e_viewTask)
        self.b_analysisPage = QWidget()
        self.b_analysisPage.setObjectName(u"b_analysisPage")
        self.gridLayout_19 = QGridLayout(self.b_analysisPage)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.analysisMain = QFrame(self.b_analysisPage)
        self.analysisMain.setObjectName(u"analysisMain")
        sizePolicy.setHeightForWidth(self.analysisMain.sizePolicy().hasHeightForWidth())
        self.analysisMain.setSizePolicy(sizePolicy)
        self.analysisMain.setFrameShape(QFrame.StyledPanel)
        self.analysisMain.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.analysisMain)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.mainBody_3 = QWidget(self.analysisMain)
        self.mainBody_3.setObjectName(u"mainBody_3")
        sizePolicy1.setHeightForWidth(self.mainBody_3.sizePolicy().hasHeightForWidth())
        self.mainBody_3.setSizePolicy(sizePolicy1)
        self.mainBody_3.setMinimumSize(QSize(0, 0))
        self.mainBody_3.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.mainBody_3)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.headerFrame_3 = QWidget(self.mainBody_3)
        self.headerFrame_3.setObjectName(u"headerFrame_3")
        self.headerFrame_3.setStyleSheet(u"background-color: #FAC898;")
        self.horizontalLayout_30 = QHBoxLayout(self.headerFrame_3)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 10)
        self.mainMenuButton_3 = QWidget(self.headerFrame_3)
        self.mainMenuButton_3.setObjectName(u"mainMenuButton_3")
        self.horizontalLayout_31 = QHBoxLayout(self.mainMenuButton_3)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.menuButton_3 = QPushButton(self.mainMenuButton_3)
        self.menuButton_3.setObjectName(u"menuButton_3")
        self.menuButton_3.setMinimumSize(QSize(30, 30))
        self.menuButton_3.setMaximumSize(QSize(30, 30))
        self.menuButton_3.setSizeIncrement(QSize(10, 10))
        self.menuButton_3.setStyleSheet(u"image: url(:/icons/assets/icons/align-justify.svg);\n"
"")
        self.menuButton_3.setIconSize(QSize(18, 18))
        self.menuButton_3.setCheckable(True)

        self.horizontalLayout_31.addWidget(self.menuButton_3)

        self.homeHeader_3 = QLabel(self.mainMenuButton_3)
        self.homeHeader_3.setObjectName(u"homeHeader_3")
        self.homeHeader_3.setFont(font)

        self.horizontalLayout_31.addWidget(self.homeHeader_3)


        self.horizontalLayout_30.addWidget(self.mainMenuButton_3)

        self.mainSearchFrame_3 = QWidget(self.headerFrame_3)
        self.mainSearchFrame_3.setObjectName(u"mainSearchFrame_3")
        self.horizontalLayout_20 = QHBoxLayout(self.mainSearchFrame_3)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.searchFrame_5 = QFrame(self.mainSearchFrame_3)
        self.searchFrame_5.setObjectName(u"searchFrame_5")
        self.searchFrame_5.setMinimumSize(QSize(240, 0))
        self.searchFrame_5.setStyleSheet(u"background-color:#fff;\n"
"")
        self.searchFrame_5.setFrameShape(QFrame.StyledPanel)
        self.searchFrame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_51 = QGridLayout(self.searchFrame_5)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(5, 5, 5, 5)
        self.analysis_search_button = QPushButton(self.searchFrame_5)
        self.analysis_search_button.setObjectName(u"analysis_search_button")
        self.analysis_search_button.setIcon(icon)
        self.analysis_search_button.setIconSize(QSize(24, 24))

        self.gridLayout_51.addWidget(self.analysis_search_button, 0, 0, 1, 1)

        self.analysis_line_edit = QLineEdit(self.searchFrame_5)
        self.analysis_line_edit.setObjectName(u"analysis_line_edit")
        self.analysis_line_edit.setStyleSheet(u"")

        self.gridLayout_51.addWidget(self.analysis_line_edit, 0, 1, 1, 1)

        self.analysis_mic_button = QPushButton(self.searchFrame_5)
        self.analysis_mic_button.setObjectName(u"analysis_mic_button")
        self.analysis_mic_button.setIcon(icon1)
        self.analysis_mic_button.setIconSize(QSize(24, 24))

        self.gridLayout_51.addWidget(self.analysis_mic_button, 0, 2, 1, 1)


        self.horizontalLayout_20.addWidget(self.searchFrame_5)


        self.horizontalLayout_30.addWidget(self.mainSearchFrame_3, 0, Qt.AlignHCenter)

        self.mainAccountFrame_3 = QWidget(self.headerFrame_3)
        self.mainAccountFrame_3.setObjectName(u"mainAccountFrame_3")
        self.horizontalLayout_34 = QHBoxLayout(self.mainAccountFrame_3)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_30.addWidget(self.mainAccountFrame_3)


        self.verticalLayout_21.addWidget(self.headerFrame_3, 0, Qt.AlignTop)

        self.subcardFrame_3 = QWidget(self.mainBody_3)
        self.subcardFrame_3.setObjectName(u"subcardFrame_3")
        sizePolicy.setHeightForWidth(self.subcardFrame_3.sizePolicy().hasHeightForWidth())
        self.subcardFrame_3.setSizePolicy(sizePolicy)
        self.subcardFrame_3.setMaximumSize(QSize(16777215, 16777215))
        self.subcardFrame_3.setStyleSheet(u"background-color: #ffffff;")
        self.horizontalLayout_40 = QHBoxLayout(self.subcardFrame_3)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.left_content = QWidget(self.subcardFrame_3)
        self.left_content.setObjectName(u"left_content")
        self.left_content.setMinimumSize(QSize(240, 0))
        self.left_content.setStyleSheet(u"#widget{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}")
        self.verticalLayout_22 = QVBoxLayout(self.left_content)
        self.verticalLayout_22.setSpacing(5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.remain_task_detail_anal = QFrame(self.left_content)
        self.remain_task_detail_anal.setObjectName(u"remain_task_detail_anal")
        self.remain_task_detail_anal.setMinimumSize(QSize(0, 200))
        self.remain_task_detail_anal.setCursor(QCursor(Qt.ArrowCursor))
        self.remain_task_detail_anal.setStyleSheet(u"#remain_task_detail_anal{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}")
        self.remain_task_detail_anal.setFrameShape(QFrame.StyledPanel)
        self.remain_task_detail_anal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.remain_task_detail_anal)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.remain_task_detail_anal)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 0))
        self.frame_30.setMaximumSize(QSize(400, 60))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_30)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_30)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_5.setFont(font2)

        self.gridLayout_41.addWidget(self.label_5, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_12.addWidget(self.frame_30)

        self.frame_32 = QFrame(self.remain_task_detail_anal)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_32)
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy3)
        self.frame_33.setStyleSheet(u"#frame_33 {\n"
"    background-color: #ffcd69;\n"
"    \n"
"    border-radius: 102px;\n"
"}\n"
"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_33)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy3.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy3)
        self.frame_34.setMinimumSize(QSize(180, 180))
        self.frame_34.setStyleSheet(u"#frame_34 {\n"
"    background-color: #ffffff;\n"
"\n"
"    border-radius: 90px;\n"
"}\n"
"")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_34)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.label_6 = QLabel(self.frame_34)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_39.addWidget(self.label_6, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_40.addWidget(self.frame_34, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.frame_33, 0, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_32)


        self.verticalLayout_22.addWidget(self.remain_task_detail_anal)

        self.all_time_anal = QFrame(self.left_content)
        self.all_time_anal.setObjectName(u"all_time_anal")
        self.all_time_anal.setStyleSheet(u"#all_time_anal{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"#anal1,#anal2, #completed_anal,#pass_due_anal{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}")
        self.all_time_anal.setFrameShape(QFrame.StyledPanel)
        self.all_time_anal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.all_time_anal)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.all_time_anal)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        self.frame_19.setFont(font3)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_19)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_29)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_29)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(21)
        font4.setBold(True)
        self.label.setFont(font4)

        self.gridLayout_18.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_17.addWidget(self.frame_29)

        self.frame_31 = QFrame(self.frame_19)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_31)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_31)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.gridLayout_17.addWidget(self.label_7, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_17.addWidget(self.frame_31)


        self.verticalLayout_10.addWidget(self.frame_19)

        self.frame_24 = QFrame(self.all_time_anal)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.urgent_task_anal = QFrame(self.frame_24)
        self.urgent_task_anal.setObjectName(u"urgent_task_anal")
        self.urgent_task_anal.setFrameShape(QFrame.StyledPanel)
        self.urgent_task_anal.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.urgent_task_anal)

        self.normal_task_anal = QFrame(self.frame_24)
        self.normal_task_anal.setObjectName(u"normal_task_anal")
        self.normal_task_anal.setFrameShape(QFrame.StyledPanel)
        self.normal_task_anal.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.normal_task_anal)


        self.verticalLayout_10.addWidget(self.frame_24)


        self.verticalLayout_22.addWidget(self.all_time_anal)


        self.horizontalLayout_40.addWidget(self.left_content)

        self.right_content = QWidget(self.subcardFrame_3)
        self.right_content.setObjectName(u"right_content")
        self.right_content.setMinimumSize(QSize(200, 0))
        self.right_content.setStyleSheet(u"#right_content_detail1 ,#right_content_detail2, #right_content_detail3{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"#right_content_header{\n"
"/*border: 2px solid #1e1e1e;\n"
"border-radius: 10px*/\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.right_content)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.right_content_detail1 = QFrame(self.right_content)
        self.right_content_detail1.setObjectName(u"right_content_detail1")
        self.right_content_detail1.setEnabled(True)
        self.right_content_detail1.setMinimumSize(QSize(0, 140))
        self.right_content_detail1.setStyleSheet(u"")
        self.right_content_detail1.setFrameShape(QFrame.StyledPanel)
        self.right_content_detail1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.right_content_detail1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.right_content_detail1)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 50))
        self.frame_35.setStyleSheet(u"")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_35)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_35)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.verticalLayout_13.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_35)

        self.frame_25 = QFrame(self.right_content_detail1)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_25)
        self.gridLayout_34.setSpacing(0)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.gridLayout_34.addWidget(self.frame_26, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_25)


        self.verticalLayout_8.addWidget(self.right_content_detail1)

        self.right_content_detail2 = QFrame(self.right_content)
        self.right_content_detail2.setObjectName(u"right_content_detail2")
        self.right_content_detail2.setMinimumSize(QSize(150, 140))
        self.right_content_detail2.setFrameShape(QFrame.StyledPanel)
        self.right_content_detail2.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.right_content_detail2)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.right_content_detail2)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 50))
        self.frame_36.setStyleSheet(u"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_36)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_36)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)

        self.verticalLayout_16.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.gridLayout_29.addWidget(self.frame_36, 0, 0, 1, 1)

        self.frame_27 = QFrame(self.right_content_detail2)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_27)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.gridLayout_42.addWidget(self.frame_28, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.frame_27, 1, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.right_content_detail2)


        self.horizontalLayout_40.addWidget(self.right_content)


        self.verticalLayout_21.addWidget(self.subcardFrame_3)


        self.gridLayout_16.addWidget(self.mainBody_3, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.analysisMain, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.b_analysisPage)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout_6.addWidget(self.homeMain, 0, 2, 1, 1)

        self.profileContent = QWidget(self.centralwidget)
        self.profileContent.setObjectName(u"profileContent")
        self.profileContent.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.profileContent)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_6.addWidget(self.profileContent, 0, 3, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setSizeIncrement(QSize(0, 0))
        self.frame_5.setStyleSheet(u"background-color: #ffffff;\n"
"border-radius: 1px solid #1e1e1e;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(110, 32))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.toDoHeader = QLabel(self.frame_7)
        self.toDoHeader.setObjectName(u"toDoHeader")
        self.toDoHeader.setEnabled(True)
        self.toDoHeader.setGeometry(QRect(0, 0, 101, 29))
        self.toDoHeader.setMinimumSize(QSize(0, 0))
        self.toDoHeader.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(24)
        font5.setBold(True)
        self.toDoHeader.setFont(font5)

        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QSize(110, 0))
        font6 = QFont()
        font6.setPointSize(15)
        self.frame_14.setFont(font6)
        self.frame_14.setToolTipDuration(0)
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_14)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 5, 0)
        self.homeButton = QPushButton(self.frame_14)
        self.homeButton.setObjectName(u"homeButton")
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        self.homeButton.setFont(font7)
        icon7 = QIcon()
        icon7.addFile(u":/icons_v2/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon7)
        self.homeButton.setIconSize(QSize(24, 24))
        self.homeButton.setCheckable(True)
        self.homeButton.setAutoExclusive(True)

        self.gridLayout_10.addWidget(self.homeButton, 0, 0, 1, 1)

        self.analysisButton = QPushButton(self.frame_14)
        self.analysisButton.setObjectName(u"analysisButton")
        self.analysisButton.setFont(font7)
        self.analysisButton.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons_v2/pie-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.analysisButton.setIcon(icon8)
        self.analysisButton.setIconSize(QSize(24, 24))
        self.analysisButton.setCheckable(True)
        self.analysisButton.setAutoExclusive(True)

        self.gridLayout_10.addWidget(self.analysisButton, 1, 0, 1, 1)

        self.calendarButton = QPushButton(self.frame_14)
        self.calendarButton.setObjectName(u"calendarButton")
        self.calendarButton.setMinimumSize(QSize(0, 0))
        self.calendarButton.setFont(font7)
        self.calendarButton.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calendarButton.setIcon(icon9)
        self.calendarButton.setIconSize(QSize(24, 24))
        self.calendarButton.setCheckable(True)
        self.calendarButton.setAutoExclusive(True)

        self.gridLayout_10.addWidget(self.calendarButton, 2, 0, 1, 1)

        self.historyButton = QPushButton(self.frame_14)
        self.historyButton.setObjectName(u"historyButton")
        self.historyButton.setFont(font7)
        icon10 = QIcon()
        icon10.addFile(u":/icons_v2/history-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.historyButton.setIcon(icon10)
        self.historyButton.setIconSize(QSize(24, 24))
        self.historyButton.setCheckable(True)
        self.historyButton.setAutoExclusive(True)

        self.gridLayout_10.addWidget(self.historyButton, 3, 0, 1, 1)

        self.taskButton = QPushButton(self.frame_14)
        self.taskButton.setObjectName(u"taskButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.taskButton.sizePolicy().hasHeightForWidth())
        self.taskButton.setSizePolicy(sizePolicy4)
        self.taskButton.setFont(font7)
        icon11 = QIcon()
        icon11.addFile(u":/icons_v2/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.taskButton.setIcon(icon11)
        self.taskButton.setIconSize(QSize(24, 24))
        self.taskButton.setCheckable(True)
        self.taskButton.setAutoExclusive(True)

        self.gridLayout_10.addWidget(self.taskButton, 4, 0, 1, 1)

        self.settingButton = QPushButton(self.frame_14)
        self.settingButton.setObjectName(u"settingButton")
        self.settingButton.setFont(font7)
        self.settingButton.setStyleSheet(u"padding-right:25px;\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons_v2/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingButton.setIcon(icon12)
        self.settingButton.setIconSize(QSize(24, 24))
        self.settingButton.setCheckable(True)
        self.settingButton.setAutoExclusive(True)

        self.gridLayout_10.addWidget(self.settingButton, 5, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_14)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMinimumSize(QSize(110, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.frame_6)


        self.gridLayout_6.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.centralwidget)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(60, 1000))
        self.frame_10.setStyleSheet(u"#frame_10{\n"
"background-color: #FAC898;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_10)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_16)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.homeMiniButton = QPushButton(self.frame_16)
        self.homeMiniButton.setObjectName(u"homeMiniButton")
        self.homeMiniButton.setFont(font6)
        self.homeMiniButton.setIcon(icon7)
        self.homeMiniButton.setIconSize(QSize(24, 24))
        self.homeMiniButton.setCheckable(True)
        self.homeMiniButton.setAutoExclusive(True)

        self.gridLayout_27.addWidget(self.homeMiniButton, 0, 0, 1, 1)

        self.analysisMiniButton = QPushButton(self.frame_16)
        self.analysisMiniButton.setObjectName(u"analysisMiniButton")
        self.analysisMiniButton.setFont(font6)
        self.analysisMiniButton.setIcon(icon8)
        self.analysisMiniButton.setIconSize(QSize(24, 24))
        self.analysisMiniButton.setCheckable(True)
        self.analysisMiniButton.setAutoExclusive(True)

        self.gridLayout_27.addWidget(self.analysisMiniButton, 1, 0, 1, 1)

        self.calendarMiniButton = QPushButton(self.frame_16)
        self.calendarMiniButton.setObjectName(u"calendarMiniButton")
        self.calendarMiniButton.setFont(font6)
        self.calendarMiniButton.setIcon(icon9)
        self.calendarMiniButton.setIconSize(QSize(24, 24))
        self.calendarMiniButton.setCheckable(True)
        self.calendarMiniButton.setAutoExclusive(True)

        self.gridLayout_27.addWidget(self.calendarMiniButton, 2, 0, 1, 1)

        self.historyMiniButton = QPushButton(self.frame_16)
        self.historyMiniButton.setObjectName(u"historyMiniButton")
        self.historyMiniButton.setFont(font6)
        self.historyMiniButton.setIcon(icon10)
        self.historyMiniButton.setIconSize(QSize(24, 24))
        self.historyMiniButton.setCheckable(True)
        self.historyMiniButton.setAutoExclusive(True)

        self.gridLayout_27.addWidget(self.historyMiniButton, 3, 0, 1, 1)

        self.taskMiniButton = QPushButton(self.frame_16)
        self.taskMiniButton.setObjectName(u"taskMiniButton")
        self.taskMiniButton.setFont(font6)
        self.taskMiniButton.setIcon(icon11)
        self.taskMiniButton.setIconSize(QSize(24, 24))
        self.taskMiniButton.setCheckable(True)
        self.taskMiniButton.setAutoExclusive(True)

        self.gridLayout_27.addWidget(self.taskMiniButton, 4, 0, 1, 1)

        self.logoutMiniButton = QPushButton(self.frame_16)
        self.logoutMiniButton.setObjectName(u"logoutMiniButton")
        self.logoutMiniButton.setIcon(icon12)
        self.logoutMiniButton.setIconSize(QSize(24, 24))
        self.logoutMiniButton.setCheckable(True)
        self.logoutMiniButton.setAutoExclusive(True)

        self.gridLayout_27.addWidget(self.logoutMiniButton, 5, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_16, 1, 0, 1, 1)

        self.fix = QFrame(self.frame_10)
        self.fix.setObjectName(u"fix")
        self.fix.setMinimumSize(QSize(0, 0))
        self.fix.setFrameShape(QFrame.StyledPanel)
        self.fix.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.fix)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_9.addWidget(self.fix, 2, 0, 1, 1)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setStyleSheet(u"#pushButton_6{\n"
"border : 1px solid #1e1e1e;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_13)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_13)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_12)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.toDoHeader_2 = QLabel(self.frame_12)
        self.toDoHeader_2.setObjectName(u"toDoHeader_2")
        self.toDoHeader_2.setEnabled(True)
        self.toDoHeader_2.setMinimumSize(QSize(0, 0))
        self.toDoHeader_2.setMaximumSize(QSize(16777215, 16777215))
        self.toDoHeader_2.setFont(font2)

        self.gridLayout_22.addWidget(self.toDoHeader_2, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.frame_12, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_13, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_10, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1052, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.menuButton.toggled.connect(self.frame_5.setVisible)
        self.menuButton.toggled.connect(self.frame_10.setHidden)
        self.menuButton_3.toggled.connect(self.frame_5.setVisible)
        self.menuButton_3.toggled.connect(self.frame_10.setHidden)
        self.menuButton_5.toggled.connect(self.frame_5.setVisible)
        self.menuButton_5.toggled.connect(self.frame_10.setHidden)
        self.menuButton_6.toggled.connect(self.frame_5.setVisible)
        self.menuButton_6.toggled.connect(self.frame_10.setHidden)
        self.analysisMiniButton.toggled.connect(self.analysisButton.setChecked)
        self.calendarButton.toggled.connect(self.calendarMiniButton.setChecked)
        self.taskMiniButton.toggled.connect(self.taskButton.setChecked)
        self.taskButton.toggled.connect(self.taskMiniButton.setChecked)
        self.homeMiniButton.toggled.connect(self.homeButton.setChecked)
        self.calendarMiniButton.toggled.connect(self.calendarButton.setChecked)
        self.analysisButton.toggled.connect(self.analysisMiniButton.setChecked)
        self.historyMiniButton.toggled.connect(self.historyButton.setChecked)
        self.historyButton.toggled.connect(self.historyMiniButton.setChecked)
        self.homeButton.toggled.connect(self.homeMiniButton.setChecked)
        self.menuButton_8.toggled.connect(self.frame_5.setVisible)
        self.menuButton_8.toggled.connect(self.frame_10.setHidden)
        self.logoutMiniButton.toggled.connect(self.settingButton.setChecked)
        self.settingButton.toggled.connect(self.logoutMiniButton.setChecked)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
        self.homeHeader.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Task", None))
        self.pushButton_2.setText("")
        self.todayTaskBG.setText("")
        self.todayHeader.setText(QCoreApplication.translate("MainWindow", u"Today Task", None))
        self.todayTask.setText(QCoreApplication.translate("MainWindow", u"variable", None))
        self.todayTaskBG_4.setText("")
        self.urgentHeader.setText(QCoreApplication.translate("MainWindow", u"Urgent Task", None))
        self.urgentTask.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.todayTaskBG_3.setText("")
        self.allTaskHeader.setText(QCoreApplication.translate("MainWindow", u"All Task", None))
        self.allTask.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.todayTaskBG_2.setText("")
        self.cancleHeader.setText(QCoreApplication.translate("MainWindow", u"Late Task", None))
        self.cancelTask.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.todayHeader_2.setText(QCoreApplication.translate("MainWindow", u"Today Task", None))
        self.todayButton.setText(QCoreApplication.translate("MainWindow", u"View more", None))
        self.urgentHeader_2.setText(QCoreApplication.translate("MainWindow", u"Urgent Task", None))
        self.urgentButton.setText(QCoreApplication.translate("MainWindow", u"View more", None))
        self.completedHeader.setText(QCoreApplication.translate("MainWindow", u"Completed Task", None))
        self.completedButton.setText(QCoreApplication.translate("MainWindow", u"View more", None))
        self.menuButton_8.setText("")
        self.homeHeader_8.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.calendar_search_button.setText("")
        self.calendar_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Task", None))
        self.calendar_mic_button.setText("")
        self.menuButton_6.setText("")
        self.homeHeader_6.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.history_search_button.setText("")
        self.history_line_edit_.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Task", None))
        self.history_mic_button.setText("")
        self.menuButton_5.setText("")
        self.homeHeader_5.setText(QCoreApplication.translate("MainWindow", u"View Task", None))
        self.view_search_button.setText("")
        self.view_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Task", None))
        self.view_mic_button.setText("")
        self.delete_Button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.edit_Button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.create_Button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.ongoing_Task_Button.setText(QCoreApplication.translate("MainWindow", u"Ongoing Task", None))
        self.complete_Task_Button.setText(QCoreApplication.translate("MainWindow", u"Complete Task", None))
        self.late_Task_Button.setText(QCoreApplication.translate("MainWindow", u"Late Task", None))
        self.menuButton_3.setText("")
        self.homeHeader_3.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.analysis_search_button.setText("")
        self.analysis_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Task", None))
        self.analysis_mic_button.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Remaining Task", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"varaible", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Normal Task", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Urgent Task", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Completed Task %", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Delay Task %", None))
        self.toDoHeader.setText(QCoreApplication.translate("MainWindow", u"ToDo", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.analysisButton.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.calendarButton.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.taskButton.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.settingButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.homeMiniButton.setText("")
        self.analysisMiniButton.setText("")
        self.calendarMiniButton.setText("")
        self.historyMiniButton.setText("")
        self.taskMiniButton.setText("")
        self.logoutMiniButton.setText("")
        self.toDoHeader_2.setText(QCoreApplication.translate("MainWindow", u"ToDo", None))
    # retranslateUi

