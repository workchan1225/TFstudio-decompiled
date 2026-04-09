# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

import abc
import re
from typing import Awaitable, Callable, Optional, Sequence, Union
import warnings
import google.auth as google
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from google.oauth2 import service_account
import google.protobuf as google
from google.protobuf import empty_pb2, json_format
from grpc import Compression
import google.api_core as google
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import general_helpers
from google.api_core import retry as retries
from google.api_core import version
PROTOBUF_VERSION = google.protobuf.__version__
DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = version.__version__)

class OperationsTransport(abc.ABC):
    '''Abstract transport class for Operations.'''
    AUTH_SCOPES = ()
    DEFAULT_HOST: str = 'longrunning.googleapis.com'
    
    def __init__(self = None, *, host, credentials, credentials_file, scopes, quota_project_id, client_info, always_use_jwt_access, url_scheme, **kwargs):
        '''Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
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
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you\'re developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _prep_wrapped_messages(self, client_info):
        self._wrapped_methods = {
            self.cancel_operation: gapic_v1.method.wrap_method(self.cancel_operation, default_retry = retries.Retry(initial = 0.5, maximum = 10, multiplier = 2, predicate = retries.if_exception_type(core_exceptions.ServiceUnavailable), deadline = 10), default_timeout = 10, default_compression = Compression.NoCompression, client_info = client_info),
            self.delete_operation: gapic_v1.method.wrap_method(self.delete_operation, default_retry = retries.Retry(initial = 0.5, maximum = 10, multiplier = 2, predicate = retries.if_exception_type(core_exceptions.ServiceUnavailable), deadline = 10), default_timeout = 10, default_compression = Compression.NoCompression, client_info = client_info),
            self.get_operation: gapic_v1.method.wrap_method(self.get_operation, default_retry = retries.Retry(initial = 0.5, maximum = 10, multiplier = 2, predicate = retries.if_exception_type(core_exceptions.ServiceUnavailable), deadline = 10), default_timeout = 10, default_compression = Compression.NoCompression, client_info = client_info),
            self.list_operations: gapic_v1.method.wrap_method(self.list_operations, default_retry = retries.Retry(initial = 0.5, maximum = 10, multiplier = 2, predicate = retries.if_exception_type(core_exceptions.ServiceUnavailable), deadline = 10), default_timeout = 10, default_compression = Compression.NoCompression, client_info = client_info) }

    
    def close(self):
        '''Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        '''
        raise NotImplementedError()

    
    def _convert_protobuf_message_to_dict(self = None, message = None):
        '''Converts protobuf message to a dictionary.

        When the dictionary is encoded to JSON, it conforms to proto3 JSON spec.

        Args:
            message(google.protobuf.message.Message): The protocol buffers message
                instance to serialize.

        Returns:
            A dict representation of the protocol buffer message.
        '''
        if PROTOBUF_VERSION[0:2] in ('3.', '4.'):
            result = json_format.MessageToDict(message, preserving_proto_field_name = True, including_default_value_fields = True)
        else:
            result = json_format.MessageToDict(message, preserving_proto_field_name = True, always_print_fields_with_no_presence = True)
        return result

    list_operations = (lambda self = None: raise NotImplementedError())()
    get_operation = (lambda self = None: raise NotImplementedError())()
    delete_operation = (lambda self = None: raise NotImplementedError())()
    cancel_operation = (lambda self = None: raise NotImplementedError())()

__all__ = ('OperationsTransport',)
