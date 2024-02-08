import datetime
from class_module import *

Admin_Notification = Notification('Admin@gmail.com','Adminpass')

user_list = []

time_now = datetime.datetime.now()

user1 = User('John', '1234', 'test@gmail.com')
user_list.append(user1)

task1 = Task('Math', 'Do homework', '2021-12-31', '23:59')

if time_now.hour == 0 and time_now.minute == 1 :
    # chek all user tasks
    for user in user_list :
        # check all tasks for each user
        for task in user.get_user_tasks() :
            if task.get_time_left() <= 1 :
                # send notification
                Admin_Notification.send_email(user, 'Task Reminder', f'{task.get_name_topic()} is due in one day') # These shit wont work until we create the email and password.

        