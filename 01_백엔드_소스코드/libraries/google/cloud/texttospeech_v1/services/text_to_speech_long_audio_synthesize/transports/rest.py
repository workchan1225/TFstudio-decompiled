# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rest.pyc (Python 3.11)

import dataclasses
import json
import logging
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.transport.requests import AuthorizedSession
from google.longrunning import operations_pb2
import google.protobuf as google
from google.protobuf import json_format
from requests import __version__ as requests_version
from google.cloud.texttospeech_v1.types import cloud_tts_lrs
from base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from rest_base import _BaseTextToSpeechLongAudioSynthesizeRestTransport

try:
    OptionalRetry = Union[(retries.Retry, gapic_v1.method._MethodDefault, None)]
except AttributeError:
    OptionalRetry = Union[(retries.Retry, object, None)]


try:
    from google.api_core import client_logging
    CLIENT_LOGGING_SUPPORTED = True
except ImportError:
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)
DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version = BASE_DEFAULT_CLIENT_INFO.gapic_version, grpc_version = None, rest_version = f'''requests@{requests_version}''')
if hasattr(DEFAULT_CLIENT_INFO, 'protobuf_runtime_version'):
    DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__

class TextToSpeechLongAudioSynthesizeRestInterceptor:
    '''Interceptor for TextToSpeechLongAudioSynthesize.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TextToSpeechLongAudioSynthesizeRestTransport.

    .. code-block:: python
        class MyCustomTextToSpeechLongAudioSynthesizeInterceptor(TextToSpeechLongAudioSynthesizeRestInterceptor):
            def pre_synthesize_long_audio(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_synthesize_long_audio(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TextToSpeechLongAudioSynthesizeRestTransport(interceptor=MyCustomTextToSpeechLongAudioSynthesizeInterceptor())
        client = TextToSpeechLongAudioSynthesizeClient(transport=transport)


    '''
    
    def pre_synthesize_long_audio(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for synthesize_long_audio

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TextToSpeechLongAudioSynthesize server.
        '''
        return (request, metadata)

    
    def post_synthesize_long_audio(self = None, response = None):
        '''Post-rpc interceptor for synthesize_long_audio

        DEPRECATED. Please use the `post_synthesize_long_audio_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TextToSpeechLongAudioSynthesize server but before
        it is returned to user code. This `post_synthesize_long_audio` interceptor runs
        before the `post_synthesize_long_audio_with_metadata` interceptor.
        '''
        return response

    
    def post_synthesize_long_audio_with_metadata(self = None, response = None, metadata = None):
        '''Post-rpc interceptor for synthesize_long_audio

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TextToSpeechLongAudioSynthesize server but before it is returned to user code.

        We recommend only using this `post_synthesize_long_audio_with_metadata`
        interceptor in new development instead of the `post_synthesize_long_audio` interceptor.
        When both interceptors are used, this `post_synthesize_long_audio_with_metadata` interceptor runs after the
        `post_synthesize_long_audio` interceptor. The (possibly modified) response returned by
        `post_synthesize_long_audio` will be passed to
        `post_synthesize_long_audio_with_metadata`.
        '''
        return (response, metadata)

    
    def pre_get_operation(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TextToSpeechLongAudioSynthesize server.
        '''
        return (request, metadata)

    
    def post_get_operation(self = None, response = None):
        '''Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the TextToSpeechLongAudioSynthesize server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_operations(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TextToSpeechLongAudioSynthesize server.
        '''
        return (request, metadata)

    
    def post_list_operations(self = None, response = None):
        '''Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the TextToSpeechLongAudioSynthesize server but before
        it is returned to user code.
        '''
        return response


TextToSpeechLongAudioSynthesizeRestStub = <NODE:12>()

class TextToSpeechLongAudioSynthesizeRestTransport(_BaseTextToSpeechLongAudioSynthesizeRestTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('TextToSpeechLongAudioSynthesizeRestTransport',)
