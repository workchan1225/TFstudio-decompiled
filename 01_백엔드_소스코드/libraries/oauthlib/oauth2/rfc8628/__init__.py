# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
oauthlib.oauth2.rfc8628
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming and providing OAuth 2.0 Device Authorization RFC8628.
'''
from oauthlib.oauth2.rfc8628.errors import SlowDownError, AuthorizationPendingError, ExpiredTokenError
import logging
log = logging.getLogger(__name__)
