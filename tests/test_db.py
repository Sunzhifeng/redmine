"""
    This module is used to test db connection and data access.
"""
from context import redmine

from redmine.db.schema import connection, User, Bug


def main():
    user = connection.User()
    user.name = 'test'
    user.password = 'test'
    user.is_admin = True
    print user
    user.save()
    bug = connection.Bug()
    print bug

if __name__ == '__main__':
    main()
