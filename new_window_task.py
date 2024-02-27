import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from new_window_task_ui import Ui_MainWindow
import class_module


############################################################################################################

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
multi_task1.add_task(task5)
multi_task1.add_task(task6)

user = class_module.User("Arm", "123", "armfiba@gmail.com")

user.add_task(multi_task1)



############################################################################################################


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


class New_MainWindow_task(QMainWindow, Ui_MainWindow):
    def __init__(self, ui, task, name=None):
        super().__init__()
        self.ui = ui
        self.task = task
        self.name = name
        self.mode = "View Task"
        self.setupUi(self)
        self.container_layout = QVBoxLayout(self.frame)

        if self.name:
            self.homeHeader_5.setText(f"Task Name: {name}")
        else:
            self.homeHeader_5.setText(f"Task Name: {self.task.name_topic}")

        self.create_Button.clicked.connect(self.create_task)
        self.delete_Button.clicked.connect(self.delete_task)
        self.edit_Button.clicked.connect(self.edit_task)

        for task in self.task:
            self.task_frame  = ClickableTaskFrame(task)
            self.task_frame_layout = QHBoxLayout(self.task_frame)

            self.name_desc_layout = QVBoxLayout()
            self.task_label_name = QLabel(f"Name: {task.name_topic}")
            self.task_label_description = QLabel(f"Description: {task.detail}")
            self.name_desc_layout.addWidget(self.task_label_name)
            self.name_desc_layout.addWidget(self.task_label_description)

            self.percentage_layout = QVBoxLayout()
            self.radio_button = QRadioButton("Complete")
            self.radio_button.toggled.connect(self.radio_button_clicked(task))
            self.radio_button.setChecked(task.is_completed)
            self.percentage_layout.addWidget(self.radio_button)

            self.task_frame_layout.addLayout(self.name_desc_layout)
            self.task_frame_layout.addLayout(self.percentage_layout)

            self.task_frame.clicked.connect(self.clicked)
            self.container_layout.addWidget(self.task_frame)


    def create_task(self):
        pass

    def delete_task(self):
        self.mode = "Delete Task"
        if self.name:
            print(f"Task Name: {self.name} : Delete Task")
            self.homeHeader_5.setText(f"Task Name: {self.name} : {self.mode}")
        else:
            self.homeHeader_5.setText(f"Task Name: {self.task.name_topic} : {self.mode}")

    def edit_task(self):
        pass

    def update_ui(self):
        for i in reversed(range(self.container_layout.count())):
            self.container_layout.itemAt(i).widget().setParent(None)

        for task in self.task:
            self.task_frame  = ClickableTaskFrame(task)
            self.task_frame_layout = QHBoxLayout(self.task_frame)

            self.name_desc_layout = QVBoxLayout()
            self.task_label_name = QLabel(f"Name: {task.name_topic}")
            self.task_label_description = QLabel(f"Description: {task.detail}")
            self.name_desc_layout.addWidget(self.task_label_name)
            self.name_desc_layout.addWidget(self.task_label_description)

            self.percentage_layout = QVBoxLayout()
            self.radio_button = QRadioButton("Complete")
            self.radio_button.toggled.connect(self.radio_button_clicked(task))
            self.radio_button.setChecked(task.is_completed)
            self.percentage_layout.addWidget(self.radio_button)

            self.task_frame_layout.addLayout(self.name_desc_layout)
            self.task_frame_layout.addLayout(self.percentage_layout)

            self.task_frame.clicked.connect(self.clicked)
            self.container_layout.addWidget(self.task_frame)

    def clicked(self, task):
        if self.mode == "Delete Task":
            self.ui.user.remove_task(task)
            self.task.remove(task)
            self.update_ui()
            print(f"Deleted task: {task.name_topic}")

        print(f"Clicked on task: {task.name_topic}")

    def radio_button_clicked(self, task):
        def on_toggled(checked):
            task.is_completed = checked
            print(f"Task {task.name_topic} is_completed = {task.is_completed}")
        return on_toggled
    
    def closeEvent(self, event):
            print("UI is closed")
            for i in self.ui.arr_update:
                i.update_ui()
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = New_MainWindow_task(multi_task1)
    window.show()
    sys.exit(app.exec())