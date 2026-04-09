# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: async_client.pyc (Python 3.11)

from collections import OrderedDict
import logging as std_logging
import re
from typing import AsyncIterable, Awaitable, Callable, Dict, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union
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
from google.ai.generativelanguage_v1beta.types import generative_service, safety
from google.ai.generativelanguage_v1beta.types import content
from google.ai.generativelanguage_v1beta.types import content as gag_content
from client import GenerativeServiceClient
from transports.base import DEFAULT_CLIENT_INFO, GenerativeServiceTransport
from transports.grpc_asyncio import GenerativeServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging
    CLIENT_LOGGING_SUPPORTED = True
except ImportError:
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

class GenerativeServiceAsyncClient:
    _client: GenerativeServiceClient = 'API for using Large Models that generate multimodal content\n    and have additional capabilities beyond text generation.\n    '
    DEFAULT_ENDPOINT = GenerativeServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = GenerativeServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = GenerativeServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = GenerativeServiceClient._DEFAULT_UNIVERSE
    cached_content_path = staticmethod(GenerativeServiceClient.cached_content_path)
    parse_cached_content_path = staticmethod(GenerativeServiceClient.parse_cached_content_path)
    model_path = staticmethod(GenerativeServiceClient.model_path)
    parse_model_path = staticmethod(GenerativeServiceClient.parse_model_path)
    common_billing_account_path = staticmethod(GenerativeServiceClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(GenerativeServiceClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(GenerativeServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(GenerativeServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(GenerativeServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(GenerativeServiceClient.parse_common_organization_path)
    common_project_path = staticmethod(GenerativeServiceClient.common_project_path)
    parse_common_project_path = staticmethod(GenerativeServiceClient.parse_common_project_path)
    common_location_path = staticmethod(GenerativeServiceClient.common_location_path)
    parse_common_location_path = staticmethod(GenerativeServiceClient.parse_common_location_path)
    from_service_account_info = (lambda cls = None, info = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_file = (lambda cls = None, filename = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_json = from_service_account_file
    get_mtls_endpoint_and_cert_source = (lambda cls = None, client_options = None: GenerativeServiceClient.get_mtls_endpoint_and_cert_source(client_options))()
    transport = (lambda self = None: self._client.transport)()
    api_endpoint = (lambda self: self._client._api_endpoint)()
    universe_domain = (lambda self = None: self._client._universe_domain)()
    get_transport_class = GenerativeServiceClient.get_transport_class
    
    def __init__(self = None, *, credentials, transport, client_options, client_info):
        '''Instantiates the generative service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,GenerativeServiceTransport,Callable[..., GenerativeServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the GenerativeServiceTransport constructor.
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
        self._client = GenerativeServiceClient(credentials = credentials, transport = transport, client_options = client_options, client_info = client_info)
        if CLIENT_LOGGING_SUPPORTED or _LOGGER.isEnabledFor(std_logging.DEBUG):
            _LOGGER.debug('Created client `google.ai.generativelanguage_v1beta.GenerativeServiceAsyncClient`.', extra = {
                'serviceName': 'google.ai.generativelanguage.v1beta.GenerativeService',
                'universeDomain': getattr(self._client._transport._credentials, 'universe_domain', ''),
                'credentialsType': f'''{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}''',
                'credentialsInfo': getattr(self.transport._credentials, 'get_cred_info', (lambda : pass))() } if hasattr(self._client._transport, '_credentials') else {
                'serviceName': 'google.ai.generativelanguage.v1beta.GenerativeService',
                'credentialsType': None })
            return None
        return None

    
    async def generate_content(self = None, request = None, *, model, contents, retry, timeout, metadata):
        '''Generates a model response given an input
        ``GenerateContentRequest``. Refer to the `text generation
        guide <https://ai.google.dev/gemini-api/docs/text-generation>`__
        for detailed usage information. Input capabilities differ
        between models, including tuned models. Refer to the `model
        guide <https://ai.google.dev/gemini-api/docs/models/gemini>`__
        and `tuning
        guide <https://ai.google.dev/gemini-api/docs/model-tuning>`__
        for details.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_generate_content():
                # Create a client
                client = generativelanguage_v1beta.GenerativeServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.GenerateContentRequest(
                    model="model_value",
                )

                # Make the request
                response = await client.generate_content(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.GenerateContentRequest, dict]]):
                The request object. Request to generate a completion from
                the model.
            model (:class:`str`):
                Required. The name of the ``Model`` to use for
                generating the completion.

                Format: ``models/{model}``.

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            contents (:class:`MutableSequence[google.ai.generativelanguage_v1beta.types.Content]`):
                Required. The content of the current conversation with
                the model.

                For single-turn queries, this is a single instance. For
                multi-turn queries like
                `chat <https://ai.google.dev/gemini-api/docs/text-generation#chat>`__,
                this is a repeated field that contains the conversation
                history and the latest request.

                This corresponds to the ``contents`` field
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
            google.ai.generativelanguage_v1beta.types.GenerateContentResponse:
                Response from the model supporting multiple candidate
                responses.

                   Safety ratings and content filtering are reported for
                   both prompt in
                   GenerateContentResponse.prompt_feedback and for each
                   candidate in finish_reason and in safety_ratings. The
                   API: - Returns either all requested candidates or
                   none of them - Returns no candidates at all only if
                   there was something wrong with the prompt (check
                   prompt_feedback) - Reports feedback on each candidate
                   in finish_reason and safety_ratings.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def generate_answer(self = None, request = None, *, model, contents, safety_settings, answer_style, retry, timeout, metadata):
        '''Generates a grounded answer from the model given an input
        ``GenerateAnswerRequest``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_generate_answer():
                # Create a client
                client = generativelanguage_v1beta.GenerativeServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.GenerateAnswerRequest(
                    model="model_value",
                    answer_style="VERBOSE",
                )

                # Make the request
                response = await client.generate_answer(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.GenerateAnswerRequest, dict]]):
                The request object. Request to generate a grounded answer from the
                ``Model``.
            model (:class:`str`):
                Required. The name of the ``Model`` to use for
                generating the grounded response.

                Format: ``model=models/{model}``.

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            contents (:class:`MutableSequence[google.ai.generativelanguage_v1beta.types.Content]`):
                Required. The content of the current conversation with
                the ``Model``. For single-turn queries, this is a single
                question to answer. For multi-turn queries, this is a
                repeated field that contains conversation history and
                the last ``Content`` in the list containing the
                question.

                Note: ``GenerateAnswer`` only supports queries in
                English.

                This corresponds to the ``contents`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            safety_settings (:class:`MutableSequence[google.ai.generativelanguage_v1beta.types.SafetySetting]`):
                Optional. A list of unique ``SafetySetting`` instances
                for blocking unsafe content.

                This will be enforced on the
                ``GenerateAnswerRequest.contents`` and
                ``GenerateAnswerResponse.candidate``. There should not
                be more than one setting for each ``SafetyCategory``
                type. The API will block any contents and responses that
                fail to meet the thresholds set by these settings. This
                list overrides the default settings for each
                ``SafetyCategory`` specified in the safety_settings. If
                there is no ``SafetySetting`` for a given
                ``SafetyCategory`` provided in the list, the API will
                use the default safety setting for that category. Harm
                categories HARM_CATEGORY_HATE_SPEECH,
                HARM_CATEGORY_SEXUALLY_EXPLICIT,
                HARM_CATEGORY_DANGEROUS_CONTENT,
                HARM_CATEGORY_HARASSMENT are supported. Refer to the
                `guide <https://ai.google.dev/gemini-api/docs/safety-settings>`__
                for detailed information on available safety settings.
                Also refer to the `Safety
                guidance <https://ai.google.dev/gemini-api/docs/safety-guidance>`__
                to learn how to incorporate safety considerations in
                your AI applications.

                This corresponds to the ``safety_settings`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            answer_style (:class:`google.ai.generativelanguage_v1beta.types.GenerateAnswerRequest.AnswerStyle`):
                Required. Style in which answers
                should be returned.

                This corresponds to the ``answer_style`` field
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
            google.ai.generativelanguage_v1beta.types.GenerateAnswerResponse:
                Response from the model for a
                grounded answer.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def stream_generate_content(self = None, request = None, *, model, contents, retry, timeout, metadata):
        '''Generates a `streamed
        response <https://ai.google.dev/gemini-api/docs/text-generation?lang=python#generate-a-text-stream>`__
        from the model given an input ``GenerateContentRequest``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_stream_generate_content():
                # Create a client
                client = generativelanguage_v1beta.GenerativeServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.GenerateContentRequest(
                    model="model_value",
                )

                # Make the request
                stream = await client.stream_generate_content(request=request)

                # Handle the response
                async for response in stream:
                    print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.GenerateContentRequest, dict]]):
                The request object. Request to generate a completion from
                the model.
            model (:class:`str`):
                Required. The name of the ``Model`` to use for
                generating the completion.

                Format: ``models/{model}``.

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            contents (:class:`MutableSequence[google.ai.generativelanguage_v1beta.types.Content]`):
                Required. The content of the current conversation with
                the model.

                For single-turn queries, this is a single instance. For
                multi-turn queries like
                `chat <https://ai.google.dev/gemini-api/docs/text-generation#chat>`__,
                this is a repeated field that contains the conversation
                history and the latest request.

                This corresponds to the ``contents`` field
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
            AsyncIterable[google.ai.generativelanguage_v1beta.types.GenerateContentResponse]:
                Response from the model supporting multiple candidate
                responses.

                   Safety ratings and content filtering are reported for
                   both prompt in
                   GenerateContentResponse.prompt_feedback and for each
                   candidate in finish_reason and in safety_ratings. The
                   API: - Returns either all requested candidates or
                   none of them - Returns no candidates at all only if
                   there was something wrong with the prompt (check
                   prompt_feedback) - Reports feedback on each candidate
                   in finish_reason and safety_ratings.

        '''
        has_flattened_params = any([
            model,
            contents])
    # WARNING: Decompyle incomplete

    
    async def embed_content(self = None, request = None, *, model, content, retry, timeout, metadata):
        '''Generates a text embedding vector from the input ``Content``
        using the specified `Gemini Embedding
        model <https://ai.google.dev/gemini-api/docs/models/gemini#text-embedding>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_embed_content():
                # Create a client
                client = generativelanguage_v1beta.GenerativeServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.EmbedContentRequest(
                    model="model_value",
                )

                # Make the request
                response = await client.embed_content(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.EmbedContentRequest, dict]]):
                The request object. Request containing the ``Content`` for the model to
                embed.
            model (:class:`str`):
                Required. The model\'s resource name. This serves as an
                ID for the Model to use.

                This name should match a model name returned by the
                ``ListModels`` method.

                Format: ``models/{model}``

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            content (:class:`google.ai.generativelanguage_v1beta.types.Content`):
                Required. The content to embed. Only the ``parts.text``
                fields will be counted.

                This corresponds to the ``content`` field
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
            google.ai.generativelanguage_v1beta.types.EmbedContentResponse:
                The response to an EmbedContentRequest.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def batch_embed_contents(self = None, request = None, *, model, requests, retry, timeout, metadata):
        '''Generates multiple embedding vectors from the input ``Content``
        which consists of a batch of strings represented as
        ``EmbedContentRequest`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_batch_embed_contents():
                # Create a client
                client = generativelanguage_v1beta.GenerativeServiceAsyncClient()

                # Initialize request argument(s)
                requests = generativelanguage_v1beta.EmbedContentRequest()
                requests.model = "model_value"

                request = generativelanguage_v1beta.BatchEmbedContentsRequest(
                    model="model_value",
                    requests=requests,
                )

                # Make the request
                response = await client.batch_embed_contents(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.BatchEmbedContentsRequest, dict]]):
                The request object. Batch request to get embeddings from
                the model for a list of prompts.
            model (:class:`str`):
                Required. The model\'s resource name. This serves as an
                ID for the Model to use.

                This name should match a model name returned by the
                ``ListModels`` method.

                Format: ``models/{model}``

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            requests (:class:`MutableSequence[google.ai.generativelanguage_v1beta.types.EmbedContentRequest]`):
                Required. Embed requests for the batch. The model in
                each of these requests must match the model specified
                ``BatchEmbedContentsRequest.model``.

                This corresponds to the ``requests`` field
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
            google.ai.generativelanguage_v1beta.types.BatchEmbedContentsResponse:
                The response to a BatchEmbedContentsRequest.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def count_tokens(self = None, request = None, *, model, contents, retry, timeout, metadata):
        '''Runs a model\'s tokenizer on input ``Content`` and returns the
        token count. Refer to the `tokens
        guide <https://ai.google.dev/gemini-api/docs/tokens>`__ to learn
        more about tokens.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_count_tokens():
                # Create a client
                client = generativelanguage_v1beta.GenerativeServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.CountTokensRequest(
                    model="model_value",
                )

                # Make the request
                response = await client.count_tokens(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.CountTokensRequest, dict]]):
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
            contents (:class:`MutableSequence[google.ai.generativelanguage_v1beta.types.Content]`):
                Optional. The input given to the model as a prompt. This
                field is ignored when ``generate_content_request`` is
                set.

                This corresponds to the ``contents`` field
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
            google.ai.generativelanguage_v1beta.types.CountTokensResponse:
                A response from CountTokens.

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
__all__ = ('GenerativeServiceAsyncClient',)
