# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base_channel.pyc (Python 3.11)

'''Abstract base classes for Channel objects and Multicallable objects.'''
import abc
from typing import Generic, Optional
import grpc
from  import _base_call
from _typing import DeserializingFunction
from _typing import MetadataType
from _typing import RequestIterableType
from _typing import RequestType
from _typing import ResponseType
from _typing import SerializingFunction

def UnaryUnaryMultiCallable():
    '''UnaryUnaryMultiCallable'''
    __doc__ = 'Enables asynchronous invocation of a unary-call RPC.'
    __call__ = (lambda self = None, request = None, *, timeout, metadata: pass)()

UnaryUnaryMultiCallable = <NODE:27>(UnaryUnaryMultiCallable, 'UnaryUnaryMultiCallable', Generic[(RequestType, ResponseType)], abc.ABC)

def UnaryStreamMultiCallable():
    '''UnaryStreamMultiCallable'''
    __doc__ = 'Enables asynchronous invocation of a server-streaming RPC.'
    __call__ = (lambda self = None, request = None, *, timeout, metadata: pass)()

UnaryStreamMultiCallable = <NODE:27>(UnaryStreamMultiCallable, 'UnaryStreamMultiCallable', Generic[(RequestType, ResponseType)], abc.ABC)

class StreamUnaryMultiCallable(abc.ABC):
    '''Enables asynchronous invocation of a client-streaming RPC.'''
    __call__ = (lambda self, request_iterator, timeout = None, metadata = None, credentials = abc.abstractmethod, wait_for_ready = (None, None, None, None, None, None), compression = ('request_iterator', Optional[RequestIterableType], 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', _base_call.StreamUnaryCall): pass)()


class StreamStreamMultiCallable(abc.ABC):
    '''Enables asynchronous invocation of a bidirectional-streaming RPC.'''
    __call__ = (lambda self, request_iterator, timeout = None, metadata = None, credentials = abc.abstractmethod, wait_for_ready = (None, None, None, None, None, None), compression = ('request_iterator', Optional[RequestIterableType], 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', _base_call.StreamStreamCall): pass)()


class Channel(abc.ABC):
    '''Enables asynchronous RPC invocation as a client.

    Channel objects implement the Asynchronous Context Manager (aka. async
    with) type, although they are not supported to be entered and exited
    multiple times.
    '''
    __aenter__ = (lambda self: pass# WARNING: Decompyle incomplete
)()
    __aexit__ = (lambda self, exc_type, exc_val, exc_tb: pass# WARNING: Decompyle incomplete
)()
    close = (lambda self = abc.abstractmethod, grace = abc.abstractmethod: pass# WARNING: Decompyle incomplete
)()
    get_state = (lambda self = None, try_to_connect = None: pass)()
    wait_for_state_change = (lambda self = None, last_observed_state = None: pass# WARNING: Decompyle incomplete
)()
    channel_ready = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    unary_unary = (lambda self = None, method = None, request_serializer = abc.abstractmethod, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', UnaryUnaryMultiCallable): pass)()
    unary_stream = (lambda self = None, method = None, request_serializer = abc.abstractmethod, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', UnaryStreamMultiCallable): pass)()
    stream_unary = (lambda self = None, method = None, request_serializer = abc.abstractmethod, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', StreamUnaryMultiCallable): pass)()
    stream_stream = (lambda self = None, method = None, request_serializer = abc.abstractmethod, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', StreamStreamMultiCallable): pass)()
