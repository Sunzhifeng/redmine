"""
    This module is used to read/write disk file.
"""

import json


def read(path):
    data = None
    with open(path, 'r') as f:
        data = f.read()

    return data


def write(path, content):
    with open(path, 'w') as f:
        f.write(content)


def loads(json_str):
    return json.loads(json_str)


def dumps(a_dict):
    return json.dumps(d)

