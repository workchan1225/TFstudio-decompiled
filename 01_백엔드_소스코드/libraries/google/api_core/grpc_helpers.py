# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grpc_helpers.pyc (Python 3.11)

'''Helpers for :mod:`grpc`.'''
import collections
import functools
from typing import Generic, Iterator, Optional, TypeVar
import warnings
import google.auth as google
import google.auth.credentials as google
import google.auth.transport.grpc as google
import google.auth.transport.requests as google
import google.protobuf as google
import grpc
from google.api_core import exceptions, general_helpers
PROTOBUF_VERSION = google.protobuf.__version__
if PROTOBUF_VERSION[0:2] == '3.':
    
    try:
        import grpc_gcp
        warnings.warn('Support for grpcio-gcp is deprecated. This feature will be\n            removed from `google-api-core` after January 1, 2024. If you need to\n            continue to use this feature, please pin to a specific version of\n            `google-api-core`.', DeprecationWarning)
        HAS_GRPC_GCP = True
    except ImportError:
        HAS_GRPC_GCP = False
    except:
        HAS_GRPC_GCP = False

    _STREAM_WRAP_CLASSES = (grpc.UnaryStreamMultiCallable, grpc.StreamStreamMultiCallable)
    P = TypeVar('P')
    
    def _patch_callable_name(callable_):
        '''Fix-up gRPC callable attributes.

    gRPC callable lack the ``__name__`` attribute which causes
    :func:`functools.wraps` to error. This adds the attribute if needed.
    '''
        if not hasattr(callable_, '__name__'):
            callable_.__name__ = callable_.__class__.__name__
            return None

    
    def _wrap_unary_errors(callable_):
        '''Map errors for Unary-Unary and Stream-Unary gRPC callables.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _StreamingResponseIterator():
        '''_StreamingResponseIterator'''
        
        def __init__(self, wrapped, prefetch_first_result = (True,)):
            self._wrapped = wrapped
            
            try:
                if prefetch_first_result:
                    self._stored_first_result = next(self._wrapped)
                    return None
                return None
            except TypeError:
                return None
                except StopIteration:
                    return None


        
        def __iter__(self = None):
            '''This iterator is also an iterable that returns itself.'''
            return self

        
        def __next__(self = None):
            '''Get the next response from the stream.

        Returns:
            protobuf.Message: A single response from the stream.
        '''
            
            try:
                if hasattr(self, '_stored_first_result'):
                    result = self._stored_first_result
                    del self._stored_first_result
                    return result
                return None(self._wrapped)
            except grpc.RpcError:
                exc = None
                raise exceptions.from_grpc_error(exc), exc
                exc = None
                del exc


        
        def add_callback(self, callback):
            return self._wrapped.add_callback(callback)

        
        def cancel(self):
            return self._wrapped.cancel()

        
        def code(self):
            return self._wrapped.code()

        
        def details(self):
            return self._wrapped.details()

        
        def initial_metadata(self):
            return self._wrapped.initial_metadata()

        
        def is_active(self):
            return self._wrapped.is_active()

        
        def time_remaining(self):
            return self._wrapped.time_remaining()

        
        def trailing_metadata(self):
            return self._wrapped.trailing_metadata()


    _StreamingResponseIterator = <NODE:27>(_StreamingResponseIterator, '_StreamingResponseIterator', Generic[P], grpc.Call)
    GrpcStream = _StreamingResponseIterator[P]
    
    def _wrap_stream_errors(callable_):
        '''Wrap errors for Unary-Stream and Stream-Stream gRPC callables.

    The callables that return iterators require a bit more logic to re-map
    errors when iterating. This wraps both the initial invocation and the
    iterator of the return value to re-map errors.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    def wrap_errors(callable_):
        '''Wrap a gRPC callable and map :class:`grpc.RpcErrors` to friendly error
    classes.

    Errors raised by the gRPC callable are mapped to the appropriate
    :class:`google.api_core.exceptions.GoogleAPICallError` subclasses.
    The original `grpc.RpcError` (which is usually also a `grpc.Call`) is
    available from the ``response`` property on the mapped exception. This
    is useful for extracting metadata from the original error.

    Args:
        callable_ (Callable): A gRPC callable.

    Returns:
        Callable: The wrapped gRPC callable.
    '''
        if isinstance(callable_, _STREAM_WRAP_CLASSES):
            return _wrap_stream_errors(callable_)
        return None(callable_)

    
    def _create_composite_credentials(credentials, credentials_file, default_scopes, scopes, ssl_credentials, quota_project_id, default_host = (None, None, None, None, None, None, None)):
        '''Create the composite credentials for secure channels.

    Args:
        credentials (google.auth.credentials.Credentials): The credentials. If
            not specified, then this function will attempt to ascertain the
            credentials from the environment using :func:`google.auth.default`.
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
        default_scopes (Sequence[str]): A optional list of scopes needed for this
            service. These are only used when credentials are not specified and
            are passed to :func:`google.auth.default`.
        scopes (Sequence[str]): A optional list of scopes needed for this
            service. These are only used when credentials are not specified and
            are passed to :func:`google.auth.default`.
        ssl_credentials (grpc.ChannelCredentials): Optional SSL channel
            credentials. This can be used to specify different certificates.
        quota_project_id (str): An optional project to use for billing and quota.
        default_host (str): The default endpoint. e.g., "pubsub.googleapis.com".

    Returns:
        grpc.ChannelCredentials: The composed channel credentials object.

    Raises:
        google.api_core.DuplicateCredentialArgs: If both a credentials object and credentials_file are passed.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    def create_channel(target, credentials, scopes, ssl_credentials, credentials_file, quota_project_id = None, default_scopes = None, default_host = None, compression = (None, None, None, None, None, None, None, None, False), attempt_direct_path = ('attempt_direct_path', Optional[bool]), **kwargs):
        '''Create a secure channel with credentials.

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
        credentials_file (str): A file with credentials that can be loaded with
            :func:`google.auth.load_credentials_from_file`. This argument is
            mutually exclusive with credentials.

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

        kwargs: Additional key-word args passed to
            :func:`grpc_gcp.secure_channel` or :func:`grpc.secure_channel`.
            Note: `grpc_gcp` is only supported in environments with protobuf < 4.0.0.

    Returns:
        grpc.Channel: The created channel.

    Raises:
        google.api_core.DuplicateCredentialArgs: If both a credentials object and credentials_file are passed.
        ValueError: If `ssl_credentials` is set and `attempt_direct_path` is set to `True`.
    '''
        if ssl_credentials and attempt_direct_path:
            raise ValueError('Using ssl_credentials with Direct Path is not supported')
        composite_credentials = _create_composite_credentials(credentials = credentials, credentials_file = credentials_file, default_scopes = default_scopes, scopes = scopes, ssl_credentials = ssl_credentials, quota_project_id = quota_project_id, default_host = default_host)
    # WARNING: Decompyle incomplete

    
    def _modify_target_for_direct_path(target = None):
        """
    Given a target, return a modified version which is compatible with Direct Path.

    Args:
        target (str): The target service address in the format 'hostname[:port]' or
            'dns://hostname[:port]'.

    Returns:
        target (str): The target service address which is converted into a format compatible with Direct Path.
            If the target contains `dns:///` or does not contain `:///`, the target will be converted in
            a format compatible with Direct Path; otherwise the original target will be returned as the
            original target may already denote Direct Path.
    """
        dns_prefix = 'dns:///'
        target = target.replace(dns_prefix, '')
        direct_path_separator = ':///'
        if direct_path_separator not in target:
            target_without_port = target.split(':')[0]
            target = f'''google-c2p{direct_path_separator}{target_without_port}'''
        return target

    _MethodCall = collections.namedtuple('_MethodCall', ('request', 'timeout', 'metadata', 'credentials', 'compression'))
    _ChannelRequest = collections.namedtuple('_ChannelRequest', ('method', 'request'))
    
    class _CallableStub(object):
        '''Stub for the grpc.*MultiCallable interfaces.'''
        
        def __init__(self, method, channel):
            self._method = method
            self._channel = channel
            self.response = None
            self.responses = None
            self.requests = []
            self.calls = []

        
        def __call__(self, request, timeout, metadata, credentials, compression = (None, None, None, None)):
            self._channel.requests.append(_ChannelRequest(self._method, request))
            self.calls.append(_MethodCall(request, timeout, metadata, credentials, compression))
            self.requests.append(request)
            response = self.response
        # WARNING: Decompyle incomplete


    
    def _simplify_method_name(method):
        '''Simplifies a gRPC method name.

    When gRPC invokes the channel to create a callable, it gives a full
    method name like "/google.pubsub.v1.Publisher/CreateTopic". This
    returns just the name of the method, in this case "CreateTopic".

    Args:
        method (str): The name of the method.

    Returns:
        str: The simplified name of the method.
    '''
        return method.rsplit('/', 1).pop()

    
    class ChannelStub(grpc.Channel):
        """A testing stub for the grpc.Channel interface.

    This can be used to test any client that eventually uses a gRPC channel
    to communicate. By passing in a channel stub, you can configure which
    responses are returned and track which requests are made.

    For example:

    .. code-block:: python

        channel_stub = grpc_helpers.ChannelStub()
        client = FooClient(channel=channel_stub)

        channel_stub.GetFoo.response = foo_pb2.Foo(name='bar')

        foo = client.get_foo(labels=['baz'])

        assert foo.name == 'bar'
        assert channel_stub.GetFoo.requests[0].labels = ['baz']

    Each method on the stub can be accessed and configured on the channel.
    Here's some examples of various configurations:

    .. code-block:: python

        # Return a basic response:

        channel_stub.GetFoo.response = foo_pb2.Foo(name='bar')
        assert client.get_foo().name == 'bar'

        # Raise an exception:
        channel_stub.GetFoo.response = NotFound('...')

        with pytest.raises(NotFound):
            client.get_foo()

        # Use a sequence of responses:
        channel_stub.GetFoo.responses = iter([
            foo_pb2.Foo(name='bar'),
            foo_pb2.Foo(name='baz'),
        ])

        assert client.get_foo().name == 'bar'
        assert client.get_foo().name == 'baz'

        # Use a callable

        def on_get_foo(request):
            return foo_pb2.Foo(name='bar' + request.id)

        channel_stub.GetFoo.response = on_get_foo

        assert client.get_foo(id='123').name == 'bar123'
    """
        
        def __init__(self, responses = ([],)):
            self.requests = []
            self._method_stubs = { }

        
        def _stub_for_method(self, method):
            method = _simplify_method_name(method)
            self._method_stubs[method] = _CallableStub(method, self)
            return self._method_stubs[method]

        
        def __getattr__(self, key):
            
            try:
                return self._method_stubs[key]
            except KeyError:
                raise AttributeError


        
        def unary_unary(self, method, request_serializer, response_deserializer, _registered_method = (None, None, False)):
            '''grpc.Channel.unary_unary implementation.'''
            return self._stub_for_method(method)

        
        def unary_stream(self, method, request_serializer, response_deserializer, _registered_method = (None, None, False)):
            '''grpc.Channel.unary_stream implementation.'''
            return self._stub_for_method(method)

        
        def stream_unary(self, method, request_serializer, response_deserializer, _registered_method = (None, None, False)):
            '''grpc.Channel.stream_unary implementation.'''
            return self._stub_for_method(method)

        
        def stream_stream(self, method, request_serializer, response_deserializer, _registered_method = (None, None, False)):
            '''grpc.Channel.stream_stream implementation.'''
            return self._stub_for_method(method)

        
        def subscribe(self, callback, try_to_connect = (False,)):
            '''grpc.Channel.subscribe implementation.'''
            pass

        
        def unsubscribe(self, callback):
            '''grpc.Channel.unsubscribe implementation.'''
            pass

        
        def close(self):
            '''grpc.Channel.close implementation.'''
            pass


    return None
