#!/usr/bin/env python3

"""
    This module includes all models that are mapped into tables for mysqldb.
"""

import time
import uuid

from orm import Model
from orm import StringField, BooleanField, FloatField, TextField


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class Base(Model):
    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    create_at = FloatField(default=time.time)    # ignore time zone and date


class User(Base):
    __table__ = 'users'

    name = StringField(ddl='varchar(50)')    # it is not eid.
    password = StringField(ddl='varchar(50)')
    admin = BooleanField()
    email = StringFeild(ddl='varchar(50)')


class Ticket(Base):
    num = IntegerField()
    title = StringField(ddl='varchar(200)')
    description = TextField()
    submitter_id = StringField(ddl='varchar(50)')
    submitter_name = StringField(ddl='varchar(50)')
    status = StringField(ddl='varchar(50)')


class Bug(Ticket):
    __table__ = 'bugs'

    found_in = StringField(ddl='varchar(200)')


class Improvement(Ticket):
    __table__ = 'improvements'


class Feature(Ticket):
    __table__ = 'features'

    target_sprint = TextField()


class Ticketing(Base):
    """ represent the mapping relation of tickets and user.
    """
    __table__ = 'Ticketing'

    ticket_id = StringField(ddl='varchar(50)')
    assignee_id = StringField(ddl='varchar(50)')
    assignee_name = StringField(ddl='varchar(50)')
