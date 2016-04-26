
class TicketHandler(object):
    def assign_ticket(self, ticket, user):
        ticket.assignee = user
        ticket.status = "doing"
        print 'assign ticket <%s:%s > to %s .' % (ticket.id, ticket.title, user.username)

    def release_code(self, ticket, user):
        ticket.status = "done"
        print '%s release code for ticket <%s:%s>.' % (user.username, ticket.id, ticket.title)
