# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wsgi.pyc (Python 3.11)

from __future__ import annotations
import io
import typing as t
from functools import partial
from functools import update_wrapper
from exceptions import ClientDisconnected
from exceptions import RequestEntityTooLarge
from sansio import utils as _sansio_utils
from sansio.utils import host_is_trusted
if t.TYPE_CHECKING:
    from _typeshed.wsgi import WSGIApplication
    from _typeshed.wsgi import WSGIEnvironment

def responder(f = None):
    """Marks a function as responder.  Decorate a function with it and it
    will automatically call the return value as WSGI application.

    Example::

        @responder
        def application(environ, start_response):
            return Response('Hello World!')
    """
    pass
# WARNING: Decompyle incomplete


def get_current_url(environ = None, root_only = None, strip_querystring = None, host_only = (False, False, False, None), trusted_hosts = ('environ', 'WSGIEnvironment', 'root_only', 'bool', 'strip_querystring', 'bool', 'host_only', 'bool', 'trusted_hosts', 't.Iterable[str] | None', 'return', 'str')):
    """Recreate the URL for a request from the parts in a WSGI
    environment.

    The URL is an IRI, not a URI, so it may contain Unicode characters.
    Use :func:`~werkzeug.urls.iri_to_uri` to convert it to ASCII.

    :param environ: The WSGI environment to get the URL parts from.
    :param root_only: Only build the root path, don't include the
        remaining path or query string.
    :param strip_querystring: Don't include the query string.
    :param host_only: Only build the scheme and host.
    :param trusted_hosts: A list of trusted host names to validate the
        host against.
    """
    parts = {
        'scheme': environ['wsgi.url_scheme'],
        'host': get_host(environ, trusted_hosts) }
    if not host_only:
        parts['root_path'] = environ.get('SCRIPT_NAME', '')
        if not root_only:
            parts['path'] = environ.get('PATH_INFO', '')
            if not strip_querystring:
                parts['query_string'] = environ.get('QUERY_STRING', '').encode('latin1')
# WARNING: Decompyle incomplete


def _get_server(environ = None):
    name = environ.get('SERVER_NAME')
# WARNING: Decompyle incomplete


def get_host(environ = None, trusted_hosts = None):
    """Return the host for the given WSGI environment.

    The ``Host`` header is preferred, then ``SERVER_NAME`` if it's not
    set. The returned host will only contain the port if it is different
    than the standard port for the protocol.

    Optionally, verify that the host is trusted using
    :func:`host_is_trusted` and raise a
    :exc:`~werkzeug.exceptions.SecurityError` if it is not.

    :param environ: A WSGI environment dict.
    :param trusted_hosts: A list of trusted host names.

    :return: Host, with port if necessary.
    :raise ~werkzeug.exceptions.SecurityError: If the host is not
        trusted.
    """
    return _sansio_utils.get_host(environ['wsgi.url_scheme'], environ.get('HTTP_HOST'), _get_server(environ), trusted_hosts)


def get_content_length(environ = None):
    '''Return the ``Content-Length`` header value as an int. If the header is not given
    or the ``Transfer-Encoding`` header is ``chunked``, ``None`` is returned to indicate
    a streaming request. If the value is not an integer, or negative, 0 is returned.

    :param environ: The WSGI environ to get the content length from.

    .. versionadded:: 0.9
    '''
    return _sansio_utils.get_content_length(http_content_length = environ.get('CONTENT_LENGTH'), http_transfer_encoding = environ.get('HTTP_TRANSFER_ENCODING'))


def get_input_stream(environ = None, safe_fallback = None, max_content_length = None):
    '''Return the WSGI input stream, wrapped so that it may be read safely without going
    past the ``Content-Length`` header value or ``max_content_length``.

    If ``Content-Length`` exceeds ``max_content_length``, a
    :exc:`RequestEntityTooLarge`` ``413 Content Too Large`` error is raised.

    If the WSGI server sets ``environ["wsgi.input_terminated"]``, it indicates that the
    server handles terminating the stream, so it is safe to read directly. For example,
    a server that knows how to handle chunked requests safely would set this.

    If ``max_content_length`` is set, it can be enforced on streams if
    ``wsgi.input_terminated`` is set. Otherwise, an empty stream is returned unless the
    user explicitly disables this safe fallback.

    If the limit is reached before the underlying stream is exhausted (such as a file
    that is too large, or an infinite stream), the remaining contents of the stream
    cannot be read safely. Depending on how the server handles this, clients may show a
    "connection reset" failure instead of seeing the 413 response.

    :param environ: The WSGI environ containing the stream.
    :param safe_fallback: Return an empty stream when ``Content-Length`` is not set.
        Disabling this allows infinite streams, which can be a denial-of-service risk.
    :param max_content_length: The maximum length that content-length or streaming
        requests may not exceed.

    .. versionchanged:: 2.3.2
        ``max_content_length`` is only applied to streaming requests if the server sets
        ``wsgi.input_terminated``.

    .. versionchanged:: 2.3
        Check ``max_content_length`` and raise an error if it is exceeded.

    .. versionadded:: 0.9
    '''
    stream = t.cast(t.IO[bytes], environ['wsgi.input'])
    content_length = get_content_length(environ)
