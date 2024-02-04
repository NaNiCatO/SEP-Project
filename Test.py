import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from untitled import Ui_MainWindow

# Create a model
# 1 element have
# Name : nameTask(string)
# description : text(string)

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

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


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.listView.clicked.connect(self.clicked)

    def clicked(self, index):
        print(index.data())


if __name__ == "__main__":
    # testing the model using Mainwindow
    app = QApplication(sys.argv)
    tasks = [Task("Task 1", "Description 1"), Task("Task 2", "Description 2")]
    model = TaskList(tasks)
    window = MainWindow()
    window.ui.listView.setModel(model)
    window.show()
    sys.exit(app.exec_())
    

