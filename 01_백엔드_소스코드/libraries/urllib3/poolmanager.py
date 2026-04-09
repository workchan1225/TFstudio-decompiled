# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: poolmanager.pyc (Python 3.11)

from __future__ import annotations
import functools
import logging
import typing
import warnings
from types import TracebackType
from urllib.parse import urljoin
from _collections import HTTPHeaderDict, RecentlyUsedContainer
from _request_methods import RequestMethods
from connection import ProxyConfig
from connectionpool import HTTPConnectionPool, HTTPSConnectionPool, port_by_scheme
from exceptions import LocationValueError, MaxRetryError, ProxySchemeUnknown, URLSchemeUnknown
from response import BaseHTTPResponse
from util.connection import _TYPE_SOCKET_OPTIONS
from util.proxy import connection_requires_http_tunnel
from util.retry import Retry
from util.timeout import Timeout
from util.url import Url, parse_url
if typing.TYPE_CHECKING:
    import ssl
    from typing_extensions import Self
__all__ = [
    'PoolManager',
    'ProxyManager',
    'proxy_from_url']
log = logging.getLogger(__name__)
SSL_KEYWORDS = ('key_file', 'cert_file', 'cert_reqs', 'ca_certs', 'ca_cert_data', 'ssl_version', 'ssl_minimum_version', 'ssl_maximum_version', 'ca_cert_dir', 'ssl_context', 'key_password', 'server_hostname')
_DEFAULT_BLOCKSIZE = 16384

class PoolKey(typing.NamedTuple):
    key_blocksize: 'int | None' = '\n    All known keyword arguments that could be provided to the pool manager, its\n    pools, or the underlying connections.\n\n    All custom key schemes should include the fields in this key at a minimum.\n    '


def _default_key_normalizer(key_class = None, request_context = None):
    '''
    Create a pool key out of a request context dictionary.

    According to RFC 3986, both the scheme and host are case-insensitive.
    Therefore, this function normalizes both before constructing the pool
    key for an HTTPS request. If you wish to change this behaviour, provide
    alternate callables to ``key_fn_by_scheme``.

    :param key_class:
        The class to use when constructing the key. This should be a namedtuple
        with the ``scheme`` and ``host`` keys at a minimum.
    :type  key_class: namedtuple
    :param request_context:
        A dictionary-like object that contain the context for a request.
    :type  request_context: dict

    :return: A namedtuple that can be used as a connection pool key.
    :rtype:  PoolKey
    '''
    context = request_context.copy()
    context['scheme'] = context['scheme'].lower()
    context['host'] = context['host'].lower()
# WARNING: Decompyle incomplete

key_fn_by_scheme = {
    'http': functools.partial(_default_key_normalizer, PoolKey),
    'https': functools.partial(_default_key_normalizer, PoolKey) }
pool_classes_by_scheme = {
    'http': HTTPConnectionPool,
    'https': HTTPSConnectionPool }

class PoolManager(RequestMethods):
    pass
# WARNING: Decompyle incomplete


class ProxyManager(PoolManager):
    pass
# WARNING: Decompyle incomplete


def proxy_from_url(url = None, **kw):
    pass
# WARNING: Decompyle incomplete
