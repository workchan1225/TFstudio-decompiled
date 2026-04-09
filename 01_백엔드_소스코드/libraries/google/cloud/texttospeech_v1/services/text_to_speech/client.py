# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

from collections import OrderedDict
from http import HTTPStatus
import json
import logging as std_logging
import os
import re
from typing import Callable, Dict, Iterable, Iterator, Mapping, MutableMapping, MutableSequence, Optional, Sequence, Tuple, Type, Union, cast
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
import google.protobuf as google
from google.cloud.texttospeech_v1 import gapic_version as package_version

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
from google.cloud.texttospeech_v1.types import cloud_tts
from transports.base import DEFAULT_CLIENT_INFO, TextToSpeechTransport
from transports.grpc import TextToSpeechGrpcTransport
from transports.grpc_asyncio import TextToSpeechGrpcAsyncIOTransport
from transports.rest import TextToSpeechRestTransport

class TextToSpeechClientMeta(type):
    '''Metaclass for the TextToSpeech client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    '''
    _transport_registry = OrderedDict()
    _transport_registry['grpc'] = TextToSpeechGrpcTransport
    _transport_registry['grpc_asyncio'] = TextToSpeechGrpcAsyncIOTransport
    _transport_registry['rest'] = TextToSpeechRestTransport
    
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



