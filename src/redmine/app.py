from user import User
from ticket import Ticket, BugTicket, FeatureTicket, ImprovementTicket
from service import TicketService, BugTicketService, FeatureTicketService, ImprovementTicketService
from IOC import features, FeatureUtils, RequiredFeature


class Main(object):
    bugService = RequiredFeature('bugService', FeatureUtils.isInstanceOf(TicketService))
    featureService = RequiredFeature('featureService', FeatureUtils.isInstanceOf(TicketService))
    user = RequiredFeature('user', FeatureUtils.isInstanceOf(User))

    def print_info(self):
        print self.bugService.my_info()
        print self.featureService.my_info()


if __name__ == '__main__':
    features.provide('bug', BugTicket('bug','ezhifsu','foundin'))
    features.provide('feature', FeatureTicket('feature','ezhifsu','target'))

    features.provide('bugService', BugTicketService) # singleton lifestyle
    features.provide('featureService', FeatureTicketService())

    Main().print_info()
