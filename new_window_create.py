import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from new_window_create_ui import Ui_Form
import class_module
from datetime import datetime
import ZODB, ZODB.FileStorage
import transaction


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


############################################################################################################


class New_MainWindow_create(QWidget, Ui_Form):
    def __init__(self, ui,connection, new_window = None, MultiTask=None):
        super().__init__()
        self.connection = connection
        self.root = self.connection.root()
        self.ui = ui
        self.MultiTask = MultiTask
        self.new_window = new_window
        self.setupUi(self)
        self.confirm_button.accepted.connect(self.accept)
        self.confirm_button.rejected.connect(self.reject)

    def accept(self):
        name_topic = self.topic_lineEdit.text()
        detail = self.detail_lineEdit.text()
        due_date = self.calendarWidget.selectedDate().toString("yyyy-M-d")
        time = self.timeEdit.time().toString("hh:mm")
        urgent = self.urgent_task_check_box.isChecked()
        print(name_topic, detail, due_date, time, urgent)
        # Check if the date has passed
        if datetime.strptime(due_date, '%Y-%m-%d') < datetime.now():
            print("Date has passed")
            return
        if self.sub_task_check_box.isChecked():
            task = class_module.MultiTask(name_topic, detail, due_date, time, urgent)
        else:
            task = class_module.Task(name_topic, detail, due_date, time, urgent)

        if self.MultiTask:
            self.MultiTask.add_task(task)
        else:
            print("User: ", self.ui.user.name)
            self.root.user[self.ui.user.name].add_task(task)
            # self.ui.user.add_task(task)
        self.close()

    def reject(self):
        self.close()

    def closeEvent(self, event):
        print("UI is closed")
        self.ui.categorized_task.update_tasks()
        for i in self.ui.arr_update:
            i.update_ui()
        if self.new_window:
            self.new_window.update_ui()
        
        transaction.commit()
        event.accept()

class New_MainWindow_edit(QWidget, Ui_Form):
    def __init__(self, ui, task,  new_window = None):
        super().__init__()
        self.ui = ui
        self.task = task
        self.new_window = new_window
        self.setupUi(self)
        self.set_values()
        self.confirm_button.accepted.connect(self.accept)
        self.confirm_button.rejected.connect(self.reject)

    def set_values(self):
        self.topic_lineEdit.setText(self.task.name_topic)
        self.detail_lineEdit.setText(self.task.detail)
        self.urgent_task_check_box.setChecked(self.task.urgent)

        parts = self.task.time.split(':')
        if len(parts) == 2:
            hours = int(parts[0])
            minutes = int(parts[1])

            # Create a QTime object from the parsed values
            selected_time = QTime(hours, minutes)

            # Set the selected time in the time edit widget
            self.timeEdit.setTime(selected_time)

        parts = self.task.due_date.strftime("%Y-%m-%d").split('-')
        if len(parts) == 3:
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            # Create a QDate object from the parsed values
            selected_date = QDate(year, month, day)
            # Set the selected date in the calendar widget
            self.calendarWidget.setSelectedDate(selected_date)


    def accept(self):
        self.task.name_topic = self.topic_lineEdit.text()
        self.task.detail = self.detail_lineEdit.text()
        self.task.due_date = datetime.strptime(self.calendarWidget.selectedDate().toString("yyyy-M-d"),'%Y-%m-%d')
        self.task.time = self.timeEdit.time().toString("hh:mm")
        self.task.urgent = self.urgent_task_check_box.isChecked()
        self.close()

    def reject(self):
        self.close()

    def closeEvent(self, event):
        print("UI is closed")
        self.ui.categorized_task.update_tasks()
        for i in self.ui.arr_update:
            i.update_ui()
        if self.new_window:
            self.new_window.update_ui()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = New_MainWindow_create(user)
    window.show()
    sys.exit(app.exec())