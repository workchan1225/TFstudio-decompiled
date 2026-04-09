# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: serving.pyc (Python 3.11)

'''A WSGI and HTTP server for use **during development only**. This
server is convenient to use, but is not designed to be particularly
stable, secure, or efficient. Use a dedicate WSGI server and HTTP
server when deploying to production.

It provides features like interactive debugging and code reloading. Use
``run_simple`` to start the server. Put this in a ``run.py`` script:

.. code-block:: python

    from myapp import create_app
    from werkzeug import run_simple
'''
from __future__ import annotations
import errno
import io
import os
import selectors
import socket
import socketserver
import sys
import typing as t
from datetime import datetime as dt
from datetime import timedelta
from datetime import timezone
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import unquote
from urllib.parse import urlsplit
from _internal import _log
from _internal import _wsgi_encoding_dance
from exceptions import InternalServerError
from urls import uri_to_iri

try:
    import ssl
    connection_dropped_errors: 'tuple[type[Exception], ...]' = (ConnectionError, socket.timeout, ssl.SSLEOFError)
except ImportError:
    
    class _SslDummy:
        
        def __getattr__(self = None, name = None):
            raise RuntimeError('SSL is unavailable because this Python runtime was not compiled with SSL/TLS support.')


    ssl = _SslDummy()
    connection_dropped_errors = (ConnectionError, socket.timeout)

_log_add_style = True
if os.name == 'nt':
    
    try:
        __import__('colorama')
    except ImportError:
        _log_add_style = False

    can_fork = hasattr(os, 'fork')

try:
    af_unix = socket.AF_UNIX
except AttributeError:
    af_unix = None

LISTEN_QUEUE = 128
_TSSLContextArg = t.Optional[t.Union[('ssl.SSLContext', tuple[(str, t.Optional[str])], t.Literal['adhoc'])]]
if t.TYPE_CHECKING:
    from _typeshed.wsgi import WSGIApplication
    from _typeshed.wsgi import WSGIEnvironment
    from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKeyWithSerialization
    from cryptography.x509 import Certificate

class DechunkedInput(io.RawIOBase):
    """An input stream that handles Transfer-Encoding 'chunked'"""
    
    def __init__(self = None, rfile = None):
        self._rfile = rfile
        self._done = False
        self._len = 0

    
    def readable(self = None):
        return True

    
    def read_chunk_len(self = None):
        
        try:
            line = self._rfile.readline().decode('latin1')
            _len = int(line.strip(), 16)
        except ValueError:
            e = None
            raise OSError('Invalid chunk header'), e
            e = None
            del e

        if _len < 0:
            raise OSError('Negative chunk length not allowed')
        return _len

    
    def readinto(self = None, buf = None):
        read = 0
    # WARNING: Decompyle incomplete



class WSGIRequestHandler(BaseHTTPRequestHandler):
    pass
# WARNING: Decompyle incomplete


def _ansi_style(value = None if can_fork else None, *styles):
    if not _log_add_style:
        return value
    codes = {
        'bold': None,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'magenta': 35,
        'cyan': 36 }
    for style in styles:
        value = f'''\x1b[{codes[style]}m{value}'''
        return f'''{value}\x1b[0m'''


def generate_adhoc_ssl_pair(cn = None):
    
    try:
        x509 = x509
        import cryptography
        default_backend = default_backend
        import cryptography.hazmat.backends
        hashes = hashes
        import cryptography.hazmat.primitives
        rsa = rsa
        import cryptography.hazmat.primitives.asymmetric
        NameOID = NameOID
        import cryptography.x509.oid
    except ImportError:
        raise TypeError('Using ad-hoc certificates requires the cryptography library.'), None

    backend = default_backend()
    pkey = rsa.generate_private_key(public_exponent = 65537, key_size = 2048, backend = backend)
# WARNING: Decompyle incomplete


def make_ssl_devcert(base_path = None, host = None, cn = None):
    """Creates an SSL key for development.  This should be used instead of
    the ``'adhoc'`` key which generates a new cert on each server start.
    It accepts a path for where it should store the key and cert and
    either a host or CN.  If a host is given it will use the CN
    ``*.host/CN=host``.

    For more information see :func:`run_simple`.

    .. versionadded:: 0.9

    :param base_path: the path to the certificate and key.  The extension
                      ``.crt`` is added for the certificate, ``.key`` is
                      added for the key.
    :param host: the name of the host.  This can be used as an alternative
                 for the `cn`.
    :param cn: the `CN` to use.
    """
    pass
# WARNING: Decompyle incomplete


def generate_adhoc_ssl_context():
    '''Generates an adhoc SSL context for the development server.'''
    import atexit
    import tempfile
    (cert, pkey) = generate_adhoc_ssl_pair()
    serialization = serialization
    import cryptography.hazmat.primitives
    (cert_handle, cert_file) = tempfile.mkstemp()
    (pkey_handle, pkey_file) = tempfile.mkstemp()
    atexit.register(os.remove, pkey_file)
    atexit.register(os.remove, cert_file)
    os.write(cert_handle, cert.public_bytes(serialization.Encoding.PEM))
    os.write(pkey_handle, pkey.private_bytes(encoding = serialization.Encoding.PEM, format = serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm = serialization.NoEncryption()))
    os.close(cert_handle)
    os.close(pkey_handle)
    ctx = load_ssl_context(cert_file, pkey_file)
    return ctx


