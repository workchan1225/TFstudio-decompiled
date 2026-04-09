# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: face.pyc (Python 3.11)

'''Interfaces defining the Face layer of RPC Framework.'''
import abc
import collections
import enum
from grpc.framework.common import cardinality
from grpc.framework.common import style
from grpc.framework.foundation import future
from grpc.framework.foundation import stream

class NoSuchMethodError(Exception):
    pass
# WARNING: Decompyle incomplete


def Abortion():
    '''Abortion'''
    __doc__ = 'A value describing RPC abortion.\n\n    Attributes:\n      kind: A Kind value identifying how the RPC failed.\n      initial_metadata: The initial metadata from the other side of the RPC or\n        None if no initial metadata value was received.\n      terminal_metadata: The terminal metadata from the other side of the RPC or\n        None if no terminal metadata value was received.\n      code: The code value from the other side of the RPC or None if no code value\n        was received.\n      details: The details value from the other side of the RPC or None if no\n        details value was received.\n    '
    Kind = <NODE:12>()

Abortion = <NODE:27>(Abortion, 'Abortion', collections.namedtuple('Abortion', ('kind', 'initial_metadata', 'terminal_metadata', 'code', 'details')))

def AbortionError():
    '''AbortionError'''
    pass
# WARNING: Decompyle incomplete

AbortionError = <NODE:27>(AbortionError, 'AbortionError', Exception, metaclass = abc.ABCMeta)

class CancellationError(AbortionError):
    '''Indicates that an RPC has been cancelled.'''
    pass


class ExpirationError(AbortionError):
    '''Indicates that an RPC has expired ("timed out").'''
    pass


class LocalShutdownError(AbortionError):
    '''Indicates that an RPC has terminated due to local shutdown of RPCs.'''
    pass


class RemoteShutdownError(AbortionError):
    '''Indicates that an RPC has terminated due to remote shutdown of RPCs.'''
    pass


class NetworkError(AbortionError):
    '''Indicates that some error occurred on the network.'''
    pass


class LocalError(AbortionError):
    '''Indicates that an RPC has terminated due to a local defect.'''
    pass


class RemoteError(AbortionError):
    '''Indicates that an RPC has terminated due to a remote defect.'''
    pass


class RpcContext(abc.ABC):
    '''Provides RPC-related information and action.'''
    is_active = (lambda self: raise NotImplementedError())()
    time_remaining = (lambda self: raise NotImplementedError())()
    add_abortion_callback = (lambda self, abortion_callback: raise NotImplementedError())()
    cancel = (lambda self: raise NotImplementedError())()
    protocol_context = (lambda self: raise NotImplementedError())()


def Call():
    '''Call'''
    __doc__ = 'Invocation-side utility object for an RPC.'
    initial_metadata = (lambda self: raise NotImplementedError())()
    terminal_metadata = (lambda self: raise NotImplementedError())()
    code = (lambda self: raise NotImplementedError())()
    details = (lambda self: raise NotImplementedError())()

Call = <NODE:27>(Call, 'Call', RpcContext, metaclass = abc.ABCMeta)

def ServicerContext():
    '''ServicerContext'''
    __doc__ = 'A context object passed to method implementations.'
    invocation_metadata = (lambda self: raise NotImplementedError())()
    initial_metadata = (lambda self, initial_metadata: raise NotImplementedError())()
    terminal_metadata = (lambda self, terminal_metadata: raise NotImplementedError())()
    code = (lambda self, code: raise NotImplementedError())()
    details = (lambda self, details: raise NotImplementedError())()

ServicerContext = <NODE:27>(ServicerContext, 'ServicerContext', RpcContext, metaclass = abc.ABCMeta)

class ResponseReceiver(abc.ABC):
    '''Invocation-side object used to accept the output of an RPC.'''
    initial_metadata = (lambda self, initial_metadata: raise NotImplementedError())()
    response = (lambda self, response: raise NotImplementedError())()
    complete = (lambda self, terminal_metadata, code, details: raise NotImplementedError())()


