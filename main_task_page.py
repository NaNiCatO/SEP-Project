import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from class_module import MultiTask


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


class Task_page():
    def __init__(self, ui, tasks=None):
        self.mode = "View Task"
        self.ui = ui
        self.tasks = tasks
        self.container_layout = QVBoxLayout(self.ui.taskList_frame)
        
        
        self.ui.create_Button.clicked.connect(self.add_task)
        self.ui.delete_Button.clicked.connect(self.delete_task)
        self.ui.edit_Button.clicked.connect(self.edit_task)
        #self.ui.taskList.itemClicked.connect(self.clicked)

        
        for task in tasks:
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
            else:
                self.radio_button = QRadioButton("Complete")
                self.radio_button.toggled.connect(self.radio_button_clicked(task))
                self.radio_button.setChecked(task.is_completed)
                self.percentage_layout.addWidget(self.radio_button)

            self.task_frame_layout.addLayout(self.name_desc_layout)
            self.task_frame_layout.addLayout(self.percentage_layout)

            self.task_frame.clicked.connect(self.clicked)
            self.container_layout.addWidget(self.task_frame)



    def add_task(self):
        pass

    def delete_task(self):
        if self.mode == "Delete Task":
            self.mode = "View Task"
        else:
            self.mode = "Delete Task"
        self.ui.homeHeader_5.setText(self.mode)

    def edit_task(self):

        self.mode = "Edit Task"
        self.ui.homeHeader_5.setText(self.mode)

    def clicked(self, task):
        if self.mode == "Delete Task":
            self.ui.user.remove_task(task)
            self.update_ui()
            print(f"Deleted task: {task.name_topic}")

        print(f"Clicked on task: {task.name_topic}")
        

    def update_ui(self):
        for i in reversed(range(self.container_layout.count())):
            self.container_layout.itemAt(i).widget().setParent(None)
        for task in self.tasks:
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
            else:
                self.radio_button = QRadioButton("Complete")
                self.radio_button.toggled.connect(self.radio_button_clicked(task))
                self.radio_button.setChecked(task.is_completed)
                self.percentage_layout.addWidget(self.radio_button)

            self.task_frame_layout.addLayout(self.name_desc_layout)
            self.task_frame_layout.addLayout(self.percentage_layout)

            self.task_frame.clicked.connect(self.clicked)
            self.container_layout.addWidget(self.task_frame)
            


    def radio_button_clicked(self, task):
        def on_toggled(checked):
            task.is_completed = checked
            print(f"Task {task.name_topic} is_completed = {task.is_completed}")
        return on_toggled