# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

"""gRPC's Python API."""
import abc
import contextlib
import enum
import logging
import sys
from grpc import _compression
from grpc._cython import cygrpc as _cygrpc
from grpc._runtime_protos import protos
from grpc._runtime_protos import protos_and_services
from grpc._runtime_protos import services
logging.getLogger(__name__).addHandler(logging.NullHandler())

try:
    from grpc._grpcio_metadata import __version__
except ImportError:
    __version__ = 'dev0'


class FutureTimeoutError(Exception):
    '''Indicates that a method call on a Future timed out.'''
    pass


class FutureCancelledError(Exception):
    '''Indicates that the computation underlying a Future was cancelled.'''
    pass


class Future(abc.ABC):
    '''A representation of a computation in another control flow.

    Computations represented by a Future may be yet to be begun,
    may be ongoing, or may have already completed.
    '''
    cancel = (lambda self: raise NotImplementedError())()
    cancelled = (lambda self: raise NotImplementedError())()
    running = (lambda self: raise NotImplementedError())()
    done = (lambda self: raise NotImplementedError())()
    result = (lambda self, timeout = (None,): raise NotImplementedError())()
    exception = (lambda self, timeout = (None,): raise NotImplementedError())()
    traceback = (lambda self, timeout = (None,): raise NotImplementedError())()
    add_done_callback = (lambda self, fn: raise NotImplementedError())()

ChannelConnectivity = <NODE:12>()
StatusCode = <NODE:12>()

class Status(abc.ABC):
    '''Describes the status of an RPC.

    This is an EXPERIMENTAL API.

    Attributes:
      code: A StatusCode object to be sent to the client.
      details: A UTF-8-encodable string to be sent to the client upon
        termination of the RPC.
      trailing_metadata: The trailing :term:`metadata` in the RPC.
    '''
    pass


class RpcError(Exception):
    '''Raised by the gRPC library to indicate non-OK-status RPC termination.'''
    pass


class RpcContext(abc.ABC):
    '''Provides RPC-related information and action.'''
    is_active = (lambda self: raise NotImplementedError())()
    time_remaining = (lambda self: raise NotImplementedError())()
    cancel = (lambda self: raise NotImplementedError())()
    add_callback = (lambda self, callback: raise NotImplementedError())()


def Call():
    '''Call'''
    __doc__ = 'Invocation-side utility object for an RPC.'
    initial_metadata = (lambda self: raise NotImplementedError())()
    trailing_metadata = (lambda self: raise NotImplementedError())()
    code = (lambda self: raise NotImplementedError())()
    details = (lambda self: raise NotImplementedError())()

Call = <NODE:27>(Call, 'Call', RpcContext, metaclass = abc.ABCMeta)

class ClientCallDetails(abc.ABC):
    '''Describes an RPC to be invoked.

    Attributes:
      method: The method name of the RPC.
      timeout: An optional duration of time in seconds to allow for the RPC.
      metadata: Optional :term:`metadata` to be transmitted to
        the service-side of the RPC.
      credentials: An optional CallCredentials for the RPC.
      wait_for_ready: An optional flag to enable :term:`wait_for_ready` mechanism.
      compression: An element of grpc.compression, e.g.
        grpc.compression.Gzip.
    '''
    pass


class UnaryUnaryClientInterceptor(abc.ABC):
    '''Affords intercepting unary-unary invocations.'''
    intercept_unary_unary = (lambda self, continuation, client_call_details, request: raise NotImplementedError())()


class UnaryStreamClientInterceptor(abc.ABC):
    '''Affords intercepting unary-stream invocations.'''
    intercept_unary_stream = (lambda self, continuation, client_call_details, request: raise NotImplementedError())()


class StreamUnaryClientInterceptor(abc.ABC):
    '''Affords intercepting stream-unary invocations.'''
    intercept_stream_unary = (lambda self, continuation, client_call_details, request_iterator: raise NotImplementedError())()


