"""
    This module includes all validators that used in document defines.
"""

import re

class ValidatorUtils(object):
    """ this class defines some useful validators.
    """
    @classmethod
    def email_validator(cls, value):
        email = re.compile('/^([\w-_]+(?:\.[\w-_]+)*)@((?:[a-z0-9]+(?:-[a-zA-Z0-9]+)*)+\.[a-z]{2,6})$/i',\
                           re.IGNORECASE)
        if not email.match(value):
            raise ValidationError('%s is not a valid email' % value)
