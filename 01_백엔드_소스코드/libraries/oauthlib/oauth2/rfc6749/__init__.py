# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
oauthlib.oauth2.rfc6749
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming and providing OAuth 2.0 RFC6749.
'''
import functools
import logging
from endpoints.base import BaseEndpoint, catch_errors_and_unavailability
from errors import FatalClientError, OAuth2Error, ServerError, TemporarilyUnavailableError
log = logging.getLogger(__name__)
