"""
    This moudle is used to handle some services related to requirements.
"""


from ticket import Ticket, BugTicket, FeatureTicket, ImprovementTicket
from IOC import features, FeatureUtils, RequiredFeature


class TicketService(object):
    """ define some interfaces for ticket services.
    """
    baseTicket = RequiredFeature('bug', FeatureUtils.isInstanceOf(Ticket))

    def create(self, ticket):
        pass

    def assign(self, ticket, user):
        pass

    def verify(self, ticket):
        pass

    def close(self, ticket):
        pass


class BugTicketSerivce(TicketService):
    """
    """
    bugTicket = RequiredFeature('bug', FeatureUtils.isInstanceOf(Ticket))

    def create(self, ticket):
        ticket.save()

    def assign(self, ticket, user):
        ticket.assignee_id = user.id
        ticket.assignee_name = user.name
        bugTicket.update(ticket)

    def verify(self, ticket):
        ticket.status = 'verified'
        ticket.update()

    def feed_back(self, ticket, content):
        pass

    def close(self, ticket):
        ticket.status = 'closed'
        ticket.update()


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
