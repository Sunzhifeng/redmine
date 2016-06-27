import logging
logging.basicConfig(level=logging.INFO)

class User(object):

    def __init__(self, id, username, password, email):
        self._id  = id
        self._username = username
        self._password = password
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        # do some check for password
        self._password = value

    @property
    def email(self):
        return self._email

    def __str__(self):
        return 'User object (id=%s, name=%s, email=%s)' % (self._id, self._username, self._email)

