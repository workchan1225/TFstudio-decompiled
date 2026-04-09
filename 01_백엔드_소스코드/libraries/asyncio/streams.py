# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: streams.pyc (Python 3.11)

__all__ = ('StreamReader', 'StreamWriter', 'StreamReaderProtocol', 'open_connection', 'start_server')
import collections
import socket
import sys
import warnings
import weakref
if hasattr(socket, 'AF_UNIX'):
    __all__ += ('open_unix_connection', 'start_unix_server')
from  import coroutines
from  import events
from  import exceptions
from  import format_helpers
from  import protocols
from log import logger
from tasks import sleep
_DEFAULT_LIMIT = 65536

async def open_connection(host = None, port = (None, None), *, limit, **kwds):
    """A wrapper for create_connection() returning a (reader, writer) pair.

    The reader returned is a StreamReader instance; the writer is a
    StreamWriter instance.

    The arguments are all the usual arguments to create_connection()
    except protocol_factory; most common are positional host and port,
    with various optional keyword arguments following.

    Additional optional keyword arguments are loop (to set the event loop
    instance to use) and limit (to set the buffer limit passed to the
    StreamReader).

    (If you want to customize the StreamReader and/or
    StreamReaderProtocol classes, just copy the code -- there's
    really nothing special here except some convenience.)
    """
    pass
# WARNING: Decompyle incomplete


async def start_server(client_connected_cb = None, host = (None, None), port = {
    'limit': _DEFAULT_LIMIT }, *, limit, **kwds):
    '''Start a socket server, call back for each client connected.

    The first parameter, `client_connected_cb`, takes two parameters:
    client_reader, client_writer.  client_reader is a StreamReader
    object, while client_writer is a StreamWriter object.  This
    parameter can either be a plain callback function or a coroutine;
    if it is a coroutine, it will be automatically converted into a
    Task.

    The rest of the arguments are all the usual arguments to
    loop.create_server() except protocol_factory; most common are
    positional host and port, with various optional keyword arguments
    following.  The return value is the same as loop.create_server().

    Additional optional keyword argument is limit (to set the buffer
    limit passed to the StreamReader).

    The return value is the same as loop.create_server(), i.e. a
    Server object which can be used to stop the service.
    '''
    pass
# WARNING: Decompyle incomplete

if hasattr(socket, 'AF_UNIX'):
    
    async def open_unix_connection(path = None, *, limit, **kwds):
        '''Similar to `open_connection` but works with UNIX Domain Sockets.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def start_unix_server(client_connected_cb = None, path = (None,), *, limit, **kwds):
        '''Similar to `start_server` but works with UNIX Domain Sockets.'''
        pass
    # WARNING: Decompyle incomplete


class FlowControlMixin(protocols.Protocol):
    '''Reusable flow control logic for StreamWriter.drain().

    This implements the protocol methods pause_writing(),
    resume_writing() and connection_lost().  If the subclass overrides
    these it must call the super methods.

    StreamWriter.drain() must wait for _drain_helper() coroutine.
    '''
    
    def __init__(self, loop = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def pause_writing(self):
        pass
    # WARNING: Decompyle incomplete

    
    def resume_writing(self):
        pass
    # WARNING: Decompyle incomplete

    
    def connection_lost(self, exc):
        self._connection_lost = True
        if not self._paused:
            return None
    # WARNING: Decompyle incomplete

    
    async def _drain_helper(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_close_waiter(self, stream):
        raise NotImplementedError



class StreamReaderProtocol(protocols.Protocol, FlowControlMixin):
    pass
# WARNING: Decompyle incomplete


class StreamWriter:
    '''Wraps a Transport.

    This exposes write(), writelines(), [can_]write_eof(),
    get_extra_info() and close().  It adds drain() which returns an
    optional Future on which you can wait for flow control.  It also
    adds a transport property which references the Transport
    directly.
    '''
    
    def __init__(self, transport, protocol, reader, loop):
        self._transport = transport
        self._protocol = protocol
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        info = [
            self.__class__.__name__,
            f'''transport={self._transport!r}''']
    # WARNING: Decompyle incomplete

    transport = (lambda self: self._transport)()
    
    def write(self, data):
        self._transport.write(data)

    
    def writelines(self, data):
        self._transport.writelines(data)

    
    def write_eof(self):
        return self._transport.write_eof()

    
    def can_write_eof(self):
        return self._transport.can_write_eof()

    
    def close(self):
        return self._transport.close()

    
    def is_closing(self):
        return self._transport.is_closing()

    
    async def wait_closed(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_extra_info(self, name, default = (None,)):
        return self._transport.get_extra_info(name, default)

    
    async def drain(self):
        '''Flush the write buffer.

        The intended use is to write

          w.write(data)
          await w.drain()
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def start_tls(self = property, sslcontext = {
        'server_hostname': None,
        'ssl_handshake_timeout': None }, *, server_hostname, ssl_handshake_timeout):
        '''Upgrade an existing stream-based connection to TLS.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __del__(self):
        if not self._transport.is_closing():
            if self._loop.is_closed():
                warnings.warn('loop is closed', ResourceWarning)
                return None
            None.close()
            warnings.warn(f'''unclosed {self!r}''', ResourceWarning)
            return None



class StreamReader:
    _source_traceback = None
    
    def __init__(self, limit, loop = (_DEFAULT_LIMIT, None)):
        if limit <= 0:
            raise ValueError('Limit cannot be <= 0')
        self._limit = limit
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        info = [
            'StreamReader']
        if self._buffer:
            info.append(f'''{len(self._buffer)} bytes''')
        if self._eof:
            info.append('eof')
        if self._limit != _DEFAULT_LIMIT:
            info.append(f'''limit={self._limit}''')
        if self._waiter:
            info.append(f'''waiter={self._waiter!r}''')
        if self._exception:
            info.append(f'''exception={self._exception!r}''')
        if self._transport:
            info.append(f'''transport={self._transport!r}''')
        if self._paused:
            info.append('paused')
        return '<{}>'.format(' '.join(info))

    
    def exception(self):
        return self._exception

    
    def set_exception(self, exc):
        self._exception = exc
        waiter = self._waiter
    # WARNING: Decompyle incomplete

    
    def _wakeup_waiter(self):
        '''Wakeup read*() functions waiting for data or EOF.'''
        waiter = self._waiter
    # WARNING: Decompyle incomplete

    
    def set_transport(self, transport):
        pass
    # WARNING: Decompyle incomplete

    
    def _maybe_resume_transport(self):
        if self._paused or len(self._buffer) <= self._limit:
            self._paused = False
            self._transport.resume_reading()
            return None
        return None

    
    def feed_eof(self):
        self._eof = True
        self._wakeup_waiter()

    
    def at_eof(self):
