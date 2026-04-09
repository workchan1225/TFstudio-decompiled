# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _abc.pyc (Python 3.11)

from __future__ import annotations
import socket
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar
import trio
if TYPE_CHECKING:
    from types import TracebackType
    from typing_extensions import Self
    from _socket import SocketType
    from lowlevel import Task

class Clock(ABC):
    '''The interface for custom run loop clocks.'''
    __slots__ = ()
    start_clock = (lambda self = None: pass)()
    current_time = (lambda self = None: pass)()
    deadline_to_sleep_time = (lambda self = None, deadline = None: pass)()


class Instrument(ABC):
    """The interface for run loop instrumentation.

    Instruments don't have to inherit from this abstract base class, and all
    of these methods are optional. This class serves mostly as documentation.

    """
    __slots__ = ()
    
    def before_run(self = None):
        '''Called at the beginning of :func:`trio.run`.'''
        pass

    
    def after_run(self = None):
        '''Called just before :func:`trio.run` returns.'''
        pass

    
    def task_spawned(self = None, task = None):
        '''Called when the given task is created.

        Args:
            task (trio.lowlevel.Task): The new task.

        '''
        pass

    
    def task_scheduled(self = None, task = None):
        '''Called when the given task becomes runnable.

        It may still be some time before it actually runs, if there are other
        runnable tasks ahead of it.

        Args:
            task (trio.lowlevel.Task): The task that became runnable.

        '''
        pass

    
    def before_task_step(self = None, task = None):
        '''Called immediately before we resume running the given task.

        Args:
            task (trio.lowlevel.Task): The task that is about to run.

        '''
        pass

    
    def after_task_step(self = None, task = None):
        '''Called when we return to the main run loop after a task has yielded.

        Args:
            task (trio.lowlevel.Task): The task that just ran.

        '''
        pass

    
    def task_exited(self = None, task = None):
        '''Called when the given task exits.

        Args:
            task (trio.lowlevel.Task): The finished task.

        '''
        pass

    
    def before_io_wait(self = None, timeout = None):
        '''Called before blocking to wait for I/O readiness.

        Args:
            timeout (float): The number of seconds we are willing to wait.

        '''
        pass

    
    def after_io_wait(self = None, timeout = None):
        '''Called after handling pending I/O.

        Args:
            timeout (float): The number of seconds we were willing to
                wait. This much time may or may not have elapsed, depending on
                whether any I/O was ready.

        '''
        pass



class HostnameResolver(ABC):
    '''If you have a custom hostname resolver, then implementing
    :class:`HostnameResolver` allows you to register this to be used by Trio.

    See :func:`trio.socket.set_custom_hostname_resolver`.

    '''
    __slots__ = ()
    getaddrinfo = (lambda self, host, port = None, family = None, type = abstractmethod, proto = (0, 0, 0, 0), flags = ('host', 'bytes | None', 'port', 'bytes | str | int | None', 'family', 'int', 'type', 'int', 'proto', 'int', 'flags', 'int', 'return', 'list[tuple[socket.AddressFamily, socket.SocketKind, int, str, tuple[str, int] | tuple[str, int, int, int] | tuple[int, bytes]]]'): pass# WARNING: Decompyle incomplete
)()
    getnameinfo = (lambda self = None, sockaddr = None, flags = abstractmethod: pass# WARNING: Decompyle incomplete
)()


class SocketFactory(ABC):
    '''If you write a custom class implementing the Trio socket interface,
    then you can use a :class:`SocketFactory` to get Trio to use it.

    See :func:`trio.socket.set_custom_socket_factory`.

    '''
    __slots__ = ()
    socket = (lambda self = None, family = None, type = abstractmethod, proto = (socket.AF_INET, socket.SOCK_STREAM, 0): pass)()


class AsyncResource(ABC):
    '''A standard interface for resources that needs to be cleaned up, and
    where that cleanup may require blocking operations.

    This class distinguishes between "graceful" closes, which may perform I/O
    and thus block, and a "forceful" close, which cannot. For example, cleanly
    shutting down a TLS-encrypted connection requires sending a "goodbye"
    message; but if a peer has become non-responsive, then sending this
    message might block forever, so we may want to just drop the connection
    instead. Therefore the :meth:`aclose` method is unusual in that it
    should always close the connection (or at least make its best attempt)
    *even if it fails*; failure indicates a failure to achieve grace, not a
    failure to close the connection.

    Objects that implement this interface can be used as async context
    managers, i.e., you can write::

      async with create_resource() as some_async_resource:
          ...

    Entering the context manager is synchronous (not a checkpoint); exiting it
    calls :meth:`aclose`. The default implementations of
    ``__aenter__`` and ``__aexit__`` should be adequate for all subclasses.

    '''
    __slots__ = ()
    aclose = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete



