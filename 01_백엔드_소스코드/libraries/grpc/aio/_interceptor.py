# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _interceptor.pyc (Python 3.11)

'''Interceptors implementation of gRPC Asyncio Python.'''
from __future__ import annotations
from abc import ABCMeta
from abc import abstractmethod
import asyncio
import collections
import functools
from typing import AsyncIterable, AsyncIterator, Awaitable, Callable, List, Optional, Sequence, Union
import grpc
from grpc._cython import cygrpc
from  import _base_call
from _call import AioRpcError
from _call import StreamStreamCall
from _call import StreamUnaryCall
from _call import UnaryStreamCall
from _call import UnaryUnaryCall
from _call import _API_STYLE_ERROR
from _call import _RPC_ALREADY_FINISHED_DETAILS
from _call import _RPC_HALF_CLOSED_DETAILS
from _metadata import Metadata
from _typing import DeserializingFunction
from _typing import DoneCallbackType
from _typing import EOFType
from _typing import RequestIterableType
from _typing import RequestType
from _typing import ResponseIterableType
from _typing import ResponseType
from _typing import SerializingFunction
from _utils import _timeout_to_deadline
_LOCAL_CANCELLATION_DETAILS = 'Locally cancelled by application!'

def ServerInterceptor():
    '''ServerInterceptor'''
    __doc__ = 'Affords intercepting incoming RPCs on the service-side.\n\n    This is an EXPERIMENTAL API.\n    '
    intercept_service = (lambda self = None, continuation = None, handler_call_details = abstractmethod: pass# WARNING: Decompyle incomplete
)()

ServerInterceptor = <NODE:27>(ServerInterceptor, 'ServerInterceptor', metaclass = ABCMeta)

def ClientCallDetails():
    '''ClientCallDetails'''
    wait_for_ready: 'Optional[bool]' = 'Describes an RPC to be invoked.\n\n    This is an EXPERIMENTAL API.\n\n    Args:\n        method: The method name of the RPC.\n        timeout: An optional duration of time in seconds to allow for the RPC.\n        metadata: Optional metadata to be transmitted to the service-side of\n          the RPC.\n        credentials: An optional CallCredentials for the RPC.\n        wait_for_ready: An optional flag to enable :term:`wait_for_ready` mechanism.\n    '

ClientCallDetails = <NODE:27>(ClientCallDetails, 'ClientCallDetails', collections.namedtuple('ClientCallDetails', ('method', 'timeout', 'metadata', 'credentials', 'wait_for_ready')), grpc.ClientCallDetails)

def ClientInterceptor():
    '''ClientInterceptor'''
    __doc__ = 'Base class used for all Aio Client Interceptor classes'

ClientInterceptor = <NODE:27>(ClientInterceptor, 'ClientInterceptor', metaclass = ABCMeta)

def UnaryUnaryClientInterceptor():
    '''UnaryUnaryClientInterceptor'''
    __doc__ = 'Affords intercepting unary-unary invocations.'
    intercept_unary_unary = (lambda self = None, continuation = None, client_call_details = abstractmethod, request = ('continuation', 'Callable[[ClientCallDetails, RequestType], UnaryUnaryCall]', 'client_call_details', 'ClientCallDetails', 'request', 'RequestType', 'return', 'Union[UnaryUnaryCall, ResponseType]'): pass# WARNING: Decompyle incomplete
)()

UnaryUnaryClientInterceptor = <NODE:27>(UnaryUnaryClientInterceptor, 'UnaryUnaryClientInterceptor', ClientInterceptor, metaclass = ABCMeta)

def UnaryStreamClientInterceptor():
    '''UnaryStreamClientInterceptor'''
    __doc__ = 'Affords intercepting unary-stream invocations.'
    intercept_unary_stream = (lambda self = None, continuation = None, client_call_details = abstractmethod, request = ('continuation', 'Callable[[ClientCallDetails, RequestType], UnaryStreamCall]', 'client_call_details', 'ClientCallDetails', 'request', 'RequestType', 'return', 'Union[ResponseIterableType, UnaryStreamCall]'): pass# WARNING: Decompyle incomplete
)()

UnaryStreamClientInterceptor = <NODE:27>(UnaryStreamClientInterceptor, 'UnaryStreamClientInterceptor', ClientInterceptor, metaclass = ABCMeta)

