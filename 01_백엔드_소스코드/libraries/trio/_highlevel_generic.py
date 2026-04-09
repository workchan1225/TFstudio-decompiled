# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _highlevel_generic.pyc (Python 3.11)

from __future__ import annotations
from typing import Generic, TypeGuard, TypeVar
import attrs
import trio
from trio._util import final
from abc import AsyncResource, HalfCloseableStream, ReceiveStream, SendStream
SendStreamT = TypeVar('SendStreamT', bound = SendStream)
ReceiveStreamT = TypeVar('ReceiveStreamT', bound = ReceiveStream)

async def aclose_forcefully(resource = None):
    """Close an async resource or async generator immediately, without
    blocking to do any graceful cleanup.

    :class:`~trio.abc.AsyncResource` objects guarantee that if their
    :meth:`~trio.abc.AsyncResource.aclose` method is cancelled, then they will
    still close the resource (albeit in a potentially ungraceful
    fashion). :func:`aclose_forcefully` is a convenience function that
    exploits this behavior to let you force a resource to be closed without
    blocking: it works by calling ``await resource.aclose()`` and then
    cancelling it immediately.

    Most users won't need this, but it may be useful on cleanup paths where
    you can't afford to block, or if you want to close a resource and don't
    care about handling it gracefully. For example, if
    :class:`~trio.SSLStream` encounters an error and cannot perform its
    own graceful close, then there's no point in waiting to gracefully shut
    down the underlying transport either, so it calls ``await
    aclose_forcefully(self.transport_stream)``.

    Note that this function is async, and that it acts as a checkpoint, but
    unlike most async functions it cannot block indefinitely (at least,
    assuming the underlying resource object is correctly implemented).

    """
    pass
# WARNING: Decompyle incomplete


def _is_halfclosable(stream = None):
    '''Check if the stream has a send_eof() method.'''
    return hasattr(stream, 'send_eof')


def StapledStream():
    '''StapledStream'''
    receive_stream: 'ReceiveStreamT' = 'This class `staples <https://en.wikipedia.org/wiki/Staple_(fastener)>`__\n    together two unidirectional streams to make single bidirectional stream.\n\n    Args:\n      send_stream (~trio.abc.SendStream): The stream to use for sending.\n      receive_stream (~trio.abc.ReceiveStream): The stream to use for\n          receiving.\n\n    Example:\n\n       A silly way to make a stream that echoes back whatever you write to\n       it::\n\n          left, right = trio.testing.memory_stream_pair()\n          echo_stream = StapledStream(SocketStream(left), SocketStream(right))\n          await echo_stream.send_all(b"x")\n          assert await echo_stream.receive_some() == b"x"\n\n    :class:`StapledStream` objects implement the methods in the\n    :class:`~trio.abc.HalfCloseableStream` interface. They also have two\n    additional public attributes:\n\n    .. attribute:: send_stream\n\n       The underlying :class:`~trio.abc.SendStream`. :meth:`send_all` and\n       :meth:`wait_send_all_might_not_block` are delegated to this object.\n\n    .. attribute:: receive_stream\n\n       The underlying :class:`~trio.abc.ReceiveStream`. :meth:`receive_some`\n       is delegated to this object.\n\n    '
    
    async def send_all(self = None, data = None):
        '''Calls ``self.send_stream.send_all``.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def wait_send_all_might_not_block(self = None):
        '''Calls ``self.send_stream.wait_send_all_might_not_block``.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def send_eof(self = None):
        '''Shuts down the send side of the stream.

        If :meth:`self.send_stream.send_eof() <trio.abc.HalfCloseableStream.send_eof>` exists,
        then this calls it. Otherwise, this calls
        :meth:`self.send_stream.aclose() <trio.abc.AsyncResource.aclose>`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def receive_some(self = None, max_bytes = None):
        '''Calls ``self.receive_stream.receive_some``.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        '''Calls ``aclose`` on both underlying streams.'''
        pass
    # WARNING: Decompyle incomplete


StapledStream = <NODE:27>(StapledStream, 'StapledStream', HalfCloseableStream, Generic[(SendStreamT, ReceiveStreamT)])()()