class UnaryUnaryMultiCallable(abc.ABC):
    '''Affords invoking a unary-unary RPC in any call style.'''
    __call__ = (lambda self, request, timeout, metadata, with_call, protocol_options = (None, False, None): raise NotImplementedError())()
    future = (lambda self, request, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    event = (lambda self, request, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()


class UnaryStreamMultiCallable(abc.ABC):
    '''Affords invoking a unary-stream RPC in any call style.'''
    __call__ = (lambda self, request, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    event = (lambda self, request, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()


class StreamUnaryMultiCallable(abc.ABC):
    '''Affords invoking a stream-unary RPC in any call style.'''
    __call__ = (lambda self, request_iterator, timeout, metadata, with_call, protocol_options = (None, False, None): raise NotImplementedError())()
    future = (lambda self, request_iterator, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    event = (lambda self, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()


class StreamStreamMultiCallable(abc.ABC):
    '''Affords invoking a stream-stream RPC in any call style.'''
    __call__ = (lambda self, request_iterator, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    event = (lambda self, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()


class MethodImplementation(abc.ABC):
    '''A sum type that describes a method implementation.

    Attributes:
      cardinality: A cardinality.Cardinality value.
      style: A style.Service value.
      unary_unary_inline: The implementation of the method as a callable value
        that takes a request value and a ServicerContext object and returns a
        response value. Only non-None if cardinality is
        cardinality.Cardinality.UNARY_UNARY and style is style.Service.INLINE.
      unary_stream_inline: The implementation of the method as a callable value
        that takes a request value and a ServicerContext object and returns an
        iterator of response values. Only non-None if cardinality is
        cardinality.Cardinality.UNARY_STREAM and style is style.Service.INLINE.
      stream_unary_inline: The implementation of the method as a callable value
        that takes an iterator of request values and a ServicerContext object and
        returns a response value. Only non-None if cardinality is
        cardinality.Cardinality.STREAM_UNARY and style is style.Service.INLINE.
      stream_stream_inline: The implementation of the method as a callable value
        that takes an iterator of request values and a ServicerContext object and
        returns an iterator of response values. Only non-None if cardinality is
        cardinality.Cardinality.STREAM_STREAM and style is style.Service.INLINE.
      unary_unary_event: The implementation of the method as a callable value that
        takes a request value, a response callback to which to pass the response
        value of the RPC, and a ServicerContext. Only non-None if cardinality is
        cardinality.Cardinality.UNARY_UNARY and style is style.Service.EVENT.
      unary_stream_event: The implementation of the method as a callable value
        that takes a request value, a stream.Consumer to which to pass the
        response values of the RPC, and a ServicerContext. Only non-None if
        cardinality is cardinality.Cardinality.UNARY_STREAM and style is
        style.Service.EVENT.
      stream_unary_event: The implementation of the method as a callable value
        that takes a response callback to which to pass the response value of the
        RPC and a ServicerContext and returns a stream.Consumer to which the
        request values of the RPC should be passed. Only non-None if cardinality
        is cardinality.Cardinality.STREAM_UNARY and style is style.Service.EVENT.
      stream_stream_event: The implementation of the method as a callable value
        that takes a stream.Consumer to which to pass the response values of the
        RPC and a ServicerContext and returns a stream.Consumer to which the
        request values of the RPC should be passed. Only non-None if cardinality
        is cardinality.Cardinality.STREAM_STREAM and style is
        style.Service.EVENT.
    '''
    pass


class MultiMethodImplementation(abc.ABC):
    '''A general type able to service many methods.'''
    service = (lambda self, group, method, response_consumer, context: raise NotImplementedError())()


class GenericStub(abc.ABC):
    '''Affords RPC invocation via generic methods.'''
    blocking_unary_unary = (lambda self, group, method, request, timeout, metadata, with_call, protocol_options = (None, False, None): raise NotImplementedError())()
    future_unary_unary = (lambda self, group, method, request, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    inline_unary_stream = (lambda self, group, method, request, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    blocking_stream_unary = (lambda self, group, method, request_iterator, timeout, metadata, with_call, protocol_options = (None, False, None): raise NotImplementedError())()
    future_stream_unary = (lambda self, group, method, request_iterator, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    inline_stream_stream = (lambda self, group, method, request_iterator, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    event_unary_unary = (lambda self, group, method, request, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    event_unary_stream = (lambda self, group, method, request, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    event_stream_unary = (lambda self, group, method, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    event_stream_stream = (lambda self, group, method, receiver, abortion_callback, timeout, metadata, protocol_options = (None, None): raise NotImplementedError())()
    unary_unary = (lambda self, group, method: raise NotImplementedError())()
    unary_stream = (lambda self, group, method: raise NotImplementedError())()
    stream_unary = (lambda self, group, method: raise NotImplementedError())()
    stream_stream = (lambda self, group, method: raise NotImplementedError())()


class DynamicStub(abc.ABC):
    '''Affords RPC invocation via attributes corresponding to afforded methods.

    Instances of this type may be scoped to a single group so that attribute
    access is unambiguous.

    Instances of this type respond to attribute access as follows: if the
    requested attribute is the name of a unary-unary method, the value of the
    attribute will be a UnaryUnaryMultiCallable with which to invoke an RPC; if
    the requested attribute is the name of a unary-stream method, the value of the
    attribute will be a UnaryStreamMultiCallable with which to invoke an RPC; if
    the requested attribute is the name of a stream-unary method, the value of the
    attribute will be a StreamUnaryMultiCallable with which to invoke an RPC; and
    if the requested attribute is the name of a stream-stream method, the value of
    the attribute will be a StreamStreamMultiCallable with which to invoke an RPC.
    '''
    pass
