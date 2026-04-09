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
from google.protobuf import timestamp_pb2
from google.ai.generativelanguage_v1beta.services.retriever_service import pagers
from google.ai.generativelanguage_v1beta.types import retriever, retriever_service
from transports.base import DEFAULT_CLIENT_INFO, RetrieverServiceTransport
from transports.grpc import RetrieverServiceGrpcTransport
from transports.grpc_asyncio import RetrieverServiceGrpcAsyncIOTransport
from transports.rest import RetrieverServiceRestTransport

class RetrieverServiceClientMeta(type):
    '''Metaclass for the RetrieverService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    '''
    _transport_registry = OrderedDict()
    _transport_registry['grpc'] = RetrieverServiceGrpcTransport
    _transport_registry['grpc_asyncio'] = RetrieverServiceGrpcAsyncIOTransport
    _transport_registry['rest'] = RetrieverServiceRestTransport
    
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



def RetrieverServiceClient():
    '''RetrieverServiceClient'''
    __doc__ = 'An API for semantic search over a corpus of user uploaded\n    content.\n    '
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
    chunk_path = (lambda corpus = None, document = None, chunk = staticmethod: 'corpora/{corpus}/documents/{document}/chunks/{chunk}'.format(corpus = corpus, document = document, chunk = chunk))()
    parse_chunk_path = (lambda path = None: m = re.match('^corpora/(?P<corpus>.+?)/documents/(?P<document>.+?)/chunks/(?P<chunk>.+?)$', path)m.groupdict() if m else { })()
    corpus_path = (lambda corpus = None: 'corpora/{corpus}'.format(corpus = corpus))()
    parse_corpus_path = (lambda path = None: m = re.match('^corpora/(?P<corpus>.+?)$', path)m.groupdict() if m else { })()
    document_path = (lambda corpus = None, document = None: 'corpora/{corpus}/documents/{document}'.format(corpus = corpus, document = document))()
    parse_document_path = (lambda path = None: m = re.match('^corpora/(?P<corpus>.+?)/documents/(?P<document>.+?)$', path)m.groupdict() if m else { })()
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
    _get_universe_domain = (lambda client_universe_domain = staticmethod, universe_domain_env = staticmethod: universe_domain = RetrieverServiceClient._DEFAULT_UNIVERSE# WARNING: Decompyle incomplete
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
        '''Instantiates the retriever service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,RetrieverServiceTransport,Callable[..., RetrieverServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the RetrieverServiceTransport constructor.
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

    
    def create_corpus(self = None, request = None, *, corpus, retry, timeout, metadata):
        '''Creates an empty ``Corpus``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_create_corpus():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.CreateCorpusRequest(
                )

                # Make the request
                response = client.create_corpus(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.CreateCorpusRequest, dict]):
                The request object. Request to create a ``Corpus``.
            corpus (google.ai.generativelanguage_v1beta.types.Corpus):
                Required. The ``Corpus`` to create.
                This corresponds to the ``corpus`` field
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
            google.ai.generativelanguage_v1beta.types.Corpus:
                A Corpus is a collection of Documents.
                   A project can create up to 5 corpora.

        '''
        has_flattened_params = any([
            corpus])
    # WARNING: Decompyle incomplete

    
    def get_corpus(self = None, request = None, *, name, retry, timeout, metadata):
        '''Gets information about a specific ``Corpus``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_get_corpus():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.GetCorpusRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_corpus(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.GetCorpusRequest, dict]):
                The request object. Request for getting information about a specific
                ``Corpus``.
            name (str):
                Required. The name of the ``Corpus``. Example:
                ``corpora/my-corpus-123``

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
            google.ai.generativelanguage_v1beta.types.Corpus:
                A Corpus is a collection of Documents.
                   A project can create up to 5 corpora.

        '''
        has_flattened_params = any([
            name])
    # WARNING: Decompyle incomplete

    
    def update_corpus(self = None, request = None, *, corpus, update_mask, retry, timeout, metadata):
        '''Updates a ``Corpus``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_update_corpus():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.UpdateCorpusRequest(
                )

                # Make the request
                response = client.update_corpus(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.UpdateCorpusRequest, dict]):
                The request object. Request to update a ``Corpus``.
            corpus (google.ai.generativelanguage_v1beta.types.Corpus):
                Required. The ``Corpus`` to update.
                This corresponds to the ``corpus`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to update. Currently, this
                only supports updating ``display_name``.

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
            google.ai.generativelanguage_v1beta.types.Corpus:
                A Corpus is a collection of Documents.
                   A project can create up to 5 corpora.

        '''
        has_flattened_params = any([
            corpus,
            update_mask])
    # WARNING: Decompyle incomplete

    
    def delete_corpus(self = None, request = None, *, name, retry, timeout, metadata):
        '''Deletes a ``Corpus``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_delete_corpus():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.DeleteCorpusRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_corpus(request=request)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.DeleteCorpusRequest, dict]):
                The request object. Request to delete a ``Corpus``.
            name (str):
                Required. The resource name of the ``Corpus``. Example:
                ``corpora/my-corpus-123``

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

    
    def list_corpora(self = None, request = None, *, retry, timeout, metadata):
        '''Lists all ``Corpora`` owned by the user.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_list_corpora():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.ListCorporaRequest(
                )

                # Make the request
                page_result = client.list_corpora(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.ListCorporaRequest, dict]):
                The request object. Request for listing ``Corpora``.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.services.retriever_service.pagers.ListCorporaPager:
                Response from ListCorpora containing a paginated list of Corpora.
                   The results are sorted by ascending
                   corpus.create_time.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        '''
        if not isinstance(request, retriever_service.ListCorporaRequest):
            request = retriever_service.ListCorporaRequest(request)
        rpc = self._transport._wrapped_methods[self._transport.list_corpora]
        self._validate_universe_domain()
        response = rpc(request, retry = retry, timeout = timeout, metadata = metadata)
        response = pagers.ListCorporaPager(method = rpc, request = request, response = response, retry = retry, timeout = timeout, metadata = metadata)
        return response

    
    def query_corpus(self = None, request = None, *, retry, timeout, metadata):
        '''Performs semantic search over a ``Corpus``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_query_corpus():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.QueryCorpusRequest(
                    name="name_value",
                    query="query_value",
                )

                # Make the request
                response = client.query_corpus(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.QueryCorpusRequest, dict]):
                The request object. Request for querying a ``Corpus``.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.types.QueryCorpusResponse:
                Response from QueryCorpus containing a list of relevant
                chunks.

        '''
        if not isinstance(request, retriever_service.QueryCorpusRequest):
            request = retriever_service.QueryCorpusRequest(request)
        rpc = self._transport._wrapped_methods[self._transport.query_corpus]
        metadata = tuple(metadata) + (gapic_v1.routing_header.to_grpc_metadata((('name', request.name),)),)
        self._validate_universe_domain()
        response = rpc(request, retry = retry, timeout = timeout, metadata = metadata)
        return response

    
    def create_document(self = None, request = None, *, parent, document, retry, timeout, metadata):
        '''Creates an empty ``Document``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_create_document():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.CreateDocumentRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_document(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.CreateDocumentRequest, dict]):
                The request object. Request to create a ``Document``.
            parent (str):
                Required. The name of the ``Corpus`` where this
                ``Document`` will be created. Example:
                ``corpora/my-corpus-123``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            document (google.ai.generativelanguage_v1beta.types.Document):
                Required. The ``Document`` to create.
                This corresponds to the ``document`` field
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
            google.ai.generativelanguage_v1beta.types.Document:
                A Document is a collection of Chunks.
                   A Corpus can have a maximum of 10,000 Documents.

        '''
        has_flattened_params = any([
            parent,
            document])
    # WARNING: Decompyle incomplete

    
    def get_document(self = None, request = None, *, name, retry, timeout, metadata):
        '''Gets information about a specific ``Document``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_get_document():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.GetDocumentRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_document(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.GetDocumentRequest, dict]):
                The request object. Request for getting information about a specific
                ``Document``.
            name (str):
                Required. The name of the ``Document`` to retrieve.
                Example: ``corpora/my-corpus-123/documents/the-doc-abc``

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
            google.ai.generativelanguage_v1beta.types.Document:
                A Document is a collection of Chunks.
                   A Corpus can have a maximum of 10,000 Documents.

        '''
        has_flattened_params = any([
            name])
    # WARNING: Decompyle incomplete

    
    def update_document(self = None, request = None, *, document, update_mask, retry, timeout, metadata):
        '''Updates a ``Document``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_update_document():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.UpdateDocumentRequest(
                )

                # Make the request
                response = client.update_document(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.UpdateDocumentRequest, dict]):
                The request object. Request to update a ``Document``.
            document (google.ai.generativelanguage_v1beta.types.Document):
                Required. The ``Document`` to update.
                This corresponds to the ``document`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to update. Currently, this
                only supports updating ``display_name`` and
                ``custom_metadata``.

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
            google.ai.generativelanguage_v1beta.types.Document:
                A Document is a collection of Chunks.
                   A Corpus can have a maximum of 10,000 Documents.

        '''
        has_flattened_params = any([
            document,
            update_mask])
    # WARNING: Decompyle incomplete

    
    def delete_document(self = None, request = None, *, name, retry, timeout, metadata):
        '''Deletes a ``Document``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_delete_document():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.DeleteDocumentRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_document(request=request)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.DeleteDocumentRequest, dict]):
                The request object. Request to delete a ``Document``.
            name (str):
                Required. The resource name of the ``Document`` to
                delete. Example:
                ``corpora/my-corpus-123/documents/the-doc-abc``

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

    
    def list_documents(self = None, request = None, *, parent, retry, timeout, metadata):
        '''Lists all ``Document``\\ s in a ``Corpus``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_list_documents():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.ListDocumentsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_documents(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.ListDocumentsRequest, dict]):
                The request object. Request for listing ``Document``\\ s.
            parent (str):
                Required. The name of the ``Corpus`` containing
                ``Document``\\ s. Example: ``corpora/my-corpus-123``

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
            google.ai.generativelanguage_v1beta.services.retriever_service.pagers.ListDocumentsPager:
                Response from ListDocuments containing a paginated list of Documents.
                   The Documents are sorted by ascending
                   document.create_time.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        '''
        has_flattened_params = any([
            parent])
    # WARNING: Decompyle incomplete

    
    def query_document(self = None, request = None, *, retry, timeout, metadata):
        '''Performs semantic search over a ``Document``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_query_document():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.QueryDocumentRequest(
                    name="name_value",
                    query="query_value",
                )

                # Make the request
                response = client.query_document(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.QueryDocumentRequest, dict]):
                The request object. Request for querying a ``Document``.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.types.QueryDocumentResponse:
                Response from QueryDocument containing a list of
                relevant chunks.

        '''
        if not isinstance(request, retriever_service.QueryDocumentRequest):
            request = retriever_service.QueryDocumentRequest(request)
        rpc = self._transport._wrapped_methods[self._transport.query_document]
        metadata = tuple(metadata) + (gapic_v1.routing_header.to_grpc_metadata((('name', request.name),)),)
        self._validate_universe_domain()
        response = rpc(request, retry = retry, timeout = timeout, metadata = metadata)
        return response

    
    def create_chunk(self = None, request = None, *, parent, chunk, retry, timeout, metadata):
        '''Creates a ``Chunk``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_create_chunk():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                chunk = generativelanguage_v1beta.Chunk()
                chunk.data.string_value = "string_value_value"

                request = generativelanguage_v1beta.CreateChunkRequest(
                    parent="parent_value",
                    chunk=chunk,
                )

                # Make the request
                response = client.create_chunk(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.CreateChunkRequest, dict]):
                The request object. Request to create a ``Chunk``.
            parent (str):
                Required. The name of the ``Document`` where this
                ``Chunk`` will be created. Example:
                ``corpora/my-corpus-123/documents/the-doc-abc``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            chunk (google.ai.generativelanguage_v1beta.types.Chunk):
                Required. The ``Chunk`` to create.
                This corresponds to the ``chunk`` field
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
            google.ai.generativelanguage_v1beta.types.Chunk:
                A Chunk is a subpart of a Document that is treated as an independent unit
                   for the purposes of vector representation and
                   storage. A Corpus can have a maximum of 1 million
                   Chunks.

        '''
        has_flattened_params = any([
            parent,
            chunk])
    # WARNING: Decompyle incomplete

    
    def batch_create_chunks(self = None, request = None, *, retry, timeout, metadata):
        '''Batch create ``Chunk``\\ s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_batch_create_chunks():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                requests = generativelanguage_v1beta.CreateChunkRequest()
                requests.parent = "parent_value"
                requests.chunk.data.string_value = "string_value_value"

                request = generativelanguage_v1beta.BatchCreateChunksRequest(
                    requests=requests,
                )

                # Make the request
                response = client.batch_create_chunks(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.BatchCreateChunksRequest, dict]):
                The request object. Request to batch create ``Chunk``\\ s.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.types.BatchCreateChunksResponse:
                Response from BatchCreateChunks containing a list of
                created Chunks.

        '''
        if not isinstance(request, retriever_service.BatchCreateChunksRequest):
            request = retriever_service.BatchCreateChunksRequest(request)
        rpc = self._transport._wrapped_methods[self._transport.batch_create_chunks]
        metadata = tuple(metadata) + (gapic_v1.routing_header.to_grpc_metadata((('parent', request.parent),)),)
        self._validate_universe_domain()
        response = rpc(request, retry = retry, timeout = timeout, metadata = metadata)
        return response

    
    def get_chunk(self = None, request = None, *, name, retry, timeout, metadata):
        '''Gets information about a specific ``Chunk``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_get_chunk():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.GetChunkRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_chunk(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.GetChunkRequest, dict]):
                The request object. Request for getting information about a specific
                ``Chunk``.
            name (str):
                Required. The name of the ``Chunk`` to retrieve.
                Example:
                ``corpora/my-corpus-123/documents/the-doc-abc/chunks/some-chunk``

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
            google.ai.generativelanguage_v1beta.types.Chunk:
                A Chunk is a subpart of a Document that is treated as an independent unit
                   for the purposes of vector representation and
                   storage. A Corpus can have a maximum of 1 million
                   Chunks.

        '''
        has_flattened_params = any([
            name])
    # WARNING: Decompyle incomplete

    
    def update_chunk(self = None, request = None, *, chunk, update_mask, retry, timeout, metadata):
        '''Updates a ``Chunk``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_update_chunk():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                chunk = generativelanguage_v1beta.Chunk()
                chunk.data.string_value = "string_value_value"

                request = generativelanguage_v1beta.UpdateChunkRequest(
                    chunk=chunk,
                )

                # Make the request
                response = client.update_chunk(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.UpdateChunkRequest, dict]):
                The request object. Request to update a ``Chunk``.
            chunk (google.ai.generativelanguage_v1beta.types.Chunk):
                Required. The ``Chunk`` to update.
                This corresponds to the ``chunk`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to update. Currently, this
                only supports updating ``custom_metadata`` and ``data``.

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
            google.ai.generativelanguage_v1beta.types.Chunk:
                A Chunk is a subpart of a Document that is treated as an independent unit
                   for the purposes of vector representation and
                   storage. A Corpus can have a maximum of 1 million
                   Chunks.

        '''
        has_flattened_params = any([
            chunk,
            update_mask])
    # WARNING: Decompyle incomplete

    
    def batch_update_chunks(self = None, request = None, *, retry, timeout, metadata):
        '''Batch update ``Chunk``\\ s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_batch_update_chunks():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                requests = generativelanguage_v1beta.UpdateChunkRequest()
                requests.chunk.data.string_value = "string_value_value"

                request = generativelanguage_v1beta.BatchUpdateChunksRequest(
                    requests=requests,
                )

                # Make the request
                response = client.batch_update_chunks(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.BatchUpdateChunksRequest, dict]):
                The request object. Request to batch update ``Chunk``\\ s.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ai.generativelanguage_v1beta.types.BatchUpdateChunksResponse:
                Response from BatchUpdateChunks containing a list of
                updated Chunks.

        '''
        if not isinstance(request, retriever_service.BatchUpdateChunksRequest):
            request = retriever_service.BatchUpdateChunksRequest(request)
        rpc = self._transport._wrapped_methods[self._transport.batch_update_chunks]
        metadata = tuple(metadata) + (gapic_v1.routing_header.to_grpc_metadata((('parent', request.parent),)),)
        self._validate_universe_domain()
        response = rpc(request, retry = retry, timeout = timeout, metadata = metadata)
        return response

    
    def delete_chunk(self = None, request = None, *, name, retry, timeout, metadata):
        '''Deletes a ``Chunk``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_delete_chunk():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.DeleteChunkRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_chunk(request=request)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.DeleteChunkRequest, dict]):
                The request object. Request to delete a ``Chunk``.
            name (str):
                Required. The resource name of the ``Chunk`` to delete.
                Example:
                ``corpora/my-corpus-123/documents/the-doc-abc/chunks/some-chunk``

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

    
    def batch_delete_chunks(self = None, request = None, *, retry, timeout, metadata):
        '''Batch delete ``Chunk``\\ s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_batch_delete_chunks():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                requests = generativelanguage_v1beta.DeleteChunkRequest()
                requests.name = "name_value"

                request = generativelanguage_v1beta.BatchDeleteChunksRequest(
                    requests=requests,
                )

                # Make the request
                client.batch_delete_chunks(request=request)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.BatchDeleteChunksRequest, dict]):
                The request object. Request to batch delete ``Chunk``\\ s.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        '''
        if not isinstance(request, retriever_service.BatchDeleteChunksRequest):
            request = retriever_service.BatchDeleteChunksRequest(request)
        rpc = self._transport._wrapped_methods[self._transport.batch_delete_chunks]
        metadata = tuple(metadata) + (gapic_v1.routing_header.to_grpc_metadata((('parent', request.parent),)),)
        self._validate_universe_domain()
        rpc(request, retry = retry, timeout = timeout, metadata = metadata)

    
    def list_chunks(self = None, request = None, *, parent, retry, timeout, metadata):
        '''Lists all ``Chunk``\\ s in a ``Document``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            def sample_list_chunks():
                # Create a client
                client = generativelanguage_v1beta.RetrieverServiceClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.ListChunksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_chunks(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ai.generativelanguage_v1beta.types.ListChunksRequest, dict]):
                The request object. Request for listing ``Chunk``\\ s.
            parent (str):
                Required. The name of the ``Document`` containing
                ``Chunk``\\ s. Example:
                ``corpora/my-corpus-123/documents/the-doc-abc``

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
            google.ai.generativelanguage_v1beta.services.retriever_service.pagers.ListChunksPager:
                Response from ListChunks containing a paginated list of Chunks.
                   The Chunks are sorted by ascending chunk.create_time.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        '''
        has_flattened_params = any([
            parent])
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


RetrieverServiceClient = <NODE:27>(RetrieverServiceClient, 'RetrieverServiceClient', metaclass = RetrieverServiceClientMeta)
DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = package_version.__version__)
__all__ = ('RetrieverServiceClient',)
