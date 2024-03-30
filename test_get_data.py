import ZODB, ZODB.FileStorage
import transaction
import class_module

mys = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(mys)
connection = db.open()
root = connection.root()

# get data from database
user = root.user['Arm']
user_tasks = user.get_user_tasks()
categorized_task = class_module.Task

history = user.history

# get history
print(history)