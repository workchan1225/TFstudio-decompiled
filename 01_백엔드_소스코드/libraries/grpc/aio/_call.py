# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _call.pyc (Python 3.11)

'''Invocation-side implementation of gRPC Asyncio Python.'''
import asyncio
import enum
from functools import partial
import inspect
import logging
import traceback
from typing import Any, AsyncIterator, Generator, Generic, Optional, Tuple, Union
import grpc
from grpc import _common
from grpc._cython import cygrpc
from  import _base_call
from _metadata import Metadata
from _typing import DeserializingFunction
from _typing import DoneCallbackType
from _typing import EOFType
from _typing import MetadataType
from _typing import MetadatumType
from _typing import RequestIterableType
from _typing import RequestType
from _typing import ResponseType
from _typing import SerializingFunction
__all__ = ('AioRpcError', 'Call', 'UnaryUnaryCall', 'UnaryStreamCall')
_LOCAL_CANCELLATION_DETAILS = 'Locally cancelled by application!'
_GC_CANCELLATION_DETAILS = 'Cancelled upon garbage collection!'
_RPC_ALREADY_FINISHED_DETAILS = 'RPC already finished.'
_RPC_HALF_CLOSED_DETAILS = 'RPC is half closed after calling "done_writing".'
_API_STYLE_ERROR = 'The iterator and read/write APIs may not be mixed on a single RPC.'
_OK_CALL_REPRESENTATION = '<{} of RPC that terminated with:\n\tstatus = {}\n\tdetails = "{}"\n>'
_NON_OK_CALL_REPRESENTATION = '<{} of RPC that terminated with:\n\tstatus = {}\n\tdetails = "{}"\n\tdebug_error_string = "{}"\n>'
_LOGGER = logging.getLogger(__name__)

class AioRpcError(grpc.RpcError):
    pass
# WARNING: Decompyle incomplete


def _create_rpc_error(initial_metadata = None, status = None):
    return AioRpcError(_common.CYGRPC_STATUS_CODE_TO_STATUS_CODE[status.code()], Metadata.from_tuple(initial_metadata), Metadata.from_tuple(status.trailing_metadata()), details = status.details(), debug_error_string = status.debug_error_string())


class Call:
    _response_deserializer: Optional[DeserializingFunction] = 'Base implementation of client RPC Call object.\n\n    Implements logic around final status, metadata and cancellation.\n    '
    
    def __init__(self, cython_call, metadata = None, request_serializer = None, response_deserializer = None, loop = ('cython_call', cygrpc._AioCall, 'metadata', Metadata, 'request_serializer', Optional[SerializingFunction], 'response_deserializer', Optional[DeserializingFunction], 'loop', asyncio.AbstractEventLoop, 'return', None)):
        self._loop = loop
        self._cython_call = cython_call
        self._metadata = tuple(metadata)
        self._request_serializer = request_serializer
        self._response_deserializer = response_deserializer

    
    def __del__(self = None):
        if not hasattr(self, '_cython_call') or self._cython_call.done():
            self._cancel(_GC_CANCELLATION_DETAILS)
            return None
        return None

    
    def cancelled(self = None):
        return self._cython_call.cancelled()

    
    def _cancel(self = None, details = None):
        '''Forwards the application cancellation reasoning.'''
        if not self._cython_call.done():
            self._cython_call.cancel(details)
            return True

    
    def cancel(self = None):
        return self._cancel(_LOCAL_CANCELLATION_DETAILS)

    
    def done(self = None):
        return self._cython_call.done()

    
    def add_done_callback(self = None, callback = None):
        cb = partial(callback, self)
        self._cython_call.add_done_callback(cb)

    
    def time_remaining(self = None):
        return self._cython_call.time_remaining()

    
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

    
    async def _raise_for_status(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _repr(self = None):
        return repr(self._cython_call)

    
    def __repr__(self = None):
        return self._repr()

    
    def __str__(self = None):
        return self._repr()



class _APIStyle(enum.IntEnum):
    UNKNOWN = 0
    ASYNC_GENERATOR = 1
    READER_WRITER = 2


def _UnaryResponseMixin():
    '''_UnaryResponseMixin'''
    pass
# WARNING: Decompyle incomplete

_UnaryResponseMixin = <NODE:27>(_UnaryResponseMixin, '_UnaryResponseMixin', Call, Generic[ResponseType])

class _StreamResponseMixin(Call):
    pass
# WARNING: Decompyle incomplete


class _StreamRequestMixin(Call):
    pass
# WARNING: Decompyle incomplete


class UnaryUnaryCall(_base_call.UnaryUnaryCall, Call, _UnaryResponseMixin):
    pass
# WARNING: Decompyle incomplete


class UnaryStreamCall(_base_call.UnaryStreamCall, Call, _StreamResponseMixin):
    pass
# WARNING: Decompyle incomplete


class StreamUnaryCall(_base_call.StreamUnaryCall, Call, _UnaryResponseMixin, _StreamRequestMixin):
    pass
# WARNING: Decompyle incomplete


class StreamStreamCall(_base_call.StreamStreamCall, Call, _StreamResponseMixin, _StreamRequestMixin):
    pass
# WARNING: Decompyle incomplete
