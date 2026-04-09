# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: windows_events.pyc (Python 3.11)

'''Selector and proactor event loops for Windows.'''
import sys
if sys.platform != 'win32':
    raise ImportError('win32 only')
import _overlapped
import _winapi
import errno
import math
import msvcrt
import socket
import struct
import time
import weakref
from  import events
from  import base_subprocess
from  import futures
from  import exceptions
from  import proactor_events
from  import selector_events
from  import tasks
from  import windows_utils
from log import logger
__all__ = ('SelectorEventLoop', 'ProactorEventLoop', 'IocpProactor', 'DefaultEventLoopPolicy', 'WindowsSelectorEventLoopPolicy', 'WindowsProactorEventLoopPolicy')
NULL = _winapi.NULL
INFINITE = _winapi.INFINITE
ERROR_CONNECTION_REFUSED = 1225
ERROR_CONNECTION_ABORTED = 1236
CONNECT_PIPE_INIT_DELAY = 0.001
CONNECT_PIPE_MAX_DELAY = 0.1

class _OverlappedFuture(futures.Future):
    pass
# WARNING: Decompyle incomplete


class _BaseWaitHandleFuture(futures.Future):
    pass
# WARNING: Decompyle incomplete


class _WaitCancelFuture(_BaseWaitHandleFuture):
    pass
# WARNING: Decompyle incomplete


class _WaitHandleFuture(_BaseWaitHandleFuture):
    pass
# WARNING: Decompyle incomplete


class PipeServer(object):
    '''Class representing a pipe server.

    This is much like a bound, listening socket.
    '''
    
    def __init__(self, address):
        self._address = address
        self._free_instances = weakref.WeakSet()
        self._pipe = None
        self._accept_pipe_future = None
        self._pipe = self._server_pipe_handle(True)

    
    def _get_unconnected_pipe(self):
        tmp, self._pipe = self._pipe, self._server_pipe_handle(False)
        return tmp

    
    def _server_pipe_handle(self, first):
        if self.closed():
            return None
        flags = None.PIPE_ACCESS_DUPLEX | _winapi.FILE_FLAG_OVERLAPPED
        if first:
            flags |= _winapi.FILE_FLAG_FIRST_PIPE_INSTANCE
        h = _winapi.CreateNamedPipe(self._address, flags, _winapi.PIPE_TYPE_MESSAGE | _winapi.PIPE_READMODE_MESSAGE | _winapi.PIPE_WAIT, _winapi.PIPE_UNLIMITED_INSTANCES, windows_utils.BUFSIZE, windows_utils.BUFSIZE, _winapi.NMPWAIT_WAIT_FOREVER, _winapi.NULL)
        pipe = windows_utils.PipeHandle(h)
        self._free_instances.add(pipe)
        return pipe

    
    def closed(self):
        return self._address is None

    
    def close(self):
        pass
    # WARNING: Decompyle incomplete

    __del__ = close


class _WindowsSelectorEventLoop(selector_events.BaseSelectorEventLoop):
    '''Windows version of selector event loop.'''
    pass


class ProactorEventLoop(proactor_events.BaseProactorEventLoop):
    pass
# WARNING: Decompyle incomplete


