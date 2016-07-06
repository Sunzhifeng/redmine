"""
    This module is used to test mongodb connectionection and data access.
"""
import context
import data
from db.mongo.document import  connection
from db.mongo.document import User, Bug, Improvement, Feature, Ticketing

def add_user1():
    user1 = connection.User()
    user1.name = 'user1'
    user1.password = 'user1'
    user1.email = 'user1@example.com'
    user1.test_field = ''
    user1.save()

def add_user2():
    user2 = connection.User()
    user2.name = 'user2'
    user2.password = 'user2'
    user2.email = 'user2@example.com'
    user2.save()

def add_bug():
    bug = connection.Bug()
    user1 = connection.User.find_one({'name': 'user1'})
    bug.num = int('001')
    bug.title = 'bug-001 for testing'
    bug.description = 'an example bug for test'
    bug.found_in = 'anywhere'
    bug.submitter_id = user1._id
    bug.submitter_name = user1.name
    bug.save()


def add_feature():
    feature = connection.Feature()
    user2 = connection.User.find_one({'name': 'user2'})
    feature.num = int('001')
    feature.title = 'feature-001 for testing'
    feature.description = ''
    feature.target_sprint ='enough is ok'
    feature.submitter_id = user2._id
    feature.submitter_name = user2.name
    feature.save()

def assign_bug():
    ticketing = connection.Ticketing()
    bug = connection.Bug.find_one({'num': 001})
    user2 = connection.User.find_one({'name': 'user2'})
    connection.close()
    ticketing.ticket_id = bug._id
    ticketing.assignee_id = user2._id
    ticketing.assignee_name = user2.name
    ticketing.save()


def main():
    add_user1()
    add_user2()
    add_bug()
    add_feature()
    assign_bug()

if __name__ == '__main__':
    main()
