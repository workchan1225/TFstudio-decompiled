# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: memory.pyc (Python 3.11)

from __future__ import annotations
__all__ = ('MemoryObjectReceiveStream', 'MemoryObjectSendStream', 'MemoryObjectStreamStatistics')
import warnings
from collections import OrderedDict, deque
from dataclasses import dataclass, field
from types import TracebackType
from typing import Generic, NamedTuple, TypeVar
from  import BrokenResourceError, ClosedResourceError, EndOfStream, WouldBlock
from _core._testing import TaskInfo, get_current_task
from abc import Event, ObjectReceiveStream, ObjectSendStream
from lowlevel import checkpoint
T_Item = TypeVar('T_Item')
T_co = TypeVar('T_co', covariant = True)
T_contra = TypeVar('T_contra', contravariant = True)

class MemoryObjectStreamStatistics(NamedTuple):
    tasks_waiting_receive: 'int' = 'MemoryObjectStreamStatistics'


def _MemoryObjectItemReceiver():
    '''_MemoryObjectItemReceiver'''
    task_info: 'TaskInfo' = field(init = False, default_factory = get_current_task)
    item: 'T_Item' = field(init = False)
    
    def __repr__(self = None):
        item = getattr(self, 'item', None)
        return f'''{self.__class__.__name__}(task_info={self.task_info}, item={item!r})'''


_MemoryObjectItemReceiver = <NODE:27>(_MemoryObjectItemReceiver, '_MemoryObjectItemReceiver', Generic[T_Item])()

def _MemoryObjectStreamState():
    '''_MemoryObjectStreamState'''
    max_buffer_size: 'float' = field()
    buffer: 'deque[T_Item]' = field(init = False, default_factory = deque)
    open_send_channels: 'int' = field(init = False, default = 0)
    open_receive_channels: 'int' = field(init = False, default = 0)
    waiting_receivers: 'OrderedDict[Event, _MemoryObjectItemReceiver[T_Item]]' = field(init = False, default_factory = OrderedDict)
    waiting_senders: 'OrderedDict[Event, T_Item]' = field(init = False, default_factory = OrderedDict)
    
    def statistics(self = None):
        return MemoryObjectStreamStatistics(len(self.buffer), self.max_buffer_size, self.open_send_channels, self.open_receive_channels, len(self.waiting_senders), len(self.waiting_receivers))


_MemoryObjectStreamState = <NODE:27>(_MemoryObjectStreamState, '_MemoryObjectStreamState', Generic[T_Item])()

