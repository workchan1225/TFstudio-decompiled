# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: messages.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import codecs
import collections
from collections.abc import AsyncIterator, Iterable
from typing import Any, Callable, Generic, Literal, TypeVar, overload
from exceptions import ConcurrencyError
from frames import OP_BINARY, OP_CONT, OP_TEXT, Frame
from typing import Data
__all__ = [
    'Assembler']
UTF8Decoder = codecs.getincrementaldecoder('utf-8')
T = TypeVar('T')

def SimpleQueue():
    '''SimpleQueue'''
    __doc__ = '\n    Simplified version of :class:`asyncio.Queue`.\n\n    Provides only the subset of functionality needed by :class:`Assembler`.\n\n    '
    
    def __init__(self = None):
        self.loop = asyncio.get_running_loop()
        self.get_waiter = None
        self.queue = collections.deque()

    
    def __len__(self = None):
        return len(self.queue)

    
    def put(self = None, item = None):
        '''Put an item into the queue without waiting.'''
        self.queue.append(item)
    # WARNING: Decompyle incomplete

    
    async def get(self = None, block = None):
        '''Remove and return an item from the queue, waiting if necessary.'''
        pass
    # WARNING: Decompyle incomplete

    
    def reset(self = None, items = None):
        '''Put back items into an empty, idle queue.'''
        pass
    # WARNING: Decompyle incomplete

    
    def abort(self = None):
        '''Close the queue, raising EOFError in get() if necessary.'''
        pass
    # WARNING: Decompyle incomplete


SimpleQueue = <NODE:27>(SimpleQueue, 'SimpleQueue', Generic[T])

class Assembler:
    """
    Assemble messages from frames.

    :class:`Assembler` expects only data frames. The stream of frames must
    respect the protocol; if it doesn't, the behavior is undefined.

    Args:
        pause: Called when the buffer of frames goes above the high water mark;
            should pause reading from the network.
        resume: Called when the buffer of frames goes below the low water mark;
            should resume reading from the network.

    """
    
    def __init__(self = None, high = None, low = None, pause = (None, None, (lambda : pass), (lambda : pass)), resume = ('high', 'int | None', 'low', 'int | None', 'pause', 'Callable[[], Any]', 'resume', 'Callable[[], Any]', 'return', 'None')):
        self.frames = SimpleQueue()
    # WARNING: Decompyle incomplete

    get = (lambda self = None, decode = None: pass# WARNING: Decompyle incomplete
)()
    get = (lambda self = None, decode = None: pass# WARNING: Decompyle incomplete
)()
    get = (lambda self = None, decode = None: pass# WARNING: Decompyle incomplete
)()
    
    async def get(self = None, decode = None):
        '''
        Read the next message.

        :meth:`get` returns a single :class:`str` or :class:`bytes`.

        If the message is fragmented, :meth:`get` waits until the last frame is
        received, then it reassembles the message and returns it. To receive
        messages frame by frame, use :meth:`get_iter` instead.

        Args:
            decode: :obj:`False` disables UTF-8 decoding of text frames and
                returns :class:`bytes`. :obj:`True` forces UTF-8 decoding of
                binary frames and returns :class:`str`.

        Raises:
            EOFError: If the stream of frames has ended.
            UnicodeDecodeError: If a text frame contains invalid UTF-8.
            ConcurrencyError: If two coroutines run :meth:`get` or
                :meth:`get_iter` concurrently.

        '''
        pass
    # WARNING: Decompyle incomplete

    get_iter = (lambda self = None, decode = None: pass)()
    get_iter = (lambda self = None, decode = None: pass)()
    get_iter = (lambda self = None, decode = None: pass)()
    
    def get_iter(self = None, decode = None):
        """
        Stream the next message.

        Iterating the return value of :meth:`get_iter` asynchronously yields a
        :class:`str` or :class:`bytes` for each frame in the message.

        The iterator must be fully consumed before calling :meth:`get_iter` or
        :meth:`get` again. Else, :exc:`ConcurrencyError` is raised.

        This method only makes sense for fragmented messages. If messages aren't
        fragmented, use :meth:`get` instead.

        Args:
            decode: :obj:`False` disables UTF-8 decoding of text frames and
                returns :class:`bytes`. :obj:`True` forces UTF-8 decoding of
                binary frames and returns :class:`str`.

        Raises:
            EOFError: If the stream of frames has ended.
            UnicodeDecodeError: If a text frame contains invalid UTF-8.
            ConcurrencyError: If two coroutines run :meth:`get` or
                :meth:`get_iter` concurrently.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def put(self = None, frame = None):
        '''
        Add ``frame`` to the next message.

        Raises:
            EOFError: If the stream of frames has ended.

        '''
        if self.closed:
            raise EOFError('stream of frames ended')
        self.frames.put(frame)
        self.maybe_pause()

    
    def maybe_pause(self = None):
        '''Pause the writer if queue is above the high water mark.'''
        pass
    # WARNING: Decompyle incomplete

    
    def maybe_resume(self = None):
        '''Resume the writer if queue is below the low water mark.'''
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        '''
        End the stream of frames.

        Calling :meth:`close` concurrently with :meth:`get`, :meth:`get_iter`,
        or :meth:`put` is safe. They will raise :exc:`EOFError`.

        '''
        if self.closed:
            return None
        self.closed = None
        self.frames.abort()
