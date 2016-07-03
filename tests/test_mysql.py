"""
    This module is used to test mysqldb connection and data access.
"""
import context

import sys
import asyncio
from db.mysql.model import User
from db.mysql.orm import create_pool
from db.handler import UserHandler
from data import USER1, USER2, BUG, IMPROVEMENT

@asyncio.coroutine
def _db_connection(loop):
    yield from create_pool(loop=loop, user='root', password='123456', db='redmine')


@asyncio.coroutine
def test_save(loop):
    yield from _db_connection(loop)
    #user = User(name='test', password='test', admin=True, email='test@test.com')
    user = User(**USER1)
    yield from user.save()


@asyncio.coroutine
def test_find(loop):
    yield from _db_connection(loop)
    users = yield from User.findAll(name='test')
    print(users)


@asyncio.coroutine
def test_remove(loop):
    yield from _db_connection(loop)
    users = yield from User.findAll(name='test')
    for user in users:
        yield from user.remove()


@asyncio.coroutine
def test_update(loop):
    yield from _db_connection(loop)
    users = yield from User.findAll(name='test')
    for user in users:
        user.name = 'test_update'
        yield from user.update()

def main():
    loop = asyncio.get_event_loop()
    tasks = [test_remove(loop), test_save(loop), test_update(loop), test_find(loop)]
    loop.run_until_complete(test_save(loop))

if __name__ == '__main__':
    main()
