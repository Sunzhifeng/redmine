"""
    This module is used to contact with db.
"""

class BaseHandler(object):

    def get(self, id):
        pass

    def list(self):
        pass

    def update(self, id, **options):
        pass


class TicketHandler(BaseHandler):
    pass

class UserHandler(BaseHandler):
    pass
