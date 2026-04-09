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
from google.protobuf import empty_pb2
from google.protobuf import json_format
from requests import __version__ as requests_version
from google.ai.generativelanguage_v1beta.types import permission as gag_permission
from google.ai.generativelanguage_v1beta.types import permission
from google.ai.generativelanguage_v1beta.types import permission_service
from base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from rest_base import _BasePermissionServiceRestTransport

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

class PermissionServiceRestInterceptor:
    '''Interceptor for PermissionService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the PermissionServiceRestTransport.

    .. code-block:: python
        class MyCustomPermissionServiceInterceptor(PermissionServiceRestInterceptor):
            def pre_create_permission(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_permission(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_permission(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_permission(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_permission(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_permissions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_permissions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_transfer_ownership(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_transfer_ownership(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_permission(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_permission(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = PermissionServiceRestTransport(interceptor=MyCustomPermissionServiceInterceptor())
        client = PermissionServiceClient(transport=transport)


    '''
    
    def pre_create_permission(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for create_permission

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PermissionService server.
        '''
        return (request, metadata)

    
    def post_create_permission(self = None, response = None):
        '''Post-rpc interceptor for create_permission

        Override in a subclass to manipulate the response
        after it is returned by the PermissionService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_delete_permission(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for delete_permission

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PermissionService server.
        '''
        return (request, metadata)

    
    def pre_get_permission(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_permission

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PermissionService server.
        '''
        return (request, metadata)

    
    def post_get_permission(self = None, response = None):
        '''Post-rpc interceptor for get_permission

        Override in a subclass to manipulate the response
        after it is returned by the PermissionService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_permissions(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PermissionService server.
        '''
        return (request, metadata)

    
    def post_list_permissions(self = None, response = None):
        '''Post-rpc interceptor for list_permissions

        Override in a subclass to manipulate the response
        after it is returned by the PermissionService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_transfer_ownership(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for transfer_ownership

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PermissionService server.
        '''
        return (request, metadata)

    
    def post_transfer_ownership(self = None, response = None):
        '''Post-rpc interceptor for transfer_ownership

        Override in a subclass to manipulate the response
        after it is returned by the PermissionService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_update_permission(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for update_permission

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PermissionService server.
        '''
        return (request, metadata)

    
    def post_update_permission(self = None, response = None):
        '''Post-rpc interceptor for update_permission

        Override in a subclass to manipulate the response
        after it is returned by the PermissionService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_get_operation(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PermissionService server.
        '''
        return (request, metadata)

    
    def post_get_operation(self = None, response = None):
        '''Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the PermissionService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_operations(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PermissionService server.
        '''
        return (request, metadata)

    
    def post_list_operations(self = None, response = None):
        '''Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the PermissionService server but before
        it is returned to user code.
        '''
        return response


PermissionServiceRestStub = <NODE:12>()

class PermissionServiceRestTransport(_BasePermissionServiceRestTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('PermissionServiceRestTransport',)
