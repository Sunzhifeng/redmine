
class TicketHandler(object):
    def assign_ticket(self, ticket, user):
        ticket.assignee = user
        print 'assign ticket %s  to %s ' % (ticket.title, user.username)

    def release_code(self, user, ticket)
        print ('{user.username} release ticket {ticket.title} code'.\
            format(user = user, ticket = ticket))
