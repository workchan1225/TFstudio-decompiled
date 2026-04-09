# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
    oauthlib
    ~~~~~~~~

    A generic, spec-compliant, thorough implementation of the OAuth
    request-signing logic.

    :copyright: (c) The OAuthlib Community
    :license: BSD-3-Clause, see LICENSE for details.
'''
import logging
from logging import NullHandler
__author__ = 'The OAuthlib Community'
__version__ = '3.3.1'
logging.getLogger('oauthlib').addHandler(NullHandler())
_DEBUG = False

def set_debug(debug_val):
    '''Set value of debug flag

    :param debug_val: Value to set. Must be a bool value.
    '''
    global _DEBUG
    _DEBUG = debug_val


def get_debug():
    '''Get debug mode value.

    :return: `True` if debug mode is on, `False` otherwise
    '''
    return _DEBUG
