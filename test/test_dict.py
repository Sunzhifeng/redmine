#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../tool'))

from mydict import toDict

def main():
    d = {'name': 'Sunzhifeng'}
    mydict = toDict(d)

if __name__ == '__main__':
     main()
