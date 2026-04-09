# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base_connection.pyc (Python 3.11)

from __future__ import annotations
import typing
from util.connection import _TYPE_SOCKET_OPTIONS
from util.timeout import _DEFAULT_TIMEOUT, _TYPE_TIMEOUT
from util.url import Url
_TYPE_BODY = typing.Union[(bytes, typing.IO[typing.Any], typing.Iterable[bytes], str)]

class ProxyConfig(typing.NamedTuple):
    assert_fingerprint: 'str | None' = 'ProxyConfig'


class _ResponseOptions(typing.NamedTuple):
    enforce_content_length: 'bool' = '_ResponseOptions'

if typing.TYPE_CHECKING:
    import ssl
    from typing import Protocol
    from response import BaseHTTPResponse
    
    class BaseHTTPConnection(Protocol):
        proxy_is_verified: 'bool | None' = 'BaseHTTPConnection'
        
        def __init__(self = None, host = None, port = None, *, timeout, source_address, blocksize, socket_options, proxy, proxy_config):
            pass

        
        def set_tunnel(self = None, host = None, port = None, headers = (None, None, 'http'), scheme = ('host', 'str', 'port', 'int | None', 'headers', 'typing.Mapping[str, str] | None', 'scheme', 'str', 'return', 'None')):
            pass

        
        def connect(self = None):
            pass

        
        def request(self = None, method = None, url = None, body = None, headers = (None, None), *, chunked, preload_content, decode_content, enforce_content_length):
            pass

        
        def getresponse(self = None):
            pass

        
        def close(self = None):
            pass

        is_closed = (lambda self = None: pass)()
        is_connected = (lambda self = None: pass)()
        has_connected_to_proxy = (lambda self = None: pass)()

    
    class BaseHTTPSConnection(Protocol, BaseHTTPConnection):
        key_password: 'str | None' = 'BaseHTTPSConnection'
        
        def __init__(self = None, host = None, port = None, *, timeout, source_address, blocksize, socket_options, proxy, proxy_config, cert_reqs, assert_hostname, assert_fingerprint, server_hostname, ssl_context, ca_certs, ca_cert_dir, ca_cert_data, ssl_minimum_version, ssl_maximum_version, ssl_version, cert_file, key_file, key_password):
            pass


    return None
