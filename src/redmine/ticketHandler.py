class TicketHandler(object):
    def assign_ticket(self, tId, uId):
        ticket = TicketDao.get(tId)
        user = userDao.get(uId)
        ticket.assignee = user
        print 'assign ticket <%s:%s > to %s .' % (ticket.id, ticket.title, user.username)

    def release_code(self, ticket, user):
        ticket.status = "done"
        print '%s release code for ticket <%s:%s>.' % (user.username, ticket.id, ticket.title)

    def update_ticket_status(self, tId, status):
        ticket = TicketDao.get(tId)
        ticket.status = status
        TicketDao.update(ticket)

    def get_tickets(self):
        return TicketDao.list()


