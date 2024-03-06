from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_py.main_stack import Ui_MainWindow
import class_module
from main_home_page import Home_page
from main_task_page import Task_page
from circular_progressbar import Analysis_page
from new_window_task import New_MainWindow_task
import sys
from Login_Register import *
import ZODB , ZODB.FileStorage
import transaction

############################################################################################################

# task1 = class_module.Task("Math", "Do exercise 1-5", "2024-2-26", "20:00")
# task2 = class_module.Task("Physics", "Do exercise 1-5", "2024-2-26", "20:00", True)
# task3 = class_module.Task("Chemistry", "Do exercise 1-5", "2024-2-27", "20:00")
# task4 = class_module.Task("English", "Do exercise 1-5", "2024-2-27", "20:00", True)
# task5 = class_module.Task("History", "Do exercise 1-5", "2024-2-28", "20:00")
# task6 = class_module.Task("Biology", "Do exercise 1-5", "2024-2-28", "20:00", True)

# # MultiTask(name_topic, detail, due_date)
# multi_task1 = class_module.MultiTask("Study", "Do exercise", "2024-2-26", "20:00")
# multi_task1.add_task(task1)
# multi_task1.add_task(task2)
# multi_task1.add_task(task3)
# multi_task1.add_task(task4)

# user = class_module.User("Arm", "123", "armfiba@gmail.com")
# user.add_task(task1)
# user.add_task(task2)
# user.add_task(task3)
# user.add_task(task4)
# user.add_task(task5)
# user.add_task(task6)
# user.add_task(multi_task1)

# user = root.user['Arm']



############################################################################################################



class Sidebar(QMainWindow, Ui_MainWindow):
    def __init__(self, user, connection):
        super().__init__()
        self.connection = connection
        self.root = self.connection.root()
        self.setupUi(self) 
        self.user = user
        self.categorized_task = class_module.Task_handlers(self.user.get_user_tasks())

        # set home page as default 
        self.stackedWidget.setCurrentIndex(0)

        self.setup_home_page()
        self.task_page = Task_page(self,self.connection, self.categorized_task.Tasks)
        self.analyse_page = Analysis_page(self,self.connection, self.categorized_task)

        self.arr_update = [self.home_page, self.task_page]

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

    def switch_to_home(self):
        # self.update_ui()
        self.categorized_task.update_tasks()
        self.home_page.update_ui()
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_analysis(self):
        # self.update_ui()
        self.categorized_task.update_tasks()
        self.analysis_page.update_ui()
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_calendar(self):
        # self.update_ui()
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_history(self):
        # self.update_ui()
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
        self.new_MainWindow_task_page = New_MainWindow_task(self, self.categorized_task.get_today_tasks(), "Today")
        self.new_MainWindow_task_page.show()
        

    def switch_to_urgent(self):
        self.new_MainWindow_task_page = New_MainWindow_task(self, self.categorized_task.get_urgent_tasks(), "Urgent")
        self.new_MainWindow_task_page.show()
        self.home_page.update_ui()

    def switch_to_completed(self):
        self.new_MainWindow_task_page = New_MainWindow_task(self, self.categorized_task.get_completed_tasks(), "Completed")
        self.new_MainWindow_task_page.show()
        self.home_page.update_ui()

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Sidebar() 
    window.show()
    sys.exit(app.exec())