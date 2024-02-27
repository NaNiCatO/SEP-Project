from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_stack import Ui_MainWindow

from class_module import MultiTask
import sys
import class_module



task1 = class_module.Task("Math", "Do exercise 1-5", "2024-2-26", "20:00")
task2 = class_module.Task("Physics", "Do exercise 1-5", "2024-2-26", "20:00", True)
task3 = class_module.Task("Chemistry", "Do exercise 1-5", "2024-2-27", "20:00")
task4 = class_module.Task("English", "Do exercise 1-5", "2024-2-27", "20:00", True)
task5 = class_module.Task("History", "Do exercise 1-5", "2024-2-28", "20:00")
task6 = class_module.Task("Biology", "Do exercise 1-5", "2024-2-28", "20:00", True)

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

class MainWindow(QMainWindow):
    def __init__(self, tasks):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tasks = tasks

        # Create a container frame
        self.container_frame = QFrame()
        self.container_frame.setObjectName("container")
        self.setCentralWidget(self.container_frame)

        # Create a layout for the container frame
        self.container_layout = QVBoxLayout(self.container_frame)

        # Add tasks to the container layout
        for task in self.tasks.get_urgent_tasks():
            task_frame = ClickableTaskFrame(task)
            task_frame.clicked.connect(self.clicked)

            task_layout = QHBoxLayout(task_frame)

            name_desc_layout = QVBoxLayout()
            task_label_name = QLabel(f"Name: {task.name_topic}")
            task_label_description = QLabel(f"Description: {task.detail}")
            name_desc_layout.addWidget(task_label_name)
            name_desc_layout.addWidget(task_label_description)

            percentage_layout = QVBoxLayout()
            if isinstance(task, MultiTask):
                task_label_percentage = QLabel(f"{task.progress}%")
                percentage_layout.addWidget(task_label_percentage)

            radio_button = QRadioButton("Complete")
            radio_button.toggled.connect(self.radio_button_clicked(task))
            
            percentage_layout.addWidget(radio_button)

            task_layout.addLayout(name_desc_layout)
            task_layout.addLayout(percentage_layout)

            self.container_layout.addWidget(task_frame)

    def clicked(self, task):
        print(f"Clicked on task: {task.name_topic} is_completed = {task.is_completed}")

    def radio_button_clicked(self, task):
        def on_toggled(checked):
            task.is_completed = checked
            print(f"Task {task.name_topic} is_completed = {task.is_completed}")
        return on_toggled


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(type_task)
    window.show()
    sys.exit(app.exec())