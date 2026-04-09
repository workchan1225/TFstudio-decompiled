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
from google.ai.generativelanguage_v1beta.types import safety, text_service
from client import TextServiceClient
from transports.base import DEFAULT_CLIENT_INFO, TextServiceTransport
from transports.grpc_asyncio import TextServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging
    CLIENT_LOGGING_SUPPORTED = True
except ImportError:
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

class TextServiceAsyncClient:
    _client: TextServiceClient = 'API for using Generative Language Models (GLMs) trained to\n    generate text.\n    Also known as Large Language Models (LLM)s, these generate text\n    given an input prompt from the user.\n    '
    DEFAULT_ENDPOINT = TextServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = TextServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = TextServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = TextServiceClient._DEFAULT_UNIVERSE
    model_path = staticmethod(TextServiceClient.model_path)
    parse_model_path = staticmethod(TextServiceClient.parse_model_path)
    common_billing_account_path = staticmethod(TextServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(TextServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(TextServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(TextServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(TextServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(TextServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(TextServiceClient.common_project_path)
    parse_common_project_path = staticmethod(TextServiceClient.parse_common_project_path)
    common_location_path = staticmethod(TextServiceClient.common_location_path)
    parse_common_location_path = staticmethod(TextServiceClient.parse_common_location_path)
    from_service_account_info = (lambda cls = None, info = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_file = (lambda cls = None, filename = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_json = from_service_account_file
    get_mtls_endpoint_and_cert_source = (lambda cls = None, client_options = None: TextServiceClient.get_mtls_endpoint_and_cert_source(client_options))()
    transport = (lambda self = None: self._client.transport)()
    api_endpoint = (lambda self: self._client._api_endpoint)()
    universe_domain = (lambda self = None: self._client._universe_domain)()
    get_transport_class = TextServiceClient.get_transport_class
    
    def __init__(self = None, *, credentials, transport, client_options, client_info):
        '''Instantiates the text service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,TextServiceTransport,Callable[..., TextServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the TextServiceTransport constructor.
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
        self._client = TextServiceClient(credentials = credentials, transport = transport, client_options = client_options, client_info = client_info)
        if CLIENT_LOGGING_SUPPORTED or _LOGGER.isEnabledFor(std_logging.DEBUG):
            _LOGGER.debug('Created client `google.ai.generativelanguage_v1beta.TextServiceAsyncClient`.', extra = {
                'serviceName': 'google.ai.generativelanguage.v1beta.TextService',
                'universeDomain': getattr(self._client._transport._credentials, 'universe_domain', ''),
                'credentialsType': f'''{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}''',
                'credentialsInfo': getattr(self.transport._credentials, 'get_cred_info', (lambda : pass))() } if hasattr(self._client._transport, '_credentials') else {
                'serviceName': 'google.ai.generativelanguage.v1beta.TextService',
                'credentialsType': None })
            return None
        return None

    
    async def generate_text(self = None, request = None, *, model, prompt, temperature, candidate_count, max_output_tokens, top_p, top_k, retry, timeout, metadata):
        '''Generates a response from the model given an input
        message.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_generate_text():
                # Create a client
                client = generativelanguage_v1beta.TextServiceAsyncClient()

                # Initialize request argument(s)
                prompt = generativelanguage_v1beta.TextPrompt()
                prompt.text = "text_value"

                request = generativelanguage_v1beta.GenerateTextRequest(
                    model="model_value",
                    prompt=prompt,
                )

                # Make the request
                response = await client.generate_text(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.GenerateTextRequest, dict]]):
                The request object. Request to generate a text completion
                response from the model.
            model (:class:`str`):
                Required. The name of the ``Model`` or ``TunedModel`` to
                use for generating the completion. Examples:
                models/text-bison-001
                tunedModels/sentence-translator-u3b7m

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            prompt (:class:`google.ai.generativelanguage_v1beta.types.TextPrompt`):
                Required. The free-form input text
                given to the model as a prompt.
                Given a prompt, the model will generate
                a TextCompletion response it predicts as
                the completion of the input text.

                This corresponds to the ``prompt`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            temperature (:class:`float`):
                Optional. Controls the randomness of the output. Note:
                The default value varies by model, see the
                ``Model.temperature`` attribute of the ``Model``
                returned the ``getModel`` function.

                Values can range from [0.0,1.0], inclusive. A value
                closer to 1.0 will produce responses that are more
                varied and creative, while a value closer to 0.0 will
                typically result in more straightforward responses from
                the model.

                This corresponds to the ``temperature`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            candidate_count (:class:`int`):
                Optional. Number of generated responses to return.

                This value must be between [1, 8], inclusive. If unset,
                this will default to 1.

                This corresponds to the ``candidate_count`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            max_output_tokens (:class:`int`):
                Optional. The maximum number of tokens to include in a
                candidate.

                If unset, this will default to output_token_limit
                specified in the ``Model`` specification.

                This corresponds to the ``max_output_tokens`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            top_p (:class:`float`):
                Optional. The maximum cumulative probability of tokens
                to consider when sampling.

                The model uses combined Top-k and nucleus sampling.

                Tokens are sorted based on their assigned probabilities
                so that only the most likely tokens are considered.
                Top-k sampling directly limits the maximum number of
                tokens to consider, while Nucleus sampling limits number
                of tokens based on the cumulative probability.

                Note: The default value varies by model, see the
                ``Model.top_p`` attribute of the ``Model`` returned the
                ``getModel`` function.

                This corresponds to the ``top_p`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            top_k (:class:`int`):
                Optional. The maximum number of tokens to consider when
                sampling.

                The model uses combined Top-k and nucleus sampling.

                Top-k sampling considers the set of ``top_k`` most
                probable tokens. Defaults to 40.

                Note: The default value varies by model, see the
                ``Model.top_k`` attribute of the ``Model`` returned the
                ``getModel`` function.

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
            google.ai.generativelanguage_v1beta.types.GenerateTextResponse:
                The response from the model,
                including candidate completions.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def embed_text(self = None, request = None, *, model, text, retry, timeout, metadata):
        '''Generates an embedding from the model given an input
        message.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_embed_text():
                # Create a client
                client = generativelanguage_v1beta.TextServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.EmbedTextRequest(
                    model="model_value",
                )

                # Make the request
                response = await client.embed_text(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.EmbedTextRequest, dict]]):
                The request object. Request to get a text embedding from
                the model.
            model (:class:`str`):
                Required. The model name to use with
                the format model=models/{model}.

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            text (:class:`str`):
                Optional. The free-form input text
                that the model will turn into an
                embedding.

                This corresponds to the ``text`` field
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
            google.ai.generativelanguage_v1beta.types.EmbedTextResponse:
                The response to a EmbedTextRequest.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def batch_embed_text(self = None, request = None, *, model, texts, retry, timeout, metadata):
        '''Generates multiple embeddings from the model given
        input text in a synchronous call.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_batch_embed_text():
                # Create a client
                client = generativelanguage_v1beta.TextServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.BatchEmbedTextRequest(
                    model="model_value",
                )

                # Make the request
                response = await client.batch_embed_text(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.BatchEmbedTextRequest, dict]]):
                The request object. Batch request to get a text embedding
                from the model.
            model (:class:`str`):
                Required. The name of the ``Model`` to use for
                generating the embedding. Examples:
                models/embedding-gecko-001

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            texts (:class:`MutableSequence[str]`):
                Optional. The free-form input texts
                that the model will turn into an
                embedding. The current limit is 100
                texts, over which an error will be
                thrown.

                This corresponds to the ``texts`` field
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
            google.ai.generativelanguage_v1beta.types.BatchEmbedTextResponse:
                The response to a EmbedTextRequest.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def count_text_tokens(self = None, request = None, *, model, prompt, retry, timeout, metadata):
        '''Runs a model\'s tokenizer on a text and returns the
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

            async def sample_count_text_tokens():
                # Create a client
                client = generativelanguage_v1beta.TextServiceAsyncClient()

                # Initialize request argument(s)
                prompt = generativelanguage_v1beta.TextPrompt()
                prompt.text = "text_value"

                request = generativelanguage_v1beta.CountTextTokensRequest(
                    model="model_value",
                    prompt=prompt,
                )

                # Make the request
                response = await client.count_text_tokens(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.CountTextTokensRequest, dict]]):
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
            prompt (:class:`google.ai.generativelanguage_v1beta.types.TextPrompt`):
                Required. The free-form input text
                given to the model as a prompt.

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
            google.ai.generativelanguage_v1beta.types.CountTextTokensResponse:
                A response from CountTextTokens.

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
__all__ = ('TextServiceAsyncClient',)
