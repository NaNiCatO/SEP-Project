# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_task.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCalendarWidget, QCheckBox,
    QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QTimeEdit,
    QVBoxLayout, QWidget)
import ui_py.icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(697, 444)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_create_task_frame = QFrame(Form)
        self.main_create_task_frame.setObjectName(u"main_create_task_frame")
        self.main_create_task_frame.setStyleSheet(u"*{\n"
"color: #000;\n"
"border : none;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: #007bff; /* Blue border when focused */\n"
"    border-style: solid;\n"
"}\n"
"#main_create_task_frame{\n"
"background-color: #d9d9d9;\n"
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
"    cursor: pointer;\n"
"    transition: background-color 0.3s ease;\n"
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
""
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
        self.gridLayout_11 = QGridLayout(self.main_create_task_frame)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.viewTaskHeafer = QFrame(self.main_create_task_frame)
        self.viewTaskHeafer.setObjectName(u"viewTaskHeafer")
        self.viewTaskHeafer.setMinimumSize(QSize(0, 50))
        self.viewTaskHeafer.setFrameShape(QFrame.StyledPanel)
        self.viewTaskHeafer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.viewTaskHeafer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainMenuButton_4 = QWidget(self.viewTaskHeafer)
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


        self.gridLayout_11.addWidget(self.viewTaskHeafer, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.main_create_task_frame)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMaximumSize(QSize(16777215, 16777215))
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_15)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.frame_15)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.topicNameHeadline = QLabel(self.frame_9)
        self.topicNameHeadline.setObjectName(u"topicNameHeadline")

        self.gridLayout_4.addWidget(self.topicNameHeadline, 0, 0, 1, 1)

        self.topic_lineEdit = QLineEdit(self.frame_9)
        self.topic_lineEdit.setObjectName(u"topic_lineEdit")
        self.topic_lineEdit.setStyleSheet(u"QLineEdit:focus {\n"
"    border-color: #007bff; /* Blue border when focused */\n"
"    border-style: solid;\n"
"}")

        self.gridLayout_4.addWidget(self.topic_lineEdit, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_9, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.detailHeadline = QLabel(self.frame_10)
        self.detailHeadline.setObjectName(u"detailHeadline")
        self.detailHeadline.setMargin(5)

        self.horizontalLayout_6.addWidget(self.detailHeadline)

        self.detail_lineEdit = QLineEdit(self.frame_10)
        self.detail_lineEdit.setObjectName(u"detail_lineEdit")
        self.detail_lineEdit.setStyleSheet(u"QLineEdit:focus {\n"
"    border-color: #007bff; /* Blue border when focused */\n"
"    border-style: solid;\n"
"}")

        self.horizontalLayout_6.addWidget(self.detail_lineEdit)


        self.gridLayout_7.addWidget(self.frame_10, 1, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_17)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"margin-left: 10px;\n"
"margin-right: 25px;")

        self.horizontalLayout_9.addWidget(self.label, 0, Qt.AlignLeft)

        self.timeEdit = QTimeEdit(self.frame_17)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy1)
        self.timeEdit.setMinimumSize(QSize(200, 0))
        self.timeEdit.setStyleSheet(u"QTimeEdit {\n"
"    background-color: #f0f0f0; \n"
"    border: 2px solid #f26e56; \n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    selection-background-color: #007bff;  \n"
"    selection-color: #ffffff; \n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"    border-color: #007bff; \n"
"    border-style: solid;\n"
"}\n"
"\n"
"QTimeEdit::up-button {\n"
"    width: 30px; \n"
"    height: 20px; \n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right; \n"
"}\n"
"\n"
"QTimeEdit::down-button {\n"
"    width: 30px; \n"
"    height: 20px; \n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right; \n"
"}\n"
"")
        self.timeEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.horizontalLayout_9.addWidget(self.timeEdit)


        self.horizontalLayout_4.addWidget(self.frame_17, 0, Qt.AlignLeft)


        self.gridLayout_7.addWidget(self.frame_12, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_13)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(12, 0, 0, 0)
        self.subTaskHeadline = QLabel(self.frame_11)
        self.subTaskHeadline.setObjectName(u"subTaskHeadline")
        self.subTaskHeadline.setStyleSheet(u"margin-left: 10px;")
        self.subTaskHeadline.setMargin(5)

        self.horizontalLayout_7.addWidget(self.subTaskHeadline, 0, Qt.AlignLeft)

        self.sub_task_check_box = QCheckBox(self.frame_11)
        self.sub_task_check_box.setObjectName(u"sub_task_check_box")

        self.horizontalLayout_7.addWidget(self.sub_task_check_box, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_11, 0, Qt.AlignLeft)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.subTaskHeadline_2 = QLabel(self.frame_14)
        self.subTaskHeadline_2.setObjectName(u"subTaskHeadline_2")
        self.subTaskHeadline_2.setStyleSheet(u"margin-left: 20px;")
        self.subTaskHeadline_2.setMargin(5)

        self.horizontalLayout_8.addWidget(self.subTaskHeadline_2, 0, Qt.AlignLeft)

        self.urgent_task_check_box = QCheckBox(self.frame_14)
        self.urgent_task_check_box.setObjectName(u"urgent_task_check_box")

        self.horizontalLayout_8.addWidget(self.urgent_task_check_box)


        self.verticalLayout_5.addWidget(self.frame_14, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.frame_13)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget = QCalendarWidget(self.frame_4)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"\n"
