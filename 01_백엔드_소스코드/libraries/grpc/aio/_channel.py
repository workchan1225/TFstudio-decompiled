# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _channel.pyc (Python 3.11)

'''Invocation-side implementation of gRPC Asyncio Python.'''
import asyncio
import sys
from typing import Any, Iterable, List, Optional, Sequence
import grpc
from grpc import _common
from grpc import _compression
from grpc import _grpcio_metadata
from grpc._cython import cygrpc
from  import _base_call
from  import _base_channel
from _call import StreamStreamCall
from _call import StreamUnaryCall
from _call import UnaryStreamCall
from _call import UnaryUnaryCall
from _interceptor import ClientInterceptor
from _interceptor import InterceptedStreamStreamCall
from _interceptor import InterceptedStreamUnaryCall
from _interceptor import InterceptedUnaryStreamCall
from _interceptor import InterceptedUnaryUnaryCall
from _interceptor import StreamStreamClientInterceptor
from _interceptor import StreamUnaryClientInterceptor
from _interceptor import UnaryStreamClientInterceptor
from _interceptor import UnaryUnaryClientInterceptor
from _metadata import Metadata
from _typing import ChannelArgumentType
from _typing import DeserializingFunction
from _typing import MetadataType
from _typing import RequestIterableType
from _typing import RequestType
from _typing import ResponseType
from _typing import SerializingFunction
from _utils import _timeout_to_deadline
_USER_AGENT = 'grpc-python-asyncio/{}'.format(_grpcio_metadata.__version__)
if sys.version_info[1] < 7:
    
    def _all_tasks():
        return asyncio.Task.all_tasks()

else:
    
    def _all_tasks():
        return asyncio.all_tasks()


def _augment_channel_arguments(base_options = None, compression = None):
    compression_channel_argument = _compression.create_channel_option(compression)
    user_agent_channel_argument = ((cygrpc.ChannelArgKey.primary_user_agent_string, _USER_AGENT),)
    return tuple(base_options) + compression_channel_argument + user_agent_channel_argument


class _BaseMultiCallable:
    _loop: asyncio.AbstractEventLoop = 'Base class of all multi callable objects.\n\n    Handles the initialization logic and stores common attributes.\n    '
    
    def __init__(self, channel, method, request_serializer, response_deserializer = None, interceptors = None, references = None, loop = ('channel', cygrpc.AioChannel, 'method', bytes, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], 'interceptors', Optional[Sequence[ClientInterceptor]], 'references', List[Any], 'loop', asyncio.AbstractEventLoop, 'return', None)):
        self._loop = loop
        self._channel = channel
        self._method = method
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer
        self._interceptors = interceptors
        self._references = references

    _init_metadata = (lambda metadata = None, compression = None: if not metadata:
passmetadata = Metadata()if isinstance(metadata, Metadata) and isinstance(metadata, Sequence):
metadata = Metadata.from_tuple(tuple(metadata))# WARNING: Decompyle incomplete
)()


class UnaryUnaryMultiCallable(_base_channel.UnaryUnaryMultiCallable, _BaseMultiCallable):
    
    def __call__(self = None, request = None, *, timeout, metadata, credentials, wait_for_ready, compression):
        metadata = self._init_metadata(metadata, compression)
        if not self._interceptors:
            call = UnaryUnaryCall(request, _timeout_to_deadline(timeout), metadata, credentials, wait_for_ready, self._channel, self._method, self._request_serializer, self._response_deserializer, self._loop)
        else:
            call = InterceptedUnaryUnaryCall(self._interceptors, request, timeout, metadata, credentials, wait_for_ready, self._channel, self._method, self._request_serializer, self._response_deserializer, self._loop)
        return call



class UnaryStreamMultiCallable(_base_channel.UnaryStreamMultiCallable, _BaseMultiCallable):
    
    def __call__(self = None, request = None, *, timeout, metadata, credentials, wait_for_ready, compression):
        metadata = self._init_metadata(metadata, compression)
        if not self._interceptors:
            call = UnaryStreamCall(request, _timeout_to_deadline(timeout), metadata, credentials, wait_for_ready, self._channel, self._method, self._request_serializer, self._response_deserializer, self._loop)
        else:
            call = InterceptedUnaryStreamCall(self._interceptors, request, timeout, metadata, credentials, wait_for_ready, self._channel, self._method, self._request_serializer, self._response_deserializer, self._loop)
        return call



