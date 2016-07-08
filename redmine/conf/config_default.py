#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Default configurations
"""

configs = {
    'db': {
            'mysql': {
                'host': '127.0.0.1',
                'port': 3306,
                'user': 'root',
                'password': '123456',
                'db': 'redmine'
            },
            'mongo': {
                'ip': '127.0.0.1',
                'port': 2017
            }
    },
    'session': {
                'secret': 'ReDmInE'
    }
}
