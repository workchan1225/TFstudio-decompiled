# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: token.pyc (Python 3.11)

'''
oauthlib.oauth2.rfc6749
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming and providing OAuth 2.0 RFC6749.
'''
import logging
from oauthlib.common import Request
from oauthlib.oauth2.rfc6749 import utils
from base import BaseEndpoint, catch_errors_and_unavailability
log = logging.getLogger(__name__)

class TokenEndpoint(BaseEndpoint):
    '''Token issuing endpoint.

    The token endpoint is used by the client to obtain an access token by
    presenting its authorization grant or refresh token.  The token
    endpoint is used with every authorization grant except for the
    implicit grant type (since an access token is issued directly).

    The means through which the client obtains the location of the token
    endpoint are beyond the scope of this specification, but the location
    is typically provided in the service documentation.

    The endpoint URI MAY include an "application/x-www-form-urlencoded"
    formatted (per `Appendix B`_) query component,
    which MUST be retained when adding additional query parameters.  The
    endpoint URI MUST NOT include a fragment component::

        https://example.com/path?query=component             # OK
        https://example.com/path?query=component#fragment    # Not OK

    Since requests to the token endpoint result in the transmission of
    clear-text credentials (in the HTTP request and response), the
    authorization server MUST require the use of TLS as described in
    Section 1.6 when sending requests to the token endpoint::

        # We will deny any request which URI schema is not with https

    The client MUST use the HTTP "POST" method when making access token
    requests::

        # HTTP method is currently not enforced

    Parameters sent without a value MUST be treated as if they were
    omitted from the request.  The authorization server MUST ignore
    unrecognized request parameters.  Request and response parameters
    MUST NOT be included more than once::

        # Delegated to each grant type.

    .. _`Appendix B`: https://tools.ietf.org/html/rfc6749#appendix-B
    '''
    valid_request_methods = ('POST',)
    
    def __init__(self, default_grant_type, default_token_type, grant_types):
        BaseEndpoint.__init__(self)
        self._grant_types = grant_types
        self._default_token_type = default_token_type
        self._default_grant_type = default_grant_type

    grant_types = (lambda self: self._grant_types)()
    default_grant_type = (lambda self: self._default_grant_type)()
    default_grant_type_handler = (lambda self: self.grant_types.get(self.default_grant_type))()
    default_token_type = (lambda self: self._default_token_type)()
    create_token_response = (lambda self, uri, http_method, body, headers, credentials, grant_type_for_scope, claims = ('POST', None, None, None, None, None): request = Request(uri, http_method = http_method, body = body, headers = headers)self.validate_token_request(request)request.scopes = utils.scope_to_list(request.scope)request.extra_credentials = credentialsif grant_type_for_scope:
request.grant_type = grant_type_for_scopeif claims:
request.claims = claimsgrant_type_handler = self.grant_types.get(request.grant_type, self.default_grant_type_handler)log.debug('Dispatching grant_type %s request to %r.', request.grant_type, grant_type_handler)grant_type_handler.create_token_response(request, self.default_token_type))()
    
    def validate_token_request(self, request):
        self._raise_on_bad_method(request)
        self._raise_on_bad_post_request(request)
