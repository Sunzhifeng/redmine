#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Configuration
'''

import sys

sys.path.append('../tool')

from  mydict import merge, toDict
import config_default


configs = config_default.configs
try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)
