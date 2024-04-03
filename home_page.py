from PySide6.QtWidgets import *
from PySide6.QtCore import *
from class_module import MultiTask


from specialObject import ClickableTaskFrame
import sys
import class_module
from ui_py.main_stack import Ui_MainWindow
from new_window_task import New_MainWindow_task

user = class_module.User("Arm","123","1")
type_task = class_module.Task_handlers(user.get_user_tasks())
type_task.update_tasks()

class Home_page():
    def __init__(self, ui : Ui_MainWindow, user, tasks=None):
        self.ui = ui
        self.tasks = tasks
        self.user = user
        self.container_layout_arr = [QVBoxLayout(self.ui.todayMainTask), QVBoxLayout(self.ui.urgentMainTask), QVBoxLayout(self.ui.completedMainTask)]

        today_tasks = self.tasks.get_today_tasks()
        urgent_tasks = self.tasks.get_urgent_tasks()
        # upcoming_tasks = tasks.get_upcoming_tasks()
        completed_tasks = self.tasks.get_completed_tasks()
        self.ui.todayTask.setText(str(len(today_tasks)) + " Task")
        self.ui.urgentTask.setText(str(len(urgent_tasks)) + " Task")
        self.ui.allTask.setText(str(len(self.tasks.Tasks)) + " Task")
        self.ui.cancelTask.setText(str(len(self.tasks.Late_tasks)) + " Task")
        
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
                else:
                    self.radio_button = QRadioButton("Complete")
                    self.radio_button.toggled.connect(self.radio_button_clicked(task))
                    self.radio_button.setStyleSheet(stylesheet)
                    self.radio_button.setChecked(task.is_completed)
                    self.percentage_layout.addWidget(self.radio_button)

                self.task_frame_layout.addLayout(self.name_desc_layout)
                self.task_frame_layout.addLayout(self.percentage_layout)

                self.task_frame.clicked.connect(self.clicked)
                self.container_layout.addWidget(self.task_frame)


    def clicked(self, task):
        print(f"Clicked on task: {task.name_topic}")
        if isinstance(task, MultiTask):
            self.new_window = New_MainWindow_task(self.ui, self.user, task, task.name_topic)
            self.new_window.show()


    def radio_button_clicked(self, task):
        def on_toggled(checked):
            task.is_completed = checked
            print(f"Task {task.name_topic} is_completed = {task.is_completed}")
        return on_toggled
    
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
        self.ui.cancelTask.setText(str(len(self.tasks.Late_tasks)) + " Task")

        task_arr = [today_tasks, urgent_tasks, completed_tasks]

        for i in range(len(task_arr)):

            for j in reversed(range(self.container_layout_arr[i].count())):
                self.container_layout_arr[i].itemAt(j).widget().setParent(None)

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
                else:
                    self.radio_button = QRadioButton("Complete")
                    self.radio_button.toggled.connect(self.radio_button_clicked(task))
                    self.radio_button.setStyleSheet(stylesheet)
                    self.radio_button.setChecked(task.is_completed)
                    self.percentage_layout.addWidget(self.radio_button)

                self.task_frame_layout.addLayout(self.name_desc_layout)
                self.task_frame_layout.addLayout(self.percentage_layout)

                self.task_frame.clicked.connect(self.clicked)
                self.container_layout.addWidget(self.task_frame)



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
            print(f"Task description: {task.due_date}")
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(type_task)
    window.show()
    sys.exit(app.exec())


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