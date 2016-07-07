"""
    This module is used to handle db operations.
"""
from exception import UnImplementException, UnKnownAttributeExcetpion
from document import connection, Ticket, Bug, Improvement, Feature, User, Ticketing


class Handler(object):
    """ this class defines interfaces that interact with db.
    """
    def create(self, data):
        raise UnImplementException("SubClass of Handler: <creat>")

    def delete(self, _filter):
        raise UnImplementException("SubClass of Handler: <delete>")

    def update(self, _filter, data):
        raise UnImplementException("SubClass of Handler: <update>")

    def get(self, _filter):
        raise UnImplementException("SubClass of Handler: <get>")

    def list(self):
        raise UnImplementException("SubClass of Handler: <list>")


class HandlerImp(Handler):
    """ this class implements the interfaces that interact with db.
    """
    conn = connection

    def __init__(self, Cls):
        self.Cls = Cls

    def create(self, data):
        checkattrs(self.Cls, data)
        obj = self.conn[self.Cls.__name__]()
        assignattrs(obj, data)
        obj.save()

    def delete(self, _filter):
        checkattrs(self.Cls, _filter)
        objs = self.conn[self.Cls.__name__].find(_filter)
        del_count = 0
        for obj in objs:
            obj.delete()
            del_count = del_count + 1
        return del_count

    def update(self, _filter, data):
        checkattrs(self.Cls, _filter)
        checkattrs(self.Cls, data)
        objs = self.conn[self.Cls.__name__].find_and_modify(_filter, data)
        return objs

    def get(self, _filter):
        checkattrs(self.Cls, _filter)
        return [obj for obj in self.conn[self.Cls.__name__].find(_filter)]

    def list(self):
        return [obj for obj in self.conn[self.Cls.__name__].find()]


class TicketHandler(HandlerImp):
    """
    """
    def __init__(self, Cls):
        if issubclass(Cls.__name__, Ticket):
            super(TicketHandler, self).__init__(Cls)  # ignore ?
        else:
            raise UnExpectClassException('TicketHandler can not handle <%s>' % Cls)


class UserHandler(HandlerImp):
    """
    """
    def __init__(self, Cls):
        if issubclass(Cls, User):
            super(UserHandler, self).__init__(Cls)
        else:
            raise UnExpectClassException('UserHandler can not handle <%s>' % Cls)


class TicketingHandler(HandlerImp):
    """
    """
    def __init__(self, Cls):
        if issubclass(Cls, Ticketing):
            super(TicketingHandler, self).__init__(Cls)
        else:
            raise UnExpectClassException('TicketingHandler can not handle <%s>' % Cls)


def checkattrs(Cls, _filter):
    """ check if some class include all the attributes in _filter.
    """
    if len(_filter) == 0:
        raise Exception('filter is None')
    for(attr, value) in _filter.items():
        if not attr in Cls._namespaces:
            raise UnKnownAttributeExcetpion('%s has no attribute <%s>' % (Cls, attr))


def assignattrs(obj, data):
    """ assign all attribute values in data to obj.
    """
    for (attr, value) in data.items():
        obj[attr] = value
