import datetime
from email.message import EmailMessage
import smtplib
import ssl
import persistent


class User(persistent.Persistent):
    def __init__(self, name, password, email) :
        self.name = name
        self.password = password
        self.email = email
        self.user_tasks = []
        self.all_complete_tasks = []
        self.history = {}
        self.check_date_exist(self.get_date_today())
        self.check_event_exist(self.get_date_today(), "Create Account")
        self.history[self.get_date_today()]["Create Account"].append((self.name, self.email))
    
    def check_date_exist(self, date) :
        if date in self.history :
            return True
        else:
            self.history[date] = {}
    
    def check_event_exist(self, date, event) :
        if event in self.history[date] :
            return True
        else:
            self.history[date][event] = []
    
    def get_date_today(self) :
        return datetime.datetime.today().strftime('%Y-%m-%d')

    
    def add_history(self, date, event, task , old_data = None , new_data = None) :
        self.check_date_exist(date)
        self.check_event_exist(date, event)
        if old_data == None :
            self.history[date][event].append((task.get_name_topic(), old_data))
        else :
            self.history[date][event].append((task.get_name_topic(), old_data, new_data)) 
    
    def get_history(self) :
        return self.history

    def get_email_data(self) :
        return {
            'name' : self.name,
            'email' : self.email
        }
    
    def get_task(self, name_topic) :
        for task in self.user_tasks :
            if task.get_name_topic() == name_topic :
                return task
        return None
    
    def get_task_due_date_by_name(self, name_topic) :
        for task in self.user_tasks :
            if task.get_name_topic() == name_topic :
                return task.get_due_date(), task.get_time()
        return None
    
    def add_task(self, task) :
        self.user_tasks.append(task)

    def remove_task(self, task) :
        self.user_tasks.remove(task)

    def get_user_tasks(self) :
        return self.user_tasks
    
    def change_email(self, new_email) :
        self.email = new_email

    def login(self, password) :
        if self.password == password :
            return True
        return False

    def get_all_complete_tasks(self) :
        # For History / Log
        return self.all_complete_tasks 
    
    def complete_task(self, task) :
        task.is_completed = True
        self.all_complete_tasks.append(task)
    
    

class Task(persistent.Persistent):
    def __init__(self, name_topic, detail, due_date, time, urgent=False) :
        self.name_topic = name_topic
        self.detail = detail
        self.due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d')
        self.time = time
        self.urgent = urgent
        self.is_completed = False
        self.start_date = datetime.datetime.today()

    def get_name_topic(self) :
        return self.name_topic

    def get_time(self) :
        return self.time
    
    def get_due_date(self) :
        return self.due_date
    
    def get_day_left(self) :
        #format: YYYY-MM-DD find the difference between today and due date
        today = datetime.datetime.today()
        return self.due_date - today

class MultiTask(Task, persistent.Persistent) :
    def __init__(self, name_topic, detail, due_date, time, urgent=False) :
        super().__init__(name_topic, detail, due_date, time, urgent)
        self.progress = 0 # 0%-100%
        self.tasks = []

    def add_task(self, task) :
        self.tasks.append(task)

    def remove_task(self, task) :
        self.tasks.remove(task)
    
    def update_progress(self) :
        self.progress = 0
        if len(self.tasks) == 0 :
            self.progress = 0
        else :
            for task in self.tasks :
                if task.is_completed :
                    self.progress += 100/len(self.tasks)
        if self.progress == 100 :
            self.is_completed = True
        else:
            self.is_completed = False

    def get_task(self, name_topic) :
        for task in self.tasks :
            if task.get_name_topic() == name_topic :
                return task
        return None


class Task_handlers(persistent.Persistent) :
    def __init__(self, Tasks) :
        self.Tasks = Tasks
        self.Today_tasks = []
        self.Urgent_tasks = []
        self.Upcoming_tasks = []
        self.Completed_tasks = []
        self.Late_tasks = []
        self.update_tasks()

    def get_today_tasks(self) :
        return self.Today_tasks
    
    def get_urgent_tasks(self) :
        return self.Urgent_tasks
    
    def get_upcoming_tasks(self) :
        return self.Upcoming_tasks
    
    def get_completed_tasks(self) :
        return self.Completed_tasks
    
    def get_late_tasks(self) :
        return self.Late_tasks
    
    def number_of_tasks(self) :
        return len(self.Tasks)
    
    def number_of_completed_tasks(self) :
        return len(self.Completed_tasks)
    
    def number_of_late_tasks(self) :
        return len(self.Late_tasks)
    
    def number_of_urgent_tasks(self) :
        return len(self.Urgent_tasks)
    
    def number_of_today_tasks(self) :
        return len(self.Today_tasks)
    
    def number_of_upcoming_tasks(self) :
        return len(self.Upcoming_tasks)
    
    def update_tasks(self) :
        self.Today_tasks = []
        self.Urgent_tasks = []
        self.Upcoming_tasks = []
        self.Completed_tasks = []
        self.Late_tasks = []
        for task in self.Tasks :
            if task.is_completed :
                self.Completed_tasks.append(task)
            elif task.urgent :
                self.Urgent_tasks.append(task)
            elif task.get_day_left().days == -1 :
                self.Today_tasks.append(task)
            elif task.get_day_left().days < -1 :
                self.Late_tasks.append(task)
            else :
                self.Upcoming_tasks.append(task)

class Notification(persistent.Persistent):
    def __init__(self, app_email, app_password) :
        self.app_email = app_email
        self.app_password = app_password
    
    def send_email(self, user, subject, message) :
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.app_email
        msg['To'] = user.get_email_data()['email']
        msg.set_content(message)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp :
            smtp.login(self.app_email, self.app_password)
            smtp.sendmail(self.app_email, user.get_email_data()['email'], msg.as_string())
