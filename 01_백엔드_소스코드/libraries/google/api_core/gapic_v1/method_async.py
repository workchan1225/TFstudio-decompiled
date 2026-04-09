# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: method_async.pyc (Python 3.11)

'''AsyncIO helpers for wrapping gRPC methods with common functionality.

This is used by gapic clients to provide common error mapping, retry, timeout,
compression, pagination, and long-running operations to gRPC methods.
'''
import functools
from google.api_core import grpc_helpers_async
from google.api_core.gapic_v1 import client_info
from google.api_core.gapic_v1.method import _GapicCallable
from google.api_core.gapic_v1.method import DEFAULT
from google.api_core.gapic_v1.method import USE_DEFAULT_METADATA
_DEFAULT_ASYNC_TRANSPORT_KIND = 'grpc_asyncio'

def wrap_method(func, default_retry, default_timeout, default_compression, client_info, kind = (None, None, None, client_info.DEFAULT_CLIENT_INFO, _DEFAULT_ASYNC_TRANSPORT_KIND)):
    '''Wrap an async RPC method with common behavior.

    Returns:
        Callable: A new callable that takes optional ``retry``, ``timeout``,
            and ``compression`` arguments and applies the common error mapping,
            retry, timeout, metadata, and compression behavior to the low-level RPC method.
    '''
    if kind == _DEFAULT_ASYNC_TRANSPORT_KIND:
        func = grpc_helpers_async.wrap_errors(func)
# WARNING: Decompyle incomplete
