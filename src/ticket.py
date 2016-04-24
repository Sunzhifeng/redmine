
class Ticket(object):
    def __init__(self, id, title, author, assignee=None):
        self._id = id
        self._title = title
        self._author = author
        self._assignee = assignee

    @property
    def id(self):
        return self._id
