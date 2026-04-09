# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: device_authorization.pyc (Python 3.11)

'''
oauthlib.oauth2.rfc8628
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming and providing OAuth 2.0 RFC8628.
'''
import logging
from typing import Callable
from oauthlib.common import Request, generate_token
from oauthlib.oauth2.rfc6749 import errors
from oauthlib.oauth2.rfc6749.endpoints.base import BaseEndpoint, catch_errors_and_unavailability
log = logging.getLogger(__name__)

class DeviceAuthorizationEndpoint(BaseEndpoint):
    '''DeviceAuthorization endpoint - used by the client to initiate
    the authorization flow by requesting a set of verification codes
    from the authorization server by making an HTTP "POST" request to
    the device authorization endpoint.

    The client authentication requirements of Section 3.2.1 of [RFC6749]
    apply to requests on this endpoint, which means that confidential
    clients (those that have established client credentials) authenticate
    in the same manner as when making requests to the token endpoint, and
    public clients provide the "client_id" parameter to identify
    themselves.
    '''
    
    def __init__(self, request_validator, verification_uri = None, expires_in = None, interval = None, verification_uri_complete = (1800, None, None, None), user_code_generator = ('user_code_generator', Callable[([
        None], str)])):
        '''
        :param request_validator: An instance of RequestValidator.
        :type request_validator: oauthlib.oauth2.rfc6749.RequestValidator.
        :param verification_uri: a string containing the URL that can be polled by the client application
        :param expires_in: a number that represents the lifetime of the `user_code` and `device_code`
        :param interval: an option number that represents the number of seconds between each poll requests
        :param verification_uri_complete: a string of a function that can be called with `user_data` as parameter
        :param user_code_generator: a callable that returns a configurable user code
        '''
        self.request_validator = request_validator
        self._expires_in = expires_in
        self._interval = interval
        self._verification_uri = verification_uri
        self._verification_uri_complete = verification_uri_complete
        self.user_code_generator = user_code_generator
        BaseEndpoint.__init__(self)

    interval = (lambda self: self._interval)()
    expires_in = (lambda self: self._expires_in)()
    verification_uri = (lambda self: self._verification_uri)()
    
    def verification_uri_complete(self, user_code):
        if not self._verification_uri_complete:
            return None
        if None(self._verification_uri_complete, str):
            return self._verification_uri_complete.format(user_code = user_code)
        if None(self._verification_uri_complete):
            return self._verification_uri_complete(user_code)

    validate_device_authorization_request = (lambda self, request: for param in ('client_id', 'scope'):
duplicate_params = request.duplicate_paramsexcept ValueError:
raise errors.InvalidRequestFatalError(description = 'Unable to parse query string', request = request)if param in duplicate_params:
raise errors.InvalidRequestFatalError(description = 'Duplicate %s parameter.' % param, request = request)continueif request.headers['Content-Type'] != 'application/x-www-form-urlencoded':
raise errors.InvalidRequestError('Content-Type must be application/x-www-form-urlencoded', request = request)if not request.client_id:
raise errors.MissingClientIdError(request = request)if not self.request_validator.validate_client_id(request.client_id, request):
raise errors.InvalidClientIdError(request = request)self._raise_on_invalid_client(request))()
    create_device_authorization_response = (lambda self, uri, http_method, body, headers = ('POST', None, None): request = Request(uri, http_method, body, headers)self.validate_device_authorization_request(request)log.debug('Pre resource owner authorization validation ok for %r.', request)headers = { }user_code = self.user_code_generator() if self.user_code_generator else generate_token()data = {
'verification_uri': self.verification_uri,
'expires_in': self.expires_in,
'user_code': user_code,
'device_code': generate_token() }# WARNING: Decompyle incomplete
)()
