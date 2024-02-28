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


def init_database():
    

    root.user = BTrees.OOBTree.BTree()
    root.notification = BTrees.OOBTree.BTree()
    root.task = BTrees.OOBTree.BTree()
    root.multi_task = BTrees.OOBTree.BTree()
    root.task_handlers = BTrees.OOBTree.BTree()

    root.user = BTrees.OOBTree.BTree()
    root.notification = BTrees.OOBTree.BTree()
    root.task = BTrees.OOBTree.BTree()
    root.multi_task = BTrees.OOBTree.BTree()
    root.task_handlers = BTrees.OOBTree.BTree()

    root.user['Arm'] = User("Arm", "123", "armfiba@gmail.com")
    root.task['Math'] = Task("Math", "Do exercise 1-5", "2024-2-26", "20:00")
    root.task['Physics'] = Task("Physics", "Do exercise 1-5", "2024-2-26", "20:00", True)
    root.task['Chemistry'] = Task("Chemistry", "Do exercise 1-5", "2024-2-27", "20:00")
    root.task['English'] = Task("English", "Do exercise 1-5", "2024-2-27", "20:00", True)
    root.task['History'] = Task("History", "Do exercise 1-5", "2024-2-28", "20:00")
    root.task['Biology'] = Task("Biology", "Do exercise 1-5", "2024-2-28", "20:00", True)

    root.multi_task['Study'] = MultiTask("Study", "Do exercise", "2024-2-26", "20:00")
    root.multi_task['Study'].add_task(root.task['Math'])
    root.multi_task['Study'].add_task(root.task['Physics'])
    root.multi_task['Study'].add_task(root.task['Chemistry'])
    root.multi_task['Study'].add_task(root.task['English'])

    root.user['Arm'].add_task(root.task['Math'])
    root.user['Arm'].add_task(root.task['Physics'])
    root.user['Arm'].add_task(root.task['Chemistry'])
    root.user['Arm'].add_task(root.task['English'])
    root.user['Arm'].add_task(root.task['History'])
    root.user['Arm'].add_task(root.task['Biology'])
    root.user['Arm'].add_task(root.multi_task['Study'])


    root.notification['notification'] = Notification('sep.todoapp@gmail.com', 'Septodolist')


    return connection

if __name__ == "__main__":
    connection = init_database()
