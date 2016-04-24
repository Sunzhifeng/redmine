#!/usr/bin/python

from user import User
from ticket import Ticket
from ticketHandle import TicketHandler

def main():
    eId = 'exxxx'
    username = 'mmm'
    passsword = '*****'
    email = 'xx_xx@com.cn'
    tId = 'txxxx'
    title = 'tilte_description'

    author = new User(eId, username, password, email)
    assignee = new User(eId, username, password, email)
    ticket = new Ticket(tId, title, author)
    ticketHandler = new TicketHandler()

    ticketHandler.assign_ticket(ticket, assignee)
    ticketHandler.release_code(ticket, assignee)

