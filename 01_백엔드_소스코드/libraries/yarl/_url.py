# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _url.pyc (Python 3.11)

import re
import sys
import warnings
from collections.abc import Mapping, Sequence
from enum import Enum
from functools import _CacheInfo, lru_cache
from ipaddress import ip_address
from typing import TYPE_CHECKING, Any, NoReturn, TypedDict, TypeVar, Union, cast, overload
from urllib.parse import SplitResult, uses_relative
import idna
from multidict import MultiDict, MultiDictProxy, istr
from propcache.api import under_cached_property as cached_property
from _parse import USES_AUTHORITY, SplitURLType, make_netloc, query_to_pairs, split_netloc, split_url, unsplit_result
from _path import normalize_path, normalize_path_segments
from _query import Query, QueryVariable, SimpleQuery, get_str_query, get_str_query_from_iterable, get_str_query_from_sequence_iterable
from _quoters import FRAGMENT_QUOTER, FRAGMENT_REQUOTER, PATH_QUOTER, PATH_REQUOTER, PATH_SAFE_UNQUOTER, PATH_UNQUOTER, QS_UNQUOTER, QUERY_QUOTER, QUERY_REQUOTER, QUOTER, REQUOTER, UNQUOTER, human_quote
DEFAULT_PORTS = {
    'http': 80,
    'https': 443,
    'ws': 80,
    'wss': 443,
    'ftp': 21 }
USES_RELATIVE = frozenset(uses_relative)
SCHEME_REQUIRES_HOST = frozenset(('http', 'https', 'ws', 'wss', 'ftp'))
NOT_REG_NAME = re.compile("\n        # any character not in the unreserved or sub-delims sets, plus %\n        # (validated with the additional check for pct-encoded sequences below)\n        [^a-z0-9\\-._~!$&'()*+,;=%]\n    |\n        # % only allowed if it is part of a pct-encoded\n        # sequence of 2 hex digits.\n        %(?![0-9a-f]{2})\n    ", re.VERBOSE)
_T = TypeVar('_T')
if sys.version_info >= (3, 11):
    from typing import Self
else:
    Self = Any

class UndefinedType(Enum):
    '''Singleton type for use with not set sentinel values.'''
    _singleton = 0

UNDEFINED = UndefinedType._singleton

class CacheInfo(TypedDict):
    encode_host: _CacheInfo = 'Host encoding cache.'


def _InternalURLCache():
    '''_InternalURLCache'''
    suffixes: tuple[(str, ...)] = '_InternalURLCache'

_InternalURLCache = <NODE:27>(_InternalURLCache, '_InternalURLCache', TypedDict, total = False)

def rewrite_module(obj = None):
    obj.__module__ = 'yarl'
    return obj

encode_url = (lambda url_str = None: cache = { }(scheme, netloc, path, query, fragment) = split_url(url_str)if not netloc:
host = ''elif ':' in netloc and '@' in netloc or '[' in netloc:
(username, password, host, port) = split_netloc(netloc)else:
username = Nonepassword = Noneport = Nonehost = netloc# WARNING: Decompyle incomplete
)()
pre_encoded_url = (lambda url_str = None: self = object.__new__(URL)val = split_url(url_str)(self._scheme, self._netloc, self._path, self._query, self._fragment) = valself._cache = { }self)()
build_pre_encoded_url = (lambda scheme, authority, user, password, host, port = None, path = None, query_string = lru_cache, fragment = ('scheme', str, 'authority', str, 'user', Union[(str, None)], 'password', Union[(str, None)], 'host', str, 'port', Union[(int, None)], 'path', str, 'query_string', str, 'fragment', str, 'return', 'URL'): self = object.__new__(URL)self._scheme = schemeif authority:
self._netloc = authority# WARNING: Decompyle incomplete
)()

def from_parts_uncached(scheme, netloc = None, path = None, query = None, fragment = ('scheme', str, 'netloc', str, 'path', str, 'query', str, 'fragment', str, 'return', 'URL')):
    '''Create a new URL from parts.'''
    self = object.__new__(URL)
    self._scheme = scheme
    self._netloc = netloc
    self._path = path
    self._query = query
    self._fragment = fragment
    self._cache = { }
    return self

from_parts = lru_cache(from_parts_uncached)
URL = <NODE:12>()
_DEFAULT_IDNA_SIZE = 256
_DEFAULT_ENCODE_SIZE = 512
_idna_decode = (lambda raw = None: try:
idna.decode(raw.encode('ascii'))except UnicodeError:
)()
_idna_encode = (lambda host = None: try:
idna.encode(host, uts46 = True).decode('ascii')except UnicodeError:
)()
_encode_host = (lambda host = None, validate_host = None:
