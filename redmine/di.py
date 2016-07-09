"""
    This moudle is used to handle all DI in app.
"""
from mongokit import Connection
from db.mongo.document import Bug, Feature, Improvement, Ticketing, User
from handler import TicketHandler, UserHandler, TicketingHandler
from service import BugService, FeatureService, ImprovementService, UserService, TicketingService
from ioc import features, FeatureUtils, RequiredFeature
from conf.config import configs


def execute():
    """ this function is used to execute dependency inject (DI).
    """
    # provider db connection
    connection = Connection(configs.db.mongo)
    connection.register([Bug, Feature, Improvement, Ticketing, User])
    features.provide(Connection.__name__, connection)  # signletion

    # provider handler
    features.provide(UserHandler.__name__, UserHandler(User))
    features.provide('bugHandler', TicketHandler(Bug))
    features.provide('featureHandler', TicketHandler(Feature))
    features.provide('imporvementHandler', TicketHandler(Improvement))
    features.provide('ticketingHandler', TicketingHandler(Ticketing))

    # provider service
    features.provide(UserService.__name__, UserService())
    features.provide('bugService', BugService())
    features.provide('featureService', FeatureService())
    features.provide('improvementService', ImprovementService())
    features.provide('ticketingService', TicketingService())
