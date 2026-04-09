# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: interfaces.pyc (Python 3.11)

'''Constants and interfaces of the Beta API of gRPC Python.'''
import abc
import grpc
ChannelConnectivity = grpc.ChannelConnectivity
ChannelConnectivity.FATAL_FAILURE = ChannelConnectivity.SHUTDOWN
StatusCode = grpc.StatusCode

class GRPCCallOptions(object):
    '''A value encapsulating gRPC-specific options passed on RPC invocation.

    This class and its instances have no supported interface - it exists to
    define the type of its instances and its instances exist to be passed to
    other functions.
    '''
    
    def __init__(self, disable_compression, subcall_of, credentials):
        self.disable_compression = disable_compression
        self.subcall_of = subcall_of
        self.credentials = credentials



def grpc_call_options(disable_compression, credentials = (False, None)):
    '''Creates a GRPCCallOptions value to be passed at RPC invocation.

    All parameters are optional and should always be passed by keyword.

    Args:
      disable_compression: A boolean indicating whether or not compression should
        be disabled for the request object of the RPC. Only valid for
        request-unary RPCs.
      credentials: A CallCredentials object to use for the invoked RPC.
    '''
    return GRPCCallOptions(disable_compression, None, credentials)

GRPCAuthMetadataContext = grpc.AuthMetadataContext
GRPCAuthMetadataPluginCallback = grpc.AuthMetadataPluginCallback
GRPCAuthMetadataPlugin = grpc.AuthMetadataPlugin

class GRPCServicerContext(abc.ABC):
    '''Exposes gRPC-specific options and behaviors to code servicing RPCs.'''
    peer = (lambda self: raise NotImplementedError())()
    disable_next_response_compression = (lambda self: raise NotImplementedError())()


class GRPCInvocationContext(abc.ABC):
    '''Exposes gRPC-specific options and behaviors to code invoking RPCs.'''
    disable_next_request_compression = (lambda self: raise NotImplementedError())()


class Server(abc.ABC):
    '''Services RPCs.'''
    add_insecure_port = (lambda self, address: raise NotImplementedError())()
    add_secure_port = (lambda self, address, server_credentials: raise NotImplementedError())()
    start = (lambda self: raise NotImplementedError())()
    stop = (lambda self, grace: raise NotImplementedError())()
