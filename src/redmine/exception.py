"""
    This module is used to define exceptions.
"""
import Exception


class UnImplementException(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return message


class UnExpectClassException(Exception):
    pass
