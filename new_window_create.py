import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from new_window_create_ui import Ui_Form
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


class New_MainWindow_create(QWidget, Ui_Form):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.setupUi(self)
        self.confirm_button.accepted.connect(self.accept)
        self.confirm_button.rejected.connect(self.reject)

    def accept(self):
        name_topic = self.topic_lineEdit.text()
        detail = self.detail_lineEdit.text()
        due_date = self.calendarWidget.selectedDate().toString("yyyy-M-d")
        time = self.timeEdit.time().toString()
        urgent = self.urgent_task_check_box.isChecked()
        print(name_topic, detail, due_date, time, urgent)
        if self.sub_task_check_box.isChecked():
            task = class_module.MultiTask(name_topic, detail, due_date, time, urgent)
        else:
            task = class_module.Task(name_topic, detail, due_date, time, urgent)

        self.ui.user.add_task(task)
        self.close()

    def reject(self):
        self.close()

    def closeEvent(self, event):
        print("UI is closed")
        self.ui.categorized_task.update_tasks()
        for i in self.ui.arr_update:
            i.update_ui()
        event.accept()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = New_MainWindow_create(user)
    window.show()
    sys.exit(app.exec())