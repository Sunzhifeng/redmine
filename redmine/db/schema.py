#!/usr/bin/env python
"""
    This module includes all documents that are mapped into collections in mongodb.
"""
import uuid
import time
import datetime
import logging

from mongokit import Document, Connection
from validator import ValidatorUtils

logger = logging.getLogger(__name__)

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 27017

connection = Connection(DEFAULT_HOST, DEFAULT_PORT)
#connection = MongoDB(DEFAULT_HOST, DEFAULT_PORT)

class MongoDB(object):
    """ This class is used as interface for mongoDB operation.
    """
    def __init__(self, ip=DEFAULT_HOST, port=DEFAULT_PORT):
        self.ip = ip
        self.port = port
        self.client = None

    def __repr__(self):
        return '%s:%s' % (self.ip, self.port)

    def __enter__(self):
        self._connect()
        return self

    def __exit__(self, *unused):
        self.client.close()

    def _connect(self):
        try:
            self.client = Connection(self.ip, self.port)
            logger.debug("Connected to %s:%s" % (self.ip, self.port))
        except pymongo.errors.ConnectionFailure as error:
            logger.error("Couldn't connect to server: %s" % error)
            raise


def next_id():
    """ 50 bits for uuid
    """
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class RootDoc(Document):
    """ the root document is used to define commons.
    """
    __database__ = 'redmine'
    use_dot_notation = True
    skip_validation = True

    structure = {
        '_id': basestring,
        'create_at': datetime.datetime
    }

    required_fields = ['create_at', '_id']

    default_values = {
        '_id': next_id,
        'create_at': datetime.datetime.utcnow
    }


@connection.register
class User(RootDoc):
    """
    """
    __collection__ = 'users'

    structure = {
        'name': basestring,
        'password': basestring,
        'is_admin': bool,
        'email': basestring
    }

    required_fields = ['name', 'password', 'email']

    default_values = {
        'is_admin': False
    }

    validators = {
        'email': ValidatorUtils.email_validator
    }


@connection.register
class Ticket(RootDoc):
    """
    """
    structure = {
        'no': int,
        'title': basestring,
        'description': basestring,
        'status': basestring,
        'submitter_id': uuid.UUID,
        'submitter_name': basestring
    }

    required_fields = ['no', 'title', 'status',
                       'submitter_id', 'submitter_name']


@connection.register
class Bug(Ticket):
    __collection__ = 'bugs'

    structure = {
        'found_in': basestring,
    }


@connection.register
class Improvement(Ticket):
    __collection__ = 'improvements'


@connection.register
class Feature(Ticket):
    __collection__ = 'features'

    structure = {
        'target_sprint': basestring
    }

    required_fields = ['target_sprint']


@connection.register
class Ticketing(RootDoc):
    """ represent the mapping relation of tickets and user.
    """
    __collection__ = 'Ticketing'

    structure = {
        'ticket_id': uuid.UUID,
        'asignee_id': uuid.UUID,
        'assignee_name': basestring
    }
