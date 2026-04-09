# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _simple_stubs.pyc (Python 3.11)

'''Functions that obviate explicit stubs and explicit channels.'''
import collections
import datetime
import logging
import os
import threading
from typing import Any, AnyStr, Callable, Dict, Iterator, Optional, Sequence, Tuple, TypeVar, Union
import grpc
from grpc.experimental import experimental_api
RequestType = TypeVar('RequestType')
ResponseType = TypeVar('ResponseType')
OptionsType = Sequence[Tuple[(str, str)]]
CacheKey = Tuple[(str, OptionsType, Optional[grpc.ChannelCredentials], Optional[grpc.Compression])]
_LOGGER = logging.getLogger(__name__)
_EVICTION_PERIOD_KEY = 'GRPC_PYTHON_MANAGED_CHANNEL_EVICTION_SECONDS'
if _EVICTION_PERIOD_KEY in os.environ:
    _EVICTION_PERIOD = datetime.timedelta(seconds = float(os.environ[_EVICTION_PERIOD_KEY]))
    _LOGGER.debug('Setting managed channel eviction period to %s', _EVICTION_PERIOD)
else:
    _EVICTION_PERIOD = datetime.timedelta(minutes = 10)
_MAXIMUM_CHANNELS_KEY = 'GRPC_PYTHON_MANAGED_CHANNEL_MAXIMUM'
if _MAXIMUM_CHANNELS_KEY in os.environ:
    _MAXIMUM_CHANNELS = int(os.environ[_MAXIMUM_CHANNELS_KEY])
    _LOGGER.debug('Setting maximum managed channels to %d', _MAXIMUM_CHANNELS)
else:
    _MAXIMUM_CHANNELS = 256
_DEFAULT_TIMEOUT_KEY = 'GRPC_PYTHON_DEFAULT_TIMEOUT_SECONDS'
if _DEFAULT_TIMEOUT_KEY in os.environ:
    _DEFAULT_TIMEOUT = float(os.environ[_DEFAULT_TIMEOUT_KEY])
    _LOGGER.debug('Setting default timeout seconds to %f', _DEFAULT_TIMEOUT)
else:
    _DEFAULT_TIMEOUT = 60

def _create_channel(target = None, options = None, channel_credentials = None, compression = ('target', str, 'options', Sequence[Tuple[(str, str)]], 'channel_credentials', Optional[grpc.ChannelCredentials], 'compression', Optional[grpc.Compression], 'return', grpc.Channel)):
    debug_msg = f'''Creating secure channel with credentials \'{channel_credentials}\', options \'{options}\' and compression \'{compression}\''''
    _LOGGER.debug(debug_msg)
    return grpc.secure_channel(target, credentials = channel_credentials, options = options, compression = compression)


class ChannelCache:
    _singleton = None
    _lock: threading.RLock = threading.RLock()
    _condition: threading.Condition = threading.Condition(lock = _lock)
    _eviction_thread: threading.Thread = threading.Event()
    
    def __init__(self):
        self._mapping = collections.OrderedDict()
        self._eviction_thread = threading.Thread(target = ChannelCache._perform_evictions, daemon = True)
        self._eviction_thread.start()

    get = (lambda : ChannelCache._lock# WARNING: Decompyle incomplete
)()
    
    def _evict_locked(self = None, key = None):
        (channel, _) = self._mapping.pop(key)
        _LOGGER.debug('Evicting channel %s with configuration %s.', channel, key)
        channel.close()
        del channel

    _perform_evictions = (lambda : ChannelCache._lockChannelCache._eviction_ready.set()if not ChannelCache._singleton._mapping:
ChannelCache._condition.wait()elif len(ChannelCache._singleton._mapping) > _MAXIMUM_CHANNELS:
key = next(iter(ChannelCache._singleton._mapping.keys()))ChannelCache._singleton._evict_locked(key)else:
(_, eviction_time) = (key,)now = datetime.datetime.now()if eviction_time <= now:
ChannelCache._singleton._evict_locked(key)None(None, None)continuetime_to_eviction = (eviction_time - now).total_seconds()ChannelCache._condition.wait(timeout = time_to_eviction)None(None, None))()
    
    def get_channel(self, target, options, channel_credentials, insecure = None, compression = None, method = staticmethod, _registered_method = ('target', str, 'options', Sequence[Tuple[(str, str)]], 'channel_credentials', Optional[grpc.ChannelCredentials], 'insecure', bool, 'compression', Optional[grpc.Compression], 'method', str, '_registered_method', bool, 'return', Tuple[(grpc.Channel, Optional[int])])):
        """Get a channel from cache or creates a new channel.

        This method also takes care of register method for channel,
          which means we'll register a new call handle if we're calling a
          non-registered method for an existing channel.

        Returns:
            A tuple with two items. The first item is the channel, second item is
              the call handle if the method is registered, None if it's not registered.
        """
        if insecure and channel_credentials:
            raise ValueError('The insecure option is mutually exclusive with the channel_credentials option. Please use one or the other.')
        if insecure:
            channel_credentials = grpc.experimental.insecure_channel_credentials()
    # WARNING: Decompyle incomplete

    
    def _test_only_channel_count(self = None):
        self._lock
        None(None, None)
        return 
        with None:
            if not None, len(self._mapping):
                pass


