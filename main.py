import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from output import Ui_MainWindow
import class_module
import datetime

# Create a model
# 1 element have
# Name : nameTask(string)
# description : text(string)

class Task:
    def __init__(self, name, description, persentage):
        self.name = name
        self.description = description
        self.persentage = persentage

class TaskList(QAbstractListModel):
    def __init__(self, tasks):
        super(TaskList, self).__init__()
        self.tasks = tasks

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self.tasks[index.row()]
            return f"Name: {value.name}\nDescription: {value.description}"

    def rowCount(self, index):
        return len(self.tasks)

    def addTask(self, task):
        self.beginInsertRows(QModelIndex(), 0, 0)
        self.tasks.append(task)
        self.endInsertRows()

    def removeTask(self, index):
        self.beginRemoveRows(QModelIndex(), index, index)
        del self.tasks[index]
        self.endRemoveRows()

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable
    

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


class MainWindow(QMainWindow):
    def __init__(self, tasks=None):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # tasks = [
        #     Task("Task 1", "Description 1", 50),
        #     Task("Task 2", "Description 2", 75),
        #     Task("Task 3", "Description 3", 25),
        #     Task("Task 4", "Description 4", 10),
        #     Task("Task 5", "Description 5", 80),
        #     Task("Task 6", "Description 6", 90),
        #     Task("Task 7", "Description 7", 100),
        #     Task("Task 8", "Description 8", 0),
        #     Task("Task 9", "Description 9", 50),
        #     Task("Task 10", "Description 10", 75),
        # ]

        today_tasks = tasks.get_today_tasks()
        urgent_tasks = tasks.get_urgent_tasks()
        # upcoming_tasks = tasks.get_upcoming_tasks()
        completed_tasks = tasks.get_completed_tasks()
        self.ui.todayTask.setText(str(len(today_tasks)) + " Task")
        self.ui.urgentTask.setText(str(len(urgent_tasks)) + " Task")
        self.ui.allTask.setText(str(len(tasks.Tasks)) + " Task")
        
        # self.ui.listView.clicked.connect(self.clicked)
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
                if hasattr(task, 'persentage'):
                    self.task_label_percentage = QLabel(f"{task.persentage}%")
                    self.percentage_layout.addWidget(self.task_label_percentage)

                self.task_frame_layout.addLayout(self.name_desc_layout)
                self.task_frame_layout.addLayout(self.percentage_layout)

                self.task_frame.clicked.connect(self.clicked)
                self.container_layout.addWidget(self.task_frame)

        

    def clicked(self, index):
        # print(index.data())
        print(f"Clicked on task: {index.name_topic}")

    #get text
    def seach_bar(self):
        text = self.ui.lineEdit.text()
        print(text)


if __name__ == "__main__":
    # today
    print(datetime.datetime.today())
    app = QApplication(sys.argv)
    #testing class_module
    # Task(name_topic, detail, due_date, time, urgent)
    task1 = class_module.Task("Math", "Do exercise 1-5", "2024-2-21", "20:00")
    task2 = class_module.Task("Physics", "Do exercise 1-5", "2024-2-20", "20:00", True)
    task3 = class_module.Task("Chemistry", "Do exercise 1-5", "2024-2-20", "20:00")
    task4 = class_module.Task("English", "Do exercise 1-5", "2024-2-25", "20:00", True)
    task5 = class_module.Task("History", "Do exercise 1-5", "2024-2-24", "20:00")

    # MultiTask(name_topic, detail, due_date)
    multi_task1 = class_module.MultiTask("Study", "Do exercise", "2024-2-20", "20:00")
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
    user.add_task(multi_task1)

    print(task2.get_day_left().days)

    type_task = class_module.Task_handlers(user.get_user_tasks())
    type_task.update_tasks()

    
    
    window = MainWindow(type_task)
    window.show()
    sys.exit(app.exec())


