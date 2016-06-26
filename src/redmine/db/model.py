#!/usr/bin/env python3

"""
    This module includes all models that are mapped into tables in db.
"""

import time
import uuid

from orm import Model
from orm import StringField, BooleanField, FloatField, TextField


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')    # it is not eid.
    password = StringField(ddl='varchar(50)')
    admin = BooleanField()
    email = StringFeild(ddl='varchar(50)')
    create_at = FloatField(default=time.time)    # ignore time zone and date


class Ticket(Model):
    __table__ = 'tickets'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    num = IntegerField()
    title = StringField(ddl='varchar(200)')
    category = StringField(ddl='varchar(50)')
    description = TextField()
    submitter_id = StringField(ddl='varchar(50)')
    submitter_name = StringField(ddl='varchar(50)')
    status = StringField(ddl='varchar(50)')
    create_at = FloatField(default=time.time)


class BugTicket(Ticket):
    __table__ = 'bugTickets'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    num = IntegerField()
    title = StringField(ddl='varchar(200)')
    description = TextField()
    found_in = StringField(ddl='varchar(200)')    # special attr for bug
    status = StringField(ddl='varchar(50)')
    create_at = FloatField(default=time.time)


class ImprovementTicket(Ticket):
    __table__ = 'improvementTickets'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    num = IntegerField()
    title = StringField(ddl='varchar(200)')
    description = TextField()
    status = StringField(ddl='varchar(50)')
    create_at = FloatField(default=time.time)


class FeatureTicket(Ticket):
    __table__ = 'featureTickets'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    num = IntegerField()
    title = StringField(ddl='varchar(200)')
    description = TextField()
    target_sprint = TextField()    # spicial attr for feature
    status = StringField(ddl='varchar(50)')
    create_at = FloatField(default=time.time)


class Ticketing(Model):
    """ represent the mapping relation of tickets and user.
    """
    __table__ = 'Ticketing'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    ticket_id = StringField(ddl='varchar(50)')
    assignee_id = StringField(ddl='varchar(50)')
    assignee_name = StringField(ddl='varchar(50)')
    create_at = FloatField(default=time.time)
