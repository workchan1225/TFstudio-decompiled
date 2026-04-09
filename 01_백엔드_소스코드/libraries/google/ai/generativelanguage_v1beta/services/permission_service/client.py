# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

from collections import OrderedDict
import logging as std_logging
import os
import re
from typing import Callable, Dict, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union, cast
import warnings
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.auth.transport import mtls
from google.auth.transport.grpc import SslCredentials
from google.oauth2 import service_account
from google.ai.generativelanguage_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[(retries.Retry, gapic_v1.method._MethodDefault, None)]
except AttributeError:
    OptionalRetry = Union[(retries.Retry, object, None)]


try:
    from google.api_core import client_logging
    CLIENT_LOGGING_SUPPORTED = True
except ImportError:
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)
from google.longrunning import operations_pb2
from google.protobuf import field_mask_pb2
from google.ai.generativelanguage_v1beta.services.permission_service import pagers
from google.ai.generativelanguage_v1beta.types import permission as gag_permission
from google.ai.generativelanguage_v1beta.types import permission
from google.ai.generativelanguage_v1beta.types import permission_service
from transports.base import DEFAULT_CLIENT_INFO, PermissionServiceTransport
from transports.grpc import PermissionServiceGrpcTransport
from transports.grpc_asyncio import PermissionServiceGrpcAsyncIOTransport
from transports.rest import PermissionServiceRestTransport

class PermissionServiceClientMeta(type):
    '''Metaclass for the PermissionService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    '''
    _transport_registry = OrderedDict()
    _transport_registry['grpc'] = PermissionServiceGrpcTransport
    _transport_registry['grpc_asyncio'] = PermissionServiceGrpcAsyncIOTransport
    _transport_registry['rest'] = PermissionServiceRestTransport
    
    def get_transport_class(cls = None, label = None):
        '''Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        '''
        if label:
            return cls._transport_registry[label]
        return None(iter(cls._transport_registry.values()))