"#calendarWidget QWidget{\n"
"alternate-background-color: #fec89a;\n"
"}\n"
"\n"
"#qt_calendar_navigationbar{\n"
"background-color: #f8edeb;\n"
"border: 2px solid #f8edeb;\n"
"border-bottom: 0px;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
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
"marigin-right: 5px;\n"
"	image: url(:/icons/icons_black/arrow-right.svg);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth{\n"
"marigin-right: 5px;\n"
"	image: url(:/icons/icons_black/arrow-right.svg);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth:hover,#qt_calendar_prevmonth:hover{\n"
"background-color: #f8edeb;\n"
"margin-right: 10px;\n"
"\n"
"\n"
"}\n"
"\n"
"#qt_calendar_nextmonth:pressd,#qt_calendar_prevmonth:pressd{\n"
"background-color: #f"
                        "cd5ce;\n"
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
"margin: 5px 8px;\n"
"border-radius: 5px;\n"
"padding: 0px 4px;\n"
"\n"
"\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover{\n"
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
"	image: url(:/icons/icons_black/arrow-right.svg);\n"
"subcontrol-position:right;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::up-button{\n"
"	image: url(:/icons/icons_black/arrow-right.svg);\n"
"subcontrol-position:left;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button,#qt_calend"
                        "ar_yearedit::up-button{\n"
"width:10px;\n"
"padding: 0px 5px;\n"
"border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button,#qt_calendar_yearedit::up-button{\n"
"background-color: #55aaff;\n"
"margin-right: 10px;\n"
"\n"
"}\n"
"\n"
"#calendarWidgetQToolButton QMenu{\n"
"background-color: #fff;\n"
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
"sbucontrol-position:right center;\n"
"margin-top: 10px;\n"
"width:20px;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_calendarview{\n"
"border: 2px solid #fcd5ce;\n"
"border-top:0px;\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover{\n"
"border-radius: 5px;\n"
"background-color: #cdd1d1;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected{\n"
"border-radius: 5px;\n"
"c"
                        "olor:#1e1e1e;\n"
"background-color: #ffddd2;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.calendarWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.confirm_button = QDialogButtonBox(self.frame_5)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setStyleSheet(u"QDialog {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #007bff;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QDialogButtonBox {\n"
"    background-color: transparent;\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton {\n"
"    background-color: #cce5ff; \n"
"    color: #333333;\n"
"    border: 1px solid #007bff;\n"
"    padding: 4px 8px;\n"
"    border-radius: 5px;\n"
"    transition: background-color 0.3s ease; \n"
"}\n"
"\n"
"QDialogButtonBox QPushButton:hover {\n"
"    background-color: #b3d1ff; \n"
"}\n"
"\n"
"QDialogButtonBox QPushButton:flat {\n"
"    border: none;\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton:default {\n"
"    background-color: #66b3ff; /* Pastel blue darker */\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton:primary {\n"
"    background-color: #3366ff; /* Deeper blue for primary */\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton:destructive {\n"
"    background-color: #ff9999; \n"
"}\n"
"\n"
"QDialog QLabel {\n"
"    color: #333333;\n"
"    fo"
                        "nt-size: 16px;\n"
"}\n"
"")
        self.confirm_button.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_5.addWidget(self.confirm_button)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_15, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.main_create_task_frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.homeHeader_5.setText(QCoreApplication.translate("Form", u"View Task", None))
        self.topicNameHeadline.setText(QCoreApplication.translate("Form", u"Topic Name ", None))
        self.detailHeadline.setText(QCoreApplication.translate("Form", u"Detail ", None))
        self.label.setText(QCoreApplication.translate("Form", u"Time         ", None))
        self.subTaskHeadline.setText(QCoreApplication.translate("Form", u"Sub Task  ", None))
        self.sub_task_check_box.setText("")
        self.subTaskHeadline_2.setText(QCoreApplication.translate("Form", u"Urgent task", None))
        self.urgent_task_check_box.setText("")
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())