# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _channel.pyc (Python 3.11)

'''Invocation-side implementation of gRPC Python.'''
import copy
import functools
import logging
import os
import sys
import threading
import time
import types
from typing import Any, Callable, Dict, Iterator, List, Optional, Sequence, Set, Tuple, Union
import grpc
from grpc import _common
from grpc import _compression
from grpc import _grpcio_metadata
from grpc import _observability
from grpc._cython import cygrpc
from grpc._typing import ChannelArgumentType
from grpc._typing import DeserializingFunction
from grpc._typing import IntegratedCallFactory
from grpc._typing import MetadataType
from grpc._typing import NullaryCallbackType
from grpc._typing import ResponseType
from grpc._typing import SerializingFunction
from grpc._typing import UserTag
import grpc.experimental as grpc
_LOGGER = logging.getLogger(__name__)
_USER_AGENT = 'grpc-python/{}'.format(_grpcio_metadata.__version__)
_EMPTY_FLAGS = 0
_DEFAULT_SINGLE_THREADED_UNARY_STREAM = os.getenv('GRPC_SINGLE_THREADED_UNARY_STREAM') is not None
_UNARY_UNARY_INITIAL_DUE = (cygrpc.OperationType.send_initial_metadata, cygrpc.OperationType.send_message, cygrpc.OperationType.send_close_from_client, cygrpc.OperationType.receive_initial_metadata, cygrpc.OperationType.receive_message, cygrpc.OperationType.receive_status_on_client)
_UNARY_STREAM_INITIAL_DUE = (cygrpc.OperationType.send_initial_metadata, cygrpc.OperationType.send_message, cygrpc.OperationType.send_close_from_client, cygrpc.OperationType.receive_initial_metadata, cygrpc.OperationType.receive_status_on_client)
_STREAM_UNARY_INITIAL_DUE = (cygrpc.OperationType.send_initial_metadata, cygrpc.OperationType.receive_initial_metadata, cygrpc.OperationType.receive_message, cygrpc.OperationType.receive_status_on_client)
_STREAM_STREAM_INITIAL_DUE = (cygrpc.OperationType.send_initial_metadata, cygrpc.OperationType.receive_initial_metadata, cygrpc.OperationType.receive_status_on_client)
_CHANNEL_SUBSCRIPTION_CALLBACK_ERROR_LOG_MESSAGE = 'Exception calling channel subscription callback!'
_OK_RENDEZVOUS_REPR_FORMAT = '<{} of RPC that terminated with:\n\tstatus = {}\n\tdetails = "{}"\n>'
_NON_OK_RENDEZVOUS_REPR_FORMAT = '<{} of RPC that terminated with:\n\tstatus = {}\n\tdetails = "{}"\n\tdebug_error_string = "{}"\n>'

def _deadline(timeout = None):
    pass
# WARNING: Decompyle incomplete


def _unknown_code_details(unknown_cygrpc_code = None, details = None):
    return 'Server sent unknown code {} and details "{}"'.format(unknown_cygrpc_code, details)


class _RPCState(object):
    target: Optional[str] = '_RPCState'
    
    def __init__(self, due, initial_metadata = None, trailing_metadata = None, code = None, details = ('due', Sequence[cygrpc.OperationType], 'initial_metadata', Optional[MetadataType], 'trailing_metadata', Optional[MetadataType], 'code', Optional[grpc.StatusCode], 'details', Optional[str])):
        self.condition = threading.Condition()
        self.due = set(due)
        self.initial_metadata = initial_metadata
        self.response = None
        self.trailing_metadata = trailing_metadata
        self.code = code
        self.details = details
        self.debug_error_string = None
        self.rpc_start_time = None
        self.rpc_end_time = None
        self.method = None
        self.target = None
        self.cancelled = False
        self.callbacks = []
        self.fork_epoch = cygrpc.get_fork_epoch()

    
    def reset_postfork_child(self):
        self.condition = threading.Condition()



def _abort(state = None, code = None, details = None):
    pass
# WARNING: Decompyle incomplete


def _handle_event(event = None, state = None, response_deserializer = None):
    callbacks = []
