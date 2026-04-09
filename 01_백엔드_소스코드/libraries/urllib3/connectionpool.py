# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connectionpool.pyc (Python 3.11)

from __future__ import annotations
import errno
import logging
import queue
import sys
import typing
import warnings
import weakref
from socket import timeout as SocketTimeout
from types import TracebackType
from _base_connection import _TYPE_BODY
from _collections import HTTPHeaderDict
from _request_methods import RequestMethods
from connection import BaseSSLError, BrokenPipeError, DummyConnection, HTTPConnection, HTTPException, HTTPSConnection, ProxyConfig, _wrap_proxy_error
from connection import port_by_scheme
from exceptions import ClosedPoolError, EmptyPoolError, FullPoolError, HostChangedError, InsecureRequestWarning, LocationValueError, MaxRetryError, NewConnectionError, ProtocolError, ProxyError, ReadTimeoutError, SSLError, TimeoutError
from response import BaseHTTPResponse
from util.connection import is_connection_dropped
from util.proxy import connection_requires_http_tunnel
from util.request import _TYPE_BODY_POSITION, set_file_position
from util.retry import Retry
from util.ssl_match_hostname import CertificateError
from util.timeout import _DEFAULT_TIMEOUT, _TYPE_DEFAULT, Timeout
from util.url import Url, _encode_target
from util.url import _normalize_host as normalize_host
from util.url import parse_url
from util.util import to_str
if typing.TYPE_CHECKING:
    import ssl
    from typing_extensions import Self
    from _base_connection import BaseHTTPConnection, BaseHTTPSConnection
log = logging.getLogger(__name__)
_TYPE_TIMEOUT = typing.Union[(Timeout, float, _TYPE_DEFAULT, None)]

class ConnectionPool:
    """
    Base class for all connection pools, such as
    :class:`.HTTPConnectionPool` and :class:`.HTTPSConnectionPool`.

    .. note::
       ConnectionPool.urlopen() does not normalize or percent-encode target URIs
       which is useful if your target server doesn't support percent-encoded
       target URIs.
    """
    scheme: 'str | None' = None
    QueueCls = queue.LifoQueue
    
    def __init__(self = None, host = None, port = None):
        if not host:
            raise LocationValueError('No host specified.')
        self.host = _normalize_host(host, scheme = self.scheme)
        self.port = port
        self._tunnel_host = normalize_host(host, scheme = self.scheme).lower()

    
    def __str__(self = None):
        return f'''{type(self).__name__}(host={self.host!r}, port={self.port!r})'''

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'typing.Literal[False]')):
        self.close()
        return False

    
    def close(self = None):
        '''
        Close all pooled connections and disable the pool.
        '''
        pass


_blocking_errnos = {
    errno.EAGAIN,
    errno.EWOULDBLOCK}