def MemoryObjectReceiveStream():
    '''MemoryObjectReceiveStream'''
    _state: '_MemoryObjectStreamState[T_co]' = 'MemoryObjectReceiveStream'
    _closed: 'bool' = field(init = False, default = False)
    
    def __post_init__(self = None):
        pass

    
    def receive_nowait(self = None):
        '''
        Receive the next item if it can be done without waiting.

        :return: the received item
        :raises ~anyio.ClosedResourceError: if this send stream has been closed
        :raises ~anyio.EndOfStream: if the buffer is empty and this stream has been
            closed from the sending end
        :raises ~anyio.WouldBlock: if there are no items in the buffer and no tasks
            waiting to send

        '''
        if self._closed:
            raise ClosedResourceError
        if self._state.waiting_senders:
            (send_event, item) = self._state.waiting_senders.popitem(last = False)
            self._state.buffer.append(item)
            send_event.set()
        if self._state.buffer:
            return self._state.buffer.popleft()
        if not None._state.open_send_channels:
            raise EndOfStream
        raise WouldBlock

    
    async def receive(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def clone(self = None):
        '''
        Create a clone of this receive stream.

        Each clone can be closed separately. Only when all clones have been closed will
        the receiving end of the memory stream be considered closed by the sending ends.

        :return: the cloned stream

        '''
        if self._closed:
            raise ClosedResourceError
        return MemoryObjectReceiveStream(_state = self._state)

    
    def close(self = None):
        '''
        Close the stream.

        This works the exact same way as :meth:`aclose`, but is provided as a special
        case for the benefit of synchronous callbacks.

        '''
        if not self._closed:
            self._closed = True
            if self._state.open_receive_channels == 0:
                list(self._state.waiting_senders.keys()) = self._state, self._state.open_receive_channels -= 1, .open_receive_channels
                for event in send_events:
                    event.set()
                    return None
                    return None
                    return None

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def statistics(self = None):
        '''
        Return statistics about the current state of this stream.

        .. versionadded:: 3.0
        '''
        return self._state.statistics()

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        self.close()

    
    def __del__(self = None):
        if not self._closed:
            warnings.warn(f'''Unclosed <{self.__class__.__name__} at {id(self):x}>''', ResourceWarning, stacklevel = 1, source = self)
            return None


MemoryObjectReceiveStream = <NODE:27>(MemoryObjectReceiveStream, 'MemoryObjectReceiveStream', Generic[T_co], ObjectReceiveStream[T_co])()

def MemoryObjectSendStream():
    '''MemoryObjectSendStream'''
    _state: '_MemoryObjectStreamState[T_contra]' = 'MemoryObjectSendStream'
    _closed: 'bool' = field(init = False, default = False)
    
    def __post_init__(self = None):
        pass

    
    def send_nowait(self = None, item = None):
        '''
        Send an item immediately if it can be done without waiting.

        :param item: the item to send
        :raises ~anyio.ClosedResourceError: if this send stream has been closed
        :raises ~anyio.BrokenResourceError: if the stream has been closed from the
            receiving end
        :raises ~anyio.WouldBlock: if the buffer is full and there are no tasks waiting
            to receive

        '''
        if self._closed:
            raise ClosedResourceError
        if not self._state.open_receive_channels:
            raise BrokenResourceError
    # WARNING: Decompyle incomplete

    
    async def send(self = None, item = None):
        '''
        Send an item to the stream.

        If the buffer is full, this method blocks until there is again room in the
        buffer or the item can be sent directly to a receiver.

        :param item: the item to send
        :raises ~anyio.ClosedResourceError: if this send stream has been closed
        :raises ~anyio.BrokenResourceError: if the stream has been closed from the
            receiving end

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def clone(self = None):
        '''
        Create a clone of this send stream.

        Each clone can be closed separately. Only when all clones have been closed will
        the sending end of the memory stream be considered closed by the receiving ends.

        :return: the cloned stream

        '''
        if self._closed:
            raise ClosedResourceError
        return MemoryObjectSendStream(_state = self._state)

    
    def close(self = None):
        '''
        Close the stream.

        This works the exact same way as :meth:`aclose`, but is provided as a special
        case for the benefit of synchronous callbacks.

        '''
        if not self._closed:
            self._closed = True
            if self._state.open_send_channels == 0:
                list(self._state.waiting_receivers.keys()) = self._state, self._state.open_send_channels -= 1, .open_send_channels
                self._state.waiting_receivers.clear()
                for event in receive_events:
                    event.set()
                    return None
                    return None
                    return None

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def statistics(self = None):
        '''
        Return statistics about the current state of this stream.

        .. versionadded:: 3.0
        '''
        return self._state.statistics()

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', 'type[BaseException] | None', 'exc_val', 'BaseException | None', 'exc_tb', 'TracebackType | None', 'return', 'None')):
        self.close()

    
    def __del__(self = None):
        if not self._closed:
            warnings.warn(f'''Unclosed <{self.__class__.__name__} at {id(self):x}>''', ResourceWarning, stacklevel = 1, source = self)
            return None


MemoryObjectSendStream = <NODE:27>(MemoryObjectSendStream, 'MemoryObjectSendStream', Generic[T_contra], ObjectSendStream[T_contra])()