# WARNING: Decompyle incomplete


def _event_handler(state = None, response_deserializer = None):
    pass
# WARNING: Decompyle incomplete


def _consume_request_iterator(request_iterator, state = None, call = None, request_serializer = None, event_handler = ('request_iterator', Iterator, 'state', _RPCState, 'call', Union[(cygrpc.IntegratedCall, cygrpc.SegregatedCall)], 'request_serializer', SerializingFunction, 'event_handler', Optional[UserTag], 'return', None)):
    '''Consume a request supplied by the user.'''
    pass
# WARNING: Decompyle incomplete


def _rpc_state_string(class_name = None, rpc_state = None):
    '''Calculates error string for RPC.'''
    rpc_state.condition
# WARNING: Decompyle incomplete


class _InactiveRpcError(grpc.Future, grpc.Call, grpc.RpcError):
    _state: _RPCState = 'An RPC error not tied to the execution of a particular RPC.\n\n    The RPC represented by the state object must not be in-progress or\n    cancelled.\n\n    Attributes:\n      _state: An instance of _RPCState.\n    '
    
    def __init__(self = None, state = None):
        state.condition
        self._state = _RPCState((), copy.deepcopy(state.initial_metadata), copy.deepcopy(state.trailing_metadata), state.code, copy.deepcopy(state.details))
        self._state.response = copy.copy(state.response)
        self._state.debug_error_string = copy.copy(state.debug_error_string)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def initial_metadata(self = None):
        return self._state.initial_metadata

    
    def trailing_metadata(self = None):
        return self._state.trailing_metadata

    
    def code(self = None):
        return self._state.code

    
    def details(self = None):
        return _common.decode(self._state.details)

    
    def debug_error_string(self = None):
        return _common.decode(self._state.debug_error_string)

    
    def _repr(self = None):
        return _rpc_state_string(self.__class__.__name__, self._state)

    
    def __repr__(self = None):
        return self._repr()

    
    def __str__(self = None):
        return self._repr()

    
    def cancel(self = None):
        '''See grpc.Future.cancel.'''
        return False

    
    def cancelled(self = None):
        '''See grpc.Future.cancelled.'''
        return False

    
    def running(self = None):
        '''See grpc.Future.running.'''
        return False

    
    def done(self = None):
        '''See grpc.Future.done.'''
        return True

    
    def result(self = None, timeout = None):
        '''See grpc.Future.result.'''
        raise self

    
    def exception(self = None, timeout = None):
        '''See grpc.Future.exception.'''
        return self

    
    def traceback(self = None, timeout = None):
        '''See grpc.Future.traceback.'''
        
        try:
            raise self
        except grpc.RpcError:
            return 


    
    def add_done_callback(self = None, fn = None, timeout = None):
        '''See grpc.Future.add_done_callback.'''
        fn(self)



class _Rendezvous(grpc.RpcContext, grpc.RpcError):
    pass
# WARNING: Decompyle incomplete


