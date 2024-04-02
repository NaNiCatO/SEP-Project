from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtCore
from ui_py.main_stack import Ui_MainWindow
import class_module
from home_page import Home_page
from task_page import Task_page
from circular_progressbar import Analysis_page
from new_window_task import New_MainWindow_task
from new_window_create import New_MainWindow_create
from calendar_page import Calendar_page
from history_page import History_page
import sys
import editdistance
import speech_recognition as sr
from datetime import datetime

class Sidebar(QMainWindow, Ui_MainWindow,QtCore.QObject):
    abouttoclose = Signal()
    logoutsignal = Signal()
    
    def __init__(self, user: class_module.User):
        super().__init__()
        self.setupUi(self)
        self.user = user
        self.user_tasks = self.user.get_user_tasks()
        self.categorized_task = class_module.Task_handlers(self.user.get_user_tasks())

        # set home page as default 
        self.stackedWidget.setCurrentIndex(0)

        self.setup_home_page()
        self.task_page = Task_page(self, self.user)
        self.analyse_page = Analysis_page(self, self.categorized_task)

        self.arr_update = [self.home_page, self.task_page]

        self.frame_5.hide()

        self.homeButton.clicked.connect(self.switch_to_home)
        self.homeMiniButton.clicked.connect(self.switch_to_home)
        self.analysisButton.clicked.connect(self.switch_to_analysis)
        self.analysisMiniButton.clicked.connect(self.switch_to_analysis)
        self.calendarButton.clicked.connect(self.switch_to_calendar)
        self.calendarMiniButton.clicked.connect(self.switch_to_calendar)
        self.historyButton.clicked.connect(self.switch_to_history)
        self.historyMiniButton.clicked.connect(self.switch_to_history)
        self.taskButton.clicked.connect(self.switch_to_view_task)
        self.taskMiniButton.clicked.connect(self.switch_to_view_task)

        self.pushButton.clicked.connect(self.search)
        self.lineEdit.returnPressed.connect(self.search)
        self.pushButton_2.clicked.connect(self.voice_input)
        self.analysis_search_button.clicked.connect(self.search)
        self.analysis_line_edit.returnPressed.connect(self.search)
        self.analysis_mic_button.clicked.connect(self.voice_input)
        self.calendar_search_button.clicked.connect(self.search)
        self.calendar_line_edit.returnPressed.connect(self.search)
        self.calendar_mic_button.clicked.connect(self.voice_input)
        self.history_search_button.clicked.connect(self.search)
        self.history_line_edit_.returnPressed.connect(self.search)
        self.history_mic_button.clicked.connect(self.voice_input)
        self.view_search_button.clicked.connect(self.search)
        self.view_line_edit.returnPressed.connect(self.search)
        self.view_mic_button.clicked.connect(self.voice_input)

        self.settingButton.clicked.connect(self.logout)
        self.logoutMiniButton.clicked.connect(self.logout)
    
    def logout(self):
        reply = QMessageBox.question(
            self, "Confirm Logout", "Are you sure you want to logout?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.logoutsignal.emit()
            self.close()



    def switch_to_home(self):
        # self.update_ui()
        self.categorized_task.update_tasks()
        self.home_page.update_ui()
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_analysis(self):
        # self.update_ui()
        self.categorized_task.update_tasks()
        self.analyse_page.update_ui()
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_calendar(self):
        # self.update_ui()
        self.calendar_page = Calendar_page(self, self.categorized_task)
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_history(self):
        # self.update_ui()
        self.history_page = History_page(self, self.user)
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_view_task(self):
        # self.update_ui()
        self.categorized_task.update_tasks()
        self.task_page.update_ui()
        self.stackedWidget.setCurrentIndex(3)

    def setup_home_page(self):
        self.home_page = Home_page(self, self.categorized_task)
        self.todayButton.clicked.connect(self.switch_to_today)
        self.urgentButton.clicked.connect(self.switch_to_urgent)
        self.completedButton.clicked.connect(self.switch_to_completed)


        
    def switch_to_today(self):
        self.new_MainWindow_task_page = New_MainWindow_task(self, self.user, self.categorized_task.get_today_tasks(), "Today")
        self.new_MainWindow_task_page.show()
        

    def switch_to_urgent(self):
        self.new_MainWindow_task_page = New_MainWindow_task(self, self.user, self.categorized_task.get_urgent_tasks(), "Urgent")
        self.new_MainWindow_task_page.show()
        # self.home_page.update_ui()

    def switch_to_completed(self):
        self.new_MainWindow_task_page = New_MainWindow_task(self, self.user, self.categorized_task.get_completed_tasks(), "Completed")
        self.new_MainWindow_task_page.show()
        # self.home_page.update_ui()
    
    def closeEvent(self, event):
        if self.sender() == self.logoutMiniButton or self.sender() == self.settingButton:  # Check if logout button triggered close
            self.logoutsignal.emit()
        else:
            self.abouttoclose.emit()  # Emit aboutToClose for regular close
        super().closeEvent(event)
        

    def search(self):
        text = self.lineEdit.text()
        if text == "":
            return
        print(text)
        tasks = find_similar_words(text, self.user.get_user_tasks())
        self.new_MainWindow_task_page = New_MainWindow_task(self, self.user, tasks, text)
        self.new_MainWindow_task_page.show()

    def voice_input(self):
        text:str = recognize_speech()
        if text.lower().startswith("search") or text.lower().startswith("find"):
            self.key_index = 7 if "search" in text.lower() else 5
            self.lineEdit.setText(text[self.key_index:])
            self.search()
        elif text.lower().startswith("go to") or text.lower().startswith("switch to"):
            if "home" in text.lower():
                self.switch_to_home()
            elif "analysis" in text.lower() or "analyze" in text.lower():
                self.switch_to_analysis()
            elif "calendar" in text.lower():
                self.switch_to_calendar()
            elif "history" in text.lower():
                self.switch_to_history()
            elif "task" in text.lower():
                self.switch_to_view_task()
        elif text.lower().startswith("create"):
            name, detail, due_date, time = creating_task(text)
            if "multitask" in text:
                self.create_task = New_MainWindow_create(self, self.user)
                self.create_task.sub_task_check_box.setChecked(True)
            self.create_task = New_MainWindow_create(self, self.user)
            if name:
                self.create_task.topic_lineEdit.setText(name)
            if detail:
                self.create_task.detail_lineEdit.setText(detail)
            if due_date:
                self.create_task.calendarWidget.setSelectedDate(date_formatter(due_date.strip()))
            if time:
                self.create_task.timeEdit.setTime(QTime.fromString(time, "hh:mm"))
            if "urgent" in text:
                self.create_task.urgent_task_check_box.setChecked(True)
            self.create_task.show()


    
def find_similar_words(word, word_list):
    if len(word) < 3:
        max_distance = 0
    else:
        max_distance = 2
    similar_words = []
    for candidate in word_list:
        distance = editdistance.eval(word, candidate.get_name_topic())
        if distance <= max_distance:
            similar_words.append(candidate)
        elif all(char in candidate.get_name_topic() for char in word):
            similar_words.append(candidate)
    # Sort by distance (ascending order)
    similar_words.sort(key=lambda x: editdistance.eval(word, x.get_name_topic()))  # Sort directly using editdistance
    return similar_words

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

    try:
        # Use Google Speech Recognition to convert speech to text
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def date_formatter(text):
    formats = ["%dth %B %Y", "%B %d, %Y", "%B %dth %Y", "%B %d %Y"]  # Add more formats if users might use variations

    for format_str in formats:
        try:
            # Try parsing the spoken date with each format
            desired_date = datetime.strptime(text, format_str)
            break  # Exit the loop if parsing is successful
        except ValueError:
            pass  # If parsing fails with this format, try the next one

    if desired_date:  # Check if parsing was successful with any format
    # Convert datetime to QDate and set the calendar date (as before)
        qt_date = QDate(desired_date.year, desired_date.month, desired_date.day)
        print(f"Setting the date to {qt_date.toString()}")
        return qt_date
    else:
        print("Sorry, I couldn't understand the date format. Please try again.")

def creating_task(input_str:str):
    if "task" in input_str:
        name_index = input_str.find("task")
    elif "name" in input_str:
        name_index = input_str.find("name")
    else:
        name_index = None
    name_gap = 5

    if "detail" in input_str:
        detail_index = input_str.find("detail")
        detail_gap = 7
    elif "details" in input_str:
        detail_index = input_str.find("details")
        detail_gap = 8
    else:
        detail_index = None
   

    if "due date" in input_str:
        due_date_index = input_str.find("due")
        due_date_gap = 9
    elif "date" in input_str:
        due_date_index = input_str.find("date")
        due_date_gap = 5
    else:
        due_date_index = None


    if "time" in input_str:
        time_index = input_str.find("time")
        time_gap = 5
    elif "at" in input_str:
        time_index = input_str.find("at")
        time_gap = 3
    else:
        time_index = None

    if name_index :
        name = input_str[name_index + name_gap: detail_index]
    else:
        name = None

    if detail_index:
        detail = input_str[detail_index + detail_gap: due_date_index]
    else:
        detail = None

    if due_date_index:
        due_date = input_str[due_date_index + due_date_gap: time_index]
    else:
        due_date = None

    if time_index:
        time = input_str[time_index + time_gap:time_index + time_gap + 5]
    else:
        time = None

    print(name, detail, due_date, time)

    return name, detail, due_date, time

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Sidebar() 
    window.show()
    sys.exit(app.exec())