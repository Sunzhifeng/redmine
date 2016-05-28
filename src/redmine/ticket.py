import time


class Ticket(object):
    def __init__(self, title, submitter, status=None, assignee=None):
        self._id = self._generate_id()
        self._title = title
        self._submitter = submitter
        self._status = status
        self._assignee = assignee

    def _generate_id(self):
    return self._submitter + '_' + int(time.time())

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def submitter(self):
        return self._submitter

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

    def __repr__(self):
        return 'Ticket object (id=%s, title=%s, submitter= %s, status=%s, assignee=%s)' %\
            (self._id, self._title, self._submitter, self._status, self._assignee)

class BugTicket(Ticket):
    def __init__(self, title, submitter, status, assignee, found_in):
        super(BugTicket, self).__init__(title, submitter, status, assignee)
        self._found_in = found_in

    @property
    def found_in(self):
        return self._found_in

class ImprovementTicket(Ticket):
    def __init__(self, title, submitter, status, assignee, others):
        super(BugTicket, self).__init__(title, submitter, status, assignee)
        self._other = other

class FeatureTicket(Ticket):
    def __init__(self, title, submitter, status, assignee, others):
        super(BugTicket, self).__init__(title, submitter, status, assignee)
        self._others = others


