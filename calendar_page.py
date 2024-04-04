import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from class_module import *
from ui_py.main_stack import Ui_MainWindow
from new_window_task import New_MainWindow_task
import datetime

light_blue = QColor(173, 216, 230)
orange = QColor(255, 165, 0)
light_red = QColor(255, 106, 106)
grey = QColor(192, 192, 192)
# grey but lighter = QColor(236, 236, 236)

class Calendar_page():
    def __init__(self, ui: Ui_MainWindow, user,  task: Task_handlers):
        self.ui = ui
        self.calendar = QCalendarWidget(self.ui)
        self.task = task
        self.user = user
        self.all_task = self.user.get_user_tasks()
        self.ui.stackedWidget.addWidget(self.calendar)
        self.calendar.show()
        self.highlight_dates()
        
        self.ui.calendarWidget.clicked.connect(self.show_task)
        
    def highlight_dates(self):
        for task in self.all_task:
            date = task.due_date
            year = date.year
            month = date.month
            day = date.day
            date = QDate(year, month, day)
            self.ui.calendarWidget.setDateTextFormat(date, self.highlight_format(task))

    def highlight_format(self, task):
        text_format = self.calendar.dateTextFormat(QDate())
        if task.urgent:
            text_format.setBackground(orange)
        elif task.is_completed:
            text_format.setBackground(Qt.green)
        elif task.get_day_left() < datetime.timedelta(days=0):
            text_format.setBackground(light_red)
        elif task.get_day_left() < datetime.timedelta(days=3):
            text_format.setBackground(Qt.yellow)
        else:
            text_format.setBackground(grey)

        return text_format

    def show_task(self,date):
        clicked_date = datetime.date(date.year(), date.month(), date.day())
        task_list = []
        for task in self.all_task:
            if task.due_date.date() == clicked_date:
                task_list.append(task)
        if task_list:
            self.new_window_task_page = New_MainWindow_task(self.ui, self.user, task_list, clicked_date)
            self.new_window_task_page.show()
        task_list.clear()
        