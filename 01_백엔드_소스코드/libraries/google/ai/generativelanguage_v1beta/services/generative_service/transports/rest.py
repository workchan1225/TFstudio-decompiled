# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rest.pyc (Python 3.11)

import dataclasses
import json
import logging
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.transport.requests import AuthorizedSession
from google.longrunning import operations_pb2
from google.protobuf import json_format
from requests import __version__ as requests_version
from google.ai.generativelanguage_v1beta.types import generative_service
from base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from rest_base import _BaseGenerativeServiceRestTransport

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

class GenerativeServiceRestInterceptor:
    '''Interceptor for GenerativeService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the GenerativeServiceRestTransport.

    .. code-block:: python
        class MyCustomGenerativeServiceInterceptor(GenerativeServiceRestInterceptor):
            def pre_batch_embed_contents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_embed_contents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_count_tokens(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_count_tokens(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_embed_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_embed_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_answer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_answer(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stream_generate_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stream_generate_content(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = GenerativeServiceRestTransport(interceptor=MyCustomGenerativeServiceInterceptor())
        client = GenerativeServiceClient(transport=transport)


    '''
    
    def pre_batch_embed_contents(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for batch_embed_contents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeService server.
        '''
        return (request, metadata)

    
    def post_batch_embed_contents(self = None, response = None):
        '''Post-rpc interceptor for batch_embed_contents

        Override in a subclass to manipulate the response
        after it is returned by the GenerativeService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_count_tokens(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for count_tokens

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeService server.
        '''
        return (request, metadata)

    
    def post_count_tokens(self = None, response = None):
        '''Post-rpc interceptor for count_tokens

        Override in a subclass to manipulate the response
        after it is returned by the GenerativeService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_embed_content(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for embed_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeService server.
        '''
        return (request, metadata)

    
    def post_embed_content(self = None, response = None):
        '''Post-rpc interceptor for embed_content

        Override in a subclass to manipulate the response
        after it is returned by the GenerativeService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_generate_answer(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for generate_answer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeService server.
        '''
        return (request, metadata)

    
    def post_generate_answer(self = None, response = None):
        '''Post-rpc interceptor for generate_answer

        Override in a subclass to manipulate the response
        after it is returned by the GenerativeService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_generate_content(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for generate_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeService server.
        '''
        return (request, metadata)

    
    def post_generate_content(self = None, response = None):
        '''Post-rpc interceptor for generate_content

        Override in a subclass to manipulate the response
        after it is returned by the GenerativeService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_stream_generate_content(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for stream_generate_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeService server.
        '''
        return (request, metadata)

    
    def post_stream_generate_content(self = None, response = None):
        '''Post-rpc interceptor for stream_generate_content

        Override in a subclass to manipulate the response
        after it is returned by the GenerativeService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_get_operation(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeService server.
        '''
        return (request, metadata)

    
    def post_get_operation(self = None, response = None):
        '''Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the GenerativeService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_operations(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the GenerativeService server.
        '''
        return (request, metadata)

    
    def post_list_operations(self = None, response = None):
        '''Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the GenerativeService server but before
        it is returned to user code.
        '''
        return response


GenerativeServiceRestStub = <NODE:12>()

class GenerativeServiceRestTransport(_BaseGenerativeServiceRestTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('GenerativeServiceRestTransport',)