def StreamUnaryClientInterceptor():
    '''StreamUnaryClientInterceptor'''
    __doc__ = 'Affords intercepting stream-unary invocations.'
    intercept_stream_unary = (lambda self = None, continuation = None, client_call_details = abstractmethod, request_iterator = ('continuation', 'Callable[[ClientCallDetails, RequestType], StreamUnaryCall]', 'client_call_details', 'ClientCallDetails', 'request_iterator', 'RequestIterableType', 'return', 'StreamUnaryCall'): pass# WARNING: Decompyle incomplete
)()

StreamUnaryClientInterceptor = <NODE:27>(StreamUnaryClientInterceptor, 'StreamUnaryClientInterceptor', ClientInterceptor, metaclass = ABCMeta)

def StreamStreamClientInterceptor():
    '''StreamStreamClientInterceptor'''
    __doc__ = 'Affords intercepting stream-stream invocations.'
    intercept_stream_stream = (lambda self = None, continuation = None, client_call_details = abstractmethod, request_iterator = ('continuation', 'Callable[[ClientCallDetails, RequestType], StreamStreamCall]', 'client_call_details', 'ClientCallDetails', 'request_iterator', 'RequestIterableType', 'return', 'Union[ResponseIterableType, StreamStreamCall]'): pass# WARNING: Decompyle incomplete
)()

StreamStreamClientInterceptor = <NODE:27>(StreamStreamClientInterceptor, 'StreamStreamClientInterceptor', ClientInterceptor, metaclass = ABCMeta)

