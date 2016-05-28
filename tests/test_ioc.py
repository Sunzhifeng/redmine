from context import redmine

from redmine.ticket import Ticket, BugTicket, FeatureTicket
from IOC import features, isInstanceOf, hasAttributes, hasMethods, RequiredFeature

class TicketService(object):
    def my_info(self):
        pass

class BugTicketService(TicketService):
    bugTicket = RequiredFeature('bug', isInstanceOf(Ticket))
    def my_info(self):
        return 'bug ticket service'

class FeatureTicketService(TicketService):
    featureTicket = RequiredFeature('bug', isInstanceOf(Ticket))
    def my_info(self):
        return 'feature ticket service'

class Main(object):
    bugService = RequiredFeature('bugService', hasMethods('my_info'))
    featureService = RequiredFeature('featureService', hasMethods('my_info'))

    def print_myself(self):
        print self.bugService.my_info()
        print self.featureService.my_info()



if __name__ == '__main__':
    features.provide('bug', BugTicket('bug','ezhifsu','foundin'))
    features.provide('feature', FeatureTicket('feature','ezhifsu','target'))

    features.provide('bugService', BugTicketService) # singleton lifestyle
    features.provide('featureService', FeatureTicketService())

    Main().print_myself()
