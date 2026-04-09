# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grpc_helpers_async.pyc (Python 3.11)

'''AsyncIO helpers for :mod:`grpc` supporting 3.7+.

Please combine more detailed docstring in grpc_helpers.py to use following
functions. This module is implementing the same surface with AsyncIO semantics.
'''
import asyncio
import functools
import warnings
from typing import AsyncGenerator, Generic, Iterator, Optional, TypeVar
import grpc
from grpc import aio
from google.api_core import exceptions, general_helpers, grpc_helpers
P = TypeVar('P')

class _WrappedCall(aio.Call):
    
    def __init__(self):
        self._call = None

    
    def with_call(self, call):
        '''Supplies the call object separately to keep __init__ clean.'''
        self._call = call
        return self

    
    async def initial_metadata(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def trailing_metadata(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def code(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def details(self):
        pass
    # WARNING: Decompyle incomplete

    
    def cancelled(self):
        return self._call.cancelled()

    
    def done(self):
        return self._call.done()

    
    def time_remaining(self):
        return self._call.time_remaining()

    
    def cancel(self):
        return self._call.cancel()

    
    def add_done_callback(self, callback):
        self._call.add_done_callback(callback)

    
    async def wait_for_connection(self):
        pass
    # WARNING: Decompyle incomplete



def _WrappedUnaryResponseMixin():
    '''_WrappedUnaryResponseMixin'''
    
    def __await__(self = None):
        pass
    # WARNING: Decompyle incomplete


_WrappedUnaryResponseMixin = <NODE:27>(_WrappedUnaryResponseMixin, '_WrappedUnaryResponseMixin', Generic[P], _WrappedCall)

def _WrappedStreamResponseMixin():
    '''_WrappedStreamResponseMixin'''
    
    def __init__(self):
        self._wrapped_async_generator = None

    
    async def read(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _wrapped_aiter(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        if not self._wrapped_async_generator:
            self._wrapped_async_generator = self._wrapped_aiter()
        return self._wrapped_async_generator


_WrappedStreamResponseMixin = <NODE:27>(_WrappedStreamResponseMixin, '_WrappedStreamResponseMixin', Generic[P], _WrappedCall)

class _WrappedStreamRequestMixin(_WrappedCall):
    
    async def write(self, request):
        pass
    # WARNING: Decompyle incomplete

    
    async def done_writing(self):
        pass
    # WARNING: Decompyle incomplete



def _WrappedUnaryUnaryCall():
    '''_WrappedUnaryUnaryCall'''
    __doc__ = 'Wrapped UnaryUnaryCall to map exceptions.'

_WrappedUnaryUnaryCall = <NODE:27>(_WrappedUnaryUnaryCall, '_WrappedUnaryUnaryCall', _WrappedUnaryResponseMixin[P], aio.UnaryUnaryCall)

def _WrappedUnaryStreamCall():
    '''_WrappedUnaryStreamCall'''
    __doc__ = 'Wrapped UnaryStreamCall to map exceptions.'

_WrappedUnaryStreamCall = <NODE:27>(_WrappedUnaryStreamCall, '_WrappedUnaryStreamCall', _WrappedStreamResponseMixin[P], aio.UnaryStreamCall)

def _WrappedStreamUnaryCall():
    '''_WrappedStreamUnaryCall'''
    __doc__ = 'Wrapped StreamUnaryCall to map exceptions.'

_WrappedStreamUnaryCall = <NODE:27>(_WrappedStreamUnaryCall, '_WrappedStreamUnaryCall', _WrappedUnaryResponseMixin[P], _WrappedStreamRequestMixin, aio.StreamUnaryCall)

def _WrappedStreamStreamCall():
    '''_WrappedStreamStreamCall'''
    __doc__ = 'Wrapped StreamStreamCall to map exceptions.'

_WrappedStreamStreamCall = <NODE:27>(_WrappedStreamStreamCall, '_WrappedStreamStreamCall', _WrappedStreamRequestMixin, _WrappedStreamResponseMixin[P], aio.StreamStreamCall)
GrpcAsyncStream = _WrappedStreamResponseMixin
AwaitableGrpcCall = _WrappedUnaryResponseMixin

def _wrap_unary_errors(callable_):
    '''Map errors for Unary-Unary async callables.'''
    pass
# WARNING: Decompyle incomplete


def _wrap_stream_errors(callable_, wrapper_type):
    '''Map errors for streaming RPC async callables.'''
    pass
# WARNING: Decompyle incomplete


def wrap_errors(callable_):
    '''Wrap a gRPC async callable and map :class:`grpc.RpcErrors` to
    friendly error classes.

    Errors raised by the gRPC callable are mapped to the appropriate
    :class:`google.api_core.exceptions.GoogleAPICallError` subclasses. The
    original `grpc.RpcError` (which is usually also a `grpc.Call`) is
    available from the ``response`` property on the mapped exception. This
    is useful for extracting metadata from the original error.

    Args:
        callable_ (Callable): A gRPC callable.

    Returns: Callable: The wrapped gRPC callable.
    '''
    grpc_helpers._patch_callable_name(callable_)
    if isinstance(callable_, aio.UnaryStreamMultiCallable):
        return _wrap_stream_errors(callable_, _WrappedUnaryStreamCall)
    if None(callable_, aio.StreamUnaryMultiCallable):
        return _wrap_stream_errors(callable_, _WrappedStreamUnaryCall)
    if None(callable_, aio.StreamStreamMultiCallable):
        return _wrap_stream_errors(callable_, _WrappedStreamStreamCall)
    return None(callable_)


def create_channel(target, credentials, scopes, ssl_credentials, credentials_file, quota_project_id = None, default_scopes = None, default_host = None, compression = (None, None, None, None, None, None, None, None, False), attempt_direct_path = ('attempt_direct_path', Optional[bool]), **kwargs):
    '''Create an AsyncIO secure channel with credentials.

    Args:
        target (str): The target service address in the format \'hostname:port\'.
        credentials (google.auth.credentials.Credentials): The credentials. If
            not specified, then this function will attempt to ascertain the
            credentials from the environment using :func:`google.auth.default`.
        scopes (Sequence[str]): A optional list of scopes needed for this
            service. These are only used when credentials are not specified and
            are passed to :func:`google.auth.default`.
        ssl_credentials (grpc.ChannelCredentials): Optional SSL channel
            credentials. This can be used to specify different certificates.
        credentials_file (str): Deprecated. A file with credentials that can be loaded with
            :func:`google.auth.load_credentials_from_file`. This argument is
            mutually exclusive with credentials. This argument will be
            removed in the next major version of `google-api-core`.

            .. warning::
                Important: If you accept a credential configuration (credential JSON/File/Stream)
                from an external source for authentication to Google Cloud Platform, you must
                validate it before providing it to any Google API or client library. Providing an
                unvalidated credential configuration to Google APIs or libraries can compromise
                the security of your systems and data. For more information, refer to
                `Validate credential configurations from external sources`_.

            .. _Validate credential configurations from external sources:

            https://cloud.google.com/docs/authentication/external/externally-sourced-credentials
        quota_project_id (str): An optional project to use for billing and quota.
        default_scopes (Sequence[str]): Default scopes passed by a Google client
            library. Use \'scopes\' for user-defined scopes.
        default_host (str): The default endpoint. e.g., "pubsub.googleapis.com".
        compression (grpc.Compression): An optional value indicating the
            compression method to be used over the lifetime of the channel.
        attempt_direct_path (Optional[bool]): If set, Direct Path will be attempted
            when the request is made. Direct Path is only available within a Google
            Compute Engine (GCE) environment and provides a proxyless connection
            which increases the available throughput, reduces latency, and increases
            reliability. Note:

            - This argument should only be set in a GCE environment and for Services
              that are known to support Direct Path.
            - If this argument is set outside of GCE, then this request will fail
              unless the back-end service happens to have configured fall-back to DNS.
            - If the request causes a `ServiceUnavailable` response, it is recommended
              that the client repeat the request with `attempt_direct_path` set to
              `False` as the Service may not support Direct Path.
            - Using `ssl_credentials` with `attempt_direct_path` set to `True` will
              result in `ValueError` as this combination  is not yet supported.

        kwargs: Additional key-word args passed to :func:`aio.secure_channel`.

    Returns:
        aio.Channel: The created channel.

    Raises:
        google.api_core.DuplicateCredentialArgs: If both a credentials object and credentials_file are passed.
        ValueError: If `ssl_credentials` is set and `attempt_direct_path` is set to `True`.
    '''
    pass
# WARNING: Decompyle incomplete


class FakeUnaryUnaryCall(_WrappedUnaryUnaryCall):
    '''Fake implementation for unary-unary RPCs.

    It is a dummy object for response message. Supply the intended response
    upon the initialization, and the coroutine will return the exact response
    message.
    '''
    
    def __init__(self, response = (object(),)):
        self.response = response
        self._future = asyncio.get_event_loop().create_future()
        self._future.set_result(self.response)

    
    def __await__(self):
        pass
    # WARNING: Decompyle incomplete



class FakeStreamUnaryCall(_WrappedStreamUnaryCall):
    '''Fake implementation for stream-unary RPCs.

    It is a dummy object for response message. Supply the intended response
    upon the initialization, and the coroutine will return the exact response
    message.
    '''
    
    def __init__(self, response = (object(),)):
        self.response = response
        self._future = asyncio.get_event_loop().create_future()
        self._future.set_result(self.response)

    
    def __await__(self):
        pass
    # WARNING: Decompyle incomplete

    
    async def wait_for_connection(self):
        pass
    # WARNING: Decompyle incomplete
