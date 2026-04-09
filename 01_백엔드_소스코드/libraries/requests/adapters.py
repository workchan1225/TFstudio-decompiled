# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: adapters.pyc (Python 3.11)

'''
requests.adapters
~~~~~~~~~~~~~~~~~

This module contains the transport adapters that Requests uses to define
and maintain connections.
'''
import os.path as os
import socket
from urllib3.exceptions import ClosedPoolError, ConnectTimeoutError
from urllib3.exceptions import HTTPError as _HTTPError
from urllib3.exceptions import InvalidHeader as _InvalidHeader
from urllib3.exceptions import LocationValueError, MaxRetryError, NewConnectionError, ProtocolError
from urllib3.exceptions import ProxyError as _ProxyError
from urllib3.exceptions import ReadTimeoutError, ResponseError
from urllib3.exceptions import SSLError as _SSLError
from urllib3.poolmanager import PoolManager, proxy_from_url
from urllib3.util import Timeout as TimeoutSauce
from urllib3.util import parse_url
from urllib3.util.retry import Retry
from auth import _basic_auth_str
from compat import basestring, urlparse
from cookies import extract_cookies_to_jar
from exceptions import ConnectionError, ConnectTimeout, InvalidHeader, InvalidProxyURL, InvalidSchema, InvalidURL, ProxyError, ReadTimeout, RetryError, SSLError
from models import Response
from structures import CaseInsensitiveDict
from utils import DEFAULT_CA_BUNDLE_PATH, extract_zipped_paths, get_auth_from_url, get_encoding_from_headers, prepend_scheme_if_needed, select_proxy, urldefragauth

try:
    from urllib3.contrib.socks import SOCKSProxyManager
except ImportError:
    
    def SOCKSProxyManager(*args, **kwargs):
        raise InvalidSchema('Missing dependencies for SOCKS support.')


DEFAULT_POOLBLOCK = False
DEFAULT_POOLSIZE = 10
DEFAULT_RETRIES = 0
DEFAULT_POOL_TIMEOUT = None

class BaseAdapter:
    pass
# WARNING: Decompyle incomplete


class HTTPAdapter(BaseAdapter):
    pass
# WARNING: Decompyle incomplete
