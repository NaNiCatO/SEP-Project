import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from class_module import *
from ui_py.main_stack import Ui_MainWindow
import datetime

class Calendar_page():
    def __init__(self, ui : Ui_MainWindow, task : Task_handlers):
        self.ui = ui
        self.calendar = QCalendarWidget(self.ui)
        self.task = task
        self.ui.stackedWidget.addWidget(self.calendar)
        self.calendar.show()
        self.highlight_dates()
        
        # self.calendar.clicked.connect(self.date_clicked)
    
    def highlight_dates(self):
        highlight_dates = self.task.get_urgent_tasks() + self.task.get_today_tasks() + self.task.get_upcoming_tasks()
        for task in highlight_dates:
            date = task.due_date
            year = date.year
            month = date.month
            day = date.day
            date = QDate(year, month, day)
            self.ui.calendarWidget.setDateTextFormat(date, self.highlight_format(task))
    
    def highlight_format(self,task):
        text_format = self.calendar.dateTextFormat(QDate())
        if task.urgent:
            text_format.setBackground(Qt.red)
        elif task.get_day_left() < datetime.timedelta(days=0):
            text_format.setBackground(Qt.blue)
        elif task.get_day_left() < datetime.timedelta(days=3):
            text_format.setBackground(Qt.yellow)
        else:
            text_format.setBackground(Qt.green)
            
        return text_format

    # def date_clicked(self, date):
        
    
