import context
import data
from db.mongo.document import  connection
from db.mongo.document import User, Bug, Improvement, Feature, Ticketing
from db.mongo.handler import UserHandler


def add_user1():
    user_handler = UserHandler(User)
    user_handler.create(data.USER1)

def get_user1():
    user_handler = UserHandler(User)
    print user_handler.get({'name': data.USER1['name']})

def list_all():
    user_handler = UserHandler(User)
    print user_handler.list()

def update_user1():
    user_handler = UserHandler(User)
    print user_handler.update({'name': 'test1'}, {'name': 'update_test'})

def delete_user1():
    user_handler = UserHandler(User)
    print user_handler.delete({'name': data.USER1['name']})

if __name__ == '__main__':
    add_user1()
    delete_user1()
