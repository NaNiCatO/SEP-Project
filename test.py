import ZODB , ZODB.FileStorage
import transaction

mystorage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(mystorage)
connection = db.open()
root = connection.root()

for user in root.user:
    print(user)
    user = root.user[user]
    print(user.get_user_tasks())