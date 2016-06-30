"""
    This module is used to test handler module.
"""
from context import redmine

from redmine.db.schema import User, Bug
from redmine.handler import UserHandler


def main():
    user_handler = UserHandler(User)
    user = User()
    print user
    import pdb
    pdb.set_trace()
    user_handler.create({'name': 'sunzhifeng'})



if __name__ == '__main__':
    main()
