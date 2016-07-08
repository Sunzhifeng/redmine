"""
    This module is used to handle db operations.
"""
from .exception import UnImplementException
from db.model import Bug, Feature, Improvement, User, Ticketing


class Handler(object):
    """ this class defines interfaces that interact with db.
    """
    def create(self, data):
        raise UnImplementException()

    def delete(self, _filter):
        raise UnImplementException()

    def update(self, _filter, data):
        raise UnImplementException()

    def get(self, _filter):
        raise UnImplementException()

    def list(self):
        raise UnImplementException()


class HandlerImp(Handler):
    """ this class implements the interfaces that interact with db.
    """
    def __init__(self, Cls):
        self.Cls = Cls

    def create(self, data):
        """ data is a dict that means the items attr-value.
        """
        checkattrs(self.Cls, data)
        obj = Cls()
        for (attr, value) in data.items:
            obj.attr = value
        obj.save()

    def delete(self, _filter):
        """ delete by id if id is provided, else by other attrs.
        """
        checkattrs(self.Cls, _filter)
        if '_id' in _filter:
            obj = Cls.find(_filter._id)
            return obj.remove()
        else:
            objs = Cls.findAll(_filter)
            for obj in objs:
                obj.remove()
            return len(objs)

    def update(self, _filter, data):
        """ update by id if id is provided, else by other attrs.
        """
        checkattrs(self.Cls, _filter)
        checkattrs(self.Cls, data)
        if '_id' in  _filter:
            obj = Cls.find(_filter._id)
            assignattrs(obj, data)
            obj.update()
        else:
            objs = Cls.findAll(_filter)
            for obj in objs:
                assignattrs(obj, data)
                obj.update()

    def get(self, _filter):
        """ get by id if id is provided, else by other attrs.
        """
        checkattrs(self.Cls, _filter)
        if '_id' in _filter:
            return Cls.find(_filter._id)
        else:
            return Cls.findAll(_filter)

    def list(self):
        return Cls.findAll()


def checkattrs(Cls, _filter):
    """ check if some class include all the attributes in _filter.
    """
    if len(_filter) == 0:
        return None
    for(attr, value) in _filter.items():
        if not hasattr(Cls, attr):
            raise UnKnownAttributeExcetpion('%s has no attribute <%s>' % (Cls, attr))


def assignattrs(obj, data):
    """ assign all attribute values in data to obj.
    """
    for (attr, value) in data.items():
        obj.attr = value


class TicketHandler(HandlerImp):
    """ This handler is used to handle bug, improvement, feature.
    """
    def __init__(self, Cls):
        if issubclass(Cls, Bug) or
                issubclass(Cls, Feature) or
                issubclass(Cls, Improvement):
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
