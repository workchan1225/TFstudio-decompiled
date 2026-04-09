# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _interceptor.pyc (Python 3.11)

'''Implementation of gRPC Python interceptors.'''
import collections
import sys
import types
from typing import Any, Callable, Optional, Sequence, Tuple, Union
import grpc
from _typing import DeserializingFunction
from _typing import DoneCallbackType
from _typing import MetadataType
from _typing import RequestIterableType
from _typing import SerializingFunction

class _ServicePipeline(object):
    interceptors: Tuple[grpc.ServerInterceptor] = '_ServicePipeline'
    
    def __init__(self = None, interceptors = None):
        self.interceptors = tuple(interceptors)

    
    def _continuation(self = None, thunk = None, index = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _intercept_at(self = None, thunk = None, index = None, context = ('thunk', Callable, 'index', int, 'context', grpc.HandlerCallDetails, 'return', grpc.RpcMethodHandler)):
        if index < len(self.interceptors):
            interceptor = self.interceptors[index]
            thunk = self._continuation(thunk, index + 1)
            return interceptor.intercept_service(thunk, context)
        return thunk(context)

    
    def execute(self = None, thunk = None, context = None):
        return self._intercept_at(thunk, 0, context)



def service_pipeline(interceptors = None):
    return _ServicePipeline(interceptors) if interceptors else None


def _ClientCallDetails():
    '''_ClientCallDetails'''
    pass

_ClientCallDetails = <NODE:27>(_ClientCallDetails, '_ClientCallDetails', collections.namedtuple('_ClientCallDetails', ('method', 'timeout', 'metadata', 'credentials', 'wait_for_ready', 'compression')), grpc.ClientCallDetails)

def _unwrap_client_call_details(call_details = None, default_details = None):
    
    try:
        method = call_details.method
    except AttributeError:
        method = default_details.method

    
    try:
        timeout = call_details.timeout
    except AttributeError:
        timeout = default_details.timeout

    
    try:
        metadata = call_details.metadata
    except AttributeError:
        metadata = default_details.metadata

    
    try:
        credentials = call_details.credentials
    except AttributeError:
        credentials = default_details.credentials

    
    try:
        wait_for_ready = call_details.wait_for_ready
    except AttributeError:
        wait_for_ready = default_details.wait_for_ready

    
    try:
        compression = call_details.compression
    except AttributeError:
        compression = default_details.compression

    return (method, timeout, metadata, credentials, wait_for_ready, compression)


class _FailureOutcome(grpc.Call, grpc.Future, grpc.RpcError):
    pass
# WARNING: Decompyle incomplete


class _UnaryOutcome(grpc.Future, grpc.Call):
    _call: grpc.Call = '_UnaryOutcome'
    
    def __init__(self = None, response = None, call = None):
        self._response = response
        self._call = call

    
    def initial_metadata(self = None):
        return self._call.initial_metadata()

    
    def trailing_metadata(self = None):
        return self._call.trailing_metadata()

    
    def code(self = None):
        return self._call.code()

    
    def details(self = None):
        return self._call.details()

    
    def is_active(self = None):
        return self._call.is_active()

    
    def time_remaining(self = None):
        return self._call.time_remaining()

    
    def cancel(self = None):
        return self._call.cancel()

    
    def add_callback(self = None, callback = None):
        return self._call.add_callback(callback)

    
    def cancelled(self = None):
        return False

    
    def running(self = None):
        return False

    
    def done(self = None):
        return True

    
    def result(self = None, ignored_timeout = None):
        return self._response

    
    def exception(self = None, ignored_timeout = None):
        pass

    
    def traceback(self = None, ignored_timeout = None):
        pass

    
    def add_done_callback(self = None, fn = None):
        fn(self)



class _UnaryUnaryMultiCallable(grpc.UnaryUnaryMultiCallable):
    _interceptor: grpc.UnaryUnaryClientInterceptor = '_UnaryUnaryMultiCallable'
    
    def __init__(self = None, thunk = None, method = None, interceptor = ('thunk', Callable, 'method', str, 'interceptor', grpc.UnaryUnaryClientInterceptor)):
        self._thunk = thunk
        self._method = method
        self._interceptor = interceptor

    
    def __call__(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Any)):
        (response, ignored_call) = self._with_call(request, timeout = timeout, metadata = metadata, credentials = credentials, wait_for_ready = wait_for_ready, compression = compression)
        return response

    
    def _with_call(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Tuple[(Any, grpc.Call)])):
        pass
    # WARNING: Decompyle incomplete

    
    def with_call(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Tuple[(Any, grpc.Call)])):
        return self._with_call(request, timeout = timeout, metadata = metadata, credentials = credentials, wait_for_ready = wait_for_ready, compression = compression)

    
    def future(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Any)):
        pass
    # WARNING: Decompyle incomplete