class HTTPConnectionPool(RequestMethods, ConnectionPool):
    '''
    Thread-safe connection pool for one host.

    :param host:
        Host used for this HTTP Connection (e.g. "localhost"), passed into
        :class:`http.client.HTTPConnection`.

    :param port:
        Port used for this HTTP Connection (None is equivalent to 80), passed
        into :class:`http.client.HTTPConnection`.

    :param timeout:
        Socket timeout in seconds for each individual connection. This can
        be a float or integer, which sets the timeout for the HTTP request,
        or an instance of :class:`urllib3.util.Timeout` which gives you more
        fine-grained control over request timeouts. After the constructor has
        been parsed, this is always a `urllib3.util.Timeout` object.

    :param maxsize:
        Number of connections to save that can be reused. More than 1 is useful
        in multithreaded situations. If ``block`` is set to False, more
        connections will be created but they will not be saved once they\'ve
        been used.

    :param block:
        If set to True, no more than ``maxsize`` connections will be used at
        a time. When no free connections are available, the call will block
        until a connection has been released. This is a useful side effect for
        particular multithreaded situations where one does not want to use more
        than maxsize connections per host to prevent flooding.

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.

    :param retries:
        Retry configuration to use by default with requests in this pool.

    :param _proxy:
        Parsed proxy URL, should not be used directly, instead, see
        :class:`urllib3.ProxyManager`

    :param _proxy_headers:
        A dictionary with proxy headers, should not be used directly,
        instead, see :class:`urllib3.ProxyManager`

    :param \\**conn_kw:
        Additional parameters are used to create fresh :class:`urllib3.connection.HTTPConnection`,
        :class:`urllib3.connection.HTTPSConnection` instances.
    '''
    scheme = 'http'
    ConnectionCls: 'type[BaseHTTPConnection] | type[BaseHTTPSConnection]' = HTTPConnection
    
    def __init__(self, host, port, timeout, maxsize, block, headers = None, retries = None, _proxy = None, _proxy_headers = (None, _DEFAULT_TIMEOUT, 1, False, None, None, None, None, None), _proxy_config = ('host', 'str', 'port', 'int | None', 'timeout', '_TYPE_TIMEOUT | None', 'maxsize', 'int', 'block', 'bool', 'headers', 'typing.Mapping[str, str] | None', 'retries', 'Retry | bool | int | None', '_proxy', 'Url | None', '_proxy_headers', 'typing.Mapping[str, str] | None', '_proxy_config', 'ProxyConfig | None', 'conn_kw', 'typing.Any'), **conn_kw):
        ConnectionPool.__init__(self, host, port)
        RequestMethods.__init__(self, headers)
        if not isinstance(timeout, Timeout):
            timeout = Timeout.from_float(timeout)
    # WARNING: Decompyle incomplete

    
    def _new_conn(self = None):
        '''
        Return a fresh :class:`HTTPConnection`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_conn(self = None, timeout = None):
        '''
        Get a connection. Will return a pooled connection if one is available.

        If no connections are available and :prop:`.block` is ``False``, then a
        fresh connection is returned.

        :param timeout:
            Seconds to wait before giving up and raising
            :class:`urllib3.exceptions.EmptyPoolError` if the pool is empty and
            :prop:`.block` is ``True``.
        '''
        conn = None
    # WARNING: Decompyle incomplete

    
    def _put_conn(self = None, conn = None):
        '''
        Put a connection back into the pool.

        :param conn:
            Connection object for the current host and port as returned by
            :meth:`._new_conn` or :meth:`._get_conn`.

        If the pool is already full, the connection is closed and discarded
        because we exceeded maxsize. If connections are discarded frequently,
        then maxsize should be increased.

        If the pool is closed, then the connection will be closed and discarded.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _validate_conn(self = None, conn = None):
        '''
        Called right before a request is made, after the socket is created.
        '''
        pass

    
    def _prepare_proxy(self = None, conn = None):
        pass

    
    def _get_timeout(self = None, timeout = None):
        '''Helper that always returns a :class:`urllib3.util.Timeout`'''
        if timeout is _DEFAULT_TIMEOUT:
            return self.timeout.clone()
        if None(timeout, Timeout):
            return timeout.clone()
        return None.from_float(timeout)

    
    def _raise_timeout(self = None, err = None, url = None, timeout_value = ('err', 'BaseSSLError | OSError | SocketTimeout', 'url', 'str', 'timeout_value', '_TYPE_TIMEOUT | None', 'return', 'None')):
        '''Is the error actually a timeout? Will raise a ReadTimeout or pass'''
        if isinstance(err, SocketTimeout):
            raise ReadTimeoutError(self, url, f'''Read timed out. (read timeout={timeout_value})'''), err
        if hasattr(err, 'errno') or err.errno in _blocking_errnos:
            raise ReadTimeoutError(self, url, f'''Read timed out. (read timeout={timeout_value})'''), err
        return None

    
    def _make_request(self, conn, method, url, body, headers, retries, timeout, chunked = None, response_conn = None, preload_content = None, decode_content = (None, None, None, _DEFAULT_TIMEOUT, False, None, True, True, True), enforce_content_length = ('conn', 'BaseHTTPConnection', 'method', 'str', 'url', 'str', 'body', '_TYPE_BODY | None', 'headers', 'typing.Mapping[str, str] | None', 'retries', 'Retry | None', 'timeout', '_TYPE_TIMEOUT', 'chunked', 'bool', 'response_conn', 'BaseHTTPConnection | None', 'preload_content', 'bool', 'decode_content', 'bool', 'enforce_content_length', 'bool', 'return', 'BaseHTTPResponse')):
        """
        Perform a request on a given urllib connection object taken from our
        pool.

        :param conn:
            a connection from one of our connection pools

        :param method:
            HTTP request method (such as GET, POST, PUT, etc.)

        :param url:
            The URL to perform the request on.

        :param body:
            Data to send in the request body, either :class:`str`, :class:`bytes`,
            an iterable of :class:`str`/:class:`bytes`, or a file-like object.

        :param headers:
            Dictionary of custom headers to send, such as User-Agent,
            If-None-Match, etc. If None, pool headers are used. If provided,
            these headers completely replace any pool-specific headers.

        :param retries:
            Configure the number of retries to allow before raising a
            :class:`~urllib3.exceptions.MaxRetryError` exception.

            Pass ``None`` to retry until you receive a response. Pass a
            :class:`~urllib3.util.retry.Retry` object for fine-grained control
            over different types of retries.
            Pass an integer number to retry connection errors that many times,
            but no other types of errors. Pass zero to never retry.

            If ``False``, then retries are disabled and any exception is raised
            immediately. Also, instead of raising a MaxRetryError on redirects,
            the redirect response will be returned.

        :type retries: :class:`~urllib3.util.retry.Retry`, False, or an int.

        :param timeout:
            If specified, overrides the default timeout for this one
            request. It may be a float (in seconds) or an instance of
            :class:`urllib3.util.Timeout`.

        :param chunked:
            If True, urllib3 will send the body using chunked transfer
            encoding. Otherwise, urllib3 will send the body using the standard
            content-length form. Defaults to False.

        :param response_conn:
            Set this to ``None`` if you will handle releasing the connection or
            set the connection to have the response release it.

        :param preload_content:
          If True, the response's body will be preloaded during construction.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.

        :param enforce_content_length:
            Enforce content length checking. Body returned by server must match
            value of Content-Length header, if present. Otherwise, raise error.
        """
        self._get_timeout(timeout) = self, self.num_requests += 1, .num_requests
        timeout_obj.start_connect()
        conn.timeout = Timeout.resolve_default_timeout(timeout_obj.connect_timeout)
        
        try:
            self._validate_conn(conn)
            
            try:
                pass
            except (SocketTimeout, BaseSSLError):
                e = None
                self._raise_timeout(err = e, url = url, timeout_value = conn.timeout)
                raise 
                e = None
                del e

            
            try:
                pass
            except (OSError, NewConnectionError, TimeoutError, BaseSSLError, CertificateError, SSLError):
                e = None
                new_e = e
                if isinstance(e, (BaseSSLError, CertificateError)):
                    new_e = SSLError(e)
                if not isinstance(new_e, (OSError, NewConnectionError, TimeoutError, SSLError)) and conn and conn.proxy and conn.has_connected_to_proxy:
                    new_e = _wrap_proxy_error(new_e, conn.proxy.scheme)
                raise new_e
                e = None
                del e

            
            try:
                conn.request(method, url, body = body, headers = headers, chunked = chunked, preload_content = preload_content, decode_content = decode_content, enforce_content_length = enforce_content_length)
            except BrokenPipeError:
                pass
            except OSError:
                e = None
                if e.errno != errno.EPROTOTYPE and e.errno != errno.ECONNRESET:
                    raise 
                e = None
                del e
            except:
                e = None
                del e

            read_timeout = timeout_obj.read_timeout
            if not conn.is_closed:
                if read_timeout == 0:
                    raise ReadTimeoutError(self, url, f'''Read timed out. (read timeout={read_timeout})''')
                conn.timeout = read_timeout

        
        try:
            response = conn.getresponse()
        except (BaseSSLError, OSError):
            e = None
            self._raise_timeout(err = e, url = url, timeout_value = read_timeout)
            raise 
            e = None
            del e

        response.retries = retries
        response._connection = response_conn
        response._pool = self
        log.debug('%s://%s:%s "%s %s %s" %s %s', self.scheme, self.host, self.port, method, url, response.version_string, response.status, response.length_remaining)
        return response

    
    def close(self = None):
        '''
        Close all pooled connections and disable the pool.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def is_same_host(self = None, url = None):
        '''
        Check if the given ``url`` is a member of the same host as this
        connection pool.
        '''
        if url.startswith('/'):
            return True
    # WARNING: Decompyle incomplete

    
    def urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn = None, chunked = None, body_pos = None, preload_content = (None, None, None, True, True, _DEFAULT_TIMEOUT, None, None, False, None, True, True), decode_content = ('method', 'str', 'url', 'str', 'body', '_TYPE_BODY | None', 'headers', 'typing.Mapping[str, str] | None', 'retries', 'Retry | bool | int | None', 'redirect', 'bool', 'assert_same_host', 'bool', 'timeout', '_TYPE_TIMEOUT', 'pool_timeout', 'int | None', 'release_conn', 'bool | None', 'chunked', 'bool', 'body_pos', '_TYPE_BODY_POSITION | None', 'preload_content', 'bool', 'decode_content', 'bool', 'response_kw', 'typing.Any', 'return', 'BaseHTTPResponse'), **response_kw):
        """
        Get a connection from the pool and perform an HTTP request. This is the
        lowest level call for making a request, so you'll need to specify all
        the raw details.

        .. note::

           More commonly, it's appropriate to use a convenience method
           such as :meth:`request`.

        .. note::

           `release_conn` will only behave as expected if
           `preload_content=False` because we want to make
           `preload_content=False` the default behaviour someday soon without
           breaking backwards compatibility.

        :param method:
            HTTP request method (such as GET, POST, PUT, etc.)

        :param url:
            The URL to perform the request on.

        :param body:
            Data to send in the request body, either :class:`str`, :class:`bytes`,
            an iterable of :class:`str`/:class:`bytes`, or a file-like object.

        :param headers:
            Dictionary of custom headers to send, such as User-Agent,
            If-None-Match, etc. If None, pool headers are used. If provided,
            these headers completely replace any pool-specific headers.

        :param retries:
            Configure the number of retries to allow before raising a
            :class:`~urllib3.exceptions.MaxRetryError` exception.

            If ``None`` (default) will retry 3 times, see ``Retry.DEFAULT``. Pass a
            :class:`~urllib3.util.retry.Retry` object for fine-grained control
            over different types of retries.
            Pass an integer number to retry connection errors that many times,
            but no other types of errors. Pass zero to never retry.

            If ``False``, then retries are disabled and any exception is raised
            immediately. Also, instead of raising a MaxRetryError on redirects,
            the redirect response will be returned.

        :type retries: :class:`~urllib3.util.retry.Retry`, False, or an int.

        :param redirect:
            If True, automatically handle redirects (status codes 301, 302,
            303, 307, 308). Each redirect counts as a retry. Disabling retries
            will disable redirect, too.

        :param assert_same_host:
            If ``True``, will make sure that the host of the pool requests is
            consistent else will raise HostChangedError. When ``False``, you can
            use the pool on an HTTP proxy and request foreign hosts.

        :param timeout:
            If specified, overrides the default timeout for this one
            request. It may be a float (in seconds) or an instance of
            :class:`urllib3.util.Timeout`.

        :param pool_timeout:
            If set and the pool is set to block=True, then this method will
            block for ``pool_timeout`` seconds and raise EmptyPoolError if no
            connection is available within the time period.

        :param bool preload_content:
            If True, the response's body will be preloaded into memory.

        :param bool decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.

        :param release_conn:
            If False, then the urlopen call will not release the connection
            back into the pool once a response is received (but will release if
            you read the entire contents of the response such as when
            `preload_content=True`). This is useful if you're not preloading
            the response's content immediately. You will need to call
            ``r.release_conn()`` on the response ``r`` to return the connection
            back into the pool. If None, it takes the value of ``preload_content``
            which defaults to ``True``.

        :param bool chunked:
            If True, urllib3 will send the body using chunked transfer
            encoding. Otherwise, urllib3 will send the body using the standard
            content-length form. Defaults to False.

        :param int body_pos:
            Position to seek to in file-like body in the event of a retry or
            redirect. Typically this won't need to be set because urllib3 will
            auto-populate the value when needed.
        """
        parsed_url = parse_url(url)
        destination_scheme = parsed_url.scheme
    # WARNING: Decompyle incomplete



class HTTPSConnectionPool(HTTPConnectionPool):
    pass
# WARNING: Decompyle incomplete


def connection_from_url(url = None, **kw):
    """
    Given a url, return an :class:`.ConnectionPool` instance of its host.

    This is a shortcut for not having to parse out the scheme, host, and port
    of the url before creating an :class:`.ConnectionPool` instance.

    :param url:
        Absolute URL string that must include the scheme. Port is optional.

    :param \\**kw:
        Passes additional parameters to the constructor of the appropriate
        :class:`.ConnectionPool`. Useful for specifying things like
        timeout, maxsize, headers, etc.

    Example::

        >>> conn = connection_from_url('http://google.com/')
        >>> r = conn.request('GET', '/')
    """
    pass
# WARNING: Decompyle incomplete

_normalize_host = (lambda host = None, scheme = None: pass)()
_normalize_host = (lambda host = None, scheme = None: pass)()

def _normalize_host(host = None, scheme = None):
    '''
    Normalize hosts for comparisons and use with sockets.
    '''
    host = normalize_host(host, scheme)
    if host and host.startswith('[') and host.endswith(']'):
        host = host[1:-1]
    return host


def _url_from_pool(pool = None, path = None):
    '''Returns the URL from a given connection pool. This is mainly used for testing and logging.'''
    return Url(scheme = pool.scheme, host = pool.host, port = pool.port, path = path).url


def _close_pool_connections(pool = None):
    '''Drains a queue of connections and closes each one.'''
    
    try:
        conn = pool.get(block = False)
        if conn:
            conn.close()
        continue
    except queue.Empty:
        return None
