from PySide6.QtWidgets import *
from PySide6.QtCore import *
from class_module import MultiTask
from PySide6.QtGui import QMouseEvent

import sys
import class_module
from main_stack import Ui_MainWindow



task1 = class_module.Task("Math", "Do exercise 1-5", "2024-2-26", "20:00")
task2 = class_module.Task("Physics", "Do exercise 1-5", "2024-2-26", "20:00", True)
task3 = class_module.Task("Chemistry", "Do exercise 1-5", "2024-2-27", "20:00")
task4 = class_module.Task("English", "Do exercise 1-5", "2024-2-27", "20:00", True)
task5 = class_module.Task("History", "Do exercise 1-5", "2024-2-28", "20:00")
task6 = class_module.Task("Biology", "Do exercise 1-5", "2024-2-28", "20:00", True)

# MultiTask(name_topic, detail, due_date)
multi_task1 = class_module.MultiTask("Study", "Do exercise", "2024-2-26", "20:00")
multi_task1.add_task(task1)
multi_task1.add_task(task2)
multi_task1.add_task(task3)
multi_task1.add_task(task4)

user = class_module.User("Arm", "123", "armfiba@gmail.com")
user.add_task(task1)
user.add_task(task2)
user.add_task(task3)
user.add_task(task4)
user.add_task(task5)
user.add_task(task6)
user.add_task(multi_task1)

print(task2.get_day_left().days)

type_task = class_module.Task_handlers(user.get_user_tasks())
type_task.update_tasks()



class ClickableTaskFrame(QFrame):
    clicked = Signal(object)

    def __init__(self, task, *args, **kwargs):
        super(ClickableTaskFrame, self).__init__(*args, **kwargs)
        self.task = task

    def mousePressEvent(self, event):
        self.clicked.emit(self.task)

    def enterEvent(self, event):
        self.setStyleSheet("background-color: lightgray;")

    def leaveEvent(self, event):
        self.setStyleSheet("background-color: none;")


class Home_page():
    def __init__(self, ui, tasks=None):
        self.ui = ui
        self.tasks = tasks
        self.container_layout_arr = [QVBoxLayout(self.ui.todayMainTask), QVBoxLayout(self.ui.urgentMainTask), QVBoxLayout(self.ui.completedMainTask)]

        today_tasks = self.tasks.get_today_tasks()
        urgent_tasks = self.tasks.get_urgent_tasks()
        # upcoming_tasks = tasks.get_upcoming_tasks()
        completed_tasks = self.tasks.get_completed_tasks()
        self.ui.todayTask.setText(str(len(today_tasks)) + " Task")
        self.ui.urgentTask.setText(str(len(urgent_tasks)) + " Task")
        self.ui.allTask.setText(str(len(self.tasks.Tasks)) + " Task")
        
        # self.listView.clicked.connect(self.clicked)
        task_arr = [today_tasks, urgent_tasks, completed_tasks]
        

        for i in range(len(task_arr)):
            self.container_layout = self.container_layout_arr[i]
            for task in task_arr[i]:
                self.task_frame  = ClickableTaskFrame(task)
                self.task_frame_layout = QHBoxLayout(self.task_frame)

                self.name_desc_layout = QVBoxLayout()
                self.task_label_name = QLabel(f"Name: {task.name_topic}")
                self.task_label_description = QLabel(f"Description: {task.detail}")
                self.name_desc_layout.addWidget(self.task_label_name)
                self.name_desc_layout.addWidget(self.task_label_description)

                self.percentage_layout = QVBoxLayout()
                if isinstance(task, MultiTask):
                    self.task_label_percentage = QLabel(f"{task.progress}%")
                    self.percentage_layout.addWidget(self.task_label_percentage)

                self.task_frame_layout.addLayout(self.name_desc_layout)
                self.task_frame_layout.addLayout(self.percentage_layout)

                self.task_frame.clicked.connect(self.clicked)
                self.container_layout.addWidget(self.task_frame)


    def clicked(self, task):
        print(f"Clicked on task: {task.name_topic}")

    # get text
    def seach_bar(self):
        text = self.lineEdit.text()
        print(text)

    def update_ui(self):
        today_tasks = self.tasks.get_today_tasks()
        urgent_tasks = self.tasks.get_urgent_tasks()
        completed_tasks = self.tasks.get_completed_tasks()
        self.ui.todayTask.setText(str(len(today_tasks)) + " Task")
        self.ui.urgentTask.setText(str(len(urgent_tasks)) + " Task")
        self.ui.allTask.setText(str(len(self.tasks.Tasks)) + " Task")

        task_arr = [today_tasks, urgent_tasks, completed_tasks]

        for i in range(len(task_arr)):

            for j in reversed(range(self.container_layout_arr[i].count())):
                self.container_layout_arr[i].itemAt(j).widget().setParent(None)

            container_layout = self.container_layout_arr[i]

            for task in task_arr[i]:
                task_frame = ClickableTaskFrame(task)
                task_frame_layout = QHBoxLayout(task_frame)

                name_desc_layout = QVBoxLayout()
                task_label_name = QLabel(f"Name: {task.name_topic}")
                task_label_description = QLabel(f"Description: {task.detail}")
                name_desc_layout.addWidget(task_label_name)
                name_desc_layout.addWidget(task_label_description)

                percentage_layout = QVBoxLayout()
                if isinstance(task, MultiTask):
                    task_label_percentage = QLabel(f"{task.progress}%")
                    percentage_layout.addWidget(task_label_percentage)

                task_frame_layout.addLayout(name_desc_layout)
                task_frame_layout.addLayout(percentage_layout)

                task_frame.clicked.connect(self.clicked)
                container_layout.addWidget(task_frame)