class _UnaryStreamMultiCallable(grpc.UnaryStreamMultiCallable):
    _interceptor: grpc.UnaryStreamClientInterceptor = '_UnaryStreamMultiCallable'
    
    def __init__(self = None, thunk = None, method = None, interceptor = ('thunk', Callable, 'method', str, 'interceptor', grpc.UnaryStreamClientInterceptor)):
        self._thunk = thunk
        self._method = method
        self._interceptor = interceptor

    
    def __call__(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression])):
        pass
    # WARNING: Decompyle incomplete



class _StreamUnaryMultiCallable(grpc.StreamUnaryMultiCallable):
    _interceptor: grpc.StreamUnaryClientInterceptor = '_StreamUnaryMultiCallable'
    
    def __init__(self = None, thunk = None, method = None, interceptor = ('thunk', Callable, 'method', str, 'interceptor', grpc.StreamUnaryClientInterceptor)):
        self._thunk = thunk
        self._method = method
        self._interceptor = interceptor

    
    def __call__(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request_iterator', RequestIterableType, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Any)):
        (response, ignored_call) = self._with_call(request_iterator, timeout = timeout, metadata = metadata, credentials = credentials, wait_for_ready = wait_for_ready, compression = compression)
        return response

    
    def _with_call(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request_iterator', RequestIterableType, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Tuple[(Any, grpc.Call)])):
        pass
    # WARNING: Decompyle incomplete

    
    def with_call(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request_iterator', RequestIterableType, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Tuple[(Any, grpc.Call)])):
        return self._with_call(request_iterator, timeout = timeout, metadata = metadata, credentials = credentials, wait_for_ready = wait_for_ready, compression = compression)

    
    def future(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request_iterator', RequestIterableType, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Any)):
        pass
    # WARNING: Decompyle incomplete



class _StreamStreamMultiCallable(grpc.StreamStreamMultiCallable):
    _interceptor: grpc.StreamStreamClientInterceptor = '_StreamStreamMultiCallable'
    
    def __init__(self = None, thunk = None, method = None, interceptor = ('thunk', Callable, 'method', str, 'interceptor', grpc.StreamStreamClientInterceptor)):
        self._thunk = thunk
        self._method = method
        self._interceptor = interceptor

    
    def __call__(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request_iterator', RequestIterableType, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression])):
        pass
    # WARNING: Decompyle incomplete



class _Channel(grpc.Channel):
    _interceptor: Union[(grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor, grpc.StreamStreamClientInterceptor, grpc.StreamUnaryClientInterceptor)] = '_Channel'
    
    def __init__(self = None, channel = None, interceptor = None):
        self._channel = channel
        self._interceptor = interceptor

    
    def subscribe(self = None, callback = None, try_to_connect = None):
        self._channel.subscribe(callback, try_to_connect = try_to_connect)

    
    def unsubscribe(self = None, callback = None):
        self._channel.unsubscribe(callback)

    
    def unary_unary(self = None, method = None, request_serializer = None, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', grpc.UnaryUnaryMultiCallable)):
        pass
    # WARNING: Decompyle incomplete

    
    def unary_stream(self = None, method = None, request_serializer = None, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', grpc.UnaryStreamMultiCallable)):
        pass
    # WARNING: Decompyle incomplete

    
    def stream_unary(self = None, method = None, request_serializer = None, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', grpc.StreamUnaryMultiCallable)):
        pass
    # WARNING: Decompyle incomplete

    
    def stream_stream(self = None, method = None, request_serializer = None, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', grpc.StreamStreamMultiCallable)):
        pass
    # WARNING: Decompyle incomplete

    
    def _close(self):
        self._channel.close()

    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close()
        return False

    
    def close(self):
        self._channel.close()



def intercept_channel(channel = None, *interceptors):
    for interceptor in reversed(list(interceptors)):
        if not isinstance(interceptor, grpc.UnaryUnaryClientInterceptor) and isinstance(interceptor, grpc.UnaryStreamClientInterceptor) and isinstance(interceptor, grpc.StreamUnaryClientInterceptor) and isinstance(interceptor, grpc.StreamStreamClientInterceptor):
            error_msg = 'interceptor must be grpc.UnaryUnaryClientInterceptor or grpc.UnaryStreamClientInterceptor or grpc.StreamUnaryClientInterceptor or grpc.StreamStreamClientInterceptor'
            raise TypeError(error_msg)
        channel = _Channel(channel, interceptor)
        return channel
