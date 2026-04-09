# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connection.pyc (Python 3.11)

from __future__ import annotations
import datetime
import http.client as http
import logging
import os
import re
import socket
import sys
import threading
import typing
import warnings
from http.client import HTTPConnection as _HTTPConnection
from http.client import HTTPException
from http.client import ResponseNotReady
from socket import timeout as SocketTimeout
if typing.TYPE_CHECKING:
    from response import HTTPResponse
    from util.ssl_ import _TYPE_PEER_CERT_RET_DICT
    from util.ssltransport import SSLTransport
from _collections import HTTPHeaderDict
from http2 import probe as http2_probe
from util.response import assert_header_parsing
from util.timeout import _DEFAULT_TIMEOUT, _TYPE_TIMEOUT, Timeout
from util.util import to_str
from util.wait import wait_for_read

try:
    import ssl
    BaseSSLError = ssl.SSLError
except (ImportError, AttributeError):
    ssl = None
    
    class BaseSSLError(BaseException):
        pass


from _base_connection import _TYPE_BODY
from _base_connection import ProxyConfig
from _base_connection import _ResponseOptions
from _version import __version__
from exceptions import ConnectTimeoutError, HeaderParsingError, NameResolutionError, NewConnectionError, ProxyError, SystemTimeWarning
from util import SKIP_HEADER, SKIPPABLE_HEADERS, connection, ssl_
from util.request import body_to_chunks
from util.ssl_ import assert_fingerprint as _assert_fingerprint
from util.ssl_ import create_urllib3_context, is_ipaddress, resolve_cert_reqs, resolve_ssl_version, ssl_wrap_socket
from util.ssl_match_hostname import CertificateError, match_hostname
from util.url import Url
ConnectionError = ConnectionError
BrokenPipeError = BrokenPipeError
log = logging.getLogger(__name__)
port_by_scheme = {
    'http': 80,
    'https': 443 }
RECENT_DATE = datetime.date(2025, 1, 1)
_CONTAINS_CONTROL_CHAR_RE = re.compile("[^-!#$%&'*+.^_`|~0-9a-zA-Z]")

class HTTPConnection(_HTTPConnection):
    pass
# WARNING: Decompyle incomplete


class HTTPSConnection(HTTPConnection):
    pass
# WARNING: Decompyle incomplete


class _WrappedAndVerifiedSocket(typing.NamedTuple):
    is_verified: 'bool' = '\n    Wrapped socket and whether the connection is\n    verified after the TLS handshake\n    '


def _ssl_wrap_socket_and_match_hostname(sock = None, *, cert_reqs, ssl_version, ssl_minimum_version, ssl_maximum_version, cert_file, key_file, key_password, ca_certs, ca_cert_dir, ca_cert_data, assert_hostname, assert_fingerprint, server_hostname, ssl_context, tls_in_tls):
    '''Logic for constructing an SSLContext from all TLS parameters, passing
    that down into ssl_wrap_socket, and then doing certificate verification
    either via hostname or fingerprint. This function exists to guarantee
    that both proxies and targets have the same behavior when connecting via TLS.
    '''
    default_ssl_context = False
# WARNING: Decompyle incomplete


def _match_hostname(cert = None, asserted_hostname = None, hostname_checks_common_name = None):
    stripped_hostname = asserted_hostname.strip('[]')
    if is_ipaddress(stripped_hostname):
        asserted_hostname = stripped_hostname
    
    try:
        match_hostname(cert, asserted_hostname, hostname_checks_common_name)
        return None
    except CertificateError:
        e = None
        log.warning('Certificate did not match expected hostname: %s. Certificate: %s', asserted_hostname, cert)
        e._peer_cert = cert
        raise 
        e = None
        del e



def _wrap_proxy_error(err = None, proxy_scheme = None):
    error_normalized = ' '.join(re.split('[^a-z]', str(err).lower()))
    if not 'wrong version number' in error_normalized:
        if not 'unknown protocol' in error_normalized:
            is_likely_http_proxy = 'record layer failure' in error_normalized
            http_proxy_warning = '. Your proxy appears to only use HTTP and not HTTPS, try changing your proxy URL to be HTTP. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#https-proxy-error-http-proxy'
    new_err = ProxyError(f'''Unable to connect to proxy{http_proxy_warning if is_likely_http_proxy and proxy_scheme == 'https' else ''}''', err)
    new_err.__cause__ = err
    return new_err


def _get_default_user_agent():
    return f'''python-urllib3/{__version__}'''


class DummyConnection:
    '''Used to detect a failed ConnectionCls import.'''
    pass

if not ssl:
    HTTPSConnection = DummyConnection
VerifiedHTTPSConnection = HTTPSConnection

def _url_from_connection(conn = None, path = None):
    '''Returns the URL from a given connection. This is mainly used for testing and logging.'''
    scheme = 'https' if isinstance(conn, HTTPSConnection) else 'http'
    return Url(scheme = scheme, host = conn.host, port = conn.port, path = path).url
