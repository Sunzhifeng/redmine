import context
from db.mongo.document import  connection, User

from multiprocessing  import Pool


def create(data):
    user = connection.User()
    user.name = data['name']
    user.password = data['password']
    user.email = data['email']
    user.save()


if __name__ == '__main__':
    p = Pool(4)
    while True:
        print 'APP: 1. create a user 2. exit'
        option = raw_input()
        if int(option) == 1:
            name = raw_input('name:')
            email = raw_input('email:')
            password = raw_input('password:')
            is_admin = raw_input('is_admin:')
            confirm = raw_input('ok ? (y/n)')
            if confirm == 'y':
                user = {}
                user['name'] = name
                user['email'] = email
                user['password'] = password
                user['is_admin'] = is_admin
                p.apply_async(create, args=(user,))
            else:
                continue
        if int(option) == 2:
            break

    p.close()
    p.join()
    print 'End.'
