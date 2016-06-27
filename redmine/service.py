"""
    This moudle is used to handle some services related to requirements.
"""

from ticket import Ticket, BugTicket, FeatureTicket, ImprovementTicket
from handler import TicketHandler, UserHandler, TicketingHandler
from IOC import features, FeatureUtils, RequiredFeature


class userService(object):
    """
    """
    userHandler= RequiredFeature('userHandler',
                                 FeatureUtils.isInstanceOf(UserHandler))

    def login(self, name, password):
        user = userHandler.get(name)
        if user and user.password == password:
            return True
        else:
            return False

    def regist(self, name, password, is_admin, email):
        userHanlder.create({'name': name,
                            'password': password,
                            'admin': is_admin,
                            'email': email})
        return True

    def modify_pwd(self, name, password):
        userHandler.update({'name': name}, {'password': password})


class TicketService(object):
    """ define some interfaces for ticket services.
    """
    ticketHandler = RequiredFeature('ticketHandler',
                                    FeatureUtils.isInstanceOf(TicketHandler))
    userHandler = RequiredFeature('userHandler',
                                  FeatureUtils.isInstanceOf(UserHandler))

    def create(self, num, title, description, status , submitter_name):
        submitter = userHandler.get(name=submitter_name)
        ticketHandler.create({'num': num,
                              'title': title,
                              'description': description,
                              'status': 'New',
                              'submitter_id': submitter._id,
                              'submitter_name': name})

    def verify(self, ticket_id):
        updated_fields = {'status': 'verified'}
        tickethandler.update(ticket_id, updated_fields)

    def close(self, ticket_id):
        updated_fields = {'status': 'closed'}
        ticketHandler.update(ticket_id, updated_fields)


class BugSerivce(TicketService):
    """
    """
    ticketHandler = RequiredFeature('bugHandler',
                                    FeatureUtils.isInstanceOf(TicketHandler))

    def feed_back(self, ticket_num, content):
        ticketHandler.update({'num': ticket_num}, {'found_in': content})


class ImprovementService(TicketService):
    """
    """
    ticketHandler = RequiredFeature('improvementHandler',
                                    FeatureUtils.isInstanceOf(TicketHandler))


class FeatureService(TicketService):
    """
    """
    ticketHandler = RequiredFeature('featureHandler',
                                    FeatureUtils.isInstanceOf(TicketHandler))


class TicketingService(object):
    """
    """
    userHandler = RequiredFeature('userHandler',
                                  FeatureUtils.isInstanceOf(UserHandler))
    ticketHandler = RequiredFeature('ticketHandler',
                                    FeatureUtils.isInstanceOf(TicketHandler))
    ticketingHandler = RequiredFeature('ticketingHandler',
                                       FeatureUtils.isInstanceOf(Handler))

    def assign(self, num, name):
        assignee = userHandler.get(name=username)
        ticket =ticketHandler.get(num=num)
        ticketingHandler.create(ticket_id=ticket._id,
                                assignee_id=assignee._id,
                                assignee_name=name)


class BugTicketingService(TicketingService):
    """
    """
    ticketHandler = RequiredFeature('bugHandler',
                                    FeatureUtils.isInstanceOf(TicketHandler))


class FeatureTicketingService(TicketingService):
    """
    """
    ticketHandler = RequiredFeature('featureHandler',
                                    FeatureUtils.isInstanceOf(TicketHandler))


class ImprovementTicketingService(TicketingService):
    """
    """
    ticketHandler = RequiredFeature('improvementHandler',
                                    FeatureUtils.isInstanceOf(TicketHandler))
