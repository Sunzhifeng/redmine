#!/usr/bin/env python
"""
    This module includes all documents that are mapped into collections in mongodb.
"""
import sys
import datetime

sys.path.append('../lib')

from mongokit import Document, Connection, IS
from validator import ValidatorUtils

HOSTNAME = 'localhost'
PORT = 27017
connection = Connection(host=HOSTNAME, port=PORT)

@connection.register
class RootDoc(Document):
    """ the root document is used to define commons.
    """
    __database__ = 'redmine'
    use_dot_notation = True
    skip_validation = True

    structure = {
        '_id': uuid.UUID,
        'create_at': datetime.datetime
    }

    required_fields = ['create_at', '_id']

    default_values = {
        '_id': uuid.UUID,
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
        'status': IS('New', 'Verified','Solved', 'Closed'),
        'submitter_id': uuid.UUID,
        'submitter_name': basestring
    }

    required_fields = ['no', 'title', 'status', 'submitter_id',
                       'submitter_name']


@connection.register
class Bug(Ticket):
    __collection__ = 'bugs'

    structure = {
        'found_in': basestring,
    }


@connection.register
class Improvement(Ticket):
    __collection__ = 'improvements'


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
