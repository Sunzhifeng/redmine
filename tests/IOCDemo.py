import os
from IOC import *


class Component(object):
    """ Symbolic base class for components
    """

class Bar(Component):
    con = RequiredFeature('Console', hasMethods('WriteLine'))
    title = RequiredFeature('AppTitle', isInstanceOf(str))
    user = RequiredFeature('CurrentUser', isInstanceOf(str))

    def __init__(self):
        self.x = 0

    def printYourself(self):
        self.con.WriteLine('-- Bar instance --')
        self.con.WriteLine('Title: %s' % self.title)
        self.con.WriteLine('User: %s' % self.user)
        self.con.WriteLine('X: %d' % self.x)


class SimpleConsole(Component):
    def WriteLine(self, s):
        print s

class BetterConsole(Component):
    def __init__(self, prefix=''):
        self.prefix = prefix

    def WriteLine(self, s):
        lines = s.split('\n')
        for line in lines:
            if line:
                print self.prefix, line
            else:
                print

def GetCurrentUser():
    return os.getenv('USERNAME') or 'Some User'

if __name__ == '__main__':
    print ' IOC Demo'
    features.provide('AppTitle', 'Inversion of Control ...\n\n... The Python Way')
    features.provide('CurrentUser', GetCurrentUser)
    # features.provide('Console', BetterConsole, prefix='-->') # <-- transient lifestyle
    features.provide('Console', BetterConsole(prefix='-->')) # <-- singleton lifestyle

    bar = Bar()
    bar.printYourself()
