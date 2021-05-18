import configparser

from chatdb import ChatDB

config = configparser.ConfigParser()
config.read("config.ini")

db = ChatDB(config['mysql'])
db.connect()

data = {
    'user_id': 123456789,
    'chat_id': 987654321, 
    'nicename': 'Aaron',
    'email': 'aaronxxx@gmail.com',
    'phone': '098812345678',
    'display_name': '亞倫'
}

#print(db.create_user(data))
#print(db.find_user(data).ID)
db.close()