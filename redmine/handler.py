"""
    This module is used to handle db operations.
"""
from exception import UnImplementException
from db.model import Ticket, User, Ticketing


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


class HandlerImp(object):
    """ this class implements the interfaces that interact with db.
    """
    def __init__(self, Cls):
        self.Cls = Cls

    def create(self, data):
        """ data is a dict that means the items attr-value.
        """
        checkattrs(self.Cls, data):
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
            # maybe batch update
            objs = Cls.findAll(_filter)
            for obj in objs:
                assignattrs(obj, data)
                obj.update()

    def get(self, _filter):
        """ get by id if id is provided, else by other attrs.
        """
        checkattrs(self.Cls, _filter):
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
            raise UnKnownAttributeExcetpion('%s has no attribute <%s>', % (Cls, attr))


def assignattrs(obj, data):
    """ assign all attribute values in data to obj.
    """
    for (attr, value) in data.items():
        obj.attr = value


class TicketHandler(Handler, HandlerImp):
    """
    """
    def __init__(self, Cls):
        if issubclass(Cls, Ticket):
            super().__init__()  # ignore ?
            super_classs = TicketHandler.__bases__
            HandlerImp.__init__(Cls)
        else:
            raise UnExpectClassException('TicketHandler can not handle <%s>' % Cls)


class UserHandler(Handler, Imp):
    """
    """
    def __init__(self, Cls):
        if issubclass(Cls, User):
            super().__init__()
            HandlerImp.__init__(Cls)
        else:
            raise UnExpectClassException('UserHandler can not handle <%s>' % Cls)


class TicketingHandler(Handler, HandlerImp):
    """
    """
    def __init__(self, Cls):
        if issubclass(Cls, User):
            super().__init__()
            HandlerImp.__init__(Cls)
        else:
            raise UnExpectClassException('TicketingHandler can not handle <%s>' % Cls)
