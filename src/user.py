import logging
logging.basicConfig(level=logging.INFO)

class User(object):
    __slots__ = ('id', 'username', 'password', 'email')

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
        return self.username

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
        return 'User object (id=%s, name=%s)' % (self._id, self._name)

    __repr__ == __str__
