# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sessions.pyc (Python 3.11)

'''
requests.sessions
~~~~~~~~~~~~~~~~~

This module provides a Session object to manage and persist settings across
requests (cookies, auth, proxies).
'''
import os
import sys
import time
from collections import OrderedDict
from datetime import timedelta
from _internal_utils import to_native_string
from adapters import HTTPAdapter
from auth import _basic_auth_str
from compat import Mapping, cookielib, urljoin, urlparse
from cookies import RequestsCookieJar, cookiejar_from_dict, extract_cookies_to_jar, merge_cookies
from exceptions import ChunkedEncodingError, ContentDecodingError, InvalidSchema, TooManyRedirects
from hooks import default_hooks, dispatch_hook
from models import DEFAULT_REDIRECT_LIMIT, REDIRECT_STATI, PreparedRequest, Request
from status_codes import codes
from structures import CaseInsensitiveDict
from utils import DEFAULT_PORTS, default_headers, get_auth_from_url, get_environ_proxies, get_netrc_auth, requote_uri, resolve_proxies, rewind_body, should_bypass_proxies, to_key_val_list
if sys.platform == 'win32':
    preferred_clock = time.perf_counter
else:
    preferred_clock = time.time

def merge_setting(request_setting, session_setting, dict_class = (OrderedDict,)):
    '''Determines appropriate setting for a given request, taking into account
    the explicit setting on that request, and the setting in the session. If a
    setting is a dictionary, they will be merged together using `dict_class`
    '''
    pass
# WARNING: Decompyle incomplete


def merge_hooks(request_hooks, session_hooks, dict_class = (OrderedDict,)):
    """Properly merges both requests and session hooks.

    This is necessary because when request_hooks == {'response': []}, the
    merge breaks Session hooks entirely.
    """
    pass
# WARNING: Decompyle incomplete


class SessionRedirectMixin:
    
    def get_redirect_target(self, resp):
        '''Receives a Response. Returns a redirect URI or ``None``'''
        if resp.is_redirect:
            location = resp.headers['location']
            location = location.encode('latin1')
            return to_native_string(location, 'utf8')

    
    def should_strip_auth(self, old_url, new_url):