# WARNING: Decompyle incomplete


def get_path_info(environ = None):
    '''Return ``PATH_INFO`` from  the WSGI environment.

    :param environ: WSGI environment to get the path from.

    .. versionchanged:: 3.0
        The ``charset`` and ``errors`` parameters were removed.

    .. versionadded:: 0.9
    '''
    path = environ.get('PATH_INFO', '').encode('latin1')
    return path.decode(errors = 'replace')


class ClosingIterator:
    '''The WSGI specification requires that all middlewares and gateways
    respect the `close` callback of the iterable returned by the application.
    Because it is useful to add another close action to a returned iterable
    and adding a custom iterable is a boring task this class can be used for
    that::

        return ClosingIterator(app(environ, start_response), [cleanup_session,
                                                              cleanup_locals])

    If there is just one close function it can be passed instead of the list.

    A closing iterator is not needed if the application uses response objects
    and finishes the processing if the response is started::

        try:
            return response(environ, start_response)
        finally:
            cleanup_session()
            cleanup_locals()
    '''
    
    def __init__(self = None, iterable = None, callbacks = None):
        iterator = iter(iterable)
        self._next = t.cast(t.Callable[([], bytes)], partial(next, iterator))
    # WARNING: Decompyle incomplete

    
    def __iter__(self = None):
        return self

    
    def __next__(self = None):
        return self._next()

    
    def close(self = None):
        for callback in self._callbacks:
            callback()
            return None



def wrap_file(environ = None, file = None, buffer_size = None):
    """Wraps a file.  This uses the WSGI server's file wrapper if available
    or otherwise the generic :class:`FileWrapper`.

    .. versionadded:: 0.5

    If the file wrapper from the WSGI server is used it's important to not
    iterate over it from inside the application but to pass it through
    unchanged.  If you want to pass out a file wrapper inside a response
    object you have to set :attr:`Response.direct_passthrough` to `True`.

    More information about file wrappers are available in :pep:`333`.

    :param file: a :class:`file`-like object with a :meth:`~file.read` method.
    :param buffer_size: number of bytes for one iteration.
    """
    return environ.get('wsgi.file_wrapper', FileWrapper)(file, buffer_size)


