import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_py.new_window_create_ui import Ui_Form
import class_module
from datetime import datetime
import ZODB, ZODB.FileStorage
import transaction

class New_MainWindow_create(QWidget, Ui_Form):
    update_ui_signal = Signal()
    
    def __init__(self, ui, user, MultiTask=None):
        super().__init__()
        self.ui = ui
        self.user = user
        self.MultiTask = MultiTask
        # self.new_window = new_window
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
            self.user.add_history(datetime.now().strftime('%Y-%m-%d'), "Create Subtask", self.MultiTask, task.name_topic)
        else:
            print("User: ", self.ui.user.name)
            self.user.add_task(task)
            print(datetime.now().strftime('%Y-%m-%d'))
            self.user.add_history(datetime.now().strftime('%Y-%m-%d'), "Create", task)
        self.close()

    def reject(self):
        self.close()

    def closeEvent(self, event):
        # print("UI is closed")
        self.ui.categorized_task.update_tasks()
        for i in self.ui.arr_update:
            i.update_ui()
        if self.MultiTask:
            self.update_ui_signal.emit()
        
        event.accept()

class New_MainWindow_edit(QWidget, Ui_Form):
    update_ui = Signal()
    
    def __init__(self, ui, user, task,  new_window = None):
        super().__init__()
        self.ui = ui
        self.task = task
        self.user = user
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
        # Check if any changes are made
        if self.topic_lineEdit.text() != self.task.name_topic :
            print("Topic changed")
            print(self.task.name_topic, self.topic_lineEdit.text())
            self.user.add_history(datetime.now().strftime('%Y-%m-%d'), "topic", self.task, self.task.name_topic, self.topic_lineEdit.text())
            self.task.name_topic = self.topic_lineEdit.text()
        if self.detail_lineEdit.text() != self.task.detail :
            print("Detail changed")
            print(self.task.detail, self.detail_lineEdit.text())
            self.user.add_history(datetime.now().strftime('%Y-%m-%d'), "detail", self.task, self.task.detail, self.detail_lineEdit.text())
            self.task.detail = self.detail_lineEdit.text()
        if self.urgent_task_check_box.isChecked() != self.task.urgent :
            print("Urgent changed")
            print(self.task.urgent, self.urgent_task_check_box.isChecked())
            self.user.add_history(datetime.now().strftime('%Y-%m-%d'), "urgent", self.task, self.task.urgent, self.urgent_task_check_box.isChecked())
            self.task.urgent = self.urgent_task_check_box.isChecked()
        if self.timeEdit.time().toString("hh:mm") != self.task.time :
            print("Time changed")
            print(self.task.time, self.timeEdit.time().toString("hh:mm"))
            self.user.add_history(datetime.now().strftime('%Y-%m-%d'), "time", self.task, self.task.time, self.timeEdit.time().toString("hh:mm"))
            self.task.time = self.timeEdit.time().toString("hh:mm")
        if self.calendarWidget.selectedDate().toString("yyyy-M-d") != self.task.due_date.strftime('%Y-%m-%d') :
            print("Due date changed")
            print(self.task.due_date.strftime('%Y-%m-%d'), self.calendarWidget.selectedDate().toString("yyyy-M-d"))
            self.user.add_history(datetime.now().strftime('%Y-%m-%d'), "due_date", self.task, self.task.due_date.strftime('%Y-%m-%d'), self.calendarWidget.selectedDate().toString("yyyy-M-d"))
            self.task.due_date = datetime.strptime(self.calendarWidget.selectedDate().toString("yyyy-M-d"),'%Y-%m-%d')
        self.close()
    

    def reject(self):
        self.close()

    def closeEvent(self, event):
        print("UI is closed")
        self.ui.categorized_task.update_tasks()
        for i in self.ui.arr_update:
            i.update_ui()
        event.accept()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = New_MainWindow_create(user)
#     window.show()
#     sys.exit(app.exec())