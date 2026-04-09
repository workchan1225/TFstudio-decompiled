# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import google.api_core as google
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
import google.auth as google
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from google.oauth2 import service_account
import google.protobuf as google
from google.cloud.texttospeech_v1 import gapic_version as package_version
from google.cloud.texttospeech_v1.types import cloud_tts_lrs
DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = package_version.__version__)
if hasattr(DEFAULT_CLIENT_INFO, 'protobuf_runtime_version'):
    DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__

class TextToSpeechLongAudioSynthesizeTransport(abc.ABC):
    '''Abstract transport class for TextToSpeechLongAudioSynthesize.'''
    AUTH_SCOPES = ('https://www.googleapis.com/auth/cloud-platform',)
    DEFAULT_HOST: str = 'texttospeech.googleapis.com'
    
    def __init__(self = None, *, host, credentials, credentials_file, scopes, quota_project_id, client_info, always_use_jwt_access, api_audience, **kwargs):
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'texttospeech.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
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
        self._wrapped_methods = {
            self.list_operations: gapic_v1.method.wrap_method(self.list_operations, default_timeout = None, client_info = client_info),
            self.get_operation: gapic_v1.method.wrap_method(self.get_operation, default_timeout = None, client_info = client_info),
            self.synthesize_long_audio: gapic_v1.method.wrap_method(self.synthesize_long_audio, default_timeout = 5000, client_info = client_info) }

    
    def close(self):
        '''Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        '''
        raise NotImplementedError()

    operations_client = (lambda self: raise NotImplementedError())()
    synthesize_long_audio = (lambda self = property: raise NotImplementedError())()
    list_operations = (lambda self = None: raise NotImplementedError())()
    get_operation = (lambda self = None: raise NotImplementedError())()
    kind = (lambda self = None: raise NotImplementedError())()

__all__ = ('TextToSpeechLongAudioSynthesizeTransport',)
