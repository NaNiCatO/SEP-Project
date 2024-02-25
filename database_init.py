import ZODB , ZODB.FileStorage
import transaction
import BTrees.OOBTree
from class_module import Notification as Notification

mystorage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(mystorage)
connection = db.open()
root = connection.root()

root.user = BTrees.OOBTree.BTree()
root.notification = BTrees.OOBTree.BTree()
root.task = BTrees.OOBTree.BTree()
root.task_handlers = BTrees.OOBTree.BTree()


root.notification['notification'] = Notification('sep.todoapp@gmail.com', 'Septodolist')

transaction.commit()
connection.close()