# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: introspect.pyc (Python 3.11)

'''
oauthlib.oauth2.rfc6749.endpoint.introspect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An implementation of the OAuth 2.0 `Token Introspection`.

.. _`Token Introspection`: https://tools.ietf.org/html/rfc7662
'''
import json
import logging
from oauthlib.common import Request
from errors import OAuth2Error
from base import BaseEndpoint, catch_errors_and_unavailability
log = logging.getLogger(__name__)

class IntrospectEndpoint(BaseEndpoint):
    '''Introspect token endpoint.

   This endpoint defines a method to query an OAuth 2.0 authorization
   server to determine the active state of an OAuth 2.0 token and to
   determine meta-information about this token. OAuth 2.0 deployments
   can use this method to convey information about the authorization
   context of the token from the authorization server to the protected
   resource.

   To prevent the values of access tokens from leaking into
   server-side logs via query parameters, an authorization server
   offering token introspection MAY disallow the use of HTTP GET on
   the introspection endpoint and instead require the HTTP POST method
   to be used at the introspection endpoint.
   '''
    valid_token_types = ('access_token', 'refresh_token')
    valid_request_methods = ('POST',)
    
    def __init__(self, request_validator, supported_token_types = (None,)):
