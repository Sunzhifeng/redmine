"""
    This moudle is used to handle all DI in app.
"""
from db.mysql.model import BugTicket, FeatureTicket, ImprovementTicket
from db.mysql.model import Ticketing, User
from db.handler import TicketHandler, UserHandler, TicketingHandler
from service import BugService, FeatureService, ImprovementService
from IOC import features, FeatureUtils


def execute():
    """ this function is used to execute dependency inject (DI).
    """
    features.provide('bug', BugTicket('bug','ezhifsu','foundin'))
    features.provide('feature', FeatureTicket('feature','ezhifsu','target'))
    features.provide('improvement', ImprovementTicket('bug','ezhifsu','foundin'))
    features.provider('bugHandler', TicketHandler(BugTicket))
    features.provider('featureHandler', TicketHandler(FeatureTicket))
    features.provider('imporvementHandler', TicketHandler(ImprovementTicket))
    features.provider('userHandler', UserHandler(User))
    features.provider('ticketingHandler', TicketingHandler(Ticketing))

    features.provide('bugService', BugService()) # singleton lifestyle
    features.provide('featureService', FeatureService())
    features.provide('improvementService', ImprovementService())


