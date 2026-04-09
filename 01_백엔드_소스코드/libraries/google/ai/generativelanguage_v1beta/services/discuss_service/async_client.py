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
from google.ai.generativelanguage_v1beta.types import discuss_service, safety
from client import DiscussServiceClient
from transports.base import DEFAULT_CLIENT_INFO, DiscussServiceTransport
from transports.grpc_asyncio import DiscussServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging
    CLIENT_LOGGING_SUPPORTED = True
except ImportError:
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

class DiscussServiceAsyncClient:
    _client: DiscussServiceClient = 'An API for using Generative Language Models (GLMs) in dialog\n    applications.\n    Also known as large language models (LLMs), this API provides\n    models that are trained for multi-turn dialog.\n    '
    DEFAULT_ENDPOINT = DiscussServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DiscussServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DiscussServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DiscussServiceClient._DEFAULT_UNIVERSE
    model_path = staticmethod(DiscussServiceClient.model_path)
    parse_model_path = staticmethod(DiscussServiceClient.parse_model_path)
    common_billing_account_path = staticmethod(DiscussServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(DiscussServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(DiscussServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(DiscussServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(DiscussServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(DiscussServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(DiscussServiceClient.common_project_path)
    parse_common_project_path = staticmethod(DiscussServiceClient.parse_common_project_path)
    common_location_path = staticmethod(DiscussServiceClient.common_location_path)
    parse_common_location_path = staticmethod(DiscussServiceClient.parse_common_location_path)
    from_service_account_info = (lambda cls = None, info = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_file = (lambda cls = None, filename = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_json = from_service_account_file
    get_mtls_endpoint_and_cert_source = (lambda cls = None, client_options = None: DiscussServiceClient.get_mtls_endpoint_and_cert_source(client_options))()
    transport = (lambda self = None: self._client.transport)()
    api_endpoint = (lambda self: self._client._api_endpoint)()
    universe_domain = (lambda self = None: self._client._universe_domain)()
    get_transport_class = DiscussServiceClient.get_transport_class
    
    def __init__(self = None, *, credentials, transport, client_options, client_info):
        '''Instantiates the discuss service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DiscussServiceTransport,Callable[..., DiscussServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DiscussServiceTransport constructor.
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
        self._client = DiscussServiceClient(credentials = credentials, transport = transport, client_options = client_options, client_info = client_info)
        if CLIENT_LOGGING_SUPPORTED or _LOGGER.isEnabledFor(std_logging.DEBUG):
            _LOGGER.debug('Created client `google.ai.generativelanguage_v1beta.DiscussServiceAsyncClient`.', extra = {
                'serviceName': 'google.ai.generativelanguage.v1beta.DiscussService',
                'universeDomain': getattr(self._client._transport._credentials, 'universe_domain', ''),
                'credentialsType': f'''{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}''',
                'credentialsInfo': getattr(self.transport._credentials, 'get_cred_info', (lambda : pass))() } if hasattr(self._client._transport, '_credentials') else {
                'serviceName': 'google.ai.generativelanguage.v1beta.DiscussService',
                'credentialsType': None })
            return None
        return None

    
    async def generate_message(self = None, request = None, *, model, prompt, temperature, candidate_count, top_p, top_k, retry, timeout, metadata):
        '''Generates a response from the model given an input
        ``MessagePrompt``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_generate_message():
                # Create a client
                client = generativelanguage_v1beta.DiscussServiceAsyncClient()

                # Initialize request argument(s)
                prompt = generativelanguage_v1beta.MessagePrompt()
                prompt.messages.content = "content_value"

                request = generativelanguage_v1beta.GenerateMessageRequest(
                    model="model_value",
                    prompt=prompt,
                )

                # Make the request
                response = await client.generate_message(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.GenerateMessageRequest, dict]]):
                The request object. Request to generate a message
                response from the model.
            model (:class:`str`):
                Required. The name of the model to use.

                Format: ``name=models/{model}``.

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            prompt (:class:`google.ai.generativelanguage_v1beta.types.MessagePrompt`):
                Required. The structured textual
                input given to the model as a prompt.
                Given a
                prompt, the model will return what it
                predicts is the next message in the
                discussion.

                This corresponds to the ``prompt`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            temperature (:class:`float`):
                Optional. Controls the randomness of the output.

                Values can range over ``[0.0,1.0]``, inclusive. A value
                closer to ``1.0`` will produce responses that are more
                varied, while a value closer to ``0.0`` will typically
                result in less surprising responses from the model.

                This corresponds to the ``temperature`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            candidate_count (:class:`int`):
                Optional. The number of generated response messages to
                return.

                This value must be between ``[1, 8]``, inclusive. If
                unset, this will default to ``1``.

                This corresponds to the ``candidate_count`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            top_p (:class:`float`):
                Optional. The maximum cumulative probability of tokens
                to consider when sampling.

                The model uses combined Top-k and nucleus sampling.

                Nucleus sampling considers the smallest set of tokens
                whose probability sum is at least ``top_p``.

                This corresponds to the ``top_p`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            top_k (:class:`int`):
                Optional. The maximum number of tokens to consider when
                sampling.

                The model uses combined Top-k and nucleus sampling.

                Top-k sampling considers the set of ``top_k`` most
                probable tokens.

                This corresponds to the ``top_k`` field
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
            google.ai.generativelanguage_v1beta.types.GenerateMessageResponse:
                The response from the model.

                This includes candidate messages and
                conversation history in the form of
                chronologically-ordered messages.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def count_message_tokens(self = None, request = None, *, model, prompt, retry, timeout, metadata):
        '''Runs a model\'s tokenizer on a string and returns the
        token count.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_count_message_tokens():
                # Create a client
                client = generativelanguage_v1beta.DiscussServiceAsyncClient()

                # Initialize request argument(s)
                prompt = generativelanguage_v1beta.MessagePrompt()
                prompt.messages.content = "content_value"

                request = generativelanguage_v1beta.CountMessageTokensRequest(
                    model="model_value",
                    prompt=prompt,
                )

                # Make the request
                response = await client.count_message_tokens(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.CountMessageTokensRequest, dict]]):
                The request object. Counts the number of tokens in the ``prompt`` sent to a
                model.

                Models may tokenize text differently, so each model may
                return a different ``token_count``.
            model (:class:`str`):
                Required. The model\'s resource name. This serves as an
                ID for the Model to use.

                This name should match a model name returned by the
                ``ListModels`` method.

                Format: ``models/{model}``

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            prompt (:class:`google.ai.generativelanguage_v1beta.types.MessagePrompt`):
                Required. The prompt, whose token
                count is to be returned.

                This corresponds to the ``prompt`` field
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
            google.ai.generativelanguage_v1beta.types.CountMessageTokensResponse:
                A response from CountMessageTokens.

                   It returns the model\'s token_count for the prompt.

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
__all__ = ('DiscussServiceAsyncClient',)