class StreamUnaryMultiCallable(_base_channel.StreamUnaryMultiCallable, _BaseMultiCallable):
    
    def __call__(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None, None), compression = ('request_iterator', Optional[RequestIterableType], 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', _base_call.StreamUnaryCall)):
        metadata = self._init_metadata(metadata, compression)
        if not self._interceptors:
            call = StreamUnaryCall(request_iterator, _timeout_to_deadline(timeout), metadata, credentials, wait_for_ready, self._channel, self._method, self._request_serializer, self._response_deserializer, self._loop)
        else:
            call = InterceptedStreamUnaryCall(self._interceptors, request_iterator, timeout, metadata, credentials, wait_for_ready, self._channel, self._method, self._request_serializer, self._response_deserializer, self._loop)
        return call



class StreamStreamMultiCallable(_base_channel.StreamStreamMultiCallable, _BaseMultiCallable):
    
    def __call__(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None, None), compression = ('request_iterator', Optional[RequestIterableType], 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', _base_call.StreamStreamCall)):
        metadata = self._init_metadata(metadata, compression)
        if not self._interceptors:
            call = StreamStreamCall(request_iterator, _timeout_to_deadline(timeout), metadata, credentials, wait_for_ready, self._channel, self._method, self._request_serializer, self._response_deserializer, self._loop)
        else:
            call = InterceptedStreamStreamCall(self._interceptors, request_iterator, timeout, metadata, credentials, wait_for_ready, self._channel, self._method, self._request_serializer, self._response_deserializer, self._loop)
        return call



class Channel(_base_channel.Channel):
    _stream_stream_interceptors: List[StreamStreamClientInterceptor] = 'Channel'
    
    def __init__(self, target, options = None, credentials = None, compression = None, interceptors = ('target', str, 'options', ChannelArgumentType, 'credentials', Optional[grpc.ChannelCredentials], 'compression', Optional[grpc.Compression], 'interceptors', Optional[Sequence[ClientInterceptor]])):
        '''Constructor.

        Args:
          target: The target to which to connect.
          options: Configuration options for the channel.
          credentials: A cygrpc.ChannelCredentials or None.
          compression: An optional value indicating the compression method to be
            used over the lifetime of the channel.
          interceptors: An optional list of interceptors that would be used for
            intercepting any RPC executed with that channel.
        '''
        self._unary_unary_interceptors = []
        self._unary_stream_interceptors = []
        self._stream_unary_interceptors = []
        self._stream_stream_interceptors = []
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
    # WARNING: Decompyle incomplete

    
    async def _close(self, grace):
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None, grace = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __del__(self):
        if not hasattr(self, '_channel') or self._channel.closed():
            self._channel.close()
            return None
        return None

    
    def get_state(self = None, try_to_connect = None):
        result = self._channel.check_connectivity_state(try_to_connect)
        return _common.CYGRPC_CONNECTIVITY_STATE_TO_CHANNEL_CONNECTIVITY[result]

    
    async def wait_for_state_change(self = None, last_observed_state = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def channel_ready(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_registered_call_handle(self = None, method = None):
        pass

    
    def unary_unary(self = None, method = None, request_serializer = None, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', UnaryUnaryMultiCallable)):
        return UnaryUnaryMultiCallable(self._channel, _common.encode(method), request_serializer, response_deserializer, self._unary_unary_interceptors, [
            self], self._loop)

    
    def unary_stream(self = None, method = None, request_serializer = None, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', UnaryStreamMultiCallable)):
        return UnaryStreamMultiCallable(self._channel, _common.encode(method), request_serializer, response_deserializer, self._unary_stream_interceptors, [
            self], self._loop)

    
    def stream_unary(self = None, method = None, request_serializer = None, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', StreamUnaryMultiCallable)):
        return StreamUnaryMultiCallable(self._channel, _common.encode(method), request_serializer, response_deserializer, self._stream_unary_interceptors, [
            self], self._loop)

    
    def stream_stream(self = None, method = None, request_serializer = None, response_deserializer = (None, None, False), _registered_method = ('method', str, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_method', Optional[bool], 'return', StreamStreamMultiCallable)):
        return StreamStreamMultiCallable(self._channel, _common.encode(method), request_serializer, response_deserializer, self._stream_stream_interceptors, [
            self], self._loop)



def insecure_channel(target = None, options = None, compression = None, interceptors = (None, None, None)):
    '''Creates an insecure asynchronous Channel to a server.

    Args:
      target: The server address
      options: An optional list of key-value pairs (:term:`channel_arguments`
        in gRPC Core runtime) to configure the channel.
      compression: An optional value indicating the compression method to be
        used over the lifetime of the channel.
      interceptors: An optional sequence of interceptors that will be executed for
        any call executed with this channel.

    Returns:
      A Channel.
    '''
    pass
# WARNING: Decompyle incomplete


def secure_channel(target = None, credentials = None, options = None, compression = (None, None, None), interceptors = ('target', str, 'credentials', grpc.ChannelCredentials, 'options', Optional[ChannelArgumentType], 'compression', Optional[grpc.Compression], 'interceptors', Optional[Sequence[ClientInterceptor]])):
    '''Creates a secure asynchronous Channel to a server.

    Args:
      target: The server address.
      credentials: A ChannelCredentials instance.
      options: An optional list of key-value pairs (:term:`channel_arguments`
        in gRPC Core runtime) to configure the channel.
      compression: An optional value indicating the compression method to be
        used over the lifetime of the channel.
      interceptors: An optional sequence of interceptors that will be executed for
        any call executed with this channel.

    Returns:
      An aio.Channel.
    '''
    pass
# WARNING: Decompyle incomplete