class SendStream(AsyncResource):
    """A standard interface for sending data on a byte stream.

    The underlying stream may be unidirectional, or bidirectional. If it's
    bidirectional, then you probably want to also implement
    :class:`ReceiveStream`, which makes your object a :class:`Stream`.

    :class:`SendStream` objects also implement the :class:`AsyncResource`
    interface, so they can be closed by calling :meth:`~AsyncResource.aclose`
    or using an ``async with`` block.

    If you want to send Python objects rather than raw bytes, see
    :class:`SendChannel`.

    """
    __slots__ = ()
    send_all = (lambda self = None, data = None: pass# WARNING: Decompyle incomplete
)()
    wait_send_all_might_not_block = (lambda self = None: pass# WARNING: Decompyle incomplete
)()


class ReceiveStream(AsyncResource):
    """A standard interface for receiving data on a byte stream.

    The underlying stream may be unidirectional, or bidirectional. If it's
    bidirectional, then you probably want to also implement
    :class:`SendStream`, which makes your object a :class:`Stream`.

    :class:`ReceiveStream` objects also implement the :class:`AsyncResource`
    interface, so they can be closed by calling :meth:`~AsyncResource.aclose`
    or using an ``async with`` block.

    If you want to receive Python objects rather than raw bytes, see
    :class:`ReceiveChannel`.

    `ReceiveStream` objects can be used in ``async for`` loops. Each iteration
    will produce an arbitrary sized chunk of bytes, like calling
    `receive_some` with no arguments. Every chunk will contain at least one
    byte, and the loop automatically exits when reaching end-of-file.

    """
    __slots__ = ()
    receive_some = (lambda self = None, max_bytes = None: pass# WARNING: Decompyle incomplete
)()
    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete



class Stream(ReceiveStream, SendStream):
    '''A standard interface for interacting with bidirectional byte streams.

    A :class:`Stream` is an object that implements both the
    :class:`SendStream` and :class:`ReceiveStream` interfaces.

    If implementing this interface, you should consider whether you can go one
    step further and implement :class:`HalfCloseableStream`.

    '''
    __slots__ = ()


class HalfCloseableStream(Stream):
    '''This interface extends :class:`Stream` to also allow closing the send
    part of the stream without closing the receive part.

    '''
    __slots__ = ()
    send_eof = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

T = TypeVar('T')
ReceiveType = TypeVar('ReceiveType', covariant = True)
SendType = TypeVar('SendType', contravariant = True)
T_resource = TypeVar('T_resource', bound = AsyncResource, covariant = True)

def Listener():
    '''Listener'''
    __doc__ = 'A standard interface for listening for incoming connections.\n\n    :class:`Listener` objects also implement the :class:`AsyncResource`\n    interface, so they can be closed by calling :meth:`~AsyncResource.aclose`\n    or using an ``async with`` block.\n\n    '
    __slots__ = ()
    accept = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

Listener = <NODE:27>(Listener, 'Listener', AsyncResource, Generic[T_resource])

def SendChannel():
    '''SendChannel'''
    __doc__ = 'A standard interface for sending Python objects to some receiver.\n\n    `SendChannel` objects also implement the `AsyncResource` interface, so\n    they can be closed by calling `~AsyncResource.aclose` or using an ``async\n    with`` block.\n\n    If you want to send raw bytes rather than Python objects, see\n    `SendStream`.\n\n    '
    __slots__ = ()
    send = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()

SendChannel = <NODE:27>(SendChannel, 'SendChannel', AsyncResource, Generic[SendType])

def ReceiveChannel():
    '''ReceiveChannel'''
    __doc__ = 'A standard interface for receiving Python objects from some sender.\n\n    You can iterate over a :class:`ReceiveChannel` using an ``async for``\n    loop::\n\n       async for value in receive_channel:\n           ...\n\n    This is equivalent to calling :meth:`receive` repeatedly. The loop exits\n    without error when `receive` raises `~trio.EndOfChannel`.\n\n    `ReceiveChannel` objects also implement the `AsyncResource` interface, so\n    they can be closed by calling `~AsyncResource.aclose` or using an ``async\n    with`` block.\n\n    If you want to receive raw bytes rather than Python objects, see\n    `ReceiveStream`.\n\n    '
    __slots__ = ()
    receive = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete


ReceiveChannel = <NODE:27>(ReceiveChannel, 'ReceiveChannel', AsyncResource, Generic[ReceiveType])
SendChannel.__module__ = SendChannel.__module__.replace('_abc', 'abc')
ReceiveChannel.__module__ = ReceiveChannel.__module__.replace('_abc', 'abc')
Listener.__module__ = Listener.__module__.replace('_abc', 'abc')

def Channel():
    '''Channel'''
    __doc__ = 'A standard interface for interacting with bidirectional channels.\n\n    A `Channel` is an object that implements both the `SendChannel` and\n    `ReceiveChannel` interfaces, so you can both send and receive objects.\n\n    '
    __slots__ = ()

Channel = <NODE:27>(Channel, 'Channel', SendChannel[T], ReceiveChannel[T])
Channel.__module__ = Channel.__module__.replace('_abc', 'abc')
