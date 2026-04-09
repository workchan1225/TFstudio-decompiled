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
from google.protobuf import empty_pb2
from google.protobuf import json_format
from requests import __version__ as requests_version
from google.ai.generativelanguage_v1beta.types import tuned_model as gag_tuned_model
from google.ai.generativelanguage_v1beta.types import model, model_service
from google.ai.generativelanguage_v1beta.types import tuned_model
from base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from rest_base import _BaseModelServiceRestTransport

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

class ModelServiceRestInterceptor:
    '''Interceptor for ModelService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ModelServiceRestTransport.

    .. code-block:: python
        class MyCustomModelServiceInterceptor(ModelServiceRestInterceptor):
            def pre_create_tuned_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tuned_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tuned_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tuned_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tuned_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_models(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_models(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tuned_models(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tuned_models(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tuned_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tuned_model(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ModelServiceRestTransport(interceptor=MyCustomModelServiceInterceptor())
        client = ModelServiceClient(transport=transport)


    '''
    
    def pre_create_tuned_model(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for create_tuned_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        '''
        return (request, metadata)

    
    def post_create_tuned_model(self = None, response = None):
        '''Post-rpc interceptor for create_tuned_model

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_delete_tuned_model(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for delete_tuned_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        '''
        return (request, metadata)

    
    def pre_get_model(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        '''
        return (request, metadata)

    
    def post_get_model(self = None, response = None):
        '''Post-rpc interceptor for get_model

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_get_tuned_model(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_tuned_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        '''
        return (request, metadata)

    
    def post_get_tuned_model(self = None, response = None):
        '''Post-rpc interceptor for get_tuned_model

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_models(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_models

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        '''
        return (request, metadata)

    
    def post_list_models(self = None, response = None):
        '''Post-rpc interceptor for list_models

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_tuned_models(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_tuned_models

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        '''
        return (request, metadata)

    
    def post_list_tuned_models(self = None, response = None):
        '''Post-rpc interceptor for list_tuned_models

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_update_tuned_model(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for update_tuned_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        '''
        return (request, metadata)

    
    def post_update_tuned_model(self = None, response = None):
        '''Post-rpc interceptor for update_tuned_model

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_get_operation(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        '''
        return (request, metadata)

    
    def post_get_operation(self = None, response = None):
        '''Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_operations(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ModelService server.
        '''
        return (request, metadata)

    
    def post_list_operations(self = None, response = None):
        '''Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ModelService server but before
        it is returned to user code.
        '''
        return response


ModelServiceRestStub = <NODE:12>()

class ModelServiceRestTransport(_BaseModelServiceRestTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('ModelServiceRestTransport',)