def load_ssl_context(cert_file = None, pkey_file = None, protocol = None):
    '''Loads SSL context from cert/private key files and optional protocol.
    Many parameters are directly taken from the API of
    :py:class:`ssl.SSLContext`.

    :param cert_file: Path of the certificate to use.
    :param pkey_file: Path of the private key to use. If not given, the key
                      will be obtained from the certificate file.
    :param protocol: A ``PROTOCOL`` constant from the :mod:`ssl` module.
        Defaults to :data:`ssl.PROTOCOL_TLS_SERVER`.
    '''
    pass
# WARNING: Decompyle incomplete


def is_ssl_error(error = None):
    '''Checks if the given error (or the current one) is an SSL error.'''
    pass
# WARNING: Decompyle incomplete


def select_address_family(host = None, port = None):
    '''Return ``AF_INET4``, ``AF_INET6``, or ``AF_UNIX`` depending on
    the host and port.'''
    if host.startswith('unix://'):
        return socket.AF_UNIX
    if None in host and hasattr(socket, 'AF_INET6'):
        return socket.AF_INET6
    return None.AF_INET


def get_sockaddr(host = None, port = None, family = None):
    '''Return a fully qualified socket address that can be passed to
    :func:`socket.bind`.'''
    if family == af_unix:
        return os.path.abspath(host.partition('://')[2])
    
    try:
        res = socket.getaddrinfo(host, port, family, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    except socket.gaierror:
        return 

    return res[0][4]


def get_interface_ip(family = None):
    '''Get the IP address of an external interface. Used when binding to
    0.0.0.0 or ::1 to show a more useful URL.

    :meta private:
    '''
    host = 'fd31:f903:5ab5:1::1' if family == socket.AF_INET6 else '10.253.155.219'
    s = socket.socket(family, socket.SOCK_DGRAM)
    s.connect((host, 58162))


class BaseWSGIServer(HTTPServer):
    pass
# WARNING: Decompyle incomplete


class ThreadedWSGIServer(BaseWSGIServer, socketserver.ThreadingMixIn):
    '''A WSGI server that handles concurrent requests in separate
    threads.

    Use :func:`make_server` to create a server instance.
    '''
    multithread = True
    daemon_threads = True


class ForkingWSGIServer(BaseWSGIServer, ForkingMixIn):
    pass
# WARNING: Decompyle incomplete


def make_server(host, port, app, threaded, processes = None, request_handler = None, passthrough_errors = None, ssl_context = (False, 1, None, False, None, None), fd = ('host', 'str', 'port', 'int', 'app', 'WSGIApplication', 'threaded', 'bool', 'processes', 'int', 'request_handler', 'type[WSGIRequestHandler] | None', 'passthrough_errors', 'bool', 'ssl_context', '_TSSLContextArg | None', 'fd', 'int | None', 'return', 'BaseWSGIServer')):
    '''Create an appropriate WSGI server instance based on the value of
    ``threaded`` and ``processes``.

    This is called from :func:`run_simple`, but can be used separately
    to have access to the server object, such as to run it in a separate
    thread.

    See :func:`run_simple` for parameter docs.
    '''
    if threaded and processes > 1:
        raise ValueError('Cannot have a multi-thread and multi-process server.')
    if threaded:
        return ThreadedWSGIServer(host, port, app, request_handler, passthrough_errors, ssl_context, fd = fd)
    if None > 1:
        return ForkingWSGIServer(host, port, app, processes, request_handler, passthrough_errors, ssl_context, fd = fd)
    return None(host, port, app, request_handler, passthrough_errors, ssl_context, fd = fd)


def is_running_from_reloader():
    '''Check if the server is running as a subprocess within the
    Werkzeug reloader.

    .. versionadded:: 0.10
    '''
    return os.environ.get('WERKZEUG_RUN_MAIN') == 'true'


def run_simple(hostname, port, application, use_reloader, use_debugger, use_evalex, extra_files, exclude_patterns, reloader_interval, reloader_type, threaded, processes = None, request_handler = None, static_files = None, passthrough_errors = (False, False, True, None, None, 1, 'auto', False, 1, None, None, False, None), ssl_context = ('hostname', 'str', 'port', 'int', 'application', 'WSGIApplication', 'use_reloader', 'bool', 'use_debugger', 'bool', 'use_evalex', 'bool', 'extra_files', 't.Iterable[str] | None', 'exclude_patterns', 't.Iterable[str] | None', 'reloader_interval', 'int', 'reloader_type', 'str', 'threaded', 'bool', 'processes', 'int', 'request_handler', 'type[WSGIRequestHandler] | None', 'static_files', 'dict[str, str | tuple[str, str]] | None', 'passthrough_errors', 'bool', 'ssl_context', '_TSSLContextArg | None', 'return', 'None')):
    '''Start a development server for a WSGI application. Various
    optional features can be enabled.

    .. warning::

        Do not use the development server when deploying to production.
        It is intended for use only during local development. It is not
        designed to be particularly efficient, stable, or secure.

    :param hostname: The host to bind to, for example ``\'localhost\'``.
        Can be a domain, IPv4 or IPv6 address, or file path starting
        with ``unix://`` for a Unix socket.
    :param port: The port to bind to, for example ``8080``. Using ``0``
        tells the OS to pick a random free port.
    :param application: The WSGI application to run.
    :param use_reloader: Use a reloader process to restart the server
        process when files are changed.
    :param use_debugger: Use Werkzeug\'s debugger, which will show
        formatted tracebacks on unhandled exceptions.
    :param use_evalex: Make the debugger interactive. A Python terminal
        can be opened for any frame in the traceback. Some protection is
        provided by requiring a PIN, but this should never be enabled
        on a publicly visible server.
    :param extra_files: The reloader will watch these files for changes
        in addition to Python modules. For example, watch a
        configuration file.
    :param exclude_patterns: The reloader will ignore changes to any
        files matching these :mod:`fnmatch` patterns. For example,
        ignore cache files.
    :param reloader_interval: How often the reloader tries to check for
        changes.
    :param reloader_type: The reloader to use. The ``\'stat\'`` reloader
        is built in, but may require significant CPU to watch files. The
        ``\'watchdog\'`` reloader is much more efficient but requires
        installing the ``watchdog`` package first.
    :param threaded: Handle concurrent requests using threads. Cannot be
        used with ``processes``.
    :param processes: Handle concurrent requests using up to this number
        of processes. Cannot be used with ``threaded``.
    :param request_handler: Use a different
        :class:`~BaseHTTPServer.BaseHTTPRequestHandler` subclass to
        handle requests.
    :param static_files: A dict mapping URL prefixes to directories to
        serve static files from using
        :class:`~werkzeug.middleware.SharedDataMiddleware`.
    :param passthrough_errors: Don\'t catch unhandled exceptions at the
        server level, let the server crash instead. If ``use_debugger``
        is enabled, the debugger will still catch such errors.
    :param ssl_context: Configure TLS to serve over HTTPS. Can be an
        :class:`ssl.SSLContext` object, a ``(cert_file, key_file)``
        tuple to create a typical context, or the string ``\'adhoc\'`` to
        generate a temporary self-signed certificate.

    .. versionchanged:: 2.1
        Instructions are shown for dealing with an "address already in
        use" error.

    .. versionchanged:: 2.1
        Running on ``0.0.0.0`` or ``::`` shows the loopback IP in
        addition to a real IP.

    .. versionchanged:: 2.1
        The command-line interface was removed.

    .. versionchanged:: 2.0
        Running on ``0.0.0.0`` or ``::`` shows a real IP address that
        was bound as well as a warning not to run the development server
        in production.

    .. versionchanged:: 2.0
        The ``exclude_patterns`` parameter was added.

    .. versionchanged:: 0.15
        Bind to a Unix socket by passing a ``hostname`` that starts with
        ``unix://``.

    .. versionchanged:: 0.10
        Improved the reloader and added support for changing the backend
        through the ``reloader_type`` parameter.

    .. versionchanged:: 0.9
        A command-line interface was added.

    .. versionchanged:: 0.8
        ``ssl_context`` can be a tuple of paths to the certificate and
        private key files.

    .. versionchanged:: 0.6
        The ``ssl_context`` parameter was added.

    .. versionchanged:: 0.5
       The ``static_files`` and ``passthrough_errors`` parameters were
       added.
    '''
    if not isinstance(port, int):
        raise TypeError('port must be an integer')
    if static_files:
        SharedDataMiddleware = SharedDataMiddleware
        import middleware.shared_data
        application = SharedDataMiddleware(application, static_files)
    if use_debugger:
        DebuggedApplication = DebuggedApplication
        import debug
        application = DebuggedApplication(application, evalex = use_evalex)
        application.trusted_hosts.append(hostname)
    if not is_running_from_reloader():
        fd = None
    else:
        fd = int(os.environ['WERKZEUG_SERVER_FD'])
    srv = make_server(hostname, port, application, threaded, processes, request_handler, passthrough_errors, ssl_context, fd = fd)
    srv.socket.set_inheritable(True)
    os.environ['WERKZEUG_SERVER_FD'] = str(srv.fileno())
    if not is_running_from_reloader():
        srv.log_startup()
        _log('info', _ansi_style('Press CTRL+C to quit', 'yellow'))
    if use_reloader:
        run_with_reloader = run_with_reloader
        import _reloader
        
        try:
            run_with_reloader(srv.serve_forever, extra_files = extra_files, exclude_patterns = exclude_patterns, interval = reloader_interval, reloader_type = reloader_type)
            srv.server_close()
            return None
        except:
            srv.server_close()
            srv.serve_forever()
            return None