def TextToSpeechClient():
    '''TextToSpeechClient'''
    __doc__ = 'Service that implements Google Cloud Text-to-Speech API.'
    _get_default_mtls_endpoint = (lambda api_endpoint: if not api_endpoint:
api_endpointmtls_endpoint_re = None.compile('(?P<name>[^.]+)(?P<mtls>\\.mtls)?(?P<sandbox>\\.sandbox)?(?P<googledomain>\\.googleapis\\.com)?')m = mtls_endpoint_re.match(api_endpoint)(name, mtls, sandbox, googledomain) = m.groups()if not mtls or googledomain:
api_endpointif None:
api_endpoint.replace('sandbox.googleapis.com', 'mtls.sandbox.googleapis.com')None.replace('.googleapis.com', '.mtls.googleapis.com'))()
    DEFAULT_ENDPOINT = 'texttospeech.googleapis.com'
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(DEFAULT_ENDPOINT)
    _DEFAULT_ENDPOINT_TEMPLATE = 'texttospeech.{UNIVERSE_DOMAIN}'
    _DEFAULT_UNIVERSE = 'googleapis.com'
    from_service_account_info = (lambda cls = None, info = staticmethod: credentials = service_account.Credentials.from_service_account_info(info)kwargs['credentials'] = credentials# WARNING: Decompyle incomplete
)()
    from_service_account_file = (lambda cls = None, filename = None: credentials = service_account.Credentials.from_service_account_file(filename)kwargs['credentials'] = credentials# WARNING: Decompyle incomplete
)()
    from_service_account_json = from_service_account_file
    transport = (lambda self = None: self._transport)()
    model_path = (lambda project = None, location = None, model = staticmethod: 'projects/{project}/locations/{location}/models/{model}'.format(project = project, location = location, model = model))()
    parse_model_path = (lambda path = None: m = re.match('^projects/(?P<project>.+?)/locations/(?P<location>.+?)/models/(?P<model>.+?)$', path)m.groupdict() if m else { })()
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
    _get_universe_domain = (lambda client_universe_domain = staticmethod, universe_domain_env = staticmethod: universe_domain = TextToSpeechClient._DEFAULT_UNIVERSE# WARNING: Decompyle incomplete
)()
    
    def _validate_universe_domain(self):
        """Validates client's and credentials' universe domains are consistent.

        Returns:
            bool: True iff the configured universe domain is valid.

        Raises:
            ValueError: If the configured universe domain is not valid.
        """
        return True

    
    def _add_cred_info_for_auth_errors(self = None, error = None):
        '''Adds credential info string to error details for 401/403/404 errors.

        Args:
            error (google.api_core.exceptions.GoogleAPICallError): The error to add the cred info.
        '''
        if error.code not in (HTTPStatus.UNAUTHORIZED, HTTPStatus.FORBIDDEN, HTTPStatus.NOT_FOUND):
            return None
        cred = None._transport._credentials
        if not hasattr(cred, 'get_cred_info'):
            return None
        cred_info = None.get_cred_info()
        if cred_info or hasattr(error._details, 'append'):
            error._details.append(json.dumps(cred_info))
            return None
        return None

    api_endpoint = (lambda self: self._api_endpoint)()
    universe_domain = (lambda self = None: self._universe_domain)()
    
    def __init__(self = None, *, credentials, transport, client_options, client_info):
        '''Instantiates the text to speech client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,TextToSpeechTransport,Callable[..., TextToSpeechTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
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

    
    def list_voices(self = None, request = None, *, language_code, retry, timeout, metadata):
        '''Returns a list of Voice supported for synthesis.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import texttospeech_v1

            def sample_list_voices():
                # Create a client
                client = texttospeech_v1.TextToSpeechClient()

                # Initialize request argument(s)
                request = texttospeech_v1.ListVoicesRequest(
                )

                # Make the request
                response = client.list_voices(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.texttospeech_v1.types.ListVoicesRequest, dict]):
                The request object. The top-level message sent by the client for the
                ``ListVoices`` method.
            language_code (str):
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
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.texttospeech_v1.types.ListVoicesResponse:
                The message returned to the client by the ListVoices
                method.

        '''
        flattened_params = [
            language_code]
        has_flattened_params = (lambda .0: pass# WARNING: Decompyle incomplete
)(flattened_params()) > 0
    # WARNING: Decompyle incomplete

    
    def synthesize_speech(self = None, request = None, *, input, voice, audio_config, retry, timeout, metadata):
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
            from google.cloud import texttospeech_v1

            def sample_synthesize_speech():
                # Create a client
                client = texttospeech_v1.TextToSpeechClient()

                # Initialize request argument(s)
                input = texttospeech_v1.SynthesisInput()
                input.text = "text_value"

                voice = texttospeech_v1.VoiceSelectionParams()
                voice.language_code = "language_code_value"

                audio_config = texttospeech_v1.AudioConfig()
                audio_config.audio_encoding = "M4A"

                request = texttospeech_v1.SynthesizeSpeechRequest(
                    input=input,
                    voice=voice,
                    audio_config=audio_config,
                )

                # Make the request
                response = client.synthesize_speech(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.texttospeech_v1.types.SynthesizeSpeechRequest, dict]):
                The request object. The top-level message sent by the client for the
                ``SynthesizeSpeech`` method.
            input (google.cloud.texttospeech_v1.types.SynthesisInput):
                Required. The Synthesizer requires
                either plain text or SSML as input.

                This corresponds to the ``input`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            voice (google.cloud.texttospeech_v1.types.VoiceSelectionParams):
                Required. The desired voice of the
                synthesized audio.

                This corresponds to the ``voice`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audio_config (google.cloud.texttospeech_v1.types.AudioConfig):
                Required. The configuration of the
                synthesized audio.

                This corresponds to the ``audio_config`` field
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
            google.cloud.texttospeech_v1.types.SynthesizeSpeechResponse:
                The message returned to the client by the
                SynthesizeSpeech method.

        '''
        flattened_params = [
            input,
            voice,
            audio_config]
        has_flattened_params = (lambda .0: pass# WARNING: Decompyle incomplete
)(flattened_params()) > 0
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
            from google.cloud import texttospeech_v1

            def sample_streaming_synthesize():
                # Create a client
                client = texttospeech_v1.TextToSpeechClient()

                # Initialize request argument(s)
                streaming_config = texttospeech_v1.StreamingSynthesizeConfig()
                streaming_config.voice.language_code = "language_code_value"

                request = texttospeech_v1.StreamingSynthesizeRequest(
                    streaming_config=streaming_config,
                )

                # This method expects an iterator which contains
                # \'texttospeech_v1.StreamingSynthesizeRequest\' objects
                # Here we create a generator that yields a single `request` for
                # demonstrative purposes.
                requests = [request]

                def request_generator():
                    for request in requests:
                        yield request

                # Make the request
                stream = client.streaming_synthesize(requests=request_generator())

                # Handle the response
                for response in stream:
                    print(response)

        Args:
            requests (Iterator[google.cloud.texttospeech_v1.types.StreamingSynthesizeRequest]):
                The request object iterator. Request message for the ``StreamingSynthesize`` method.
                Multiple ``StreamingSynthesizeRequest`` messages are
                sent in one call. The first message must contain a
                ``streaming_config`` that fully specifies the request
                configuration and must not contain ``input``. All
                subsequent messages must only have ``input`` set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            Iterable[google.cloud.texttospeech_v1.types.StreamingSynthesizeResponse]:
                StreamingSynthesizeResponse is the only message returned to the
                   client by StreamingSynthesize method. A series of
                   zero or more StreamingSynthesizeResponse messages are
                   streamed back to the client.

        '''
        rpc = self._transport._wrapped_methods[self._transport.streaming_synthesize]
        self._validate_universe_domain()
        response = rpc(requests, retry = retry, timeout = timeout, metadata = metadata)
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


TextToSpeechClient = <NODE:27>(TextToSpeechClient, 'TextToSpeechClient', metaclass = TextToSpeechClientMeta)
DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = package_version.__version__)
if hasattr(DEFAULT_CLIENT_INFO, 'protobuf_runtime_version'):
    DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__
__all__ = ('TextToSpeechClient',)
