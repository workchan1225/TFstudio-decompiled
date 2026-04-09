# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: async_client.pyc (Python 3.11)

from collections import OrderedDict
import logging as std_logging
import re
from typing import Callable, Dict, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from google.oauth2 import service_account
from google.ai.generativelanguage_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[(retries.AsyncRetry, gapic_v1.method._MethodDefault, None)]
except AttributeError:
    OptionalRetry = Union[(retries.AsyncRetry, object, None)]

from google.longrunning import operations_pb2
from google.protobuf import field_mask_pb2
from google.ai.generativelanguage_v1beta.services.permission_service import pagers
from google.ai.generativelanguage_v1beta.types import permission as gag_permission
from google.ai.generativelanguage_v1beta.types import permission
from google.ai.generativelanguage_v1beta.types import permission_service
from client import PermissionServiceClient
from transports.base import DEFAULT_CLIENT_INFO, PermissionServiceTransport
from transports.grpc_asyncio import PermissionServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging
    CLIENT_LOGGING_SUPPORTED = True
except ImportError:
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

class PermissionServiceAsyncClient:
    _client: PermissionServiceClient = 'Provides methods for managing permissions to PaLM API\n    resources.\n    '
    DEFAULT_ENDPOINT = PermissionServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = PermissionServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = PermissionServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = PermissionServiceClient._DEFAULT_UNIVERSE
    permission_path = staticmethod(PermissionServiceClient.permission_path)
    parse_permission_path = staticmethod(PermissionServiceClient.parse_permission_path)
    common_billing_account_path = staticmethod(PermissionServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(PermissionServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(PermissionServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(PermissionServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(PermissionServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(PermissionServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(PermissionServiceClient.common_project_path)
    parse_common_project_path = staticmethod(PermissionServiceClient.parse_common_project_path)
    common_location_path = staticmethod(PermissionServiceClient.common_location_path)
    parse_common_location_path = staticmethod(PermissionServiceClient.parse_common_location_path)
    from_service_account_info = (lambda cls = None, info = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_file = (lambda cls = None, filename = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_json = from_service_account_file
    get_mtls_endpoint_and_cert_source = (lambda cls = None, client_options = None: PermissionServiceClient.get_mtls_endpoint_and_cert_source(client_options))()
    transport = (lambda self = None: self._client.transport)()
    api_endpoint = (lambda self: self._client._api_endpoint)()
    universe_domain = (lambda self = None: self._client._universe_domain)()
    get_transport_class = PermissionServiceClient.get_transport_class
    
    def __init__(self = None, *, credentials, transport, client_options, client_info):
        '''Instantiates the permission service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,PermissionServiceTransport,Callable[..., PermissionServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
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
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you\'re developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        '''
        self._client = PermissionServiceClient(credentials = credentials, transport = transport, client_options = client_options, client_info = client_info)
        if CLIENT_LOGGING_SUPPORTED or _LOGGER.isEnabledFor(std_logging.DEBUG):
            _LOGGER.debug('Created client `google.ai.generativelanguage_v1beta.PermissionServiceAsyncClient`.', extra = {
                'serviceName': 'google.ai.generativelanguage.v1beta.PermissionService',
                'universeDomain': getattr(self._client._transport._credentials, 'universe_domain', ''),
                'credentialsType': f'''{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}''',
                'credentialsInfo': getattr(self.transport._credentials, 'get_cred_info', (lambda : pass))() } if hasattr(self._client._transport, '_credentials') else {
                'serviceName': 'google.ai.generativelanguage.v1beta.PermissionService',
                'credentialsType': None })
            return None
        return None

    
    async def create_permission(self = None, request = None, *, parent, permission, retry, timeout, metadata):
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

            async def sample_create_permission():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.CreatePermissionRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_permission(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.CreatePermissionRequest, dict]]):
                The request object. Request to create a ``Permission``.
            parent (:class:`str`):
                Required. The parent resource of the ``Permission``.
                Formats: ``tunedModels/{tuned_model}``
                ``corpora/{corpus}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            permission (:class:`google.ai.generativelanguage_v1beta.types.Permission`):
                Required. The permission to create.
                This corresponds to the ``permission`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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
        pass
    # WARNING: Decompyle incomplete

    
    async def get_permission(self = None, request = None, *, name, retry, timeout, metadata):
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

            async def sample_get_permission():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.GetPermissionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_permission(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.GetPermissionRequest, dict]]):
                The request object. Request for getting information about a specific
                ``Permission``.
            name (:class:`str`):
                Required. The resource name of the permission.

                Formats:
                ``tunedModels/{tuned_model}/permissions/{permission}``
                ``corpora/{corpus}/permissions/{permission}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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
        pass
    # WARNING: Decompyle incomplete

    
    async def list_permissions(self = None, request = None, *, parent, retry, timeout, metadata):
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

            async def sample_list_permissions():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.ListPermissionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_permissions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.ListPermissionsRequest, dict]]):
                The request object. Request for listing permissions.
            parent (:class:`str`):
                Required. The parent resource of the permissions.
                Formats: ``tunedModels/{tuned_model}``
                ``corpora/{corpus}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.services.permission_service.pagers.ListPermissionsAsyncPager:
                Response from ListPermissions containing a paginated list of
                   permissions.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def update_permission(self = None, request = None, *, permission, update_mask, retry, timeout, metadata):
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

            async def sample_update_permission():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.UpdatePermissionRequest(
                )

                # Make the request
                response = await client.update_permission(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.UpdatePermissionRequest, dict]]):
                The request object. Request to update the ``Permission``.
            permission (:class:`google.ai.generativelanguage_v1beta.types.Permission`):
                Required. The permission to update.

                The permission's ``name`` field is used to identify the
                permission to update.

                This corresponds to the ``permission`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. The list of fields to update. Accepted ones:

                -  role (``Permission.role`` field)

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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
        pass
    # WARNING: Decompyle incomplete

    
    async def delete_permission(self = None, request = None, *, name, retry, timeout, metadata):
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

            async def sample_delete_permission():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.DeletePermissionRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_permission(request=request)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.DeletePermissionRequest, dict]]):
                The request object. Request to delete the ``Permission``.
            name (:class:`str`):
                Required. The resource name of the permission. Formats:
                ``tunedModels/{tuned_model}/permissions/{permission}``
                ``corpora/{corpus}/permissions/{permission}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def transfer_ownership(self = None, request = None, *, retry, timeout, metadata):
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

            async def sample_transfer_ownership():
                # Create a client
                client = generativelanguage_v1beta.PermissionServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.TransferOwnershipRequest(
                    name="name_value",
                    email_address="email_address_value",
                )

                # Make the request
                response = await client.transfer_ownership(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.TransferOwnershipRequest, dict]]):
                The request object. Request to transfer the ownership of
                the tuned model.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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
        pass
    # WARNING: Decompyle incomplete

    
    async def list_operations(self = None, request = None, *, retry, timeout, metadata):
        '''Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
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

    
    async def get_operation(self = None, request = None, *, retry, timeout, metadata):
        '''Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
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

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self, exc_type, exc, tb):
        pass
    # WARNING: Decompyle incomplete


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = package_version.__version__)
__all__ = ('PermissionServiceAsyncClient',)
