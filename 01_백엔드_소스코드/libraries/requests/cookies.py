# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cookies.pyc (Python 3.11)

'''
requests.cookies
~~~~~~~~~~~~~~~~

Compatibility code to be able to use `cookielib.CookieJar` with requests.

requests.utils imports from here, so be careful with imports.
'''
import calendar
import copy
import time
from _internal_utils import to_native_string
from compat import Morsel, MutableMapping, cookielib, urlparse, urlunparse

try:
    import threading
except ImportError:
    import dummy_threading as threading


class MockRequest:
    '''Wraps a `requests.Request` to mimic a `urllib2.Request`.

    The code in `cookielib.CookieJar` expects this interface in order to correctly
    manage cookie policies, i.e., determine whether a cookie can be set, given the
    domains of the request and the cookie.

    The original request object is read-only. The client is responsible for collecting
    the new headers via `get_new_headers()` and interpreting them appropriately. You
    probably want `get_cookie_header`, defined below.
    '''
    
    def __init__(self, request):
        self._r = request
        self._new_headers = { }
        self.type = urlparse(self._r.url).scheme

    
    def get_type(self):
        return self.type

    
    def get_host(self):
        return urlparse(self._r.url).netloc

    
    def get_origin_req_host(self):
        return self.get_host()

    
    def get_full_url(self):
        if not self._r.headers.get('Host'):
            return self._r.url
        host = None(self._r.headers['Host'], encoding = 'utf-8')
        parsed = urlparse(self._r.url)
        return urlunparse([
            parsed.scheme,
            host,
            parsed.path,
            parsed.params,
            parsed.query,
            parsed.fragment])

    
    def is_unverifiable(self):
        return True

    
    def has_header(self, name):
