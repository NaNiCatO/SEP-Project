# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface22.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(939, 589)
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
"#cards1, #cards2, #cards3, #cards4{\n"
"background-color:;\n"
"border : 2px solid #2596be;\n"
"border-radius:15px 15px 15px 15px;\n"
"}\n"
"\n"
"#pushButton, #pushButton_3, #pushButton_4{\n"
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
"#pushButton_6, #pushButton_7, #pushButton_8, #pushButton_9{\n"
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
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_10.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)


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

        self.pushButton_9 = QPushButton(self.frame_14)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setIconSize(QSize(24, 24))

        self.verticalLayout_12.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.frame_14)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)

        self.verticalLayout_12.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.frame_14)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)

        self.verticalLayout_12.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.frame_14)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)

        self.verticalLayout_12.addWidget(self.pushButton_6)


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
        self.pushButton_2 = QPushButton(self.mainAccountFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons_v2/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.mainAccountFrame)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.cardFrame = QWidget(self.mainBody)
        self.cardFrame.setObjectName(u"cardFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.cardFrame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.cards1 = QFrame(self.cardFrame)
        self.cards1.setObjectName(u"cards1")
        self.cards1.setMinimumSize(QSize(180, 80))
        self.cards1.setMaximumSize(QSize(160, 90))
        self.cards1.setStyleSheet(u"#cards1{\n"
"background-color: #ffc148;\n"
"}")
        self.cards1.setFrameShape(QFrame.StyledPanel)
        self.cards1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.cards1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.todayTaskBG = QLabel(self.cards1)
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

        self.frame = QFrame(self.cards1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.frame, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.cards1)

        self.cards4 = QFrame(self.cardFrame)
        self.cards4.setObjectName(u"cards4")
        self.cards4.setMinimumSize(QSize(180, 80))
        self.cards4.setMaximumSize(QSize(160, 90))
        self.cards4.setStyleSheet(u"#cards4{\n"
"background-color: #f26e56;\n"
"}")
        self.cards4.setFrameShape(QFrame.StyledPanel)
        self.cards4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.cards4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.todayTaskBG_4 = QLabel(self.cards4)
        self.todayTaskBG_4.setObjectName(u"todayTaskBG_4")
        self.todayTaskBG_4.setMinimumSize(QSize(0, 0))
        self.todayTaskBG_4.setMaximumSize(QSize(40, 40))
        self.todayTaskBG_4.setStyleSheet(u"#todayTaskBG {\n"
"background-color: #d89c25;\n"
"border-radius:15px;\n"
" \n"
"}")
        self.todayTaskBG_4.setPixmap(QPixmap(u":/icons_v2/refresh-cw.svg"))
        self.todayTaskBG_4.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.todayTaskBG_4)

        self.frame_4 = QFrame(self.cards4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)


        self.horizontalLayout_9.addWidget(self.frame_4, 0, Qt.AlignLeft)


        self.horizontalLayout_7.addWidget(self.cards4)

        self.cards3 = QFrame(self.cardFrame)
        self.cards3.setObjectName(u"cards3")
        self.cards3.setMinimumSize(QSize(180, 80))
        self.cards3.setMaximumSize(QSize(160, 90))
        self.cards3.setStyleSheet(u"#cards3{\n"
"background-color: #4e82d3;\n"
"}")
        self.cards3.setFrameShape(QFrame.StyledPanel)
        self.cards3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.cards3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.todayTaskBG_3 = QLabel(self.cards3)
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

        self.frame_3 = QFrame(self.cards3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.frame_3)


        self.horizontalLayout_7.addWidget(self.cards3)

        self.cards2 = QFrame(self.cardFrame)
        self.cards2.setObjectName(u"cards2")
        self.cards2.setMinimumSize(QSize(180, 80))
        self.cards2.setMaximumSize(QSize(160, 90))
        self.cards2.setStyleSheet(u"#cards2{\n"
"background-color: #52c1c4;\n"
"}")
        self.cards2.setFrameShape(QFrame.StyledPanel)
        self.cards2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.cards2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.todayTaskBG_2 = QLabel(self.cards2)
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

        self.frame_2 = QFrame(self.cards2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_11.addWidget(self.frame_2)


        self.horizontalLayout_7.addWidget(self.cards2)


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
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.horizontalLayout_14.addWidget(self.label)

        self.pushButton = QPushButton(self.frame_8)
        self.pushButton.setObjectName(u"pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons_v2/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.pushButton)


        self.verticalLayout_6.addWidget(self.frame_8, 0, Qt.AlignTop)

        self.frame_13 = QFrame(self.widget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 290))
        self.frame_13.setStyleSheet(u"#frame_13{ \n"
"background-color:#ffffff; \n"
"border : 2px solid #2596be; \n"
"border-radius:15px 15px 15px 15px; \n"
"} ")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_13)


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
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.horizontalLayout_15.addWidget(self.label_11, 0, Qt.AlignLeft)

        self.pushButton_3 = QPushButton(self.frame_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_15.addWidget(self.pushButton_3, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.frame_12 = QFrame(self.widget_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(False)
        self.frame_12.setMinimumSize(QSize(0, 290))
        self.frame_12.setStyleSheet(u"#frame_12{ \n"
"background-color:#ffffff; \n"
"border : 2px solid #2596be; \n"
"border-radius:15px 15px 15px 15px; \n"
"} ")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_12)


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
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.horizontalLayout_16.addWidget(self.label_12, 0, Qt.AlignLeft)

        self.pushButton_4 = QPushButton(self.frame_11)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.pushButton_4, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame_10 = QFrame(self.widget_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 290))
        self.frame_10.setMaximumSize(QSize(16777215, 310))
        self.frame_10.setStyleSheet(u"#frame_10{ \n"
"background-color:#ffffff; \n"
"border : 2px solid #2596be; \n"
"border-radius:15px 15px 15px 15px; \n"
"} ")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_10)


        self.horizontalLayout_12.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.subcardFrame)


        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 939, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ToDo", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuButton.setText("")
        self.homeHeader.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.searchicon.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Task", None))
        self.pushButton_2.setText("")
        self.todayTaskBG.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Today Task", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"variable", None))
        self.todayTaskBG_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Urgent Task", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.todayTaskBG_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"All Task", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.todayTaskBG_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cancel Task", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Today Task", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"View more", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Urgent Task", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"View more", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Completed Task", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"View more", None))
    # retranslateUi

