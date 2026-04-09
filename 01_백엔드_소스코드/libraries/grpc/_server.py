# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _server.pyc (Python 3.11)

'''Service-side implementation of gRPC Python.'''
from __future__ import annotations
import abc
import collections
from concurrent import futures
import contextvars
import enum
import logging
import threading
import time
import traceback
from typing import Any, Callable, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Set, Tuple, Union
import grpc
from grpc import _common
from grpc import _compression
from grpc import _interceptor
from grpc import _observability
from grpc._cython import cygrpc
from grpc._typing import ArityAgnosticMethodHandler
from grpc._typing import ChannelArgumentType
from grpc._typing import DeserializingFunction
from grpc._typing import MetadataType
from grpc._typing import NullaryCallbackType
from grpc._typing import ResponseType
from grpc._typing import SerializingFunction
from grpc._typing import ServerCallbackTag
from grpc._typing import ServerTagCallbackType
from typing_extensions import override
_LOGGER = logging.getLogger(__name__)
_SHUTDOWN_TAG = 'shutdown'
_REQUEST_CALL_TAG = 'request_call'
_RECEIVE_CLOSE_ON_SERVER_TOKEN = 'receive_close_on_server'
_SEND_INITIAL_METADATA_TOKEN = 'send_initial_metadata'
_RECEIVE_MESSAGE_TOKEN = 'receive_message'
_SEND_MESSAGE_TOKEN = 'send_message'
_SEND_INITIAL_METADATA_AND_SEND_MESSAGE_TOKEN = 'send_initial_metadata * send_message'
_SEND_STATUS_FROM_SERVER_TOKEN = 'send_status_from_server'
_SEND_INITIAL_METADATA_AND_SEND_STATUS_FROM_SERVER_TOKEN = 'send_initial_metadata * send_status_from_server'
_OPEN = 'open'
_CLOSED = 'closed'
_CANCELLED = 'cancelled'
_EMPTY_FLAGS = 0
_DEALLOCATED_SERVER_CHECK_PERIOD_S = 1
_INF_TIMEOUT = 1e+09

def _serialized_request(request_event = None):
    return request_event.batch_operations[0].message()


def _application_code(code = None):
    cygrpc_code = _common.STATUS_CODE_TO_CYGRPC_STATUS_CODE.get(code)
# WARNING: Decompyle incomplete


def _completion_code(state = None):
    pass
# WARNING: Decompyle incomplete


def _abortion_code(state = None, code = None):
    pass
# WARNING: Decompyle incomplete


def _details(state = None):
    pass
# WARNING: Decompyle incomplete


def _HandlerCallDetails():
    '''_HandlerCallDetails'''
    pass

_HandlerCallDetails = <NODE:27>(_HandlerCallDetails, '_HandlerCallDetails', collections.namedtuple('_HandlerCallDetails', ('method', 'invocation_metadata')), grpc.HandlerCallDetails)

class _Method(abc.ABC):
    name = (lambda self = None: raise NotImplementedError())()
    handler = (lambda self = None, handler_call_details = None: raise NotImplementedError())()


class _RegisteredMethod(_Method):
    
    def __init__(self = None, name = None, registered_handler = None):
        self._name = name
        self._registered_handler = registered_handler

    name = (lambda self = None: self._name)()
    handler = (lambda self = None, handler_call_details = None: self._registered_handler)()


class _GenericMethod(_Method):
    
    def __init__(self = None, generic_handlers = None):
        self._generic_handlers = generic_handlers

    name = (lambda self = None: pass)()
    handler = (lambda self = None, handler_call_details = None: pass# WARNING: Decompyle incomplete
)()


class _RPCState(object):
    condition: 'threading.Condition' = '_RPCState'
    aborted: 'bool' = Set[str]
    
    def __init__(self):
        self.context = contextvars.Context()
        self.condition = threading.Condition()
        self.due = set()
        self.request = None
        self.client = _OPEN
        self.initial_metadata_allowed = True
        self.compression_algorithm = None
        self.disable_next_compression = False
        self.trailing_metadata = None
        self.code = None
        self.details = None
        self.statused = False
        self.rpc_errors = []
        self.callbacks = []
        self.aborted = False



def _raise_rpc_error(state = None):
    rpc_error = grpc.RpcError()
    state.rpc_errors.append(rpc_error)
    raise rpc_error


def _possibly_finish_call(state = None, token = None):
    state.due.remove(token)
    if not _is_rpc_state_active(state) and state.due:
        callbacks = state.callbacks
        state.callbacks = None
        return (state, callbacks)


def _send_status_from_server(state = None, token = None):
    pass
# WARNING: Decompyle incomplete


def _get_initial_metadata(state = None, metadata = None):
    state.condition
# WARNING: Decompyle incomplete


def _get_initial_metadata_operation(state = None, metadata = None):
    operation = cygrpc.SendInitialMetadataOperation(_get_initial_metadata(state, metadata), _EMPTY_FLAGS)
    return operation


