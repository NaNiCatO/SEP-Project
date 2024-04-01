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
        
        for date in reversed(self.history):
            date_label = QLabel(f"<b>{date}</b>")  # Bold date for emphasis
            date_label.setStyleSheet("color: darkblue;")
            self.container_layout.addWidget(date_label)
            
            separator = QFrame()
            separator.setFixedHeight(2)
            separator.setStyleSheet("background-color: darkblue; border-bottom: 1px solid darkblue;")
            self.container_layout.addWidget(separator)

            for event, details in self.history[date].items():
                text = ""

                # Format events with appropriate headings and lists
                if event == "Create Account":
                    text += f"<b><font color='#700F0F'>Create Account</font></b>: {details[0][0]}"
                elif event == "Create":
                    text += f"<b><font color='#700F0F'>Create Task:</font></b>"
                    text += f"<ul>"
                    for task in details:
                        text += f"<li>{task[0]}</li>"
                    text += f"</ul>"
                elif event in ("topic", "detail", "due_date", "urgent"):
                    text_map = {
                        "topic": "<b><font color='#700F0F'>Change Task Name:</font></b>",
                        "detail": "<b><font color='#700F0F'>Change Task Description:</font></b>",
                        "due_date": "<b><font color='#700F0F'>Change Task Due Date:</font></b>",
                        "urgent": "<b><font color='#700F0F'>Change Task Urgency:</font></b>",
                    }
                    text = f"{text_map[event]}<br>"

                    # Description list for key-value pairs
                    text += "<ul>"
                    for task in details:
                        old_value, new_value = task[1], task[2]
                        text += f"<li>Task {task[0]} : {old_value} to {new_value}</li>"
                    text += "</ul>"
                elif event == "Completed":
                    text += f"<b><font color='#700F0F'>Task Completed:</font></b>"
                    text += f"<ul>"
                    for task in details:
                        text += f"<li>{task[0]}</li>"
                    text += f"</ul>"
                elif event == "Delete":
                    text += f"<b><font color='#700F0F'>Task Deleted:</font></b>"
                    text += f"<ul>"
                    for task in details:
                        text += f"<li>{task[0]}</li>"
                    text += f"</ul>"
                elif event == "Create Subtask":
                    text += f"<b><font color='#700F0F'>Create Subtask:</font></b>"
                    text += f"<ul>"
                    for task in details:
                        text += f"<li>Create Task {task[1]} in task {task[0]}</li>"
                    text += f"</ul>"
                elif event == "Delete Subtask":
                    text += f"<b><font color='#700F0F'>Delete Subtask:</font></b>"
                    text += f"<ul>"
                    for task in details:
                        text += f"<li>Delete Task {task[1]} in task {task[0]}</li>"
                    text += f"</ul>"
                    
                
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