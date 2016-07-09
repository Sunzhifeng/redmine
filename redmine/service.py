"""
    This moudle is used to handle some services related to requirements.
"""

from handler import TicketHandler, UserHandler, TicketingHandler
from ioc import FeatureUtils as FU
from ioc import RequiredFeature as RF


class UserService(object):
    """
    """
    userHandler= RF(UserHandler.__name__, FU.isInstanceOf(UserHandler))

    def login(self, name, password):
        user = self.userHandler.get(name)
        if user and user.password == password:
            return True
        else:
            return False

    def regist(self, name, password, is_admin, email):
        user_data = {
            'name': name,
            'password': password,
            'is_admin': is_admin,
            'email': email
        }
        self.userHandler.create(user_data)
        return True

    def modify_pwd(self, name, password):
        userHandler.update({'name': name}, {'password': password})


class TicketService(object):
    """ define some interfaces for ticket services.
    """
    userHandler = RF(UserHandler.__name__, FU.isInstanceOf(UserHandler))

    def create(self, num, title, description, status , submitter_name):
        submitter = self.userHandler.get(name=submitter_name)
        self.ticketHandler.create({'num': num,
                              'title': title,
                              'description': description,
                              'status': 'New',
                              'submitter_id': submitter._id,
                              'submitter_name': name})

    def verify(self, ticket_id):
        updated_fields = {'status': 'verified'}
        self.tickethandler.update(ticket_id, updated_fields)

    def close(self, ticket_id):
        updated_fields = {'status': 'closed'}
        self.ticketHandler.update(ticket_id, updated_fields)


class BugService(TicketService):
    """
    """
    ticketHandler = RF('bugHandler', FU.isInstanceOf(TicketHandler))

    def feed_back(self, ticket_num, content):
        self.ticketHandler.update({'num': ticket_num}, {'found_in': content})


class ImprovementService(TicketService):
    """
    """
    ticketHandler = RF('improvementHandler', FU.isInstanceOf(TicketHandler))


class FeatureService(TicketService):
    """
    """
    ticketHandler = RF('featureHandler', FU.isInstanceOf(TicketHandler))


class TicketingService(object):
    """
    """
    userHandler = RF('userHandler', FU.isInstanceOf(UserHandler))
    ticketingHandler = RF('ticketingHandler', FU.isInstanceOf(TicketingHandler))

    def assign(self, num, name):
        assignee = self.userHandler.get({'name': name})
        ticket = self.ticketHandler.get({'num': num})
        self.ticketingHandler.create(ticket_id=ticket._id,
                                assignee_id=assignee._id,
                                assignee_name=name)


class BugTicketingService(TicketingService):
    """
    """
    ticketHandler = RF('bugHandler', FU.isInstanceOf(TicketHandler))


class FeatureTicketingService(TicketingService):
    """
    """
    ticketHandler = RF('featureHandler', FU.isInstanceOf(TicketHandler))


class ImprovementTicketingService(TicketingService):
    """
    """
    ticketHandler = RF('improvementHandler', FU.isInstanceOf(TicketHandler))
