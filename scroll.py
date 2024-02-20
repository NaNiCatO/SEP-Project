# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacetryscroll.ui'
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(939, 599)
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
"QLineEdit{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#searchFrame{\n"
"border-radius: 10px;\n"
"border : 2px solid #2596be;\n"
"}\n"
"\n"
"#homeHeader{\n"
"color : #f26e56;\n"
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
"background-color:#ffffff;\n"
"padding: 10px 5px; \n"
"text-align: left;\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"#analysisButton, #calendarButton, #historyButton, #taskButton{\n"
"padding: 10px 5px; \n"
"text-align: left;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QWidget(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(50, 0))
        self.verticalLayout_7 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.leftMenu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.toDoHeader = QLabel(self.frame_7)
        self.toDoHeader.setObjectName(u"toDoHeader")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.toDoHeader.setFont(font)

        self.horizontalLayout_13.addWidget(self.toDoHeader, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(16, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setSpacing(30)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.frame_14)
        self.homeButton.setObjectName(u"homeButton")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.homeButton.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons_v2/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QSize(24, 24))

        self.verticalLayout_12.addWidget(self.homeButton)

        self.analysisButton = QPushButton(self.frame_14)
        self.analysisButton.setObjectName(u"analysisButton")
        self.analysisButton.setFont(font1)
        self.analysisButton.setIconSize(QSize(24, 24))

        self.verticalLayout_12.addWidget(self.analysisButton)

        self.calendarButton = QPushButton(self.frame_14)
        self.calendarButton.setObjectName(u"calendarButton")
        self.calendarButton.setFont(font1)

        self.verticalLayout_12.addWidget(self.calendarButton)

        self.historyButton = QPushButton(self.frame_14)
        self.historyButton.setObjectName(u"historyButton")
        self.historyButton.setFont(font1)

        self.verticalLayout_12.addWidget(self.historyButton)

        self.taskButton = QPushButton(self.frame_14)
        self.taskButton.setObjectName(u"taskButton")
        self.taskButton.setFont(font1)

        self.verticalLayout_12.addWidget(self.taskButton)


        self.verticalLayout_11.addWidget(self.frame_14, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_6)


        self.verticalLayout_7.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QWidget(self.mainBody)
        self.headerFrame.setObjectName(u"headerFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.mainMenuButton = QWidget(self.headerFrame)
        self.mainMenuButton.setObjectName(u"mainMenuButton")
        self.horizontalLayout_3 = QHBoxLayout(self.mainMenuButton)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuButton = QPushButton(self.mainMenuButton)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(30, 30))
        self.menuButton.setMaximumSize(QSize(30, 30))
        self.menuButton.setSizeIncrement(QSize(10, 10))
        self.menuButton.setStyleSheet(u"image: url(:/icons/assets/icons/align-justify.svg);")
        self.menuButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_3.addWidget(self.menuButton)

        self.homeHeader = QLabel(self.mainMenuButton)
        self.homeHeader.setObjectName(u"homeHeader")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.homeHeader.setFont(font2)

        self.horizontalLayout_3.addWidget(self.homeHeader)


        self.horizontalLayout_2.addWidget(self.mainMenuButton, 0, Qt.AlignLeft)

        self.mainSearchFrame = QWidget(self.headerFrame)
        self.mainSearchFrame.setObjectName(u"mainSearchFrame")
        self.horizontalLayout_4 = QHBoxLayout(self.mainSearchFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.searchFrame = QFrame(self.mainSearchFrame)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(240, 0))
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.searchicon = QLabel(self.searchFrame)
        self.searchicon.setObjectName(u"searchicon")
        self.searchicon.setMinimumSize(QSize(30, 30))
        self.searchicon.setMaximumSize(QSize(30, 30))
        self.searchicon.setStyleSheet(u"")
        self.searchicon.setPixmap(QPixmap(u":/icons_v2/search.svg"))
        self.searchicon.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.searchicon)

        self.lineEdit = QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_4.addWidget(self.searchFrame, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.mainSearchFrame, 0, Qt.AlignHCenter)

        self.mainAccountFrame = QWidget(self.headerFrame)
        self.mainAccountFrame.setObjectName(u"mainAccountFrame")
        self.horizontalLayout_6 = QHBoxLayout(self.mainAccountFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountButton = QPushButton(self.mainAccountFrame)
        self.accountButton.setObjectName(u"accountButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons_v2/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.accountButton.setIcon(icon1)
        self.accountButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.accountButton, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.mainAccountFrame)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.cardFrame = QWidget(self.mainBody)
        self.cardFrame.setObjectName(u"cardFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.cardFrame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
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
"background-color: #d89c25;\n"
"border-radius:15px;\n"
" \n"
"}")
        self.todayTaskBG.setPixmap(QPixmap(u":/icons_v2/refresh-cw.svg"))
        self.todayTaskBG.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.todayTaskBG)

        self.frame = QFrame(self.todayCard)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.todayHeader = QLabel(self.frame)
        self.todayHeader.setObjectName(u"todayHeader")
        self.todayHeader.setFont(font2)

        self.verticalLayout_2.addWidget(self.todayHeader, 0, Qt.AlignLeft)

        self.todayTask = QLabel(self.frame)
        self.todayTask.setObjectName(u"todayTask")

        self.verticalLayout_2.addWidget(self.todayTask, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.frame, 0, Qt.AlignLeft)


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
        self.todayTaskBG_4.setPixmap(QPixmap(u":/icons_v2/refresh-cw.svg"))
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
        self.urgentHeader.setFont(font2)

        self.verticalLayout_5.addWidget(self.urgentHeader)

        self.urgentTask = QLabel(self.frame_4)
        self.urgentTask.setObjectName(u"urgentTask")

        self.verticalLayout_5.addWidget(self.urgentTask)


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
        self.allTaskHeader.setFont(font2)

        self.verticalLayout_4.addWidget(self.allTaskHeader)

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
        self.todayTaskBG_2.setPixmap(QPixmap(u":/icons_v2/refresh-cw.svg"))
        self.todayTaskBG_2.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.todayTaskBG_2)

        self.frame_2 = QFrame(self.cancleCard)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cancleHeader = QLabel(self.frame_2)
        self.cancleHeader.setObjectName(u"cancleHeader")
        self.cancleHeader.setFont(font2)

        self.verticalLayout_3.addWidget(self.cancleHeader)

        self.cancelTask = QLabel(self.frame_2)
        self.cancelTask.setObjectName(u"cancelTask")

        self.verticalLayout_3.addWidget(self.cancelTask, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_11.addWidget(self.frame_2)


        self.horizontalLayout_7.addWidget(self.cancleCard)


        self.verticalLayout.addWidget(self.cardFrame)

        self.subcardFrame = QWidget(self.mainBody)
        self.subcardFrame.setObjectName(u"subcardFrame")
        sizePolicy.setHeightForWidth(self.subcardFrame.sizePolicy().hasHeightForWidth())
        self.subcardFrame.setSizePolicy(sizePolicy)
        self.subcardFrame.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.subcardFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget = QWidget(self.subcardFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"#widget{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.frame_8 = QFrame(self.widget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(40, 40))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.todayHeader_2 = QLabel(self.frame_8)
        self.todayHeader_2.setObjectName(u"todayHeader_2")
        self.todayHeader_2.setFont(font2)

        self.horizontalLayout_14.addWidget(self.todayHeader_2)

        self.todayButton = QPushButton(self.frame_8)
        self.todayButton.setObjectName(u"todayButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons_v2/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.todayButton.setIcon(icon2)
        self.todayButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.todayButton)


        self.verticalLayout_6.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 247, 424))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.todayMainTask = QFrame(self.scrollAreaWidgetContents)
        self.todayMainTask.setObjectName(u"todayMainTask")
        self.todayMainTask.setMinimumSize(QSize(0, 400))
        self.todayMainTask.setStyleSheet(u"#todayMainTask{ \n"
"background-color:#ffffff; \n"
"border : 2px solid #2596be; \n"
"border-radius:15px 15px 15px 15px; \n"
"} ")
        self.todayMainTask.setFrameShape(QFrame.StyledPanel)
        self.todayMainTask.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.todayMainTask)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.horizontalLayout_12.addWidget(self.widget)

        self.widget_2 = QWidget(self.subcardFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"#widget_2{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.frame_9 = QFrame(self.widget_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.urgentHeader_2 = QLabel(self.frame_9)
        self.urgentHeader_2.setObjectName(u"urgentHeader_2")
        self.urgentHeader_2.setFont(font2)

        self.horizontalLayout_15.addWidget(self.urgentHeader_2, 0, Qt.AlignLeft)

        self.urgentButton = QPushButton(self.frame_9)
        self.urgentButton.setObjectName(u"urgentButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.urgentButton.setIcon(icon3)
        self.urgentButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.urgentButton, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.urgentMainTask = QFrame(self.widget_2)
        self.urgentMainTask.setObjectName(u"urgentMainTask")
        self.urgentMainTask.setEnabled(False)
        self.urgentMainTask.setMinimumSize(QSize(0, 290))
        self.urgentMainTask.setStyleSheet(u"#urgentMainTask{ \n"
"background-color:#ffffff; \n"
"border : 2px solid #2596be; \n"
"border-radius:15px 15px 15px 15px; \n"
"} ")
        self.urgentMainTask.setFrameShape(QFrame.StyledPanel)
        self.urgentMainTask.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.urgentMainTask)


        self.horizontalLayout_12.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.subcardFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"border: 2px solid #1e1e1e;\n"
"border-radius: 10px\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.widget_3)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.frame_11 = QFrame(self.widget_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.completedHeader = QLabel(self.frame_11)
        self.completedHeader.setObjectName(u"completedHeader")
        self.completedHeader.setFont(font2)

        self.horizontalLayout_16.addWidget(self.completedHeader, 0, Qt.AlignLeft)

        self.completedButton = QPushButton(self.frame_11)
        self.completedButton.setObjectName(u"completedButton")
        self.completedButton.setIcon(icon2)
        self.completedButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.completedButton, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.completedMainTask = QFrame(self.widget_3)
        self.completedMainTask.setObjectName(u"completedMainTask")
        self.completedMainTask.setMinimumSize(QSize(0, 290))
        self.completedMainTask.setMaximumSize(QSize(16777215, 310))
        self.completedMainTask.setStyleSheet(u"#completedMainTask{ \n"
"background-color:#ffffff; \n"
"border : 2px solid #2596be; \n"
"border-radius:15px 15px 15px 15px; \n"
"} ")
        self.completedMainTask.setFrameShape(QFrame.StyledPanel)
        self.completedMainTask.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.completedMainTask)


        self.horizontalLayout_12.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.subcardFrame)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 939, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toDoHeader.setText(QCoreApplication.translate("MainWindow", u"ToDo", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.analysisButton.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.calendarButton.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.historyButton.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.taskButton.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.menuButton.setText("")
        self.homeHeader.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.searchicon.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Task", None))
        self.accountButton.setText("")
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
        self.cancleHeader.setText(QCoreApplication.translate("MainWindow", u"Cancel Task", None))
        self.cancelTask.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.todayHeader_2.setText(QCoreApplication.translate("MainWindow", u"Today Task", None))
        self.todayButton.setText(QCoreApplication.translate("MainWindow", u"View more", None))
        self.urgentHeader_2.setText(QCoreApplication.translate("MainWindow", u"Urgent Task", None))
        self.urgentButton.setText(QCoreApplication.translate("MainWindow", u"View more", None))
        self.completedHeader.setText(QCoreApplication.translate("MainWindow", u"Completed Task", None))
        self.completedButton.setText(QCoreApplication.translate("MainWindow", u"View more", None))
    # retranslateUi

