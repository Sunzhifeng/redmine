"""
    This module is used to handle db operations.
"""
from exception import UnImplementException, UnKnownAttributeExcetpion
from db.schema import connection, Ticket, Bug, Improvement, Feature, User, Ticketing


class Handler(object):
    """ this class defines interfaces that interact with db.
    """
    def __init__(self):
        pass

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
    def __init__(self, Cls):
        self.Cls = Cls

    def create(self, data):
        """ data is a dict that means the items attr-value.
        """
        checkattrs(self.Cls, data)
        Cls = self.Cls
        obj = connection.Cls()
        assignattrs(obj, data)
        obj.save()

    def delete(self, _filter):
        """ delete by id if id is provided, else by other attrs.
        """
        checkattrs(self.Cls, _filter)
        objs = self.Cls.find(_filter)
        for obj in objs:
            obj.delete()
        return len(objs)

    def update(self, _filter, data):
        """ update by id if id is provided, else by other attrs.
        """
        checkattrs(self.Cls, _filter)
        checkattrs(self.Cls, data)
        objs = Cls.find_one(_filter)
        for obj in objs:
            assignattrs(obj, data)
            obj.update()
        return len(objs)

    def get(self, _filter):
        """ get by id if id is provided, else by other attrs.
        """
        checkattrs(self.Cls, _filter)
        Cls = self.Cls
        return connection.Cls.find(_filter._id)

    def list(self):
        return Cls.find()


def checkattrs(Cls, _filter):
    """ check if some class include all the attributes in _filter.
    """
    if len(_filter) == 0:
        return None
    for(attr, value) in _filter.items():
        if not attr in Cls._namespaces:
            raise UnKnownAttributeExcetpion('%s has no attribute <%s>' % (Cls, attr))


def assignattrs(obj, data):
    """ assign all attribute values in data to obj.
    """
    for (attr, value) in data.items():
        obj.attr = value


class TicketHandler(HandlerImp):
    """
    """
    def __init__(self, Cls):
        if issubclass(Cls, Ticket):
            super(TicketHandler, self).__init__(Cls)  # ignore ?
        else:
            raise UnExpectClassException('TicketHandler can not handle <%s>' % Cls)


class UserHandler( HandlerImp):
    """
    """
    def __init__(self, Cls):
        if issubclass(Cls, User):
            super(UserHandler, self).__init__(Cls)
        else:
            raise UnExpectClassException('UserHandler can not handle <%s>' % Cls)


class TicketingHandler(Handler, HandlerImp):
    """
    """
    def __init__(self, Cls):
        if issubclass(Cls, Ticketing):
            super(TicketingHandler, self).__init__(Cls)
        else:
            raise UnExpectClassException('TicketingHandler can not handle <%s>' % Cls)
