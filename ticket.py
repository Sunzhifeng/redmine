
class Ticket(object):
    def __init__(self, tId, title, author, assignee=None):
        self.tId = tId
        self.title = title
        self.author = author
        self.assignee = assignee
