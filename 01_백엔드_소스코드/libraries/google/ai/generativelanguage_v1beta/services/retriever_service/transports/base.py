# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import google.api_core as google
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
import google.auth as google
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from google.oauth2 import service_account
from google.protobuf import empty_pb2
from google.ai.generativelanguage_v1beta import gapic_version as package_version
from google.ai.generativelanguage_v1beta.types import retriever, retriever_service
DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = package_version.__version__)

class RetrieverServiceTransport(abc.ABC):
    '''Abstract transport class for RetrieverService.'''
    AUTH_SCOPES = ()
    DEFAULT_HOST: str = 'generativelanguage.googleapis.com'
    
    def __init__(self = None, *, host, credentials, credentials_file, scopes, quota_project_id, client_info, always_use_jwt_access, api_audience, **kwargs):
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'generativelanguage.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """
        scopes_kwargs = {
            'scopes': scopes,
            'default_scopes': self.AUTH_SCOPES }
        self._scopes = scopes
        if not hasattr(self, '_ignore_credentials'):
            self._ignore_credentials = False
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")
    # WARNING: Decompyle incomplete

    host = (lambda self: self._host)()
    
    def _prep_wrapped_messages(self, client_info):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        '''Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        '''
        raise NotImplementedError()

    create_corpus = (lambda self = None: raise NotImplementedError())()
    get_corpus = (lambda self = None: raise NotImplementedError())()
    update_corpus = (lambda self = None: raise NotImplementedError())()
    delete_corpus = (lambda self = None: raise NotImplementedError())()
    list_corpora = (lambda self = None: raise NotImplementedError())()
    query_corpus = (lambda self = None: raise NotImplementedError())()
    create_document = (lambda self = None: raise NotImplementedError())()
    get_document = (lambda self = None: raise NotImplementedError())()
    update_document = (lambda self = None: raise NotImplementedError())()
    delete_document = (lambda self = None: raise NotImplementedError())()
    list_documents = (lambda self = None: raise NotImplementedError())()
    query_document = (lambda self = None: raise NotImplementedError())()
    create_chunk = (lambda self = None: raise NotImplementedError())()
    batch_create_chunks = (lambda self = None: raise NotImplementedError())()
    get_chunk = (lambda self = None: raise NotImplementedError())()
    update_chunk = (lambda self = None: raise NotImplementedError())()
    batch_update_chunks = (lambda self = None: raise NotImplementedError())()
    delete_chunk = (lambda self = None: raise NotImplementedError())()
    batch_delete_chunks = (lambda self = None: raise NotImplementedError())()
    list_chunks = (lambda self = None: raise NotImplementedError())()
    list_operations = (lambda self = None: raise NotImplementedError())()
    get_operation = (lambda self = None: raise NotImplementedError())()
    kind = (lambda self = None: raise NotImplementedError())()

__all__ = ('RetrieverServiceTransport',)
