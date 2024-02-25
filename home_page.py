import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import datetime
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


class Home_page():
    def __init__(self, ui, tasks=None):
        self.ui = ui

        today_tasks = tasks.get_today_tasks()
        urgent_tasks = tasks.get_urgent_tasks()
        # upcoming_tasks = tasks.get_upcoming_tasks()
        completed_tasks = tasks.get_completed_tasks()
        self.ui.todayTask.setText(str(len(today_tasks)) + " Task")
        self.ui.urgentTask.setText(str(len(urgent_tasks)) + " Task")
        self.ui.allTask.setText(str(len(tasks.Tasks)) + " Task")
        
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


    def clicked(self, index):
        print(f"Clicked on task: {index.name_topic}")

    # get text
    def seach_bar(self):
        text = self.lineEdit.text()
        print(text)


# if __name__ == "__main__":
#     # today
#     print(datetime.datetime.today())
#     app = QApplication(sys.argv)
#     # window = MainWindow(type_task)
#     # window.show()
#     sys.exit(app.exec())


