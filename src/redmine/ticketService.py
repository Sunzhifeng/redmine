class TicketService(object):
    def assign(self, ticket, user):
        pass

    def verify(self, ticket):
        pass

    def close(self, ticket):
        pass

class BugTicketSerivce(TicketService):
    def feed_back(self):
        pass

class ImprovementTicketService(TicketService):
    pass

class FeatureTicketService(TicketService):
    pass


def ticket_factory(ticket_type):
    ticket_types = ['BugTicket',
                    'ImprovementTicket',
                    'FeatureTicket'
                    ]
    if ticket_type in ticket_types:
        return 'The given type ticket'
    elif:
        return 'no supporting ticket type'
