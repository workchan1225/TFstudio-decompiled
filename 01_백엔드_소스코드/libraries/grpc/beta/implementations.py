# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: implementations.pyc (Python 3.11)

'''Entry points into the Beta API of gRPC Python.'''
import threading
import grpc
from grpc import _auth
from grpc.beta import _client_adaptations
from grpc.beta import _metadata
from grpc.beta import _server_adaptations
from grpc.beta import interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import face
ChannelCredentials = grpc.ChannelCredentials
ssl_channel_credentials = grpc.ssl_channel_credentials
CallCredentials = grpc.CallCredentials

def metadata_call_credentials(metadata_plugin, name = (None,)):
    pass
# WARNING: Decompyle incomplete


def google_call_credentials(credentials):
    '''Construct CallCredentials from GoogleCredentials.

    Args:
      credentials: A GoogleCredentials object from the oauth2client library.

    Returns:
      A CallCredentials object for use in a GRPCCallOptions object.
    '''
    return metadata_call_credentials(_auth.GoogleCallCredentials(credentials))

access_token_call_credentials = grpc.access_token_call_credentials
composite_call_credentials = grpc.composite_call_credentials
composite_channel_credentials = grpc.composite_channel_credentials

class Channel(object):
    '''A channel to a remote host through which RPCs may be conducted.

    Only the "subscribe" and "unsubscribe" methods are supported for application
    use. This class\' instance constructor and all other attributes are
    unsupported.
    '''
    
    def __init__(self, channel):
        self._channel = channel

    
    def subscribe(self, callback, try_to_connect = (None,)):
        """Subscribes to this Channel's connectivity.

        Args:
          callback: A callable to be invoked and passed an
            interfaces.ChannelConnectivity identifying this Channel's connectivity.
            The callable will be invoked immediately upon subscription and again for
            every change to this Channel's connectivity thereafter until it is
            unsubscribed.
          try_to_connect: A boolean indicating whether or not this Channel should
            attempt to connect if it is not already connected and ready to conduct
            RPCs.
        """
        self._channel.subscribe(callback, try_to_connect = try_to_connect)

    
    def unsubscribe(self, callback):
        '''Unsubscribes a callback from this Channel\'s connectivity.

        Args:
          callback: A callable previously registered with this Channel from having
            been passed to its "subscribe" method.
        '''
        self._channel.unsubscribe(callback)



def insecure_channel(host, port):
    """Creates an insecure Channel to a remote host.

    Args:
      host: The name of the remote host to which to connect.
      port: The port of the remote host to which to connect.
        If None only the 'host' part will be used.

    Returns:
      A Channel to the remote host through which RPCs may be conducted.
    """
    pass
# WARNING: Decompyle incomplete


def secure_channel(host, port, channel_credentials):
    """Creates a secure Channel to a remote host.

    Args:
      host: The name of the remote host to which to connect.
      port: The port of the remote host to which to connect.
        If None only the 'host' part will be used.
      channel_credentials: A ChannelCredentials.

    Returns:
      A secure Channel to the remote host through which RPCs may be conducted.
    """
    pass
# WARNING: Decompyle incomplete


class StubOptions(object):
    '''A value encapsulating the various options for creation of a Stub.

    This class and its instances have no supported interface - it exists to define
    the type of its instances and its instances exist to be passed to other
    functions.
    '''
    
    def __init__(self, host, request_serializers, response_deserializers, metadata_transformer, thread_pool, thread_pool_size):
        self.host = host
        self.request_serializers = request_serializers
        self.response_deserializers = response_deserializers
        self.metadata_transformer = metadata_transformer
        self.thread_pool = thread_pool
        self.thread_pool_size = thread_pool_size


_EMPTY_STUB_OPTIONS = StubOptions(None, None, None, None, None, None)

