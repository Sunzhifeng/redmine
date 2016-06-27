#!/usr/bin/python

from user import User
from ticket import Ticket
from ticketHandler import TicketHandler

def main():
    eId = 'ezhifsu'
    username = 'Zhifeng Sun'
    password = '123456'
    email = 'example@com.cn'
    tId = '#12345'
    title = 'python practice one'

    author = User(eId, username, password, email)
    assignee = User(eId, username, password, email)
    ticket = Ticket(tId, title, author)
    print author
    print assignee
    print ticket

    ticketHandler =  TicketHandler()
    ticketHandler.assign_ticket(ticket, assignee)
    ticketHandler.release_code(ticket, assignee)

if __name__ == '__main__':
    main()

