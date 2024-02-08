class User :
    def __init__(self, name, password, email) :
        self.name = name
        self.password = password
        self.email = email
        self.user_tasks = []

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
    

class Task :
    def __init__(self, name_topic, detail, due_date, time) :
        self.name_topic = name_topic
        self.detail = detail
        self.due_date = due_date
        self.time = time
        self.is_completed = False

    def get_name_topic(self) :
        return self.name_topic

    def get_time(self) :
        return self.time
    
    def get_due_date(self) :
        return self.due_date



class MultiTask(Task) :
    def __init__(self, name_topic, detail, due_date) :
        super().__init__(name_topic, detail, due_date)
        self.progress = 0 # 0%-100%
        self.tasks = []

    def add_task(self, task) :
        self.tasks.append(task)

    def remove_task(self, task) :
        self.tasks.remove(task)
    
    def update_progress(self) :
        for task in self.tasks :
            if task.is_completed :
                self.progress += 100/len(self.tasks)

        if self.progress == 100 :
            self.is_completed = True