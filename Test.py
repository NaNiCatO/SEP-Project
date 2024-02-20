import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from scroll import Ui_MainWindow

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
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        tasks = [
            Task("Task 1", "Description 1", 50),
            Task("Task 2", "Description 2", 75),
            Task("Task 3", "Description 3", 25),
            Task("Task 4", "Description 4", 10),
            Task("Task 5", "Description 5", 80),
            Task("Task 6", "Description 6", 90),
            Task("Task 7", "Description 7", 100),
            Task("Task 8", "Description 8", 0),
            Task("Task 9", "Description 9", 50),
            Task("Task 10", "Description 10", 75),
        ]


        self.ui.todayTask.setText(str(len(tasks)) + " Task")
        # self.ui.listView.clicked.connect(self.clicked)
        container_layout = QVBoxLayout(self.ui.todayMainTask)

        for task in tasks:
            task_frame  = ClickableTaskFrame(task)
            task_frame_layout = QHBoxLayout(task_frame)

            name_desc_layout = QVBoxLayout()
            task_label_name = QLabel(f"Name: {task.name}")
            task_label_description = QLabel(f"Description: {task.description}")
            name_desc_layout.addWidget(task_label_name)
            name_desc_layout.addWidget(task_label_description)

            percentage_layout = QVBoxLayout()
            task_label_percentage = QLabel(f"{task.persentage}%")
            percentage_layout.addWidget(task_label_percentage)

            task_frame_layout.addLayout(name_desc_layout)
            task_frame_layout.addLayout(percentage_layout)

            task_frame.clicked.connect(self.clicked)
            container_layout.addWidget(task_frame)

    def clicked(self, index):
        # print(index.data())
        print(f"Clicked on task: {index.name}")

    #get text
    def seach_bar(self):
        text = self.ui.lineEdit.text()
        print(text)


if __name__ == "__main__":
    # testing the model using Mainwindow
    app = QApplication(sys.argv)
    # tasks = [Task("Task 1", "Description 1"), Task("Task 2", "Description 2")]
    # model = TaskList(tasks)
    window = MainWindow()
    # window.ui.listView.setModel(model)
    window.show()
    sys.exit(app.exec())