class _SingleThreadedRendezvous(grpc.Future, grpc.Call, _Rendezvous):
    _state: _RPCState = 'An RPC iterator operating entirely on a single thread.\n\n    The __next__ method of _SingleThreadedRendezvous does not depend on the\n    existence of any other thread, including the "channel spin thread".\n    However, this means that its interface is entirely synchronous. So this\n    class cannot completely fulfill the grpc.Future interface. The result,\n    exception, and traceback methods will never block and will instead raise\n    an exception if calling the method would result in blocking.\n\n    This means that these methods are safe to call from add_done_callback\n    handlers.\n    '
    
    def _is_complete(self = None):
        return self._state.code is not None

    
    def cancelled(self = None):
        self._state.condition
        None(None, None)
        return 
        with None:
            if not None, self._state.cancelled:
                pass

    
    def running(self = None):
        self._state.condition
        None(None, None)
        return 
        with None:
            if not None, self._state.code is None:
                pass

    
    def done(self = None):
        self._state.condition
        None(None, None)
        return 
        with None:
            if not None, self._state.code is not None:
                pass

    
    def result(self = None, timeout = None):
        '''Returns the result of the computation or raises its exception.

        This method will never block. Instead, it will raise an exception
        if calling this method would otherwise result in blocking.

        Since this method will never block, any `timeout` argument passed will
        be ignored.
        '''
        del timeout
        self._state.condition
        if not self._is_complete():
            error_msg = '_SingleThreadedRendezvous only supports result() when the RPC is complete.'
            raise grpc.experimental.UsageError(error_msg)
        if self._state.code is grpc.StatusCode.OK:
            None(None, None)
            return 
        if None._state.cancelled:
            raise grpc.FutureCancelledError()
        raise self
        with None:
            if not None:
                pass

    
    def exception(self = None, timeout = None):
        '''Return the exception raised by the computation.

        This method will never block. Instead, it will raise an exception
        if calling this method would otherwise result in blocking.

        Since this method will never block, any `timeout` argument passed will
        be ignored.
        '''
        del timeout
        self._state.condition
        if not self._is_complete():
            error_msg = '_SingleThreadedRendezvous only supports exception() when the RPC is complete.'
            raise grpc.experimental.UsageError(error_msg)
        if self._state.code is grpc.StatusCode.OK:
            None(None, None)
            return None
        if None._state.cancelled:
            raise grpc.FutureCancelledError()
        None(None, None)
        return 
        with None:
            if not None, self:
                pass

    
    def traceback(self = None, timeout = None):
        '''Access the traceback of the exception raised by the computation.

        This method will never block. Instead, it will raise an exception
        if calling this method would otherwise result in blocking.

        Since this method will never block, any `timeout` argument passed will
        be ignored.
        '''
        del timeout
        self._state.condition
        if not self._is_complete():
            msg = '_SingleThreadedRendezvous only supports traceback() when the RPC is complete.'
            raise grpc.experimental.UsageError(msg)
        if self._state.code is grpc.StatusCode.OK:
            None(None, None)
            return None
        if None._state.cancelled:
            raise grpc.FutureCancelledError()
        raise self
        except grpc.RpcError:
            None(None, None)
            return 
        with None:
            if not None:
                pass

    
    def add_done_callback(self = None, fn = None):
        self._state.condition
    # WARNING: Decompyle incomplete

    
    def initial_metadata(self = None):
        '''See grpc.Call.initial_metadata'''
        self._state.condition
    # WARNING: Decompyle incomplete

    
    def trailing_metadata(self = None):
        '''See grpc.Call.trailing_metadata'''
        self._state.condition
    # WARNING: Decompyle incomplete

    
    def code(self = None):
        '''See grpc.Call.code'''
        self._state.condition
    # WARNING: Decompyle incomplete

    
    def details(self = None):
        '''See grpc.Call.details'''
        self._state.condition
    # WARNING: Decompyle incomplete

    
    def _consume_next_event(self = None):
        event = self._call.next_event()
        self._state.condition
        callbacks = _handle_event(event, self._state, self._response_deserializer)
        for callback in callbacks:
            callback()
            None(None, None)
        with None:
            if not None:
                pass
        return event

    
    def _next_response(self = None):
        self._consume_next_event()
        self._state.condition
    # WARNING: Decompyle incomplete

    
    def _next(self = None):
        self._state.condition
    # WARNING: Decompyle incomplete

    
    def debug_error_string(self = None):
        self._state.condition
    # WARNING: Decompyle incomplete



