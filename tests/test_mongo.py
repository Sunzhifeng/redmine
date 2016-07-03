"""
    This module is used to test mongodb connection and data access.
"""
import context

from db.mongo.document import User, connection


def main():
    user = connection.User()
    user.save()

if __name__ == '__main__':
    main()
