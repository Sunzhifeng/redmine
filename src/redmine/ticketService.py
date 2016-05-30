class BaseTicketService(object):
    def assign(self, ticket, person):
        pass

    def verify(self, ticket):
        pass

    def close(self, ticket):
        pass

class BugTicketSerivce(BaseTicketService):
    def feed_back(self):
        pass

class ImprovementTicketService(BaseTicketService):
    pass

class FeatureTicketService(BaseTicketService):
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