class IocpProactor:
    '''Proactor implementation using IOCP.'''
    
    def __init__(self, concurrency = (INFINITE,)):
        self._loop = None
        self._results = []
        self._iocp = _overlapped.CreateIoCompletionPort(_overlapped.INVALID_HANDLE_VALUE, NULL, 0, concurrency)
        self._cache = { }
        self._registered = weakref.WeakSet()
        self._unregistered = []
        self._stopped_serving = weakref.WeakSet()

    
    def _check_closed(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        info = [
            'overlapped#=%s' % len(self._cache),
            'result#=%s' % len(self._results)]
    # WARNING: Decompyle incomplete

    
    def set_loop(self, loop):
        self._loop = loop

    
    def select(self, timeout = (None,)):
        if not self._results:
            self._poll(timeout)
        tmp = self._results
        self._results = []
        
        try:
            tmp = None
            return tmp
        except:
            tmp = None


    
    def _result(self, value):
        fut = self._loop.create_future()
        fut.set_result(value)
        return fut

    
    def recv(self, conn, nbytes, flags = (0,)):
        self._register_with_iocp(conn)
        ov = _overlapped.Overlapped(NULL)
        
        try:
            if isinstance(conn, socket.socket):
                ov.WSARecv(conn.fileno(), nbytes, flags)
            else:
                ov.ReadFile(conn.fileno(), nbytes)
        except BrokenPipeError:
            return 

        return self._register(ov, conn, finish_recv)

    
    def recv_into(self, conn, buf, flags = (0,)):
        self._register_with_iocp(conn)
        ov = _overlapped.Overlapped(NULL)
        
        try:
            if isinstance(conn, socket.socket):
                ov.WSARecvInto(conn.fileno(), buf, flags)
            else:
                ov.ReadFileInto(conn.fileno(), buf)
        except BrokenPipeError:
            return 

        return self._register(ov, conn, finish_recv)

    
    def recvfrom(self, conn, nbytes, flags = (0,)):
        self._register_with_iocp(conn)
        ov = _overlapped.Overlapped(NULL)
        
        try:
            ov.WSARecvFrom(conn.fileno(), nbytes, flags)
        except BrokenPipeError:
            return 

        return self._register(ov, conn, finish_recv)

    
    def recvfrom_into(self, conn, buf, flags = (0,)):
        self._register_with_iocp(conn)
        ov = _overlapped.Overlapped(NULL)
        
        try:
            ov.WSARecvFromInto(conn.fileno(), buf, flags)
        except BrokenPipeError:
            return 

        return self._register(ov, conn, finish_recv)

    
    def sendto(self, conn, buf, flags, addr = (0, None)):
        self._register_with_iocp(conn)
        ov = _overlapped.Overlapped(NULL)
        ov.WSASendTo(conn.fileno(), buf, flags, addr)
        
        def finish_send(trans, key, ov):
            pass
        # WARNING: Decompyle incomplete

        return self._register(ov, conn, finish_send)

    
    def send(self, conn, buf, flags = (0,)):
        self._register_with_iocp(conn)
        ov = _overlapped.Overlapped(NULL)
        if isinstance(conn, socket.socket):
            ov.WSASend(conn.fileno(), buf, flags)
        else:
            ov.WriteFile(conn.fileno(), buf)
        
        def finish_send(trans, key, ov):
            pass
        # WARNING: Decompyle incomplete

        return self._register(ov, conn, finish_send)

    
    def accept(self, listener):
        pass
    # WARNING: Decompyle incomplete

    
    def connect(self, conn, address):
        pass
    # WARNING: Decompyle incomplete

    
    def sendfile(self, sock, file, offset, count):
        self._register_with_iocp(sock)
        ov = _overlapped.Overlapped(NULL)
        offset_low = offset & 0xFFFFFFFF
        offset_high = offset >> 32 & 0xFFFFFFFF
        ov.TransmitFile(sock.fileno(), msvcrt.get_osfhandle(file.fileno()), offset_low, offset_high, count, 0, 0)
        
        def finish_sendfile(trans, key, ov):
            pass
        # WARNING: Decompyle incomplete

        return self._register(ov, sock, finish_sendfile)

    
    def accept_pipe(self, pipe):
        pass
    # WARNING: Decompyle incomplete

    
    async def connect_pipe(self, address):
        pass
    # WARNING: Decompyle incomplete

    
    def wait_for_handle(self, handle, timeout = (None,)):
        '''Wait for a handle.

        Return a Future object. The result of the future is True if the wait
        completed, or False if the wait did not complete (on timeout).
        '''
        return self._wait_for_handle(handle, timeout, False)

    
    def _wait_cancel(self, event, done_callback):
        fut = self._wait_for_handle(event, None, True)
        fut._done_callback = done_callback
        return fut

    
    def _wait_for_handle(self, handle, timeout, _is_cancel):
        pass
    # WARNING: Decompyle incomplete

    
    def _register_with_iocp(self, obj):
        if obj not in self._registered:
            self._registered.add(obj)
            _overlapped.CreateIoCompletionPort(obj.fileno(), self._iocp, 0, 0)
            return None

    
    def _register(self, ov, obj, callback):
        self._check_closed()
        f = _OverlappedFuture(ov, loop = self._loop)
        if f._source_traceback:
            del f._source_traceback[-1]
        if not ov.pending:
            
            try:
                value = callback(None, None, ov)
                f.set_result(value)
            except OSError:
                e = None
                f.set_exception(e)
                e = None
                del e
            except:
                e = None
                del e

            self._cache[ov.address] = (f, ov, obj, callback)
            return f

    
    def _unregister(self, ov):
        '''Unregister an overlapped object.

        Call this method when its future has been cancelled. The event can
        already be signalled (pending in the proactor event queue). It is also
        safe if the event is never signalled (because it was cancelled).
        '''
        self._check_closed()
        self._unregistered.append(ov)

    
    def _get_accept_socket(self, family):
        s = socket.socket(family)
        s.settimeout(0)
        return s

    
    def _poll(self, timeout = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _stop_serving(self, obj):
        self._stopped_serving.add(obj)

    
    def close(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __del__(self):
        self.close()



class _WindowsSubprocessTransport(base_subprocess.BaseSubprocessTransport):
    
    def _start(self, args, shell, stdin, stdout, stderr, bufsize, **kwargs):
        pass
    # WARNING: Decompyle incomplete


SelectorEventLoop = _WindowsSelectorEventLoop

class WindowsSelectorEventLoopPolicy(events.BaseDefaultEventLoopPolicy):
    _loop_factory = SelectorEventLoop


class WindowsProactorEventLoopPolicy(events.BaseDefaultEventLoopPolicy):
    _loop_factory = ProactorEventLoop

DefaultEventLoopPolicy = WindowsProactorEventLoopPolicy
