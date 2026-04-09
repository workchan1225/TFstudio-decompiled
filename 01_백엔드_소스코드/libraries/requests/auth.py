# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: auth.pyc (Python 3.11)

'''
requests.auth
~~~~~~~~~~~~~

This module contains the authentication handlers for Requests.
'''
import hashlib
import os
import re
import threading
import time
import warnings
from base64 import b64encode
from _internal_utils import to_native_string
from compat import basestring, str, urlparse
from cookies import extract_cookies_to_jar
from utils import parse_dict_header
CONTENT_TYPE_FORM_URLENCODED = 'application/x-www-form-urlencoded'
CONTENT_TYPE_MULTI_PART = 'multipart/form-data'

def _basic_auth_str(username, password):
    '''Returns a Basic Auth string.'''
    if not isinstance(username, basestring):
        warnings.warn("Non-string usernames will no longer be supported in Requests 3.0.0. Please convert the object you've passed in ({!r}) to a string or bytes object in the near future to avoid problems.".format(username), category = DeprecationWarning)
        username = str(username)
    if not isinstance(password, basestring):
        warnings.warn("Non-string passwords will no longer be supported in Requests 3.0.0. Please convert the object you've passed in ({!r}) to a string or bytes object in the near future to avoid problems.".format(type(password)), category = DeprecationWarning)
        password = str(password)
    if isinstance(username, str):
        username = username.encode('latin1')
    if isinstance(password, str):
        password = password.encode('latin1')
    authstr = 'Basic ' + to_native_string(b64encode(b':'.join((username, password))).strip())
    return authstr


class AuthBase:
    '''Base class that all auth implementations derive from'''
    
    def __call__(self, r):
        raise NotImplementedError('Auth hooks must be callable.')



class HTTPBasicAuth(AuthBase):
    '''Attaches HTTP Basic Authentication to the given Request object.'''
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    
    def __eq__(self, other):
        return all([
            self.username == getattr(other, 'username', None),
            self.password == getattr(other, 'password', None)])

    
    def __ne__(self, other):
        return not (self == other)

    
    def __call__(self, r):
        r.headers['Authorization'] = _basic_auth_str(self.username, self.password)
        return r



class HTTPProxyAuth(HTTPBasicAuth):
    '''Attaches HTTP Proxy Authentication to a given Request object.'''
    
    def __call__(self, r):
        r.headers['Proxy-Authorization'] = _basic_auth_str(self.username, self.password)
        return r



class HTTPDigestAuth(AuthBase):
    '''Attaches HTTP Digest Authentication to the given Request object.'''
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._thread_local = threading.local()

    
    def init_per_thread_state(self):
        if not hasattr(self._thread_local, 'init'):
            self._thread_local.init = True
            self._thread_local.last_nonce = ''
            self._thread_local.nonce_count = 0
            self._thread_local.chal = { }
            self._thread_local.pos = None
            self._thread_local.num_401_calls = None
            return None

    
    def build_digest_header(self, method, url):
        '''
        :rtype: str
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def handle_redirect(self, r, **kwargs):
        '''Reset num_401_calls counter on redirects.'''
        if r.is_redirect:
            self._thread_local.num_401_calls = 1
            return None

    
    def handle_401(self, r, **kwargs):
        '''
        Takes the given response and tries digest-auth, if needed.

        :rtype: requests.Response
        '''
        if not  <= 400, r.status_code or 400, r.status_code < 500:
            pass
        
        return r
    # WARNING: Decompyle incomplete

    
    def __call__(self, r):
        self.init_per_thread_state()
        if self._thread_local.last_nonce:
            r.headers['Authorization'] = self.build_digest_header(r.method, r.url)
        
        try:
            self._thread_local.pos = r.body.tell()
        except AttributeError:
            self._thread_local.pos = None

        r.register_hook('response', self.handle_401)
        r.register_hook('response', self.handle_redirect)
        self._thread_local.num_401_calls = 1
        return r

    
    def __eq__(self, other):
        return all([
            self.username == getattr(other, 'username', None),
            self.password == getattr(other, 'password', None)])

    
    def __ne__(self, other):
        return not (self == other)
