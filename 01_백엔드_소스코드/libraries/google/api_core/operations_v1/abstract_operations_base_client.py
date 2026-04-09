# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abstract_operations_base_client.pyc (Python 3.11)

from collections import OrderedDict
import os
import re
from typing import Dict, Optional, Type, Union
from google.api_core import client_options as client_options_lib
from google.api_core import gapic_v1
from google.api_core.operations_v1.transports.base import DEFAULT_CLIENT_INFO, OperationsTransport
from google.api_core.operations_v1.transports.rest import OperationsRestTransport

try:
    from google.api_core.operations_v1.transports.rest_asyncio import AsyncOperationsRestTransport
    HAS_ASYNC_REST_DEPENDENCIES = True
except ImportError:
    e = None
    HAS_ASYNC_REST_DEPENDENCIES = False
    ASYNC_REST_EXCEPTION = e
    e = None
    del e
except:
    e = None
    del e

from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.auth.transport import mtls

class AbstractOperationsBaseClientMeta(type):
    '''Metaclass for the Operations Base client.

    This provides base class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    '''
    _transport_registry = OrderedDict()
    _transport_registry['rest'] = OperationsRestTransport
    if HAS_ASYNC_REST_DEPENDENCIES:
        _transport_registry['rest_asyncio'] = AsyncOperationsRestTransport
    
    def get_transport_class(cls = None, label = None):
        '''Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        '''
        if not label == 'rest_asyncio' and HAS_ASYNC_REST_DEPENDENCIES:
            raise ASYNC_REST_EXCEPTION
        if label:
            return cls._transport_registry[label]
        return None(iter(cls._transport_registry.values()))



def AbstractOperationsBaseClient():
    '''AbstractOperationsBaseClient'''
    __doc__ = 'Manages long-running operations with an API service.\n\n    When an API method normally takes long time to complete, it can be\n    designed to return [Operation][google.api_core.operations_v1.Operation] to the\n    client, and the client can use this interface to receive the real\n    response asynchronously by polling the operation resource, or pass\n    the operation resource to another API (such as Google Cloud Pub/Sub\n    API) to receive the response. Any API service that returns\n    long-running operations should implement the ``Operations``\n    interface so developers can have a consistent client experience.\n    '
    _get_default_mtls_endpoint = (lambda api_endpoint: if not api_endpoint:
api_endpointmtls_endpoint_re = None.compile('(?P<name>[^.]+)(?P<mtls>\\.mtls)?(?P<sandbox>\\.sandbox)?(?P<googledomain>\\.googleapis\\.com)?')m = mtls_endpoint_re.match(api_endpoint)(name, mtls, sandbox, googledomain) = m.groups()if not mtls or googledomain:
api_endpointif None:
api_endpoint.replace('sandbox.googleapis.com', 'mtls.sandbox.googleapis.com')None.replace('.googleapis.com', '.mtls.googleapis.com'))()
    DEFAULT_ENDPOINT = 'longrunning.googleapis.com'
    DEFAULT_MTLS_ENDPOINT = _get_default_mtls_endpoint.__func__(DEFAULT_ENDPOINT)
    from_service_account_info = (lambda cls = None, info = staticmethod: raise NotImplementedError('`from_service_account_info` is not implemented.'))()
    from_service_account_file = (lambda cls = None, filename = None: raise NotImplementedError('`from_service_account_file` is not implemented.'))()
    from_service_account_json = from_service_account_file
    transport = (lambda self = None: self._transport)()
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
    
    def __init__(self = None, *, credentials, transport, client_options, client_info):
        '''Instantiates the operations client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, OperationsTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. It won\'t take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you\'re developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        '''
        if isinstance(client_options, dict):
            client_options = client_options_lib.from_dict(client_options)
    # WARNING: Decompyle incomplete


AbstractOperationsBaseClient = <NODE:27>(AbstractOperationsBaseClient, 'AbstractOperationsBaseClient', metaclass = AbstractOperationsBaseClientMeta)