unary_unary = (lambda request, target, method, request_serializer, response_deserializer, options, channel_credentials, insecure, call_credentials, compression = None, wait_for_ready = None, timeout = experimental_api, metadata = (None, None, (), None, False, None, None, None, _DEFAULT_TIMEOUT, None, False), _registered_method = ('request', RequestType, 'target', str, 'method', str, 'request_serializer', Optional[Callable[([
    Any], bytes)]], 'response_deserializer', Optional[Callable[([
    bytes], Any)]], 'options', Sequence[Tuple[(AnyStr, AnyStr)]], 'channel_credentials', Optional[grpc.ChannelCredentials], 'insecure', bool, 'call_credentials', Optional[grpc.CallCredentials], 'compression', Optional[grpc.Compression], 'wait_for_ready', Optional[bool], 'timeout', Optional[float], 'metadata', Optional[Sequence[Tuple[(str, Union[(str, bytes)])]]], '_registered_method', Optional[bool], 'return', ResponseType): (channel, method_handle) = ChannelCache.get().get_channel(target, options, channel_credentials, insecure, compression, method, _registered_method)multicallable = channel.unary_unary(method, request_serializer, response_deserializer, method_handle)# WARNING: Decompyle incomplete
)()
unary_stream = (lambda request, target, method, request_serializer, response_deserializer, options, channel_credentials, insecure, call_credentials, compression = None, wait_for_ready = None, timeout = experimental_api, metadata = (None, None, (), None, False, None, None, None, _DEFAULT_TIMEOUT, None, False), _registered_method = ('request', RequestType, 'target', str, 'method', str, 'request_serializer', Optional[Callable[([
    Any], bytes)]], 'response_deserializer', Optional[Callable[([
    bytes], Any)]], 'options', Sequence[Tuple[(AnyStr, AnyStr)]], 'channel_credentials', Optional[grpc.ChannelCredentials], 'insecure', bool, 'call_credentials', Optional[grpc.CallCredentials], 'compression', Optional[grpc.Compression], 'wait_for_ready', Optional[bool], 'timeout', Optional[float], 'metadata', Optional[Sequence[Tuple[(str, Union[(str, bytes)])]]], '_registered_method', Optional[bool], 'return', Iterator[ResponseType]): (channel, method_handle) = ChannelCache.get().get_channel(target, options, channel_credentials, insecure, compression, method, _registered_method)multicallable = channel.unary_stream(method, request_serializer, response_deserializer, method_handle)# WARNING: Decompyle incomplete
)()
stream_unary = (lambda request_iterator, target, method, request_serializer, response_deserializer, options, channel_credentials, insecure, call_credentials, compression = None, wait_for_ready = None, timeout = experimental_api, metadata = (None, None, (), None, False, None, None, None, _DEFAULT_TIMEOUT, None, False), _registered_method = ('request_iterator', Iterator[RequestType], 'target', str, 'method', str, 'request_serializer', Optional[Callable[([
    Any], bytes)]], 'response_deserializer', Optional[Callable[([
    bytes], Any)]], 'options', Sequence[Tuple[(AnyStr, AnyStr)]], 'channel_credentials', Optional[grpc.ChannelCredentials], 'insecure', bool, 'call_credentials', Optional[grpc.CallCredentials], 'compression', Optional[grpc.Compression], 'wait_for_ready', Optional[bool], 'timeout', Optional[float], 'metadata', Optional[Sequence[Tuple[(str, Union[(str, bytes)])]]], '_registered_method', Optional[bool], 'return', ResponseType): (channel, method_handle) = ChannelCache.get().get_channel(target, options, channel_credentials, insecure, compression, method, _registered_method)multicallable = channel.stream_unary(method, request_serializer, response_deserializer, method_handle)# WARNING: Decompyle incomplete
)()
stream_stream = (lambda request_iterator, target, method, request_serializer, response_deserializer, options, channel_credentials, insecure, call_credentials, compression = None, wait_for_ready = None, timeout = experimental_api, metadata = (None, None, (), None, False, None, None, None, _DEFAULT_TIMEOUT, None, False), _registered_method = ('request_iterator', Iterator[RequestType], 'target', str, 'method', str, 'request_serializer', Optional[Callable[([
    Any], bytes)]], 'response_deserializer', Optional[Callable[([
    bytes], Any)]], 'options', Sequence[Tuple[(AnyStr, AnyStr)]], 'channel_credentials', Optional[grpc.ChannelCredentials], 'insecure', bool, 'call_credentials', Optional[grpc.CallCredentials], 'compression', Optional[grpc.Compression], 'wait_for_ready', Optional[bool], 'timeout', Optional[float], 'metadata', Optional[Sequence[Tuple[(str, Union[(str, bytes)])]]], '_registered_method', Optional[bool], 'return', Iterator[ResponseType]): (channel, method_handle) = ChannelCache.get().get_channel(target, options, channel_credentials, insecure, compression, method, _registered_method)multicallable = channel.stream_stream(method, request_serializer, response_deserializer, method_handle)# WARNING: Decompyle incomplete
)()
