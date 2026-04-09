# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''
oauthlib.oauth2.rfc6749
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming and providing OAuth 2.0 RFC6749.
'''
import functools
import logging
from errors import FatalClientError, InvalidClientError, InvalidRequestError, OAuth2Error, ServerError, TemporarilyUnavailableError, UnsupportedTokenTypeError
log = logging.getLogger(__name__)

class BaseEndpoint:
    
    def __init__(self):
        self._available = True
        self._catch_errors = False
        self._valid_request_methods = None

    valid_request_methods = (lambda self: self._valid_request_methods)()
    valid_request_methods = (lambda self, valid_request_methods: pass# WARNING: Decompyle incomplete
)()
    available = (lambda self: self._available)()
    available = (lambda self, available: self._available = available)()
    catch_errors = (lambda self: self._catch_errors)()
    catch_errors = (lambda self, catch_errors: self._catch_errors = catch_errors)()
    
    def _raise_on_missing_token(self, request):
        '''Raise error on missing token.'''
        if not request.token:
            raise InvalidRequestError(request = request, description = 'Missing token parameter.')

    
    def _raise_on_invalid_client(self, request):
        '''Raise on failed client authentication.'''
        if self.request_validator.client_authentication_required(request):
            if not self.request_validator.authenticate_client(request):
                log.debug('Client authentication failed, %r.', request)
                raise InvalidClientError(request = request)
            return None
        if not None.request_validator.authenticate_client_id(request.client_id, request):
            log.debug('Client authentication failed, %r.', request)
            raise InvalidClientError(request = request)

    
    def _raise_on_unsupported_token(self, request):
        '''Raise on unsupported tokens.'''
        if request.token_type_hint or request.token_type_hint in self.valid_token_types or request.token_type_hint not in self.supported_token_types:
            raise UnsupportedTokenTypeError(request = request)
        return None
        return None

    
    def _raise_on_bad_method(self, request):
        pass
    # WARNING: Decompyle incomplete

    
    def _raise_on_bad_post_request(self, request):
