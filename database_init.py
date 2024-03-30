import ZODB , ZODB.FileStorage
import transaction
import BTrees.OOBTree
from class_module import Notification as Notification
from class_module import User as User
from class_module import Task as Task
from class_module import MultiTask as MultiTask



mystorage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(mystorage)
connection = db.open()
root = connection.root()

root.user = BTrees.OOBTree.BTree()
root.notification = BTrees.OOBTree.BTree()

root.user['Arm'] = User("Arm", "123", "armfiba@gmail.com")

root.user['Arm'].add_task(Task("Math", "Do exercise 1-5", "2024-2-26", "20:00"))

root.notification['notification'] = Notification('sep.todoapp@gmail.com', 'tzuk zziw vigb bshi')

transaction.commit()
connection.close()