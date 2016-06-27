from context import redmine

from redmine.ticket import Ticket, BugTicket, FeatureTicket, ImprovementTicket
from IOC import features, FeatureUtils, RequiredFeature


class TicketService(object):
    """ The base class to define the interfaces of ticket service.
    """
    def my_info(self):
        pass


class BugTicketService(TicketService):
    """
    """
    bugTicket = RequiredFeature('bug', FeatureUtils.isInstanceOf(Ticket))
    def my_info(self):
        return 'bug ticket service'


class ImprovementSerivce(TicketService):
    """
    """
    improvementTicket = RequiredFeature('improvement', FeatureUtils.isInstanceOf(Ticket))
    def my_info(self):
        return 'bug ticket service'


class FeatureTicketService(TicketService):
    """
    """
    featureTicket = RequiredFeature('feature', FeatureUtils.isInstanceOf(Ticket))
    def my_info(self):
        return 'feature ticket service'


class Main(object):
    bugService = RequiredFeature('bugService', FeatureUtils.hasMethods('my_info'))
    featureService = RequiredFeature('featureService', FeatureUtils.hasMethods('my_info'))

    def print_info(self):
        print self.bugService.my_info()
        print self.featureService.my_info()


if __name__ == '__main__':
    features.provide('bug', BugTicket('bug','ezhifsu','foundin'))
    features.provide('feature', FeatureTicket('feature','ezhifsu','target'))

    features.provide('bugService', BugTicketService) # singleton lifestyle
    features.provide('featureService', FeatureTicketService())

    Main().print_info()
