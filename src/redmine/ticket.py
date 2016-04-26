
class Ticket(object):
    def __init__(self, id, title, author, status=None, assignee=None):
        self._id = id
        self._title = title
        self._author = author
        self._status = status
        self._assignee = assignee

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, user):
        if not self._assignee:
            self._assignee = user

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    def __str__(self):
        return 'Ticket object (id=%s, title=%s, author= %s, status=%s, assignee=%s)' %\
            (self._id, self._title, self._author, self._status, self._assignee)

