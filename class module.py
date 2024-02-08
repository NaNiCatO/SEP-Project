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
    

class Task :
    def __init__(self, name_topic, detail, due_date, time) :
        self.name_topic = name_topic
        self.detail = detail
        self.due_date = due_date
        self.time = time
        self.is_completed = False



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