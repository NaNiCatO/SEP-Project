from PySide6.QtWidgets import *
from PySide6.QtCore import *
from class_module import MultiTask
from new_window_create import New_MainWindow_create, New_MainWindow_edit
from new_window_task import New_MainWindow_task
from specialObject import ClickableTaskFrame
from ui_py.main_stack import Ui_MainWindow
from class_module import Task_handlers

class History_page():
    def __init__(self, ui ,user):
        self.ui = ui
        self.user = user
        self.history = self.user.get_history()
        self.container_layout = QVBoxLayout(self.ui.history_frame)
        self.display_history()
        
    def display_history(self):
        for date in self.history:
            for event, details in self.history[date].items():
                if event == "Create Account":
                    text = f"{date} \t Create Account: {details[0][0]}"  # Username from first tuple
                elif event == "Create":
                    text = f"{date} \t Create Task:"
                    for task in details:
                        text += f"\n\t\t- {task[0]}"
                elif event in ("topic", "detail", "due_date", "urgent"):
                    text_map = {
                        "topic": "Change Task Name:",
                        "detail": "Change Task Description:",
                        "due_date": "Change Task Due Date:",
                        "urgent": "Change Task Urgency:",
                    }
                    text = f"{date} \t {text_map[event]} "
                    for task in details:
                        old_value, new_value = task[1], task[2]
                        text += f"\n\t\t- Task {task[0]}: {old_value} to {new_value}"
                elif event == "Completed":
                    text = f"{date} \t Task Completed:"
                    for task in details:
                        text += f"\n\t\t- {task}"
                elif event == "Uncompleted":
                    text = f"{date} \t Task Uncompleted:"
                    for task in details:
                        text += f"\n\t\t- {task}"
                elif event == "Delete":
                    text = f"{date} \t Task Deleted:"
                    for task in details:
                        text += f"\n\t\t- {task}"
                elif event == "Create Subtask":
                    text = f"{date} \t Create Subtask:"
                    for task in details:
                        text += f"\n\t\t- Create Task {task[1]} in task {task[0]}"
                        
                elif event == "Delete Subtask":
                    text = f"{date} \t Delete Subtask:"
                    for task in details:
                        text += f"\n\t\t- Delete Task {task[1]} from task {task[0]}"

                # Create label and add to layout
                self.event_label = QLabel(text)
                self.container_layout.addWidget(self.event_label)

                    
                    
                    

        
        
                
            