class InterceptedCall:
    _pending_add_done_callbacks: 'Sequence[DoneCallbackType]' = 'Base implementation for all intercepted call arities.\n\n    Interceptors might have some work to do before the RPC invocation with\n    the capacity of changing the invocation parameters, and some work to do\n    after the RPC invocation with the capacity for accessing to the wrapped\n    `UnaryUnaryCall`.\n\n    It handles also early and later cancellations, when the RPC has not even\n    started and the execution is still held by the interceptors or when the\n    RPC has finished but again the execution is still held by the interceptors.\n\n    Once the RPC is finally executed, all methods are finally done against the\n    intercepted call, being at the same time the same call returned to the\n    interceptors.\n\n    As a base class for all of the interceptors implements the logic around\n    final status, metadata and cancellation.\n    '
    
    def __init__(self = None, interceptors_task = None):
        self._interceptors_task = interceptors_task
        self._pending_add_done_callbacks = []
        self._interceptors_task.add_done_callback(self._fire_or_add_pending_done_callbacks)

    
    def __del__(self):
        self.cancel()

    
    def _fire_or_add_pending_done_callbacks(self = None, interceptors_task = None):
        if not self._pending_add_done_callbacks:
            return None
        call_completed = None
        
        try:
            call = interceptors_task.result()
            if call.done():
                call_completed = True
            else:
                except (AioRpcError, asyncio.CancelledError):
                    call_completed = True
                if call_completed:
                    for callback in self._pending_add_done_callbacks:
                        callback(self)

        for callback in self._pending_add_done_callbacks:
            callback = functools.partial(self._wrap_add_done_callback, callback)
            call.add_done_callback(callback)
            self._pending_add_done_callbacks = []
            return None

    
    def _wrap_add_done_callback(self = None, callback = None, unused_call = None):
        callback(self)

    
    def cancel(self = None):
        if not self._interceptors_task.done():
            return self._interceptors_task.cancel()
        
        try:
            call = self._interceptors_task.result()
        except AioRpcError:
            return False
            except asyncio.CancelledError:
                return False

        return call.cancel()

    
    def cancelled(self = None):
        if not self._interceptors_task.done():
            return False
        
        try:
            call = self._interceptors_task.result()
        except AioRpcError:
            err = None
            del err
            return None
            None = 
            del err
            except asyncio.CancelledError:
                return True

        return call.cancelled()

    
    def done(self = None):
        if not self._interceptors_task.done():
            return False
        
        try:
            call = self._interceptors_task.result()
        except (AioRpcError, asyncio.CancelledError):
            return True

        return call.done()

    
    def add_done_callback(self = None, callback = None):
        if not self._interceptors_task.done():
            self._pending_add_done_callbacks.append(callback)
            return None
        
        try:
            call = self._interceptors_task.result()
        except (AioRpcError, asyncio.CancelledError):
            callback(self)
            return None

        if call.done():
            callback(self)
            return None
        callback = None.partial(self._wrap_add_done_callback, callback)
        call.add_done_callback(callback)

    
    def time_remaining(self = None):
        raise NotImplementedError()

    
    async def initial_metadata(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def trailing_metadata(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def code(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def details(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def debug_error_string(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def wait_for_connection(self = None):
        pass
    # WARNING: Decompyle incomplete



class _InterceptedUnaryResponseMixin:
    
    def __await__(self):
        pass
    # WARNING: Decompyle incomplete



class _InterceptedStreamResponseMixin:
    _response_aiter: 'Optional[AsyncIterable[ResponseType]]' = '_InterceptedStreamResponseMixin'
    
    def _init_stream_response_mixin(self = None):
        self._response_aiter = None

    
    def _wait_for_interceptor_task_response_iterator(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def read(self = None):
        pass
    # WARNING: Decompyle incomplete



class _InterceptedStreamRequestMixin:
    _status_code_task: 'Optional[asyncio.Task]' = '_InterceptedStreamRequestMixin'
    _FINISH_ITERATOR_SENTINEL = object()
    
    def _init_stream_request_mixin(self = None, request_iterator = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _proxy_writes_as_request_iterator(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def _write_to_iterator_queue_interruptible(self = None, request = None, call = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def write(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def done_writing(self = None):
        '''Signal peer that client is done writing.

        This method is idempotent.
        '''
        pass
    # WARNING: Decompyle incomplete



class InterceptedUnaryUnaryCall(_base_call.UnaryUnaryCall, InterceptedCall, _InterceptedUnaryResponseMixin):
    pass
# WARNING: Decompyle incomplete


class InterceptedUnaryStreamCall(_base_call.UnaryStreamCall, InterceptedCall, _InterceptedStreamResponseMixin):
    pass
# WARNING: Decompyle incomplete


class InterceptedStreamUnaryCall(_base_call.StreamUnaryCall, InterceptedCall, _InterceptedStreamRequestMixin, _InterceptedUnaryResponseMixin):
    pass
# WARNING: Decompyle incomplete


class InterceptedStreamStreamCall(_base_call.StreamStreamCall, InterceptedCall, _InterceptedStreamRequestMixin, _InterceptedStreamResponseMixin):
    pass
# WARNING: Decompyle incomplete


class UnaryUnaryCallResponse(_base_call.UnaryUnaryCall):
    _response: 'ResponseType' = 'Final UnaryUnaryCall class finished with a response.'
    
    def __init__(self = None, response = None):
        self._response = response

    
    def cancel(self = None):
        return False

    
    def cancelled(self = None):
        return False

    
    def done(self = None):
        return True

    
    def add_done_callback(self = None, unused_callback = None):
        raise NotImplementedError()

    
    def time_remaining(self = None):
        raise NotImplementedError()

    
    async def initial_metadata(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def trailing_metadata(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def code(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def details(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def debug_error_string(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __await__(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def wait_for_connection(self = None):
        pass
    # WARNING: Decompyle incomplete



class _StreamCallResponseIterator:
    _response_iterator: 'AsyncIterable[ResponseType]' = '_StreamCallResponseIterator'
    
    def __init__(self = None, call = None, response_iterator = None):
        self._response_iterator = response_iterator
        self._call = call

    
    def cancel(self = None):
        return self._call.cancel()

    
    def cancelled(self = None):
        return self._call.cancelled()

    
    def done(self = None):
        return self._call.done()

    
    def add_done_callback(self = None, callback = None):
        self._call.add_done_callback(callback)

    
    def time_remaining(self = None):
        return self._call.time_remaining()

    
    async def initial_metadata(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def trailing_metadata(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def code(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def details(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def debug_error_string(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self):
        return self._response_iterator.__aiter__()

    
    async def wait_for_connection(self = None):
        pass
    # WARNING: Decompyle incomplete



class UnaryStreamCallResponseIterator(_base_call.UnaryStreamCall, _StreamCallResponseIterator):
    '''UnaryStreamCall class which uses an alternative response iterator.'''
    
    async def read(self = None):
        pass
    # WARNING: Decompyle incomplete



class StreamStreamCallResponseIterator(_base_call.StreamStreamCall, _StreamCallResponseIterator):
    '''StreamStreamCall class which uses an alternative response iterator.'''
    
    async def read(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def write(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def done_writing(self = None):
        pass
    # WARNING: Decompyle incomplete

    _done_writing_flag = (lambda self = None: self._call._done_writing_flag)()
