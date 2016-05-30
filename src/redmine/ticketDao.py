import ticket
import db
class TicketDao(object):

    def get(self, tid):
        pass

    def list(self):
        return db.getAllTickets()

    def update(self, tId, **kargs):
        db.update(tId, kargs)