class StreamStreamClientInterceptor(abc.ABC):
    '''Affords intercepting stream-stream invocations.'''
    intercept_stream_stream = (lambda self, continuation, client_call_details, request_iterator: raise NotImplementedError())()


class ChannelCredentials(object):
    '''An encapsulation of the data required to create a secure Channel.

    This class has no supported interface - it exists to define the type of its
    instances and its instances exist to be passed to other functions. For
    example, ssl_channel_credentials returns an instance of this class and
    secure_channel requires an instance of this class.
    '''
    
    def __init__(self, credentials):
        self._credentials = credentials



class CallCredentials(object):
    '''An encapsulation of the data required to assert an identity over a call.

    A CallCredentials has to be used with secure Channel, otherwise the
    metadata will not be transmitted to the server.

    A CallCredentials may be composed with ChannelCredentials to always assert
    identity for every call over that Channel.

    This class has no supported interface - it exists to define the type of its
    instances and its instances exist to be passed to other functions.
    '''
    
    def __init__(self, credentials):
        self._credentials = credentials



class AuthMetadataContext(abc.ABC):
    '''Provides information to call credentials metadata plugins.

    Attributes:
      service_url: A string URL of the service being called into.
      method_name: A string of the fully qualified method name being called.
    '''
    pass


class AuthMetadataPluginCallback(abc.ABC):
    '''Callback object received by a metadata plugin.'''
    
    def __call__(self, metadata, error):
        '''Passes to the gRPC runtime authentication metadata for an RPC.

        Args:
          metadata: The :term:`metadata` used to construct the CallCredentials.
          error: An Exception to indicate error or None to indicate success.
        '''
        raise NotImplementedError()



class AuthMetadataPlugin(abc.ABC):
    '''A specification for custom authentication.'''
    
    def __call__(self, context, callback):
        '''Implements authentication by passing metadata to a callback.

        This method will be invoked asynchronously in a separate thread.

        Args:
          context: An AuthMetadataContext providing information on the RPC that
            the plugin is being called to authenticate.
          callback: An AuthMetadataPluginCallback to be invoked either
            synchronously or asynchronously.
        '''
        raise NotImplementedError()



class ServerCredentials(object):
    '''An encapsulation of the data required to open a secure port on a Server.

    This class has no supported interface - it exists to define the type of its
    instances and its instances exist to be passed to other functions.
    '''
    
    def __init__(self, credentials):
        self._credentials = credentials



class ServerCertificateConfiguration(object):
    '''A certificate configuration for use with an SSL-enabled Server.

    Instances of this class can be returned in the certificate configuration
    fetching callback.

    This class has no supported interface -- it exists to define the
    type of its instances and its instances exist to be passed to
    other functions.
    '''
    
    def __init__(self, certificate_configuration):
        self._certificate_configuration = certificate_configuration



class UnaryUnaryMultiCallable(abc.ABC):
    '''Affords invoking a unary-unary RPC from client-side.'''
    __call__ = (lambda self, request, timeout, metadata, credentials, wait_for_ready, compression = (None, None, None, None, None): raise NotImplementedError())()
    with_call = (lambda self, request, timeout, metadata, credentials, wait_for_ready, compression = (None, None, None, None, None): raise NotImplementedError())()
    future = (lambda self, request, timeout, metadata, credentials, wait_for_ready, compression = (None, None, None, None, None): raise NotImplementedError())()


class UnaryStreamMultiCallable(abc.ABC):
    '''Affords invoking a unary-stream RPC from client-side.'''
    __call__ = (lambda self, request, timeout, metadata, credentials, wait_for_ready, compression = (None, None, None, None, None): raise NotImplementedError())()


class StreamUnaryMultiCallable(abc.ABC):
    '''Affords invoking a stream-unary RPC from client-side.'''
    __call__ = (lambda self, request_iterator, timeout, metadata, credentials, wait_for_ready, compression = (None, None, None, None, None): raise NotImplementedError())()
    with_call = (lambda self, request_iterator, timeout, metadata, credentials, wait_for_ready, compression = (None, None, None, None, None): raise NotImplementedError())()
    future = (lambda self, request_iterator, timeout, metadata, credentials, wait_for_ready, compression = (None, None, None, None, None): raise NotImplementedError())()


