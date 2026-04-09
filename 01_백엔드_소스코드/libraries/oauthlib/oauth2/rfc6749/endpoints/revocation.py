# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: revocation.pyc (Python 3.11)

'''
oauthlib.oauth2.rfc6749.endpoint.revocation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An implementation of the OAuth 2 `Token Revocation`_ spec (draft 11).

.. _`Token Revocation`: https://tools.ietf.org/html/draft-ietf-oauth-revocation-11
'''
import logging
from oauthlib.common import Request
from errors import OAuth2Error
from base import BaseEndpoint, catch_errors_and_unavailability
log = logging.getLogger(__name__)

class RevocationEndpoint(BaseEndpoint):
    '''Token revocation endpoint.

    Endpoint used by authenticated clients to revoke access and refresh tokens.
    Commonly this will be part of the Authorization Endpoint.
    '''
    valid_token_types = ('access_token', 'refresh_token')
    valid_request_methods = ('POST',)
    
    def __init__(self, request_validator, supported_token_types, enable_jsonp = (None, False)):
