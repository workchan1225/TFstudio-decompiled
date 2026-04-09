# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _streams.pyc (Python 3.11)

from __future__ import annotations
import sys
from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from typing import Any, Generic, TypeVar, Union
from _core._exceptions import EndOfStream
from _core._typedattr import TypedAttributeProvider
from _resources import AsyncResource
from _tasks import TaskGroup
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias
T_Item = TypeVar('T_Item')
T_co = TypeVar('T_co', covariant = True)
T_contra = TypeVar('T_contra', contravariant = True)

def UnreliableObjectReceiveStream():
    '''UnreliableObjectReceiveStream'''
    __doc__ = '\n    An interface for receiving objects.\n\n    This interface makes no guarantees that the received messages arrive in the order in\n    which they were sent, or that no messages are missed.\n\n    Asynchronously iterating over objects of this type will yield objects matching the\n    given type parameter.\n    '
    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    receive = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

UnreliableObjectReceiveStream = <NODE:27>(UnreliableObjectReceiveStream, 'UnreliableObjectReceiveStream', Generic[T_co], AsyncResource, TypedAttributeProvider)

def UnreliableObjectSendStream():
    '''UnreliableObjectSendStream'''
    __doc__ = '\n    An interface for sending objects.\n\n    This interface makes no guarantees that the messages sent will reach the\n    recipient(s) in the same order in which they were sent, or at all.\n    '
    send = (lambda self = None, item = None: pass# WARNING: Decompyle incomplete
)()

UnreliableObjectSendStream = <NODE:27>(UnreliableObjectSendStream, 'UnreliableObjectSendStream', Generic[T_contra], AsyncResource, TypedAttributeProvider)

def UnreliableObjectStream():
    '''UnreliableObjectStream'''
    __doc__ = '\n    A bidirectional message stream which does not guarantee the order or reliability of\n    message delivery.\n    '

UnreliableObjectStream = <NODE:27>(UnreliableObjectStream, 'UnreliableObjectStream', UnreliableObjectReceiveStream[T_Item], UnreliableObjectSendStream[T_Item])

def ObjectReceiveStream():
    '''ObjectReceiveStream'''
    __doc__ = '\n    A receive message stream which guarantees that messages are received in the same\n    order in which they were sent, and that no messages are missed.\n    '

ObjectReceiveStream = <NODE:27>(ObjectReceiveStream, 'ObjectReceiveStream', UnreliableObjectReceiveStream[T_co])

def ObjectSendStream():
    '''ObjectSendStream'''
    __doc__ = '\n    A send message stream which guarantees that messages are delivered in the same order\n    in which they were sent, without missing any messages in the middle.\n    '

ObjectSendStream = <NODE:27>(ObjectSendStream, 'ObjectSendStream', UnreliableObjectSendStream[T_contra])

def ObjectStream():
    '''ObjectStream'''
    __doc__ = '\n    A bidirectional message stream which guarantees the order and reliability of message\n    delivery.\n    '
    send_eof = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

ObjectStream = <NODE:27>(ObjectStream, 'ObjectStream', ObjectReceiveStream[T_Item], ObjectSendStream[T_Item], UnreliableObjectStream[T_Item])

class ByteReceiveStream(TypedAttributeProvider, AsyncResource):
    '''
    An interface for receiving bytes from a single peer.

    Iterating this byte stream will yield a byte string of arbitrary length, but no more
    than 65536 bytes.
    '''
    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    receive = (lambda self = None, max_bytes = None: pass# WARNING: Decompyle incomplete
)()


class ByteSendStream(TypedAttributeProvider, AsyncResource):
    '''An interface for sending bytes to a single peer.'''
    send = (lambda self = None, item = None: pass# WARNING: Decompyle incomplete
)()


class ByteStream(ByteSendStream, ByteReceiveStream):
    '''A bidirectional byte stream.'''
    send_eof = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

AnyUnreliableByteReceiveStream: 'TypeAlias' = Union[(UnreliableObjectReceiveStream[bytes], ByteReceiveStream)]
AnyUnreliableByteSendStream: 'TypeAlias' = Union[(UnreliableObjectSendStream[bytes], ByteSendStream)]
AnyUnreliableByteStream: 'TypeAlias' = Union[(UnreliableObjectStream[bytes], ByteStream)]
AnyByteReceiveStream: 'TypeAlias' = Union[(ObjectReceiveStream[bytes], ByteReceiveStream)]
AnyByteSendStream: 'TypeAlias' = Union[(ObjectSendStream[bytes], ByteSendStream)]
AnyByteStream: 'TypeAlias' = Union[(ObjectStream[bytes], ByteStream)]

def Listener():
    '''Listener'''
    __doc__ = 'An interface for objects that let you accept incoming connections.'
    serve = (lambda self = None, handler = None, task_group = abstractmethod: pass# WARNING: Decompyle incomplete
)()

Listener = <NODE:27>(Listener, 'Listener', Generic[T_co], AsyncResource, TypedAttributeProvider)

def ObjectStreamConnectable():
    '''ObjectStreamConnectable'''
    connect = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

ObjectStreamConnectable = <NODE:27>(ObjectStreamConnectable, 'ObjectStreamConnectable', Generic[T_co], metaclass = ABCMeta)

def ByteStreamConnectable():
    '''ByteStreamConnectable'''
    connect = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

ByteStreamConnectable = <NODE:27>(ByteStreamConnectable, 'ByteStreamConnectable', metaclass = ABCMeta)
AnyByteStreamConnectable: 'TypeAlias' = Union[(ObjectStreamConnectable[bytes], ByteStreamConnectable)]
