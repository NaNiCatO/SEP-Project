from PySide6.QtWidgets import *
from PySide6.QtCore import *
from class_module import MultiTask
from new_window_create import New_MainWindow_create, New_MainWindow_edit
from new_window_task import New_MainWindow_task
from specialObject import ClickableTaskFrame
from ui_py.main_stack import Ui_MainWindow
from class_module import Task_handlers



class Task_page():
    def __init__(self, ui : Ui_MainWindow,user):
        self.mode = "View Task"
        self.ui = ui
        self.user = user

        self.task = Task_handlers(self.user.get_user_tasks())
        self.arr_container_layout = [QVBoxLayout(self.ui.complete_Task_Frame) ,QVBoxLayout(self.ui.late_Task_Frame) ,QVBoxLayout(self.ui.ongoing_Task_Frame)]
        self.tasks = [self.task.get_completed_tasks(), self.task.get_late_tasks(), self.task.get_urgent_tasks() + self.task.get_today_tasks() + self.task.get_upcoming_tasks()]
        
        self.ui.complete_Task_Button.clicked.connect(self.complete_task)
        self.ui.late_Task_Button.clicked.connect(self.late_task)
        self.ui.ongoing_Task_Button.clicked.connect(self.ongoing_task)
        
        self.ui.create_Button.clicked.connect(self.add_task)
        self.ui.delete_Button.clicked.connect(self.delete_task)
        self.ui.edit_Button.clicked.connect(self.edit_task)
        #self.ui.taskList.itemClicked.connect(self.clicked)

        for counter, container_layout in enumerate(self.arr_container_layout):
            for task in self.tasks[counter]:
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
                    self.radio_button.setStyleSheet(stylesheet)
                    self.radio_button.setChecked(task.is_completed)
                    self.percentage_layout.addWidget(self.radio_button)

                self.task_frame_layout.addLayout(self.name_desc_layout)
                self.task_frame_layout.addLayout(self.percentage_layout)

                self.task_frame.clicked.connect(self.clicked)
                container_layout.addWidget(self.task_frame)


    def complete_task(self):
        self.ui.categorized_task.update_tasks()
        self.update_ui()
        self.ui.stackedWidget_2.setCurrentIndex(2)

    def late_task(self):
        self.ui.categorized_task.update_tasks()
        self.update_ui()
        self.ui.stackedWidget_2.setCurrentIndex(1)

    def ongoing_task(self):
        self.ui.categorized_task.update_tasks()
        self.update_ui()
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def add_task(self):
        self.new_window = New_MainWindow_create(self.ui,self.user)
        self.new_window.show()

    def delete_task(self):
        if self.mode == "Delete Task":
            self.mode = "View Task"
        else:
            self.mode = "Delete Task"
        self.ui.homeHeader_5.setText(self.mode)

    def edit_task(self):
        if self.mode == "Edit Task":
            self.mode = "View Task"
        else:
            self.mode = "Edit Task"
        self.ui.homeHeader_5.setText(self.mode)

    def clicked(self, task):
        if self.mode == "Delete Task":
            self.ui.user.remove_task(task)
            self.update_ui()
            print(f"Deleted task: {task.name_topic}")
        elif self.mode == "Edit Task":
            self.new_window = New_MainWindow_edit(self.ui, self.user, task)
            self.new_window.show()
        else:
            if isinstance(task, MultiTask):
                self.new_window = New_MainWindow_task(self.ui, self.user, task, task.name_topic)
                self.new_window.show()

        print(f"Clicked on task: {task.name_topic}")
        print(f"Task description: {task.due_date}")
        

    def update_ui(self):
        self.task = Task_handlers(self.user.get_user_tasks())
        self.tasks = [self.task.get_completed_tasks(), self.task.get_late_tasks(), self.task.get_urgent_tasks() + self.task.get_today_tasks() + self.task.get_upcoming_tasks()]
        for counter, container_layout in enumerate(self.arr_container_layout):
            for i in reversed(range(container_layout.count())):
                container_layout.itemAt(i).widget().setParent(None)
            for task in self.tasks[counter]:
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
                    self.radio_button.setStyleSheet(stylesheet)
                    self.radio_button.setChecked(task.is_completed)
                    self.percentage_layout.addWidget(self.radio_button)

                self.task_frame_layout.addLayout(self.name_desc_layout)
                self.task_frame_layout.addLayout(self.percentage_layout)

                self.task_frame.clicked.connect(self.clicked)
                container_layout.addWidget(self.task_frame)
            


    def radio_button_clicked(self, task):
        def on_toggled(checked):
            task.is_completed = checked
            print(f"Task {task.name_topic} is_completed = {task.is_completed}")
        return on_toggled
    


stylesheet = """
QRadioButton {
    spacing: 5px; /* spacing between the radio button and the text */
}

QRadioButton::indicator {
    width: 20px; /* width of the radio button */
    height: 20px; /* height of the radio button */
}

QRadioButton::indicator:checked {
    background-color: #90EE90; /* background color when checked */
    border: 2px solid #555; /* border color when checked */
    border-radius: 10px; /* border radius to make it round */
}

QRadioButton::indicator:unchecked {
    background-color: #fff; /* background color when unchecked */
    border: 2px solid #555; /* border color when unchecked */
    border-radius: 10px; /* border radius to make it round */
}

QRadioButton::indicator:checked:hover {
    border: 2px solid #007bff; /* border color when checked and hovered */
}

QRadioButton::indicator:unchecked:hover {
    background-color: #f3f3f3; /* background color when unchecked and hovered */
    border: 2px solid #555; /* border color when unchecked and hovered */
}

QRadioButton::indicator:checked:pressed {
    background-color: #0056b3; /* background color when checked and pressed */
    border: 2px solid #007bff; /* border color when checked and pressed */
}

QRadioButton::indicator:unchecked:pressed {
    background-color: #f3f3f3; /* background color when unchecked and pressed */
    border: 2px solid #555; /* border color when unchecked and pressed */
}
"""