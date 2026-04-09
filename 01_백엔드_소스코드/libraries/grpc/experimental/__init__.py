# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

"""gRPC's experimental APIs.

These APIs are subject to be removed during any minor version release.
"""
import copy
import functools
import sys
import warnings
import grpc
from grpc._cython import cygrpc as _cygrpc
_EXPERIMENTAL_APIS_USED = set()

class ChannelOptions(object):
    '''Indicates a channel option unique to gRPC Python.

    This enumeration is part of an EXPERIMENTAL API.

    Attributes:
      SingleThreadedUnaryStream: Perform unary-stream RPCs on a single thread.
    '''
    SingleThreadedUnaryStream = 'SingleThreadedUnaryStream'


class UsageError(Exception):
    '''Raised by the gRPC library to indicate usage not allowed by the API.'''
    pass

_insecure_channel_credentials = grpc.ChannelCredentials(_cygrpc.channel_credentials_insecure())

def insecure_channel_credentials():
    '''Creates a ChannelCredentials for use with an insecure channel.

    THIS IS AN EXPERIMENTAL API.
    '''
    return _insecure_channel_credentials


class ExperimentalApiWarning(Warning):
    '''A warning that an API is experimental.'''
    pass


def _warn_experimental(api_name, stack_offset):
    if api_name not in _EXPERIMENTAL_APIS_USED:
        _EXPERIMENTAL_APIS_USED.add(api_name)
        msg = "'{}' is an experimental API. It is subject to change or ".format(api_name) + 'removal between minor releases. Proceed with caution.'
        warnings.warn(msg, ExperimentalApiWarning, stacklevel = 2 + stack_offset)
        return None


def experimental_api(f):
    pass
# WARNING: Decompyle incomplete


def wrap_server_method_handler(wrapper, handler):
    '''Wraps the server method handler function.

    The server implementation requires all server handlers being wrapped as
    RpcMethodHandler objects. This helper function ease the pain of writing
    server handler wrappers.

    Args:
        wrapper: A wrapper function that takes in a method handler behavior
          (the actual function) and returns a wrapped function.
        handler: A RpcMethodHandler object to be wrapped.

    Returns:
        A newly created RpcMethodHandler.
    '''
    if not handler:
        return None
    if not None.request_streaming:
        if not handler.response_streaming:
            return handler._replace(unary_unary = wrapper(handler.unary_unary))
        return None._replace(unary_stream = wrapper(handler.unary_stream))
    if not None.response_streaming:
        return handler._replace(stream_unary = wrapper(handler.stream_unary))
    return None._replace(stream_stream = wrapper(handler.stream_stream))

__all__ = ('ChannelOptions', 'ExperimentalApiWarning', 'UsageError', 'insecure_channel_credentials', 'wrap_server_method_handler')
if sys.version_info > (3, 6):
    from grpc._simple_stubs import stream_stream
    from grpc._simple_stubs import stream_unary
    from grpc._simple_stubs import unary_stream
    from grpc._simple_stubs import unary_unary
    __all__ += ('unary_unary', 'unary_stream', 'stream_unary', 'stream_stream')
    return None