class _MultiThreadedRendezvous(grpc.Future, grpc.Call, _Rendezvous):
    _state: _RPCState = 'An RPC iterator that depends on a channel spin thread.\n\n    This iterator relies upon a per-channel thread running in the background,\n    dequeueing events from the completion queue, and notifying threads waiting\n    on the threading.Condition object in the _RPCState object.\n\n    This extra thread allows _MultiThreadedRendezvous to fulfill the grpc.Future interface\n    and to mediate a bidirection streaming RPC.\n    '
    
    def initial_metadata(self = None):
        '''See grpc.Call.initial_metadata'''
        pass
    # WARNING: Decompyle incomplete

    
    def trailing_metadata(self = None):
        '''See grpc.Call.trailing_metadata'''
        pass
    # WARNING: Decompyle incomplete

    
    def code(self = None):
        '''See grpc.Call.code'''
        pass
    # WARNING: Decompyle incomplete

    
    def details(self = None):
        '''See grpc.Call.details'''
        pass
    # WARNING: Decompyle incomplete

    
    def debug_error_string(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def cancelled(self = None):
        self._state.condition
        None(None, None)
        return 
        with None:
            if not None, self._state.cancelled:
                pass

    
    def running(self = None):
        self._state.condition
        None(None, None)
        return 
        with None:
            if not None, self._state.code is None:
                pass

    
    def done(self = None):
        self._state.condition
        None(None, None)
        return 
        with None:
            if not None, self._state.code is not None:
                pass

    
    def _is_complete(self = None):
        return self._state.code is not None

    
    def result(self = None, timeout = None):
        '''Returns the result of the computation or raises its exception.

        See grpc.Future.result for the full API contract.
        '''
        self._state.condition
        timed_out = _common.wait(self._state.condition.wait, self._is_complete, timeout = timeout)
        if timed_out:
            raise grpc.FutureTimeoutError()
        if self._state.code is grpc.StatusCode.OK:
            None(None, None)
            return 
        if None._state.cancelled:
            raise grpc.FutureCancelledError()
        raise self
        with None:
            if not None:
                pass

    
    def exception(self = None, timeout = None):
        '''Return the exception raised by the computation.

        See grpc.Future.exception for the full API contract.
        '''
        self._state.condition
        timed_out = _common.wait(self._state.condition.wait, self._is_complete, timeout = timeout)
        if timed_out:
            raise grpc.FutureTimeoutError()
        if self._state.code is grpc.StatusCode.OK:
            None(None, None)
            return None
        if None._state.cancelled:
            raise grpc.FutureCancelledError()
        None(None, None)
        return 
        with None:
            if not None, self:
                pass

    
    def traceback(self = None, timeout = None):
        '''Access the traceback of the exception raised by the computation.

        See grpc.future.traceback for the full API contract.
        '''
        self._state.condition
        timed_out = _common.wait(self._state.condition.wait, self._is_complete, timeout = timeout)
        if timed_out:
            raise grpc.FutureTimeoutError()
        if self._state.code is grpc.StatusCode.OK:
            None(None, None)
            return None
        if None._state.cancelled:
            raise grpc.FutureCancelledError()
        raise self
        except grpc.RpcError:
            None(None, None)
            return 
        with None:
            if not None:
                pass

    
    def add_done_callback(self = None, fn = None):
        self._state.condition
    # WARNING: Decompyle incomplete

    
    def _next(self = None):
        pass
    # WARNING: Decompyle incomplete



def _start_unary_request(request = None, timeout = None, request_serializer = None):
    deadline = _deadline(timeout)
    serialized_request = _common.serialize(request, request_serializer)
# WARNING: Decompyle incomplete


def _end_unary_response_blocking(state = None, call = None, with_call = None, deadline = ('state', _RPCState, 'call', cygrpc.SegregatedCall, 'with_call', bool, 'deadline', Optional[float], 'return', Union[(ResponseType, Tuple[(ResponseType, grpc.Call)])])):
    if state.code is grpc.StatusCode.OK:
        if with_call:
            rendezvous = _MultiThreadedRendezvous(state, call, None, deadline)
            return (state.response, rendezvous)
        return None.response
    raise None(state)


def _stream_unary_invocation_operations(metadata = None, initial_metadata_flags = None):
    return ((cygrpc.SendInitialMetadataOperation(metadata, initial_metadata_flags), cygrpc.ReceiveMessageOperation(_EMPTY_FLAGS), cygrpc.ReceiveStatusOnClientOperation(_EMPTY_FLAGS)), (cygrpc.ReceiveInitialMetadataOperation(_EMPTY_FLAGS),))


def _stream_unary_invocation_operations_and_tags(metadata = None, initial_metadata_flags = None):
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(_stream_unary_invocation_operations(metadata, initial_metadata_flags)())


def _determine_deadline(user_deadline = None):
    parent_deadline = cygrpc.get_deadline_from_context()
# WARNING: Decompyle incomplete


class _UnaryUnaryMultiCallable(grpc.UnaryUnaryMultiCallable):
    _registered_call_handle: Optional[int] = '_UnaryUnaryMultiCallable'
    __slots__ = [
        '_channel',
        '_managed_call',
        '_method',
        '_target',
        '_request_serializer',
        '_response_deserializer',
        '_context']
    
    def __init__(self, channel, managed_call, method, target = None, request_serializer = None, response_deserializer = None, _registered_call_handle = ('channel', cygrpc.Channel, 'managed_call', IntegratedCallFactory, 'method', bytes, 'target', bytes, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_call_handle', Optional[int])):
        self._channel = channel
        self._managed_call = managed_call
        self._method = method
        self._target = target
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer
        self._context = cygrpc.build_census_context()
        self._registered_call_handle = _registered_call_handle

    
    def _prepare(self, request, timeout = None, metadata = None, wait_for_ready = None, compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Tuple[(Optional[_RPCState], Optional[Sequence[cygrpc.Operation]], Optional[float], Optional[grpc.RpcError])])):
        (deadline, serialized_request, rendezvous) = _start_unary_request(request, timeout, self._request_serializer)
        initial_metadata_flags = _InitialMetadataFlags().with_wait_for_ready(wait_for_ready)
        augmented_metadata = _compression.augment_metadata(metadata, compression)
    # WARNING: Decompyle incomplete

    
    def _blocking(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Tuple[(_RPCState, cygrpc.SegregatedCall)])):
        (state, operations, deadline, rendezvous) = self._prepare(request, timeout, metadata, wait_for_ready, compression)
    # WARNING: Decompyle incomplete

    
    def __call__(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Any)):
        (state, call) = self._blocking(request, timeout, metadata, credentials, wait_for_ready, compression)
        return _end_unary_response_blocking(state, call, False, None)

    
    def with_call(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Tuple[(Any, grpc.Call)])):
        (state, call) = self._blocking(request, timeout, metadata, credentials, wait_for_ready, compression)
        return _end_unary_response_blocking(state, call, True, None)

    
    def future(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', _MultiThreadedRendezvous)):
        (state, operations, deadline, rendezvous) = self._prepare(request, timeout, metadata, wait_for_ready, compression)
    # WARNING: Decompyle incomplete



class _SingleThreadedUnaryStreamMultiCallable(grpc.UnaryStreamMultiCallable):
    _registered_call_handle: Optional[int] = '_SingleThreadedUnaryStreamMultiCallable'
    __slots__ = [
        '_channel',
        '_method',
        '_target',
        '_request_serializer',
        '_response_deserializer',
        '_context']
    
    def __init__(self, channel, method, target = None, request_serializer = None, response_deserializer = None, _registered_call_handle = ('channel', cygrpc.Channel, 'method', bytes, 'target', bytes, 'request_serializer', SerializingFunction, 'response_deserializer', DeserializingFunction, '_registered_call_handle', Optional[int])):
        self._channel = channel
        self._method = method
        self._target = target
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer
        self._context = cygrpc.build_census_context()
        self._registered_call_handle = _registered_call_handle

    
    def __call__(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', _SingleThreadedRendezvous)):
        deadline = _deadline(timeout)
        serialized_request = _common.serialize(request, self._request_serializer)
    # WARNING: Decompyle incomplete



class _UnaryStreamMultiCallable(grpc.UnaryStreamMultiCallable):
    _registered_call_handle: Optional[int] = '_UnaryStreamMultiCallable'
    __slots__ = [
        '_channel',
        '_managed_call',
        '_method',
        '_target',
        '_request_serializer',
        '_response_deserializer',
        '_context']
    
    def __init__(self, channel, managed_call, method, target = None, request_serializer = None, response_deserializer = None, _registered_call_handle = ('channel', cygrpc.Channel, 'managed_call', IntegratedCallFactory, 'method', bytes, 'target', bytes, 'request_serializer', SerializingFunction, 'response_deserializer', DeserializingFunction, '_registered_call_handle', Optional[int])):
        self._channel = channel
        self._managed_call = managed_call
        self._method = method
        self._target = target
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer
        self._context = cygrpc.build_census_context()
        self._registered_call_handle = _registered_call_handle

    
    def __call__(self, request, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request', Any, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', _MultiThreadedRendezvous)):
        (deadline, serialized_request, rendezvous) = _start_unary_request(request, timeout, self._request_serializer)
        initial_metadata_flags = _InitialMetadataFlags().with_wait_for_ready(wait_for_ready)
    # WARNING: Decompyle incomplete



class _StreamUnaryMultiCallable(grpc.StreamUnaryMultiCallable):
    _registered_call_handle: Optional[int] = '_StreamUnaryMultiCallable'
    __slots__ = [
        '_channel',
        '_managed_call',
        '_method',
        '_target',
        '_request_serializer',
        '_response_deserializer',
        '_context']
    
    def __init__(self, channel, managed_call, method, target = None, request_serializer = None, response_deserializer = None, _registered_call_handle = ('channel', cygrpc.Channel, 'managed_call', IntegratedCallFactory, 'method', bytes, 'target', bytes, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_call_handle', Optional[int])):
        self._channel = channel
        self._managed_call = managed_call
        self._method = method
        self._target = target
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer
        self._context = cygrpc.build_census_context()
        self._registered_call_handle = _registered_call_handle

    
    def _blocking(self, request_iterator, timeout, metadata = None, credentials = None, wait_for_ready = None, compression = ('request_iterator', Iterator, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Tuple[(_RPCState, cygrpc.SegregatedCall)])):
        deadline = _deadline(timeout)
        state = _RPCState(_STREAM_UNARY_INITIAL_DUE, None, None, None, None)
        initial_metadata_flags = _InitialMetadataFlags().with_wait_for_ready(wait_for_ready)
        augmented_metadata = _compression.augment_metadata(metadata, compression)
        state.rpc_start_time = time.perf_counter()
        state.method = _common.decode(self._method)
        state.target = _common.decode(self._target)
    # WARNING: Decompyle incomplete

    
    def __call__(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request_iterator', Iterator, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Any)):
        (state, call) = self._blocking(request_iterator, timeout, metadata, credentials, wait_for_ready, compression)
        return _end_unary_response_blocking(state, call, False, None)

    
    def with_call(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request_iterator', Iterator, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', Tuple[(Any, grpc.Call)])):
        (state, call) = self._blocking(request_iterator, timeout, metadata, credentials, wait_for_ready, compression)
        return _end_unary_response_blocking(state, call, True, None)

    
    def future(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request_iterator', Iterator, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', _MultiThreadedRendezvous)):
        deadline = _deadline(timeout)
        state = _RPCState(_STREAM_UNARY_INITIAL_DUE, None, None, None, None)
        event_handler = _event_handler(state, self._response_deserializer)
        initial_metadata_flags = _InitialMetadataFlags().with_wait_for_ready(wait_for_ready)
        augmented_metadata = _compression.augment_metadata(metadata, compression)
        state.rpc_start_time = time.perf_counter()
        state.method = _common.decode(self._method)
        state.target = _common.decode(self._target)
    # WARNING: Decompyle incomplete



class _StreamStreamMultiCallable(grpc.StreamStreamMultiCallable):
    _registered_call_handle: Optional[int] = '_StreamStreamMultiCallable'
    __slots__ = [
        '_channel',
        '_managed_call',
        '_method',
        '_target',
        '_request_serializer',
        '_response_deserializer',
        '_context']
    
    def __init__(self, channel, managed_call, method, target = None, request_serializer = None, response_deserializer = None, _registered_call_handle = ('channel', cygrpc.Channel, 'managed_call', IntegratedCallFactory, 'method', bytes, 'target', bytes, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], '_registered_call_handle', Optional[int])):
        self._channel = channel
        self._managed_call = managed_call
        self._method = method
        self._target = target
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer
        self._context = cygrpc.build_census_context()
        self._registered_call_handle = _registered_call_handle

    
    def __call__(self, request_iterator, timeout = None, metadata = None, credentials = None, wait_for_ready = (None, None, None, None, None), compression = ('request_iterator', Iterator, 'timeout', Optional[float], 'metadata', Optional[MetadataType], 'credentials', Optional[grpc.CallCredentials], 'wait_for_ready', Optional[bool], 'compression', Optional[grpc.Compression], 'return', _MultiThreadedRendezvous)):
        deadline = _deadline(timeout)
        state = _RPCState(_STREAM_STREAM_INITIAL_DUE, None, None, None, None)
        initial_metadata_flags = _InitialMetadataFlags().with_wait_for_ready(wait_for_ready)
        augmented_metadata = _compression.augment_metadata(metadata, compression)
        operations = ((cygrpc.SendInitialMetadataOperation(augmented_metadata, initial_metadata_flags), cygrpc.ReceiveStatusOnClientOperation(_EMPTY_FLAGS)), (cygrpc.ReceiveInitialMetadataOperation(_EMPTY_FLAGS),))
        event_handler = _event_handler(state, self._response_deserializer)
        state.rpc_start_time = time.perf_counter()
        state.method = _common.decode(self._method)
        state.target = _common.decode(self._target)
    # WARNING: Decompyle incomplete



class _InitialMetadataFlags(int):
    pass
# WARNING: Decompyle incomplete


class _ChannelCallState(object):
    threading: bool = '_ChannelCallState'
    
    def __init__(self = None, channel = None):
        self.lock = threading.Lock()
        self.channel = channel
        self.managed_calls = 0
        self.threading = False

    
    def reset_postfork_child(self = None):
        self.managed_calls = 0

    
    def __del__(self):
        
        try:
            self.channel.close(cygrpc.StatusCode.cancelled, 'Channel deallocated!')
            return None
        except (TypeError, AttributeError):
            return None




def _run_channel_spin_thread(state = None):
    pass
# WARNING: Decompyle incomplete


def _channel_managed_call_management(state = None):
    pass
# WARNING: Decompyle incomplete


class _ChannelConnectivityState(object):
    delivering: bool = '_ChannelConnectivityState'
    
    def __init__(self = None, channel = None):
        self.lock = threading.RLock()
        self.channel = channel
        self.polling = False
        self.connectivity = None
        self.try_to_connect = False
        self.callbacks_and_connectivities = []
        self.delivering = False

    
    def reset_postfork_child(self = None):
        self.polling = False
        self.connectivity = None
        self.try_to_connect = False
        self.callbacks_and_connectivities = []
        self.delivering = False



def _deliveries(state = None):
    callbacks_needing_update = []
    for callback_and_connectivity in state.callbacks_and_connectivities:
        (callback, callback_connectivity) = callback_and_connectivity
        if callback_connectivity is not state.connectivity:
            callbacks_needing_update.append(callback)
            callback_and_connectivity[1] = state.connectivity
        return callbacks_needing_update


def _deliver(state = None, initial_connectivity = None, initial_callbacks = None):
    connectivity = initial_connectivity
    callbacks = initial_callbacks
    for callback in callbacks:
        cygrpc.block_if_fork_in_progress(state)
        callback(connectivity)
        except Exception:
            _LOGGER.exception(_CHANNEL_SUBSCRIPTION_CALLBACK_ERROR_LOG_MESSAGE)
            continue
        state.lock
        callbacks = _deliveries(state)
        if callbacks:
            connectivity = state.connectivity
        else:
            state.delivering = False
            None(None, None)
            return None
        None(None, None)
    with None:
        if not None:
            pass
    continue


def _spawn_delivery(state = None, callbacks = None):
    delivering_thread = cygrpc.ForkManagedThread(target = _deliver, args = (state, state.connectivity, callbacks))
    delivering_thread.setDaemon(True)
    delivering_thread.start()
    state.delivering = True


def _poll_connectivity(state = None, channel = None, initial_try_to_connect = None):