class MainWindow(QMainWindow):
    def __init__(self, tasks=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.tasks = tasks

        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        today_tasks = self.tasks.get_today_tasks()
        urgent_tasks = self.tasks.get_urgent_tasks()
        # upcoming_tasks = tasks.get_upcoming_tasks()
        completed_tasks = self.tasks.get_completed_tasks()
        self.ui.todayTask.setText(str(len(today_tasks)) + " Task")
        self.ui.urgentTask.setText(str(len(urgent_tasks)) + " Task")
        self.ui.allTask.setText(str(len(self.tasks.Tasks)) + " Task")
        
        # self.listView.clicked.connect(self.clicked)
        task_arr = [today_tasks, urgent_tasks, completed_tasks]
        container_arr = [self.ui.todayMainTask, self.ui.urgentMainTask, self.ui.completedMainTask]

        for i in range(len(task_arr)):
            self.container_layout = QVBoxLayout(container_arr[i])
            for task in task_arr[i]:
                self.task_frame  = ClickableTaskFrame(task)
                self.task_frame_layout = QHBoxLayout(self.task_frame)

                self.name_desc_layout = QVBoxLayout()
                self.task_label_name = QLabel(f"Name: {task.name_topic}")
                self.task_label_description = QLabel(f"Description: {task.detail}")
                self.name_desc_layout.addWidget(self.task_label_name)
                self.name_desc_layout.addWidget(self.task_label_description)

                self.percentage_layout = QVBoxLayout()
                if isinstance(task, MultiTask):
                    self.task_label_percentage = QLabel(f"{task.progress}%")
                    self.percentage_layout.addWidget(self.task_label_percentage)

                self.task_frame_layout.addLayout(self.name_desc_layout)
                self.task_frame_layout.addLayout(self.percentage_layout)

                self.task_frame.clicked.connect(self.clicked)
                self.container_layout.addWidget(self.task_frame)


    def clicked(self):
        task_frame = self.sender()  # Get the sender of the signal
        if isinstance(task_frame, ClickableTaskFrame):
            task = task_frame.task
            print(f"Clicked on task: {task.name_topic}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(type_task)
    window.show()
    sys.exit(app.exec())