def PermissionServiceClient():
    '''PermissionServiceClient'''
    __doc__ = 'Provides methods for managing permissions to PaLM API\n    resources.\n    '
    _get_default_mtls_endpoint = (lambda api_endpoint: if not api_endpoint:
api_endpointmtls_endpoint_re = None.compile('(?P<name>[^.]+)(?P<mtls>\\.mtls)?(?P<sandbox>\\.sandbox)?(?P<googledomain>\\.googleapis\\.com)?')m = mtls_endpoint_re.match(api_endpoint)(name, mtls, sandbox, googledomain) = m.groups()if not mtls or googledomain:
api_endpointif None:
api_endpoint.replace('sandbox.googleapis.com', 'mtls.sandbox.googleapis.com')None.replace('.googleapis.com', '.mtls.googleapis.com'))()
    DEFAULT_ENDPOINT = 'generativelanguage.googleapis.com'
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(DEFAULT_ENDPOINT)
    _DEFAULT_ENDPOINT_TEMPLATE = 'generativelanguage.{UNIVERSE_DOMAIN}'
    _DEFAULT_UNIVERSE = 'googleapis.com'
    from_service_account_info = (lambda cls = None, info = staticmethod: credentials = service_account.Credentials.from_service_account_info(info)kwargs['credentials'] = credentials# WARNING: Decompyle incomplete
)()
    from_service_account_file = (lambda cls = None, filename = None: credentials = service_account.Credentials.from_service_account_file(filename)kwargs['credentials'] = credentials# WARNING: Decompyle incomplete
)()
    from_service_account_json = from_service_account_file
    transport = (lambda self = None: self._transport)()
    permission_path = (lambda tuned_model = None, permission = None: 'tunedModels/{tuned_model}/permissions/{permission}'.format(tuned_model = tuned_model, permission = permission))()
    parse_permission_path = (lambda path = None: m = re.match('^tunedModels/(?P<tuned_model>.+?)/permissions/(?P<permission>.+?)$', path)m.groupdict() if m else { })()
    common_billing_account_path = (lambda billing_account = None: 'billingAccounts/{billing_account}'.format(billing_account = billing_account))()
    parse_common_billing_account_path = (lambda path = None: m = re.match('^billingAccounts/(?P<billing_account>.+?)$', path)m.groupdict() if m else { })()
    common_folder_path = (lambda folder = None: 'folders/{folder}'.format(folder = folder))()
    parse_common_folder_path = (lambda path = None: m = re.match('^folders/(?P<folder>.+?)$', path)m.groupdict() if m else { })()
    common_organization_path = (lambda organization = None: 'organizations/{organization}'.format(organization = organization))()
    parse_common_organization_path = (lambda path = None: m = re.match('^organizations/(?P<organization>.+?)$', path)m.groupdict() if m else { })()
    common_project_path = (lambda project = None: 'projects/{project}'.format(project = project))()
    parse_common_project_path = (lambda path = None: m = re.match('^projects/(?P<project>.+?)$', path)m.groupdict() if m else { })()
    common_location_path = (lambda project = None, location = None: 'projects/{project}/locations/{location}'.format(project = project, location = location))()
    parse_common_location_path = (lambda path = None: m = re.match('^projects/(?P<project>.+?)/locations/(?P<location>.+?)$', path)m.groupdict() if m else { })()
    get_mtls_endpoint_and_cert_source = (lambda cls = None, client_options = None: warnings.warn('get_mtls_endpoint_and_cert_source is deprecated. Use the api_endpoint property instead.', DeprecationWarning)# WARNING: Decompyle incomplete
)()
    _read_environment_variables = (lambda : use_client_cert = os.getenv('GOOGLE_API_USE_CLIENT_CERTIFICATE', 'false').lower()use_mtls_endpoint = os.getenv('GOOGLE_API_USE_MTLS_ENDPOINT', 'auto').lower()universe_domain_env = os.getenv('GOOGLE_CLOUD_UNIVERSE_DOMAIN')if use_client_cert not in ('true', 'false'):
raise ValueError('Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be either `true` or `false`')if use_mtls_endpoint not in ('auto', 'never', 'always'):
raise MutualTLSChannelError('Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`')(use_client_cert == 'true', use_mtls_endpoint, universe_domain_env))()
    _get_client_cert_source = (lambda provided_cert_source, use_cert_flag: client_cert_source = Noneif use_cert_flag:
if provided_cert_source:
client_cert_source = provided_cert_sourceelif mtls.has_default_client_cert_source():
client_cert_source = mtls.default_client_cert_source()client_cert_source)()
    _get_api_endpoint = (lambda api_override, client_cert_source, universe_domain, use_mtls_endpoint: pass# WARNING: Decompyle incomplete
)()
    _get_universe_domain = (lambda client_universe_domain = staticmethod, universe_domain_env = staticmethod: universe_domain = PermissionServiceClient._DEFAULT_UNIVERSE# WARNING: Decompyle incomplete
)()
    
    def _validate_universe_domain(self):
        """Validates client's and credentials' universe domains are consistent.

        Returns:
            bool: True iff the configured universe domain is valid.

        Raises:
            ValueError: If the configured universe domain is not valid.
        """
        return True

    api_endpoint = (lambda self: self._api_endpoint)()
    universe_domain = (lambda self = staticmethod: self._universe_domain)()
    
    def __init__(self = None, *, credentials, transport, client_options, client_info):
        '''Instantiates the permission service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,PermissionServiceTransport,Callable[..., PermissionServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the PermissionServiceTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that the ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you\'re developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        '''
        self._client_options = client_options
        if isinstance(self._client_options, dict):
            self._client_options = client_options_lib.from_dict(self._client_options)
    # WARNING: Decompyle incomplete

    
    def create_permission(self = None, request = None, *, parent, permission, retry, timeout, metadata):
        '''Create a permission to a specific resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_create_permission():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.CreatePermissionRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_permission(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.CreatePermissionRequest, dict]):
                The request object. Request to create a ``Permission``.
            parent (str):
                Required. The parent resource of the ``Permission``.
                Formats: ``tunedModels/{tuned_model}``
                ``corpora/{corpus}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            permission (google.ai.generativelanguage_v1beta.types.Permission):
                Required. The permission to create.
                This corresponds to the ``permission`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.types.Permission:
                Permission resource grants user,
                group or the rest of the world access to
                the PaLM API resource (e.g. a tuned
                model, corpus).

                A role is a collection of permitted
                operations that allows users to perform
                specific actions on PaLM API resources.
                To make them available to users, groups,
                or service accounts, you assign roles.
                When you assign a role, you grant
                permissions that the role contains.

                There are three concentric roles. Each
                role is a superset of the previous
                role\'s permitted operations:

                - reader can use the resource (e.g.
                  tuned model, corpus) for inference
                - writer has reader\'s permissions and
                  additionally can edit and share
                - owner has writer\'s permissions and
                  additionally can delete

        '''
        has_flattened_params = any([
            parent,
            permission])
    # WARNING: Decompyle incomplete

    
    def get_permission(self = None, request = None, *, name, retry, timeout, metadata):
        '''Gets information about a specific Permission.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_get_permission():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.GetPermissionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_permission(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.GetPermissionRequest, dict]):
                The request object. Request for getting information about a specific
                ``Permission``.
            name (str):
                Required. The resource name of the permission.

                Formats:
                ``tunedModels/{tuned_model}/permissions/{permission}``
                ``corpora/{corpus}/permissions/{permission}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.types.Permission:
                Permission resource grants user,
                group or the rest of the world access to
                the PaLM API resource (e.g. a tuned
                model, corpus).

                A role is a collection of permitted
                operations that allows users to perform
                specific actions on PaLM API resources.
                To make them available to users, groups,
                or service accounts, you assign roles.
                When you assign a role, you grant
                permissions that the role contains.

                There are three concentric roles. Each
                role is a superset of the previous
                role\'s permitted operations:

                - reader can use the resource (e.g.
                  tuned model, corpus) for inference
                - writer has reader\'s permissions and
                  additionally can edit and share
                - owner has writer\'s permissions and
                  additionally can delete

        '''
        has_flattened_params = any([
            name])
    # WARNING: Decompyle incomplete

    
    def list_permissions(self = None, request = None, *, parent, retry, timeout, metadata):
        '''Lists permissions for the specific resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_list_permissions():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.ListPermissionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_permissions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.ListPermissionsRequest, dict]):
                The request object. Request for listing permissions.
            parent (str):
                Required. The parent resource of the permissions.
                Formats: ``tunedModels/{tuned_model}``
                ``corpora/{corpus}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.services.permission_service.pagers.ListPermissionsPager:
                Response from ListPermissions containing a paginated list of
                   permissions.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        '''
        has_flattened_params = any([
            parent])
    # WARNING: Decompyle incomplete

    
    def update_permission(self = None, request = None, *, permission, update_mask, retry, timeout, metadata):
        """Updates the permission.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_update_permission():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.UpdatePermissionRequest(
                )

                # Make the request
                response = client.update_permission(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.UpdatePermissionRequest, dict]):
                The request object. Request to update the ``Permission``.
            permission (google.ai.generativelanguage_v1beta.types.Permission):
                Required. The permission to update.

                The permission's ``name`` field is used to identify the
                permission to update.

                This corresponds to the ``permission`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to update. Accepted ones:

                -  role (``Permission.role`` field)

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.types.Permission:
                Permission resource grants user,
                group or the rest of the world access to
                the PaLM API resource (e.g. a tuned
                model, corpus).

                A role is a collection of permitted
                operations that allows users to perform
                specific actions on PaLM API resources.
                To make them available to users, groups,
                or service accounts, you assign roles.
                When you assign a role, you grant
                permissions that the role contains.

                There are three concentric roles. Each
                role is a superset of the previous
                role's permitted operations:

                - reader can use the resource (e.g.
                  tuned model, corpus) for inference
                - writer has reader's permissions and
                  additionally can edit and share
                - owner has writer's permissions and
                  additionally can delete

        """
        has_flattened_params = any([
            permission,
            update_mask])
    # WARNING: Decompyle incomplete

    
    def delete_permission(self = None, request = None, *, name, retry, timeout, metadata):
        '''Deletes the permission.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_delete_permission():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.DeletePermissionRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_permission(request=request)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.DeletePermissionRequest, dict]):
                The request object. Request to delete the ``Permission``.
            name (str):
                Required. The resource name of the permission. Formats:
                ``tunedModels/{tuned_model}/permissions/{permission}``
                ``corpora/{corpus}/permissions/{permission}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        '''
        has_flattened_params = any([
            name])
    # WARNING: Decompyle incomplete

    
    def transfer_ownership(self = None, request = None, *, retry, timeout, metadata):
        '''Transfers ownership of the tuned model.
        This is the only way to change ownership of the tuned
        model. The current owner will be downgraded to writer
        role.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_transfer_ownership():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.TransferOwnershipRequest(
                    name="name_value",
                    email_address="email_address_value",
                )

                # Make the request
                response = client.transfer_ownership(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.TransferOwnershipRequest, dict]):
                The request object. Request to transfer the ownership of
                the tuned model.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.types.TransferOwnershipResponse:
                Response from TransferOwnership.
        '''
        if not isinstance(request, permission_service.TransferOwnershipRequest):
            request = permission_service.TransferOwnershipRequest(request)
        rpc = self._transport._wrapped_methods[self._transport.transfer_ownership]
        metadata = tuple(metadata) + (gapic_v1.routing_header.to_grpc_metadata((('name', request.name),)),)
        self._validate_universe_domain()
        response = rpc(request, retry = retry, timeout = timeout, metadata = metadata)
        return response

    
    def __enter__(self = None):
        return self

    
    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()

    
    def list_operations(self = None, request = None, *, retry, timeout, metadata):
        '''Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_operation(self = None, request = None, *, retry, timeout, metadata):
        '''Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        '''
        pass
    # WARNING: Decompyle incomplete


PermissionServiceClient = <NODE:27>(PermissionServiceClient, 'PermissionServiceClient', metaclass = PermissionServiceClientMeta)
DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = package_version.__version__)
__all__ = ('PermissionServiceClient',)