def stub_options(host, request_serializers, response_deserializers, metadata_transformer, thread_pool, thread_pool_size = (None, None, None, None, None, None)):
    '''Creates a StubOptions value to be passed at stub creation.

    All parameters are optional and should always be passed by keyword.

    Args:
      host: A host string to set on RPC calls.
      request_serializers: A dictionary from service name-method name pair to
        request serialization behavior.
      response_deserializers: A dictionary from service name-method name pair to
        response deserialization behavior.
      metadata_transformer: A callable that given a metadata object produces
        another metadata object to be used in the underlying communication on the
        wire.
      thread_pool: A thread pool to use in stubs.
      thread_pool_size: The size of thread pool to create for use in stubs;
        ignored if thread_pool has been passed.

    Returns:
      A StubOptions value created from the passed parameters.
    '''
    return StubOptions(host, request_serializers, response_deserializers, metadata_transformer, thread_pool, thread_pool_size)


def generic_stub(channel, options = (None,)):
    '''Creates a face.GenericStub on which RPCs can be made.

    Args:
      channel: A Channel for use by the created stub.
      options: A StubOptions customizing the created stub.

    Returns:
      A face.GenericStub on which RPCs can be made.
    '''
    pass
# WARNING: Decompyle incomplete


def dynamic_stub(channel, service, cardinalities, options = (None,)):
    '''Creates a face.DynamicStub with which RPCs can be invoked.

    Args:
      channel: A Channel for the returned face.DynamicStub to use.
      service: The package-qualified full name of the service.
      cardinalities: A dictionary from RPC method name to cardinality.Cardinality
        value identifying the cardinality of the RPC method.
      options: An optional StubOptions value further customizing the functionality
        of the returned face.DynamicStub.

    Returns:
      A face.DynamicStub with which RPCs can be invoked.
    '''
    pass
# WARNING: Decompyle incomplete

ServerCredentials = grpc.ServerCredentials
ssl_server_credentials = grpc.ssl_server_credentials

class ServerOptions(object):
    '''A value encapsulating the various options for creation of a Server.

    This class and its instances have no supported interface - it exists to define
    the type of its instances and its instances exist to be passed to other
    functions.
    '''
    
    def __init__(self, multi_method_implementation, request_deserializers, response_serializers, thread_pool, thread_pool_size, default_timeout, maximum_timeout):
        self.multi_method_implementation = multi_method_implementation
        self.request_deserializers = request_deserializers
        self.response_serializers = response_serializers
        self.thread_pool = thread_pool
        self.thread_pool_size = thread_pool_size
        self.default_timeout = default_timeout
        self.maximum_timeout = maximum_timeout


_EMPTY_SERVER_OPTIONS = ServerOptions(None, None, None, None, None, None, None)

def server_options(multi_method_implementation, request_deserializers, response_serializers, thread_pool, thread_pool_size, default_timeout, maximum_timeout = (None, None, None, None, None, None, None)):
    '''Creates a ServerOptions value to be passed at server creation.

    All parameters are optional and should always be passed by keyword.

    Args:
      multi_method_implementation: A face.MultiMethodImplementation to be called
        to service an RPC if the server has no specific method implementation for
        the name of the RPC for which service was requested.
      request_deserializers: A dictionary from service name-method name pair to
        request deserialization behavior.
      response_serializers: A dictionary from service name-method name pair to
        response serialization behavior.
      thread_pool: A thread pool to use in stubs.
      thread_pool_size: The size of thread pool to create for use in stubs;
        ignored if thread_pool has been passed.
      default_timeout: A duration in seconds to allow for RPC service when
        servicing RPCs that did not include a timeout value when invoked.
      maximum_timeout: A duration in seconds to allow for RPC service when
        servicing RPCs no matter what timeout value was passed when the RPC was
        invoked.

    Returns:
      A StubOptions value created from the passed parameters.
    '''
    return ServerOptions(multi_method_implementation, request_deserializers, response_serializers, thread_pool, thread_pool_size, default_timeout, maximum_timeout)


def server(service_implementations, options = (None,)):
    '''Creates an interfaces.Server with which RPCs can be serviced.

    Args:
      service_implementations: A dictionary from service name-method name pair to
        face.MethodImplementation.
      options: An optional ServerOptions value further customizing the
        functionality of the returned Server.

    Returns:
      An interfaces.Server with which RPCs can be serviced.
    '''
    pass
# WARNING: Decompyle incomplete
