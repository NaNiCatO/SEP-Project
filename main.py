from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtCore
from ui_py.main_stack import Ui_MainWindow
import class_module
from home_page import Home_page
from task_page import Task_page
from circular_progressbar import Analysis_page
from new_window_task import New_MainWindow_task
from calendar_page import Calendar_page
from history_page import History_page
import sys
# import editdistance

class Sidebar(QMainWindow, Ui_MainWindow,QtCore.QObject):
    abouttoclose = Signal()
    logoutsignal = Signal()
    
    def __init__(self, user: class_module.User):
        super().__init__()
        self.setupUi(self)
        self.user = user
        self.user_tasks = self.user.get_user_tasks()
        self.categorized_task = class_module.Task_handlers(self.user.get_user_tasks())

        # set home page as default 
        self.stackedWidget.setCurrentIndex(0)

        self.setup_home_page()
        self.task_page = Task_page(self, self.user)
        self.analyse_page = Analysis_page(self, self.categorized_task)

        self.arr_update = [self.home_page, self.task_page]

        self.frame_5.hide()

        self.homeButton.clicked.connect(self.switch_to_home)
        self.homeMiniButton.clicked.connect(self.switch_to_home)
        self.analysisButton.clicked.connect(self.switch_to_analysis)
        self.analysisMiniButton.clicked.connect(self.switch_to_analysis)
        self.calendarButton.clicked.connect(self.switch_to_calendar)
        self.calendarMiniButton.clicked.connect(self.switch_to_calendar)
        self.historyButton.clicked.connect(self.switch_to_history)
        self.historyMiniButton.clicked.connect(self.switch_to_history)
        self.taskButton.clicked.connect(self.switch_to_view_task)
        self.taskMiniButton.clicked.connect(self.switch_to_view_task)

        # self.pushButton.clicked.connect(self.search)
        # self.lineEdit.returnPressed.connect(self.search)

     
        self.settingButton.clicked.connect(self.logout)
        self.logoutMiniButton.clicked.connect(self.logout)
    
    def logout(self):
        reply = QMessageBox.question(
            self, "Confirm Logout", "Are you sure you want to logout?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.logoutsignal.emit()
            self.close()



    def switch_to_home(self):
        # self.update_ui()
        self.categorized_task.update_tasks()
        self.home_page.update_ui()
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_analysis(self):
        # self.update_ui()
        self.categorized_task.update_tasks()
        self.analyse_page.update_ui()
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_calendar(self):
        # self.update_ui()
        self.calendar_page = Calendar_page(self, self.categorized_task)
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_history(self):
        # self.update_ui()
        self.history_page = History_page(self, self.user)
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_view_task(self):
        # self.update_ui()
        self.categorized_task.update_tasks()
        self.task_page.update_ui()
        self.stackedWidget.setCurrentIndex(3)

    def setup_home_page(self):
        self.home_page = Home_page(self, self.categorized_task)
        self.todayButton.clicked.connect(self.switch_to_today)
        self.urgentButton.clicked.connect(self.switch_to_urgent)
        self.completedButton.clicked.connect(self.switch_to_completed)


        
    def switch_to_today(self):
        self.new_MainWindow_task_page = New_MainWindow_task(self, self.user, self.categorized_task.get_today_tasks(), "Today")
        self.new_MainWindow_task_page.show()
        

    def switch_to_urgent(self):
        self.new_MainWindow_task_page = New_MainWindow_task(self, self.user, self.categorized_task.get_urgent_tasks(), "Urgent")
        self.new_MainWindow_task_page.show()
        # self.home_page.update_ui()

    def switch_to_completed(self):
        self.new_MainWindow_task_page = New_MainWindow_task(self, self.user, self.categorized_task.get_completed_tasks(), "Completed")
        self.new_MainWindow_task_page.show()
        # self.home_page.update_ui()
    
    def closeEvent(self, event):
        if self.sender() == self.logoutMiniButton or self.sender() == self.settingButton:  # Check if logout button triggered close
            self.logoutsignal.emit()
        else:
            self.abouttoclose.emit()  # Emit aboutToClose for regular close
        super().closeEvent(event)
        

    # def search(self):
    #     text = self.lineEdit.text()
    #     if text == "":
    #         return
    #     print(text)
    #     tasks = find_similar_words(text, self.user.get_user_tasks())
    #     self.new_MainWindow_task_page = New_MainWindow_task(self, tasks, text)
    #     self.new_MainWindow_task_page.show()

    
# def find_similar_words(word, word_list):
#     if len(word) < 3:
#         max_distance = 0
#     else:
#         max_distance = 2
#     similar_words = []
#     for candidate in word_list:
#         distance = editdistance.eval(word, candidate.get_name_topic())
#         if distance <= max_distance:
#             similar_words.append(candidate)
#         elif all(char in candidate.get_name_topic() for char in word):
#             similar_words.append(candidate)
#     # Sort by distance (ascending order)
#     similar_words.sort(key=lambda x: editdistance.eval(word, x.get_name_topic()))  # Sort directly using editdistance
#     return similar_words

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Sidebar() 
    window.show()
    sys.exit(app.exec())