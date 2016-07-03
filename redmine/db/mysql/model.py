#!/usr/bin/env python3

"""
    This module includes all models that are mapped into tables for mysqldb.
"""

import time
import uuid

from .orm import Model
from .orm import StringField, BooleanField, IntegerField, FloatField, TextField


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


# class Common(Model):
#     _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
#     create_at = FloatField(default=time.time)    # ignore time zone and date


class User(Model):
    __table__ = 'users'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    password = StringField(ddl='varchar(50)')
    admin = BooleanField()
    email = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)

    def __repr__(self):
        return "<User(name='%s', password='%s', admin='%s', email='%s')>" %\
                (self.name, self.password, str(self.admin), self.email)


class Bug(Model):
    __table__ = 'bugs'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    num = IntegerField()
    title = StringField(ddl='varchar(200)')
    description = TextField()
    submitter_id = StringField(ddl='varchar(50)')
    submitter_name = StringField(ddl='varchar(50)')
    status = StringField(ddl='varchar(50)')
    found_in = StringField(ddl='varchar(200)')
    created_at = FloatField(default=time.time)


class Improvement(Model):
    __table__ = 'improvements'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    num = IntegerField()
    title = StringField(ddl='varchar(200)')
    description = TextField()
    submitter_id = StringField(ddl='varchar(50)')
    submitter_name = StringField(ddl='varchar(50)')
    status = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)


class Feature(Model):
    __table__ = 'features'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    num = IntegerField()
    title = StringField(ddl='varchar(200)')
    description = TextField()
    target_sprint = TextField()
    submitter_id = StringField(ddl='varchar(50)')
    submitter_name = StringField(ddl='varchar(50)')
    status = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)


class Ticketing(Model):
    """ this model means the mapping relation of tickets and user.
    """
    __table__ = 'Ticketing'

    _id = StringField(primary_key=True, default= next_id, ddl='varchar(50)')
    ticket_id = StringField(ddl='varchar(50)')
    assignee_id = StringField(ddl='varchar(50)')
    assignee_name = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)
