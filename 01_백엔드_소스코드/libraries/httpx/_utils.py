# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _utils.pyc (Python 3.11)

from __future__ import annotations
import ipaddress
import os
import re
import typing
from urllib.request import getproxies
from _types import PrimitiveData
if typing.TYPE_CHECKING:
    from _urls import URL

def primitive_value_to_str(value = None):
    """
    Coerce a primitive data type into a string value.

    Note that we prefer JSON-style 'true'/'false' for boolean values here.
    """
    if value is True:
        return 'true'
    if None is False:
        return 'false'
# WARNING: Decompyle incomplete


def get_environment_proxies():
    '''Gets proxy information from the environment'''
    proxy_info = getproxies()
    mounts = { }
    for scheme in ('http', 'https', 'all'):
        if proxy_info.get(scheme):
            hostname = proxy_info[scheme]
            mounts[f'''{scheme}://'''] = hostname if '://' in hostname else f'''http://{hostname}'''
        no_proxy_hosts = proxy_info.get('no', '').split(',')()
        for hostname in no_proxy_hosts:
            if hostname == '*':
                
                return (lambda .0: [ host.strip() for host in .0 ]), { }
            if (lambda .0: [ host.strip() for host in .0 ]):
                if '://' in hostname:
                    continue
                if is_ipv4_hostname(hostname):
                    None = None
                    continue
                if is_ipv6_hostname(hostname):
                    mounts[f'''all://[{hostname}]'''] = None
                    continue
                if hostname.lower() == 'localhost':
                    mounts[f'''all://{hostname}'''] = None
                    continue
                mounts[f'''all://*{hostname}'''] = None
            return mounts


def to_bytes(value = None, encoding = None):
    return value.encode(encoding) if isinstance(value, str) else value


def to_str(value = None, encoding = None):
    return value if isinstance(value, str) else value.decode(encoding)


def to_bytes_or_str(value = None, match_type_of = None):
    return value if isinstance(match_type_of, str) else value.encode()


def unquote(value = None):
    if  == value[0], value[-1] or value[0], value[-1] == '"':
        pass
    
    return value


def peek_filelike_length(stream = None):
    '''
    Given a file-like stream object, return its length in number of bytes
    without reading it into memory.
    '''
    
    try:
        fd = stream.fileno()
        length = os.fstat(fd).st_size
    except (AttributeError, OSError):
        offset = stream.tell()
        length = stream.seek(0, os.SEEK_END)
        stream.seek(offset)
    except (AttributeError, OSError):
        return None

    return length


class URLPattern:
    '''
    A utility class currently used for making lookups against proxy keys...

    # Wildcard matching...
    >>> pattern = URLPattern("all://")
    >>> pattern.matches(httpx.URL("http://example.com"))
    True

    # Witch scheme matching...
    >>> pattern = URLPattern("https://")
    >>> pattern.matches(httpx.URL("https://example.com"))
    True
    >>> pattern.matches(httpx.URL("http://example.com"))
    False

    # With domain matching...
    >>> pattern = URLPattern("https://example.com")
    >>> pattern.matches(httpx.URL("https://example.com"))
    True
    >>> pattern.matches(httpx.URL("http://example.com"))
    False
    >>> pattern.matches(httpx.URL("https://other.com"))
    False

    # Wildcard scheme, with domain matching...
    >>> pattern = URLPattern("all://example.com")
    >>> pattern.matches(httpx.URL("https://example.com"))
    True
    >>> pattern.matches(httpx.URL("http://example.com"))
    True
    >>> pattern.matches(httpx.URL("https://other.com"))
    False

    # With port matching...
    >>> pattern = URLPattern("https://example.com:1234")
    >>> pattern.matches(httpx.URL("https://example.com:1234"))
    True
    >>> pattern.matches(httpx.URL("https://example.com"))
    False
    '''
    
    def __init__(self = None, pattern = None):
        URL = URL
        import _urls
        if pattern and ':' not in pattern:
            raise ValueError(f'''Proxy keys should use proper URL forms rather than plain scheme strings. Instead of "{pattern}", use "{pattern}://"''')
        url = URL(pattern)
        self.pattern = pattern
        self.scheme = '' if url.scheme == 'all' else url.scheme
        self.host = '' if url.host == '*' else url.host
        self.port = url.port
        if url.host or url.host == '*':
            self.host_regex = None
            return None
        if None.host.startswith('*.'):
            domain = re.escape(url.host[2:])
            self.host_regex = re.compile(f'''^.+\\.{domain}$''')
            return None
        if None.host.startswith('*'):
            domain = re.escape(url.host[1:])
            self.host_regex = re.compile(f'''^(.+\\.)?{domain}$''')
            return None
        domain = None.escape(url.host)
        self.host_regex = re.compile(f'''^{domain}$''')

    
    def matches(self = None, other = None):
        if self.scheme and self.scheme != other.scheme:
            return False
    # WARNING: Decompyle incomplete

    priority = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __hash__(self = None):
        return hash(self.pattern)

    
    def __lt__(self = None, other = None):
        return self.priority < other.priority

    
    def __eq__(self = None, other = None):