class FileWrapper:
    """This class can be used to convert a :class:`file`-like object into
    an iterable.  It yields `buffer_size` blocks until the file is fully
    read.

    You should not use this class directly but rather use the
    :func:`wrap_file` function that uses the WSGI server's file wrapper
    support if it's available.

    .. versionadded:: 0.5

    If you're using this object together with a :class:`Response` you have
    to use the `direct_passthrough` mode.

    :param file: a :class:`file`-like object with a :meth:`~file.read` method.
    :param buffer_size: number of bytes for one iteration.
    """
    
    def __init__(self = None, file = None, buffer_size = None):
        self.file = file
        self.buffer_size = buffer_size

    
    def close(self = None):
        if hasattr(self.file, 'close'):
            self.file.close()
            return None

    
    def seekable(self = None):
        if hasattr(self.file, 'seekable'):
            return self.file.seekable()
        if None(self.file, 'seek'):
            return True

    
    def seek(self = None, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def tell(self = None):
        if hasattr(self.file, 'tell'):
            return self.file.tell()

    
    def __iter__(self = None):
        return self

    
    def __next__(self = None):
        data = self.file.read(self.buffer_size)
        if data:
            return data
        raise None()



class _RangeWrapper:
    """This class can be used to convert an iterable object into
    an iterable that will only yield a piece of the underlying content.
    It yields blocks until the underlying stream range is fully read.
    The yielded blocks will have a size that can't exceed the original
    iterator defined block size, but that can be smaller.

    If you're using this object together with a :class:`Response` you have
    to use the `direct_passthrough` mode.

    :param iterable: an iterable object with a :meth:`__next__` method.
    :param start_byte: byte from which read will start.
    :param byte_range: how many bytes to read.
    """
    
    def __init__(self = None, iterable = None, start_byte = None, byte_range = (0, None)):
        self.iterable = iter(iterable)
        self.byte_range = byte_range
        self.start_byte = start_byte
        self.end_byte = None
    # WARNING: Decompyle incomplete

    
    def __iter__(self = None):
        return self

    
    def _next_chunk(self = None):
        
        try:
            chunk = next(self.iterable)
            return chunk
        except StopIteration:
            True = None
            raise 


    
    def _first_iteration(self = None):
        chunk = None
        if self.seekable:
            self.iterable.seek(self.start_byte)
            self.read_length = self.iterable.tell()
            contextual_read_length = self.read_length
    # WARNING: Decompyle incomplete

    
    def _next(self = None):
        if self.end_reached:
            raise StopIteration()
        chunk = None
        contextual_read_length = self.read_length
        if self.read_length == 0:
            (chunk, contextual_read_length) = self._first_iteration()
    # WARNING: Decompyle incomplete

    
    def __next__(self = None):
        chunk = self._next()
        if chunk:
            return chunk
        self.end_reached = None
        raise StopIteration()

    
    def close(self = None):
        if hasattr(self.iterable, 'close'):
            self.iterable.close()
            return None



class LimitedStream(io.RawIOBase):
    '''Wrap a stream so that it doesn\'t read more than a given limit. This is used to
    limit ``wsgi.input`` to the ``Content-Length`` header value or
    :attr:`.Request.max_content_length`.

    When attempting to read after the limit has been reached, :meth:`on_exhausted` is
    called. When the limit is a maximum, this raises :exc:`.RequestEntityTooLarge`.

    If reading from the stream returns zero bytes or raises an error,
    :meth:`on_disconnect` is called, which raises :exc:`.ClientDisconnected`. When the
    limit is a maximum and zero bytes were read, no error is raised, since it may be the
    end of the stream.

    If the limit is reached before the underlying stream is exhausted (such as a file
    that is too large, or an infinite stream), the remaining contents of the stream
    cannot be read safely. Depending on how the server handles this, clients may show a
    "connection reset" failure instead of seeing the 413 response.

    :param stream: The stream to read from. Must be a readable binary IO object.
    :param limit: The limit in bytes to not read past. Should be either the
        ``Content-Length`` header value or ``request.max_content_length``.
    :param is_max: Whether the given ``limit`` is ``request.max_content_length`` instead
        of the ``Content-Length`` header value. This changes how exhausted and
        disconnect events are handled.

    .. versionchanged:: 2.3
        Handle ``max_content_length`` differently than ``Content-Length``.

    .. versionchanged:: 2.3
        Implements ``io.RawIOBase`` rather than ``io.IOBase``.
    '''
    
    def __init__(self = None, stream = None, limit = None, is_max = (False,)):
        self._stream = stream
        self._pos = 0
        self.limit = limit
        self._limit_is_max = is_max

    is_exhausted = (lambda self = None: self._pos >= self.limit)()
    
    def on_exhausted(self = None):
        '''Called when attempting to read after the limit has been reached.

        The default behavior is to do nothing, unless the limit is a maximum, in which
        case it raises :exc:`.RequestEntityTooLarge`.

        .. versionchanged:: 2.3
            Raises ``RequestEntityTooLarge`` if the limit is a maximum.

        .. versionchanged:: 2.3
            Any return value is ignored.
        '''
        if self._limit_is_max:
            raise RequestEntityTooLarge()

    
    def on_disconnect(self = None, error = None):
        '''Called when an attempted read receives zero bytes before the limit was
        reached. This indicates that the client disconnected before sending the full
        request body.

        The default behavior is to raise :exc:`.ClientDisconnected`, unless the limit is
        a maximum and no error was raised.

        .. versionchanged:: 2.3
            Added the ``error`` parameter. Do nothing if the limit is a maximum and no
            error was raised.

        .. versionchanged:: 2.3
            Any return value is ignored.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def exhaust(self = None):
        '''Exhaust the stream by reading until the limit is reached or the client
        disconnects, returning the remaining data.

        .. versionchanged:: 2.3
            Return the remaining data.

        .. versionchanged:: 2.2.3
            Handle case where wrapped stream returns fewer bytes than requested.
        '''
        if not self.is_exhausted:
            return self.readall()

    
    def readinto(self = None, b = None):
        size = len(b)
        remaining = self.limit - self._pos
        if remaining <= 0:
            self.on_exhausted()
            return 0
        if None(self._stream, 'readinto'):
            if size <= remaining:
                
                try:
                    out_size = self._stream.readinto(b)
                except (OSError, ValueError):
                    e = None
                    self.on_disconnect(error = e)
                    e = None
                    del e
                    return 0
                    e = None
                    del e
                    temp_b = bytearray(remaining)
                    
                    try:
                        out_size = self._stream.readinto(temp_b)
                    except (OSError, ValueError):
                        e = None
                        self.on_disconnect(error = e)
                        e = None
                        del e
                        return 0
                        e = None
                        del e

                    if out_size:
                        b[:out_size] = temp_b
                    else:
                        
                        try:
                            data = self._stream.read(min(size, remaining))
                        except (OSError, ValueError):
                            e = None
                            self.on_disconnect(error = e)
                            e = None
                            del e
                            return 0
                            e = None
                            del e

                        out_size = len(data)
                        b[:out_size] = data

        if not out_size:
            self.on_disconnect()
            return 0
        return out_size

    
    def readall(self = None):
        if self.is_exhausted:
            self.on_exhausted()
            return b''
        out = None()
    # WARNING: Decompyle incomplete

    
    def tell(self = None):
        '''Return the current stream position.

        .. versionadded:: 0.9
        '''
        return self._pos

    
    def readable(self = None):
        return True