class StreamStreamMultiCallable(abc.ABC):
    '''Affords invoking a stream-stream RPC on client-side.'''
    __call__ = (lambda self, request_iterator, timeout, metadata, credentials, wait_for_ready, compression = (None, None, None, None, None): raise NotImplementedError())()


class Channel(abc.ABC):
    '''Affords RPC invocation via generic methods on client-side.

    Channel objects implement the Context Manager type, although they need not
    support being entered and exited multiple times.
    '''
    subscribe = (lambda self, callback, try_to_connect = (False,): raise NotImplementedError())()
    unsubscribe = (lambda self, callback: raise NotImplementedError())()
    unary_unary = (lambda self, method, request_serializer, response_deserializer, _registered_method = (None, None, False): raise NotImplementedError())()
    unary_stream = (lambda self, method, request_serializer, response_deserializer, _registered_method = (None, None, False): raise NotImplementedError())()
    stream_unary = (lambda self, method, request_serializer, response_deserializer, _registered_method = (None, None, False): raise NotImplementedError())()
    stream_stream = (lambda self, method, request_serializer, response_deserializer, _registered_method = (None, None, False): raise NotImplementedError())()
    close = (lambda self: raise NotImplementedError())()
    
    def __enter__(self):
        '''Enters the runtime context related to the channel object.'''
        raise NotImplementedError()

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Exits the runtime context related to the channel object.'''
        raise NotImplementedError()



def ServicerContext():
    '''ServicerContext'''
    __doc__ = 'A context object passed to method implementations.'
    invocation_metadata = (lambda self: raise NotImplementedError())()
    peer = (lambda self: raise NotImplementedError())()
    peer_identities = (lambda self: raise NotImplementedError())()
    peer_identity_key = (lambda self: raise NotImplementedError())()
    auth_context = (lambda self: raise NotImplementedError())()
    
    def set_compression(self, compression):
        '''Set the compression algorithm to be used for the entire call.

        Args:
          compression: An element of grpc.compression, e.g.
            grpc.compression.Gzip.
        '''
        raise NotImplementedError()

    send_initial_metadata = (lambda self, initial_metadata: raise NotImplementedError())()
    set_trailing_metadata = (lambda self, trailing_metadata: raise NotImplementedError())()
    
    def trailing_metadata(self):
        '''Access value to be used as trailing metadata upon RPC completion.

        This is an EXPERIMENTAL API.

        Returns:
          The trailing :term:`metadata` for the RPC.
        '''
        raise NotImplementedError()

    abort = (lambda self, code, details: raise NotImplementedError())()
    abort_with_status = (lambda self, status: raise NotImplementedError())()
    set_code = (lambda self, code: raise NotImplementedError())()
    set_details = (lambda self, details: raise NotImplementedError())()
    
    def code(self):
        '''Accesses the value to be used as status code upon RPC completion.

        This is an EXPERIMENTAL API.

        Returns:
          The StatusCode value for the RPC.
        '''
        raise NotImplementedError()

    
    def details(self):
        '''Accesses the value to be used as detail string upon RPC completion.

        This is an EXPERIMENTAL API.

        Returns:
          The details string of the RPC.
        '''
        raise NotImplementedError()

    
    def disable_next_message_compression(self):
        '''Disables compression for the next response message.

        This method will override any compression configuration set during
        server creation or set on the call.
        '''
        raise NotImplementedError()


ServicerContext = <NODE:27>(ServicerContext, 'ServicerContext', RpcContext, metaclass = abc.ABCMeta)

class RpcMethodHandler(abc.ABC):
    """An implementation of a single RPC method.

    Attributes:
      request_streaming: Whether the RPC supports exactly one request message
        or any arbitrary number of request messages.
      response_streaming: Whether the RPC supports exactly one response message
        or any arbitrary number of response messages.
      request_deserializer: A callable :term:`deserializer` that accepts a byte string and
        returns an object suitable to be passed to this object's business
        logic, or None to indicate that this object's business logic should be
        passed the raw request bytes.
      response_serializer: A callable :term:`serializer` that accepts an object produced
        by this object's business logic and returns a byte string, or None to
        indicate that the byte strings produced by this object's business logic
        should be transmitted on the wire as they are.
      unary_unary: This object's application-specific business logic as a
        callable value that takes a request value and a ServicerContext object
        and returns a response value. Only non-None if both request_streaming
        and response_streaming are False.
      unary_stream: This object's application-specific business logic as a
        callable value that takes a request value and a ServicerContext object
        and returns an iterator of response values. Only non-None if
        request_streaming is False and response_streaming is True.
      stream_unary: This object's application-specific business logic as a
        callable value that takes an iterator of request values and a
        ServicerContext object and returns a response value. Only non-None if
        request_streaming is True and response_streaming is False.
      stream_stream: This object's application-specific business logic as a
        callable value that takes an iterator of request values and a
        ServicerContext object and returns an iterator of response values.
        Only non-None if request_streaming and response_streaming are both
        True.
    """
    pass


class HandlerCallDetails(abc.ABC):
    '''Describes an RPC that has just arrived for service.

    Attributes:
      method: The method name of the RPC.
      invocation_metadata: The :term:`metadata` sent by the client.
    '''
    pass


class GenericRpcHandler(abc.ABC):
    '''An implementation of arbitrarily many RPC methods.'''
    service = (lambda self, handler_call_details: raise NotImplementedError())()


def ServiceRpcHandler():
    '''ServiceRpcHandler'''
    __doc__ = "An implementation of RPC methods belonging to a service.\n\n    A service handles RPC methods with structured names of the form\n    '/Service.Name/Service.Method', where 'Service.Name' is the value\n    returned by service_name(), and 'Service.Method' is the method\n    name.  A service can have multiple method names, but only a single\n    service name.\n    "
    service_name = (lambda self: raise NotImplementedError())()

ServiceRpcHandler = <NODE:27>(ServiceRpcHandler, 'ServiceRpcHandler', GenericRpcHandler, metaclass = abc.ABCMeta)

class ServerInterceptor(abc.ABC):
    '''Affords intercepting incoming RPCs on the service-side.'''
    intercept_service = (lambda self, continuation, handler_call_details: raise NotImplementedError())()


class Server(abc.ABC):
    '''Services RPCs.'''
    add_generic_rpc_handlers = (lambda self, generic_rpc_handlers: raise NotImplementedError())()
    
    def add_registered_method_handlers(self, service_name, method_handlers):
        '''Registers GenericRpcHandlers with this Server.

        This method is only safe to call before the server is started.

        If the same method have both generic and registered handler,
        registered handler will take precedence.

        Args:
          service_name: The service name.
          method_handlers: A dictionary that maps method names to corresponding
            RpcMethodHandler.
        '''
        pass

    add_insecure_port = (lambda self, address: raise NotImplementedError())()
    add_secure_port = (lambda self, address, server_credentials: raise NotImplementedError())()
    start = (lambda self: raise NotImplementedError())()
    stop = (lambda self, grace: raise NotImplementedError())()
    
    def wait_for_termination(self, timeout = (None,)):
        '''Block current thread until the server stops.

        This is an EXPERIMENTAL API.

        The wait will not consume computational resources during blocking, and
        it will block until one of the two following conditions are met:

        1) The server is stopped or terminated;
        2) A timeout occurs if timeout is not `None`.

        The timeout argument works in the same way as `threading.Event.wait()`.
        https://docs.python.org/3/library/threading.html#threading.Event.wait

        Args:
          timeout: A floating point number specifying a timeout for the
            operation in seconds.

        Returns:
          A bool indicates if the operation times out.
        '''
        raise NotImplementedError()



def unary_unary_rpc_method_handler(behavior, request_deserializer, response_serializer = (None, None)):
    '''Creates an RpcMethodHandler for a unary-unary RPC method.

    Args:
      behavior: The implementation of an RPC that accepts one request
        and returns one response.
      request_deserializer: An optional :term:`deserializer` for request deserialization.
      response_serializer: An optional :term:`serializer` for response serialization.

    Returns:
      An RpcMethodHandler object that is typically used by grpc.Server.
    '''
    _utilities = _utilities
    import grpc
    return _utilities.RpcMethodHandler(False, False, request_deserializer, response_serializer, behavior, None, None, None)


def unary_stream_rpc_method_handler(behavior, request_deserializer, response_serializer = (None, None)):
    '''Creates an RpcMethodHandler for a unary-stream RPC method.

    Args:
      behavior: The implementation of an RPC that accepts one request
        and returns an iterator of response values.
      request_deserializer: An optional :term:`deserializer` for request deserialization.
      response_serializer: An optional :term:`serializer` for response serialization.

    Returns:
      An RpcMethodHandler object that is typically used by grpc.Server.
    '''
    _utilities = _utilities
    import grpc
    return _utilities.RpcMethodHandler(False, True, request_deserializer, response_serializer, None, behavior, None, None)


def stream_unary_rpc_method_handler(behavior, request_deserializer, response_serializer = (None, None)):
    '''Creates an RpcMethodHandler for a stream-unary RPC method.

    Args:
      behavior: The implementation of an RPC that accepts an iterator of
        request values and returns a single response value.
      request_deserializer: An optional :term:`deserializer` for request deserialization.
      response_serializer: An optional :term:`serializer` for response serialization.

    Returns:
      An RpcMethodHandler object that is typically used by grpc.Server.
    '''
    _utilities = _utilities
    import grpc
    return _utilities.RpcMethodHandler(True, False, request_deserializer, response_serializer, None, None, behavior, None)


def stream_stream_rpc_method_handler(behavior, request_deserializer, response_serializer = (None, None)):
    '''Creates an RpcMethodHandler for a stream-stream RPC method.

    Args:
      behavior: The implementation of an RPC that accepts an iterator of
        request values and returns an iterator of response values.
      request_deserializer: An optional :term:`deserializer` for request deserialization.
      response_serializer: An optional :term:`serializer` for response serialization.

    Returns:
      An RpcMethodHandler object that is typically used by grpc.Server.
    '''
    _utilities = _utilities
    import grpc
    return _utilities.RpcMethodHandler(True, True, request_deserializer, response_serializer, None, None, None, behavior)


def method_handlers_generic_handler(service, method_handlers):
    '''Creates a GenericRpcHandler from RpcMethodHandlers.

    Args:
      service: The name of the service that is implemented by the
        method_handlers.
      method_handlers: A dictionary that maps method names to corresponding
        RpcMethodHandler.

    Returns:
      A GenericRpcHandler. This is typically added to the grpc.Server object
      with add_generic_rpc_handlers() before starting the server.
    '''
    _utilities = _utilities
    import grpc
    return _utilities.DictionaryGenericHandler(service, method_handlers)


def ssl_channel_credentials(root_certificates, private_key, certificate_chain = (None, None, None)):
    '''Creates a ChannelCredentials for use with an SSL-enabled Channel.

    Args:
      root_certificates: The PEM-encoded root certificates as a byte string,
        or None to retrieve them from a default location chosen by gRPC
        runtime.
      private_key: The PEM-encoded private key as a byte string, or None if no
        private key should be used.
      certificate_chain: The PEM-encoded certificate chain as a byte string
        to use or None if no certificate chain should be used.

    Returns:
      A ChannelCredentials for use with an SSL-enabled Channel.
    '''
    return ChannelCredentials(_cygrpc.SSLChannelCredentials(root_certificates, private_key, certificate_chain))


def xds_channel_credentials(fallback_credentials = (None,)):
    '''Creates a ChannelCredentials for use with xDS. This is an EXPERIMENTAL
      API.

    Args:
      fallback_credentials: Credentials to use in case it is not possible to
        establish a secure connection via xDS. If no fallback_credentials
        argument is supplied, a default SSLChannelCredentials is used.
    '''
    pass
# WARNING: Decompyle incomplete


def metadata_call_credentials(metadata_plugin, name = (None,)):
    '''Construct CallCredentials from an AuthMetadataPlugin.

    Args:
      metadata_plugin: An AuthMetadataPlugin to use for authentication.
      name: An optional name for the plugin.

    Returns:
      A CallCredentials.
    '''
    _plugin_wrapping = _plugin_wrapping
    import grpc
    return _plugin_wrapping.metadata_plugin_call_credentials(metadata_plugin, name)


def access_token_call_credentials(access_token):
    '''Construct CallCredentials from an access token.

    Args:
      access_token: A string to place directly in the http request
        authorization header, for example
        "authorization: Bearer <access_token>".

    Returns:
      A CallCredentials.
    '''
    _auth = _auth
    import grpc
    _plugin_wrapping = _plugin_wrapping
    import grpc
    return _plugin_wrapping.metadata_plugin_call_credentials(_auth.AccessTokenAuthMetadataPlugin(access_token), None)


def composite_call_credentials(*call_credentials):
    '''Compose multiple CallCredentials to make a new CallCredentials.

    Args:
      *call_credentials: At least two CallCredentials objects.

    Returns:
      A CallCredentials object composed of the given CallCredentials objects.
    '''
    return _cygrpc.CompositeCallCredentials(tuple((lambda .0: pass# WARNING: Decompyle incomplete
)(call_credentials())))


def composite_channel_credentials(channel_credentials, *call_credentials):
    '''Compose a ChannelCredentials and one or more CallCredentials objects.

    Args:
      channel_credentials: A ChannelCredentials object.
      *call_credentials: One or more CallCredentials objects.

    Returns:
      A ChannelCredentials composed of the given ChannelCredentials and
        CallCredentials objects.
    '''
    return _cygrpc.CompositeChannelCredentials(tuple((lambda .0: pass# WARNING: Decompyle incomplete
)(call_credentials()), channel_credentials._credentials))


def ssl_server_credentials(private_key_certificate_chain_pairs, root_certificates, require_client_auth = (None, False)):
    '''Creates a ServerCredentials for use with an SSL-enabled Server.

    Args:
      private_key_certificate_chain_pairs: A list of pairs of the form
        [PEM-encoded private key, PEM-encoded certificate chain].
      root_certificates: An optional byte string of PEM-encoded client root
        certificates that the server will use to verify client authentication.
        If omitted, require_client_auth must also be False.
      require_client_auth: A boolean indicating whether or not to require
        clients to be authenticated. May only be True if root_certificates
        is not None.

    Returns:
      A ServerCredentials for use with an SSL-enabled Server. Typically, this
      object is an argument to add_secure_port() method during server setup.
    '''
    if not private_key_certificate_chain_pairs:
        error_msg = 'At least one private key-certificate chain pair is required!'
        raise ValueError(error_msg)
# WARNING: Decompyle incomplete


def xds_server_credentials(fallback_credentials):
    '''Creates a ServerCredentials for use with xDS. This is an EXPERIMENTAL
      API.

    Args:
      fallback_credentials: Credentials to use in case it is not possible to
        establish a secure connection via xDS. No default value is provided.
    '''
    return ServerCredentials(_cygrpc.xds_server_credentials(fallback_credentials._credentials))


def insecure_server_credentials():
    '''Creates a credentials object directing the server to use no credentials.
      This is an EXPERIMENTAL API.

    This object cannot be used directly in a call to `add_secure_port`.
    Instead, it should be used to construct other credentials objects, e.g.
    with xds_server_credentials.
    '''
    return ServerCredentials(_cygrpc.insecure_server_credentials())


def ssl_server_certificate_configuration(private_key_certificate_chain_pairs, root_certificates = (None,)):
    '''Creates a ServerCertificateConfiguration for use with a Server.

    Args:
      private_key_certificate_chain_pairs: A collection of pairs of
        the form [PEM-encoded private key, PEM-encoded certificate
        chain].
      root_certificates: An optional byte string of PEM-encoded client root
        certificates that the server will use to verify client authentication.

    Returns:
      A ServerCertificateConfiguration that can be returned in the certificate
        configuration fetching callback.
    '''
    if private_key_certificate_chain_pairs:
        
        def <listcomp>(.0):
            return [ _cygrpc.SslPemKeyCertPair(key, pem) for key, pem in .0 ]

        return _cygrpc.server_certificate_config_ssl(root_certificates(<listcomp>, private_key_certificate_chain_pairs()))
    error_msg = None
    raise ValueError(error_msg)


def dynamic_ssl_server_credentials(initial_certificate_configuration, certificate_configuration_fetcher, require_client_authentication = (False,)):
    """Creates a ServerCredentials for use with an SSL-enabled Server.

    Args:
      initial_certificate_configuration (ServerCertificateConfiguration): The
        certificate configuration with which the server will be initialized.
      certificate_configuration_fetcher (callable): A callable that takes no
        arguments and should return a ServerCertificateConfiguration to
        replace the server's current certificate, or None for no change
        (i.e., the server will continue its current certificate
        config). The library will call this callback on *every* new
        client connection before starting the TLS handshake with the
        client, thus allowing the user application to optionally
        return a new ServerCertificateConfiguration that the server will then
        use for the handshake.
      require_client_authentication: A boolean indicating whether or not to
        require clients to be authenticated.

    Returns:
      A ServerCredentials.
    """
    return ServerCredentials(_cygrpc.server_credentials_ssl_dynamic_cert_config(initial_certificate_configuration, certificate_configuration_fetcher, require_client_authentication))

LocalConnectionType = <NODE:12>()

def local_channel_credentials(local_connect_type = (LocalConnectionType.LOCAL_TCP,)):
    '''Creates a local ChannelCredentials used for local connections.

    This is an EXPERIMENTAL API.

    Local credentials are used by local TCP endpoints (e.g. localhost:10000)
    also UDS connections.

    The connections created by local channel credentials are not
    encrypted, but will be checked if they are local or not.
    The UDS connections are considered secure by providing peer authentication
    and data confidentiality while TCP connections are considered insecure.

    It is allowed to transmit call credentials over connections created by
    local channel credentials.

    Local channel credentials are useful for 1) eliminating insecure_channel usage;
    2) enable unit testing for call credentials without setting up secrets.

    Args:
      local_connect_type: Local connection type (either
        grpc.LocalConnectionType.UDS or grpc.LocalConnectionType.LOCAL_TCP)

    Returns:
      A ChannelCredentials for use with a local Channel
    '''
    return ChannelCredentials(_cygrpc.channel_credentials_local(local_connect_type.value))


def local_server_credentials(local_connect_type = (LocalConnectionType.LOCAL_TCP,)):
    '''Creates a local ServerCredentials used for local connections.

    This is an EXPERIMENTAL API.

    Local credentials are used by local TCP endpoints (e.g. localhost:10000)
    also UDS connections.

    The connections created by local server credentials are not
    encrypted, but will be checked if they are local or not.
    The UDS connections are considered secure by providing peer authentication
    and data confidentiality while TCP connections are considered insecure.

    It is allowed to transmit call credentials over connections created by local
    server credentials.

    Local server credentials are useful for 1) eliminating insecure_channel usage;
    2) enable unit testing for call credentials without setting up secrets.

    Args:
      local_connect_type: Local connection type (either
        grpc.LocalConnectionType.UDS or grpc.LocalConnectionType.LOCAL_TCP)

    Returns:
      A ServerCredentials for use with a local Server
    '''
    return ServerCredentials(_cygrpc.server_credentials_local(local_connect_type.value))


def alts_channel_credentials(service_accounts = (None,)):
