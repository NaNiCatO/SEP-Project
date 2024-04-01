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
        
        self.ui.history_frame.setStyleSheet(stylesheet)
        
    def display_history(self):
        # delete previous labels from layout
        for i in reversed(range(self.container_layout.count())):
            widget = self.container_layout.itemAt(i).widget()
            widget.deleteLater()
        
        for date in self.history:
            date_label = QLabel(f"{date}")
            date_label.setObjectName("date-label")  # Assign class name
            date_label.setStyleSheet("color: blue;")  # Optional inline style

            self.container_layout.addWidget(date_label)
            for event, details in self.history[date].items():
                if event == "Create Account":
                    text = f"<font color='darkgreen'>Create Account</font>: {details[0][0]}"  # Username from first tuple
                elif event == "Create":
                    text = f"Create Task:"
                    for task in details:
                        text += f"\n\t- {task[0]}"
                elif event in ("topic", "detail", "due_date", "urgent"):
                    text_map = {
                        "topic": "Change Task Name:",
                        "detail": "Change Task Description:",
                        "due_date": "Change Task Due Date:",
                        "urgent": "Change Task Urgency:",
                    }
                    text = f"{text_map[event]} "
                    for task in details:
                        old_value, new_value = task[1], task[2]
                        text += f"\n\t- Task {task[0]}: {old_value} to {new_value}"
                elif event == "Completed":
                    text = f"Task Completed:"
                    for task in details:
                        text += f"\n\t- {task}"
                elif event == "Uncompleted":
                    text = f"Task Uncompleted:"
                    for task in details:
                        text += f"\n\t- {task}"
                elif event == "Delete":
                    text = f"Task Deleted:"
                    for task in details:
                        text += f"\n\t- {task}"
                elif event == "Create Subtask":
                    text = f"Create Subtask:"
                    for task in details:
                        text += f"\n\t- Create Task {task[1]} in task {task[0]}"
                        
                elif event == "Delete Subtask":
                    text = f"Delete Subtask:"
                    for task in details:
                        text += f"\n\t- Delete Task {task[1]} from task {task[0]}"
                
                
                    

                # Create label and add to layout
                event_label = QLabel(text)
                event_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
                self.container_layout.addWidget(event_label)

stylesheet = """
        /* History frame styling */
        #history_frame {
            background-color: #f5f5f5;
            border: 1px solid #ddd;
            border-radius: 5px;  /* Add rounded corners */
            padding: 15px;
        }

        /* Event label styling */
        QLabel {
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: #444;
            line-height: 1.5;  /* Increase line spacing for readability */
        }

        /* Date label styling (targets first child) */
        QLabel:first-child {
            font-weight: bold;
            color: #333;
        }

        /* Topic label styling (change color to light green) */
        QLabel:contains("Change Task Name:") {
            color: lightgreen;  /* Or #90EE90 for light green */
        }

        /* Task list styling */
        .task-list {
            margin-left: 20px;  /* Indent task list for better hierarchy */
            list-style: none;  /* Remove default bullet points */
            padding-left: 0;  /* Remove default list padding */
        }

        /* Task list item styling */
        .task-list-item {
            margin-bottom: 5px;  /* Add space between task items */
        }
        """