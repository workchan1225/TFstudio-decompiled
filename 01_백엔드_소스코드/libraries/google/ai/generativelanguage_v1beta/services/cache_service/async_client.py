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
from google.protobuf import duration_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import timestamp_pb2
from google.ai.generativelanguage_v1beta.services.cache_service import pagers
from google.ai.generativelanguage_v1beta.types import cached_content as gag_cached_content
from google.ai.generativelanguage_v1beta.types import cache_service
from google.ai.generativelanguage_v1beta.types import cached_content
from google.ai.generativelanguage_v1beta.types import content
from client import CacheServiceClient
from transports.base import DEFAULT_CLIENT_INFO, CacheServiceTransport
from transports.grpc_asyncio import CacheServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging
    CLIENT_LOGGING_SUPPORTED = True
except ImportError:
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

class CacheServiceAsyncClient:
    _client: CacheServiceClient = 'API for managing cache of content (CachedContent resources)\n    that can be used in GenerativeService requests. This way\n    generate content requests can benefit from preprocessing work\n    being done earlier, possibly lowering their computational cost.\n    It is intended to be used with large contexts.\n    '
    DEFAULT_ENDPOINT = CacheServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CacheServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = CacheServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = CacheServiceClient._DEFAULT_UNIVERSE
    cached_content_path = staticmethod(CacheServiceClient.cached_content_path)
    parse_cached_content_path = staticmethod(CacheServiceClient.parse_cached_content_path)
    model_path = staticmethod(CacheServiceClient.model_path)
    parse_model_path = staticmethod(CacheServiceClient.parse_model_path)
    common_billing_account_path = staticmethod(CacheServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(CacheServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(CacheServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(CacheServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(CacheServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(CacheServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(CacheServiceClient.common_project_path)
    parse_common_project_path = staticmethod(CacheServiceClient.parse_common_project_path)
    common_location_path = staticmethod(CacheServiceClient.common_location_path)
    parse_common_location_path = staticmethod(CacheServiceClient.parse_common_location_path)
    from_service_account_info = (lambda cls = None, info = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_file = (lambda cls = None, filename = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_json = from_service_account_file
    get_mtls_endpoint_and_cert_source = (lambda cls = None, client_options = None: CacheServiceClient.get_mtls_endpoint_and_cert_source(client_options))()
    transport = (lambda self = None: self._client.transport)()
    api_endpoint = (lambda self: self._client._api_endpoint)()
    universe_domain = (lambda self = None: self._client._universe_domain)()
    get_transport_class = CacheServiceClient.get_transport_class
    
    def __init__(self = None, *, credentials, transport, client_options, client_info):
        '''Instantiates the cache service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,CacheServiceTransport,Callable[..., CacheServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the CacheServiceTransport constructor.
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
        self._client = CacheServiceClient(credentials = credentials, transport = transport, client_options = client_options, client_info = client_info)
        if CLIENT_LOGGING_SUPPORTED or _LOGGER.isEnabledFor(std_logging.DEBUG):
            _LOGGER.debug('Created client `google.ai.generativelanguage_v1beta.CacheServiceAsyncClient`.', extra = {
                'serviceName': 'google.ai.generativelanguage.v1beta.CacheService',
                'universeDomain': getattr(self._client._transport._credentials, 'universe_domain', ''),
                'credentialsType': f'''{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}''',
                'credentialsInfo': getattr(self.transport._credentials, 'get_cred_info', (lambda : pass))() } if hasattr(self._client._transport, '_credentials') else {
                'serviceName': 'google.ai.generativelanguage.v1beta.CacheService',
                'credentialsType': None })
            return None
        return None

    
    async def list_cached_contents(self = None, request = None, *, retry, timeout, metadata):
        '''Lists CachedContents.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_list_cached_contents():
                # Create a client
                client = generativelanguage_v1beta.CacheServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.ListCachedContentsRequest(
                )

                # Make the request
                page_result = client.list_cached_contents(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.ListCachedContentsRequest, dict]]):
                The request object. Request to list CachedContents.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.services.cache_service.pagers.ListCachedContentsAsyncPager:
                Response with CachedContents list.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def create_cached_content(self = None, request = None, *, cached_content, retry, timeout, metadata):
        '''Creates CachedContent resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_create_cached_content():
                # Create a client
                client = generativelanguage_v1beta.CacheServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.CreateCachedContentRequest(
                )

                # Make the request
                response = await client.create_cached_content(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.CreateCachedContentRequest, dict]]):
                The request object. Request to create CachedContent.
            cached_content (:class:`google.ai.generativelanguage_v1beta.types.CachedContent`):
                Required. The cached content to
                create.

                This corresponds to the ``cached_content`` field
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
            google.ai.generativelanguage_v1beta.types.CachedContent:
                Content that has been preprocessed
                and can be used in subsequent request to
                GenerativeService.

                Cached content can be only used with
                model it was created for.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def get_cached_content(self = None, request = None, *, name, retry, timeout, metadata):
        '''Reads CachedContent resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_get_cached_content():
                # Create a client
                client = generativelanguage_v1beta.CacheServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.GetCachedContentRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_cached_content(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.GetCachedContentRequest, dict]]):
                The request object. Request to read CachedContent.
            name (:class:`str`):
                Required. The resource name referring to the content
                cache entry. Format: ``cachedContents/{id}``

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
            google.ai.generativelanguage_v1beta.types.CachedContent:
                Content that has been preprocessed
                and can be used in subsequent request to
                GenerativeService.

                Cached content can be only used with
                model it was created for.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def update_cached_content(self = None, request = None, *, cached_content, update_mask, retry, timeout, metadata):
        '''Updates CachedContent resource (only expiration is
        updatable).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_update_cached_content():
                # Create a client
                client = generativelanguage_v1beta.CacheServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.UpdateCachedContentRequest(
                )

                # Make the request
                response = await client.update_cached_content(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.UpdateCachedContentRequest, dict]]):
                The request object. Request to update CachedContent.
            cached_content (:class:`google.ai.generativelanguage_v1beta.types.CachedContent`):
                Required. The content cache entry to
                update

                This corresponds to the ``cached_content`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The list of fields to update.
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
            google.ai.generativelanguage_v1beta.types.CachedContent:
                Content that has been preprocessed
                and can be used in subsequent request to
                GenerativeService.

                Cached content can be only used with
                model it was created for.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete_cached_content(self = None, request = None, *, name, retry, timeout, metadata):
        '''Deletes CachedContent resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_delete_cached_content():
                # Create a client
                client = generativelanguage_v1beta.CacheServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.DeleteCachedContentRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_cached_content(request=request)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.DeleteCachedContentRequest, dict]]):
                The request object. Request to delete CachedContent.
            name (:class:`str`):
                Required. The resource name referring to the content
                cache entry Format: ``cachedContents/{id}``

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
__all__ = ('CacheServiceAsyncClient',)
