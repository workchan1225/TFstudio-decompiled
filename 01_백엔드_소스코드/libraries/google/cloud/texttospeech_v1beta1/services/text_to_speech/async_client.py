# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: async_client.pyc (Python 3.11)

from collections import OrderedDict
import logging as std_logging
import re
from typing import AsyncIterable, AsyncIterator, Awaitable, Callable, Dict, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from google.oauth2 import service_account
import google.protobuf as google
from google.cloud.texttospeech_v1beta1 import gapic_version as package_version

try:
    OptionalRetry = Union[(retries.AsyncRetry, gapic_v1.method._MethodDefault, None)]
except AttributeError:
    OptionalRetry = Union[(retries.AsyncRetry, object, None)]

from google.longrunning import operations_pb2
from google.cloud.texttospeech_v1beta1.types import cloud_tts
from client import TextToSpeechClient
from transports.base import DEFAULT_CLIENT_INFO, TextToSpeechTransport
from transports.grpc_asyncio import TextToSpeechGrpcAsyncIOTransport

try:
    from google.api_core import client_logging
    CLIENT_LOGGING_SUPPORTED = True
except ImportError:
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

class TextToSpeechAsyncClient:
    _client: TextToSpeechClient = 'Service that implements Google Cloud Text-to-Speech API.'
    DEFAULT_ENDPOINT = TextToSpeechClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = TextToSpeechClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = TextToSpeechClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = TextToSpeechClient._DEFAULT_UNIVERSE
    model_path = staticmethod(TextToSpeechClient.model_path)
    parse_model_path = staticmethod(TextToSpeechClient.parse_model_path)
    common_billing_account_path = staticmethod(TextToSpeechClient.common_billing_account_path)
    parse_common_billing_account_path = staticmethod(TextToSpeechClient.parse_common_billing_account_path)
    common_folder_path = staticmethod(TextToSpeechClient.common_folder_path)
    parse_common_folder_path = staticmethod(TextToSpeechClient.parse_common_folder_path)
    common_organization_path = staticmethod(TextToSpeechClient.common_organization_path)
    parse_common_organization_path = staticmethod(TextToSpeechClient.parse_common_organization_path)
    common_project_path = staticmethod(TextToSpeechClient.common_project_path)
    parse_common_project_path = staticmethod(TextToSpeechClient.parse_common_project_path)
    common_location_path = staticmethod(TextToSpeechClient.common_location_path)
    parse_common_location_path = staticmethod(TextToSpeechClient.parse_common_location_path)
    from_service_account_info = (lambda cls = None, info = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_file = (lambda cls = None, filename = None: pass# WARNING: Decompyle incomplete
)()
    from_service_account_json = from_service_account_file
    get_mtls_endpoint_and_cert_source = (lambda cls = None, client_options = None: TextToSpeechClient.get_mtls_endpoint_and_cert_source(client_options))()
    transport = (lambda self = None: self._client.transport)()
    api_endpoint = (lambda self: self._client._api_endpoint)()
    universe_domain = (lambda self = None: self._client._universe_domain)()
    get_transport_class = TextToSpeechClient.get_transport_class
    
    def __init__(self = None, *, credentials, transport, client_options, client_info):
        '''Instantiates the text to speech async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,TextToSpeechTransport,Callable[..., TextToSpeechTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the TextToSpeechTransport constructor.
                If set to None, a transport is chosen automatically.
                NOTE: "rest" transport functionality is currently in a
                beta state (preview). We welcome your feedback via an
                issue in this library\'s source repository.
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
        self._client = TextToSpeechClient(credentials = credentials, transport = transport, client_options = client_options, client_info = client_info)
        if CLIENT_LOGGING_SUPPORTED or _LOGGER.isEnabledFor(std_logging.DEBUG):
            _LOGGER.debug('Created client `google.cloud.texttospeech_v1beta1.TextToSpeechAsyncClient`.', extra = {
                'serviceName': 'google.cloud.texttospeech.v1beta1.TextToSpeech',
                'universeDomain': getattr(self._client._transport._credentials, 'universe_domain', ''),
                'credentialsType': f'''{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}''',
                'credentialsInfo': getattr(self.transport._credentials, 'get_cred_info', (lambda : pass))() } if hasattr(self._client._transport, '_credentials') else {
                'serviceName': 'google.cloud.texttospeech.v1beta1.TextToSpeech',
                'credentialsType': None })
            return None
        return None

    
    async def list_voices(self = None, request = None, *, language_code, retry, timeout, metadata):
        '''Returns a list of Voice supported for synthesis.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import texttospeech_v1beta1

            async def sample_list_voices():
                # Create a client
                client = texttospeech_v1beta1.TextToSpeechAsyncClient()

                # Initialize request argument(s)
                request = texttospeech_v1beta1.ListVoicesRequest(
                )

                # Make the request
                response = await client.list_voices(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.texttospeech_v1beta1.types.ListVoicesRequest, dict]]):
                The request object. The top-level message sent by the client for the
                ``ListVoices`` method.
            language_code (:class:`str`):
                Optional. Recommended.
                `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
                language tag. If not specified, the API will return all
                supported voices. If specified, the ListVoices call will
                only return voices that can be used to synthesize this
                language_code. For example, if you specify ``"en-NZ"``,
                all ``"en-NZ"`` voices will be returned. If you specify
                ``"no"``, both ``"no-\\*"`` (Norwegian) and ``"nb-\\*"``
                (Norwegian Bokmal) voices will be returned.

                This corresponds to the ``language_code`` field
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
            google.cloud.texttospeech_v1beta1.types.ListVoicesResponse:
                The message returned to the client by the ListVoices
                method.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def synthesize_speech(self = None, request = None, *, input, voice, audio_config, retry, timeout, metadata):
        '''Synthesizes speech synchronously: receive results
        after all text input has been processed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import texttospeech_v1beta1

            async def sample_synthesize_speech():
                # Create a client
                client = texttospeech_v1beta1.TextToSpeechAsyncClient()

                # Initialize request argument(s)
                input = texttospeech_v1beta1.SynthesisInput()
                input.text = "text_value"

                voice = texttospeech_v1beta1.VoiceSelectionParams()
                voice.language_code = "language_code_value"

                audio_config = texttospeech_v1beta1.AudioConfig()
                audio_config.audio_encoding = "M4A"

                request = texttospeech_v1beta1.SynthesizeSpeechRequest(
                    input=input,
                    voice=voice,
                    audio_config=audio_config,
                )

                # Make the request
                response = await client.synthesize_speech(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.texttospeech_v1beta1.types.SynthesizeSpeechRequest, dict]]):
                The request object. The top-level message sent by the client for the
                ``SynthesizeSpeech`` method.
            input (:class:`google.cloud.texttospeech_v1beta1.types.SynthesisInput`):
                Required. The Synthesizer requires
                either plain text or SSML as input.

                This corresponds to the ``input`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            voice (:class:`google.cloud.texttospeech_v1beta1.types.VoiceSelectionParams`):
                Required. The desired voice of the
                synthesized audio.

                This corresponds to the ``voice`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audio_config (:class:`google.cloud.texttospeech_v1beta1.types.AudioConfig`):
                Required. The configuration of the
                synthesized audio.

                This corresponds to the ``audio_config`` field
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
            google.cloud.texttospeech_v1beta1.types.SynthesizeSpeechResponse:
                The message returned to the client by the
                SynthesizeSpeech method.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def streaming_synthesize(self = None, requests = None, *, retry, timeout, metadata):
        '''Performs bidirectional streaming speech synthesis:
        receives audio while sending text.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import texttospeech_v1beta1

            async def sample_streaming_synthesize():
                # Create a client
                client = texttospeech_v1beta1.TextToSpeechAsyncClient()

                # Initialize request argument(s)
                streaming_config = texttospeech_v1beta1.StreamingSynthesizeConfig()
                streaming_config.voice.language_code = "language_code_value"

                request = texttospeech_v1beta1.StreamingSynthesizeRequest(
                    streaming_config=streaming_config,
                )

                # This method expects an iterator which contains
                # \'texttospeech_v1beta1.StreamingSynthesizeRequest\' objects
                # Here we create a generator that yields a single `request` for
                # demonstrative purposes.
                requests = [request]

                def request_generator():
                    for request in requests:
                        yield request

                # Make the request
                stream = await client.streaming_synthesize(requests=request_generator())

                # Handle the response
                async for response in stream:
                    print(response)

        Args:
            requests (AsyncIterator[`google.cloud.texttospeech_v1beta1.types.StreamingSynthesizeRequest`]):
                The request object AsyncIterator. Request message for the ``StreamingSynthesize`` method.
                Multiple ``StreamingSynthesizeRequest`` messages are
                sent in one call. The first message must contain a
                ``streaming_config`` that fully specifies the request
                configuration and must not contain ``input``. All
                subsequent messages must only have ``input`` set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            AsyncIterable[google.cloud.texttospeech_v1beta1.types.StreamingSynthesizeResponse]:
                StreamingSynthesizeResponse is the only message returned to the
                   client by StreamingSynthesize method. A series of
                   zero or more StreamingSynthesizeResponse messages are
                   streamed back to the client.

        '''
        rpc = self._client._transport._wrapped_methods[self._client._transport.streaming_synthesize]
        self._client._validate_universe_domain()
        response = rpc(requests, retry = retry, timeout = timeout, metadata = metadata)
        return response

    
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
if hasattr(DEFAULT_CLIENT_INFO, 'protobuf_runtime_version'):
    DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__
__all__ = ('TextToSpeechAsyncClient',)
