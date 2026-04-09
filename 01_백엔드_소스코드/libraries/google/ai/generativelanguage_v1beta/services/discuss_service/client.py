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
from google.ai.generativelanguage_v1beta.types import discuss_service, safety
from transports.base import DEFAULT_CLIENT_INFO, DiscussServiceTransport
from transports.grpc import DiscussServiceGrpcTransport
from transports.grpc_asyncio import DiscussServiceGrpcAsyncIOTransport
from transports.rest import DiscussServiceRestTransport

class DiscussServiceClientMeta(type):
    '''Metaclass for the DiscussService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    '''
    _transport_registry = OrderedDict()
    _transport_registry['grpc'] = DiscussServiceGrpcTransport
    _transport_registry['grpc_asyncio'] = DiscussServiceGrpcAsyncIOTransport
    _transport_registry['rest'] = DiscussServiceRestTransport
    
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



def DiscussServiceClient():
    '''DiscussServiceClient'''
    __doc__ = 'An API for using Generative Language Models (GLMs) in dialog\n    applications.\n    Also known as large language models (LLMs), this API provides\n    models that are trained for multi-turn dialog.\n    '
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
    model_path = (lambda model = None: 'models/{model}'.format(model = model))()
    parse_model_path = (lambda path = None: m = re.match('^models/(?P<model>.+?)$', path)m.groupdict() if m else { })()
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
    _get_universe_domain = (lambda client_universe_domain = staticmethod, universe_domain_env = staticmethod: universe_domain = DiscussServiceClient._DEFAULT_UNIVERSE# WARNING: Decompyle incomplete
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
        '''Instantiates the discuss service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DiscussServiceTransport,Callable[..., DiscussServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
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

    
    def generate_message(self = None, request = None, *, model, prompt, temperature, candidate_count, top_p, top_k, retry, timeout, metadata):
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

            def sample_generate_message():
                # Create a client
                client = generativelanguage_v1beta.DiscussServiceClient()

                # Initialize request argument(s)
                prompt = generativelanguage_v1beta.MessagePrompt()
                prompt.messages.content = "content_value"

                request = generativelanguage_v1beta.GenerateMessageRequest(
                    model="model_value",
                    prompt=prompt,
                )

                # Make the request
                response = client.generate_message(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.GenerateMessageRequest, dict]):
                The request object. Request to generate a message
                response from the model.
            model (str):
                Required. The name of the model to use.

                Format: ``name=models/{model}``.

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            prompt (google.ai.generativelanguage_v1beta.types.MessagePrompt):
                Required. The structured textual
                input given to the model as a prompt.
                Given a
                prompt, the model will return what it
                predicts is the next message in the
                discussion.

                This corresponds to the ``prompt`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            temperature (float):
                Optional. Controls the randomness of the output.

                Values can range over ``[0.0,1.0]``, inclusive. A value
                closer to ``1.0`` will produce responses that are more
                varied, while a value closer to ``0.0`` will typically
                result in less surprising responses from the model.

                This corresponds to the ``temperature`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            candidate_count (int):
                Optional. The number of generated response messages to
                return.

                This value must be between ``[1, 8]``, inclusive. If
                unset, this will default to ``1``.

                This corresponds to the ``candidate_count`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            top_p (float):
                Optional. The maximum cumulative probability of tokens
                to consider when sampling.

                The model uses combined Top-k and nucleus sampling.

                Nucleus sampling considers the smallest set of tokens
                whose probability sum is at least ``top_p``.

                This corresponds to the ``top_p`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            top_k (int):
                Optional. The maximum number of tokens to consider when
                sampling.

                The model uses combined Top-k and nucleus sampling.

                Top-k sampling considers the set of ``top_k`` most
                probable tokens.

                This corresponds to the ``top_k`` field
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
            google.ai.generativelanguage_v1beta.types.GenerateMessageResponse:
                The response from the model.

                This includes candidate messages and
                conversation history in the form of
                chronologically-ordered messages.

        '''
        has_flattened_params = any([
            model,
            prompt,
            temperature,
            candidate_count,
            top_p,
            top_k])
    # WARNING: Decompyle incomplete

    
    def count_message_tokens(self = None, request = None, *, model, prompt, retry, timeout, metadata):
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

            def sample_count_message_tokens():
                # Create a client
                client = generativelanguage_v1beta.DiscussServiceClient()

                # Initialize request argument(s)
                prompt = generativelanguage_v1beta.MessagePrompt()
                prompt.messages.content = "content_value"

                request = generativelanguage_v1beta.CountMessageTokensRequest(
                    model="model_value",
                    prompt=prompt,
                )

                # Make the request
                response = client.count_message_tokens(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.CountMessageTokensRequest, dict]):
                The request object. Counts the number of tokens in the ``prompt`` sent to a
                model.

                Models may tokenize text differently, so each model may
                return a different ``token_count``.
            model (str):
                Required. The model\'s resource name. This serves as an
                ID for the Model to use.

                This name should match a model name returned by the
                ``ListModels`` method.

                Format: ``models/{model}``

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            prompt (google.ai.generativelanguage_v1beta.types.MessagePrompt):
                Required. The prompt, whose token
                count is to be returned.

                This corresponds to the ``prompt`` field
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
            google.ai.generativelanguage_v1beta.types.CountMessageTokensResponse:
                A response from CountMessageTokens.

                   It returns the model\'s token_count for the prompt.

        '''
        has_flattened_params = any([
            model,
            prompt])
    # WARNING: Decompyle incomplete

    
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


DiscussServiceClient = <NODE:27>(DiscussServiceClient, 'DiscussServiceClient', metaclass = DiscussServiceClientMeta)
DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = package_version.__version__)
__all__ = ('DiscussServiceClient',)
