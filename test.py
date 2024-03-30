import datetime
from email.message import EmailMessage
import smtplib
import ssl
import persistent

class Notification(persistent.Persistent):
    def __init__(self, app_email, app_password) :
        self.app_email = app_email
        self.app_password = app_password
    
    def send_email(self, user , subject, message) :
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.app_email
        msg['To'] = user.get_email_data()['email']
        msg.set_content(message)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp :
            smtp.login(self.app_email, self.app_password)
            smtp.sendmail(self.app_email, user.get_email_data()['email'], msg.as_string())




class User(persistent.Persistent):
    def __init__(self, name, password, email) :
        self.name = name
        self.password = password
        self.email = email
        self.user_tasks = []
        self.all_complete_tasks = []

    def get_email_data(self) :
        return {
            'name' : self.name,
            'email' : self.email
        }
    
    def change_email(self, new_email) :
        self.email = new_email

    def login(self, password) :
        if self.password == password :
            return True
        return False

    
            
Notification_test = Notification('sep.todoapp@gmail.com', 'tzuk zziw vigb bshi')

User_test = User('Tee', '123', 'yourmail')

Notification_test.send_email(User_test, 'Test', 'This is a test email')