def _abort(state = None, call = None, code = None, details = ('state', '_RPCState', 'call', 'cygrpc.Call', 'code', 'cygrpc.StatusCode', 'details', 'bytes', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def _receive_close_on_server(state = None):
    pass
# WARNING: Decompyle incomplete


def _receive_message(state = None, call = None, request_deserializer = None):
    pass
# WARNING: Decompyle incomplete


def _send_initial_metadata(state = None):
    pass
# WARNING: Decompyle incomplete


def _send_message(state = None, token = None):
    pass
# WARNING: Decompyle incomplete


class _Context(grpc.ServicerContext):
    request_deserializer: 'Optional[DeserializingFunction]' = '_Context'
    
    def __init__(self = None, rpc_event = None, state = None, request_deserializer = ('rpc_event', 'cygrpc.BaseEvent', 'state', '_RPCState', 'request_deserializer', 'Optional[DeserializingFunction]')):
        self._rpc_event = rpc_event
        self._state = state
        self._request_deserializer = request_deserializer

    
    def is_active(self = None):
        self._state.condition
        None(None, None)
        return 
        with None:
            if not None, _is_rpc_state_active(self._state):
                pass

    
    def time_remaining(self = None):
        return max(self._rpc_event.call_details.deadline - time.time(), 0)

    
    def cancel(self = None):
        self._rpc_event.call.cancel()

    
    def add_callback(self = None, callback = None):
        self._state.condition
    # WARNING: Decompyle incomplete

    
    def disable_next_message_compression(self = None):
        self._state.condition
        self._state.disable_next_compression = True
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def invocation_metadata(self = None):
        return self._rpc_event.invocation_metadata

    
    def peer(self = None):
        return _common.decode(self._rpc_event.call.peer())

    
    def peer_identities(self = None):
        return cygrpc.peer_identities(self._rpc_event.call)

    
    def peer_identity_key(self = None):
        id_key = cygrpc.peer_identity_key(self._rpc_event.call)
    # WARNING: Decompyle incomplete

    
    def auth_context(self = None):
        auth_context = cygrpc.auth_context(self._rpc_event.call)
    # WARNING: Decompyle incomplete

    
    def set_compression(self = None, compression = None):
        self._state.condition
        self._state.compression_algorithm = compression
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def send_initial_metadata(self = None, initial_metadata = None):
        self._state.condition
        if self._state.client is _CANCELLED:
            _raise_rpc_error(self._state)
        if self._state.initial_metadata_allowed:
            operation = _get_initial_metadata_operation(self._state, initial_metadata)
            self._rpc_event.call.start_server_batch((operation,), _send_initial_metadata(self._state))
            self._state.initial_metadata_allowed = False
            self._state.due.add(_SEND_INITIAL_METADATA_TOKEN)
        else:
            error_msg = 'Initial metadata no longer allowed!'
            raise ValueError(error_msg)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def set_trailing_metadata(self = None, trailing_metadata = None):
        self._state.condition
        self._state.trailing_metadata = trailing_metadata
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def trailing_metadata(self = None):
        return self._state.trailing_metadata

    
    def abort(self = None, code = None, details = None):
        if code == grpc.StatusCode.OK:
            _LOGGER.error('abort() called with StatusCode.OK; returning UNKNOWN')
            code = grpc.StatusCode.UNKNOWN
            details = ''
        self._state.condition
        self._state.code = code
        self._state.details = _common.encode(details)
        self._state.aborted = True
        raise Exception()
        with None:
            if not None:
                pass

    
    def abort_with_status(self = None, status = None):
        self._state.trailing_metadata = status.trailing_metadata
        self.abort(status.code, status.details)

    
    def set_code(self = None, code = None):
        self._state.condition
        self._state.code = code
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def code(self = None):
        return self._state.code

    
    def set_details(self = None, details = None):
        self._state.condition
        self._state.details = _common.encode(details)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def details(self = None):
        return self._state.details

    
    def _finalize_state(self = None):
        pass



class _RequestIterator(object):
    _request_deserializer: 'Optional[DeserializingFunction]' = '_RequestIterator'
    
    def __init__(self = None, state = None, call = None, request_deserializer = ('state', '_RPCState', 'call', 'cygrpc.Call', 'request_deserializer', 'Optional[DeserializingFunction]')):
        self._state = state
        self._call = call
        self._request_deserializer = request_deserializer

    
    def _raise_or_start_receive_message(self = None):
        if self._state.client is _CANCELLED:
            _raise_rpc_error(self._state)
            return None
        if not None(self._state):
            raise StopIteration()
        self._call.start_server_batch((cygrpc.ReceiveMessageOperation(_EMPTY_FLAGS),), _receive_message(self._state, self._call, self._request_deserializer))
        self._state.due.add(_RECEIVE_MESSAGE_TOKEN)

    
    def _look_for_request(self = None):
        if self._state.client is _CANCELLED:
            _raise_rpc_error(self._state)
    # WARNING: Decompyle incomplete

    
    def _next(self = None):
        self._state.condition
        self._raise_or_start_receive_message()
        self._state.condition.wait()
        request = self._look_for_request()
    # WARNING: Decompyle incomplete

    
    def __iter__(self = None):
        return self

    
    def __next__(self = None):
        return self._next()

    
    def next(self = None):
        return self._next()



def _unary_request(rpc_event = None, state = None, request_deserializer = None):
    pass
# WARNING: Decompyle incomplete


def _call_behavior(rpc_event, state = None, behavior = None, argument = None, request_deserializer = (None,), send_response_callback = ('rpc_event', 'cygrpc.BaseEvent', 'state', '_RPCState', 'behavior', 'ArityAgnosticMethodHandler', 'argument', 'Any', 'request_deserializer', 'Optional[DeserializingFunction]', 'send_response_callback', 'Optional[Callable[[ResponseType], None]]', 'return', 'Tuple[Union[ResponseType, Iterator[ResponseType]], bool]')):
    _create_servicer_context = _create_servicer_context
    import grpc
    context = _create_servicer_context(rpc_event, state, request_deserializer)
    response_or_iterator = None
# WARNING: Decompyle incomplete


def _take_response_from_response_iterator(rpc_event = None, state = None, response_iterator = None):
    
    try:
        return (next(response_iterator), True)
    except StopIteration:
        return (None, True)
        except Exception:
            exception = None
            state.condition
            if state.aborted:
                _abort(state, rpc_event.call, cygrpc.StatusCode.unknown, b'RPC Aborted')
            elif exception not in state.rpc_errors:
                details = 'Exception iterating responses: {}'.format(exception)
                _LOGGER.exception(details)
                _abort(state, rpc_event.call, cygrpc.StatusCode.unknown, _common.encode(details))
            None(None, None)
        except:
            with None:
                if not None:
                    pass
        exception = None
        del exception
        return (None, False)
        exception = None
        del exception



def _serialize_response(rpc_event = None, state = None, response = None, response_serializer = ('rpc_event', 'cygrpc.BaseEvent', 'state', '_RPCState', 'response', 'Any', 'response_serializer', 'Optional[SerializingFunction]', 'return', 'Optional[bytes]')):
    serialized_response = _common.serialize(response, response_serializer)
# WARNING: Decompyle incomplete


def _get_send_message_op_flags_from_state(state = None):
    if state.disable_next_compression:
        return cygrpc.WriteFlag.no_compress


def _reset_per_message_state(state = None):
    state.condition
    state.disable_next_compression = False
    None(None, None)
    return None
    with None:
        if not None:
            pass


def _send_response(rpc_event = None, state = None, serialized_response = None):
    state.condition
    if not _is_rpc_state_active(state):
        None(None, None)
        return False
    if None.initial_metadata_allowed:
        operations = (_get_initial_metadata_operation(state, None), cygrpc.SendMessageOperation(serialized_response, _get_send_message_op_flags_from_state(state)))
        state.initial_metadata_allowed = False
        token = _SEND_INITIAL_METADATA_AND_SEND_MESSAGE_TOKEN
    else:
        operations = (cygrpc.SendMessageOperation(serialized_response, _get_send_message_op_flags_from_state(state)),)
        token = _SEND_MESSAGE_TOKEN
    rpc_event.call.start_server_batch(operations, _send_message(state, token))
    state.due.add(token)
    _reset_per_message_state(state)
    state.condition.wait()
    if token not in state.due:
        None(None, None)
        return 
    with None:
        if not None:
            pass


def _status(rpc_event = None, state = None, serialized_response = None):
    state.condition
# WARNING: Decompyle incomplete


def _unary_response_in_pool(rpc_event, state, behavior = None, argument_thunk = None, request_deserializer = None, response_serializer = ('rpc_event', 'cygrpc.BaseEvent', 'state', '_RPCState', 'behavior', 'ArityAgnosticMethodHandler', 'argument_thunk', 'Callable[[], Any]', 'request_deserializer', 'Optional[SerializingFunction]', 'response_serializer', 'Optional[SerializingFunction]', 'return', 'None')):
    cygrpc.install_context_from_request_call_event(rpc_event)
# WARNING: Decompyle incomplete


def _stream_response_in_pool(rpc_event, state, behavior = None, argument_thunk = None, request_deserializer = None, response_serializer = ('rpc_event', 'cygrpc.BaseEvent', 'state', '_RPCState', 'behavior', 'ArityAgnosticMethodHandler', 'argument_thunk', 'Callable[[], Any]', 'request_deserializer', 'Optional[DeserializingFunction]', 'response_serializer', 'Optional[SerializingFunction]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete


def _is_rpc_state_active(state = None):
