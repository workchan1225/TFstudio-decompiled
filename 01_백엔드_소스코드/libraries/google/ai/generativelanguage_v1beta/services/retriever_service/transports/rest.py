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
from google.ai.generativelanguage_v1beta.types import retriever, retriever_service
from base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from rest_base import _BaseRetrieverServiceRestTransport

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

class RetrieverServiceRestInterceptor:
    '''Interceptor for RetrieverService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the RetrieverServiceRestTransport.

    .. code-block:: python
        class MyCustomRetrieverServiceInterceptor(RetrieverServiceRestInterceptor):
            def pre_batch_create_chunks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_chunks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_delete_chunks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_batch_update_chunks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_chunks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_chunk(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_chunk(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_corpus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_corpus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_chunk(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_corpus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_chunk(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_chunk(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_corpus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_corpus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_chunks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_chunks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_corpora(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_corpora(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_documents(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_documents(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_corpus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_corpus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_document(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_chunk(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_chunk(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_corpus(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_corpus(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_document(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_document(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = RetrieverServiceRestTransport(interceptor=MyCustomRetrieverServiceInterceptor())
        client = RetrieverServiceClient(transport=transport)


    '''
    
    def pre_batch_create_chunks(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for batch_create_chunks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_batch_create_chunks(self = None, response = None):
        '''Post-rpc interceptor for batch_create_chunks

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_batch_delete_chunks(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for batch_delete_chunks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def pre_batch_update_chunks(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for batch_update_chunks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_batch_update_chunks(self = None, response = None):
        '''Post-rpc interceptor for batch_update_chunks

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_create_chunk(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for create_chunk

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_create_chunk(self = None, response = None):
        '''Post-rpc interceptor for create_chunk

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_create_corpus(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for create_corpus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_create_corpus(self = None, response = None):
        '''Post-rpc interceptor for create_corpus

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_create_document(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for create_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_create_document(self = None, response = None):
        '''Post-rpc interceptor for create_document

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_delete_chunk(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for delete_chunk

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def pre_delete_corpus(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for delete_corpus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def pre_delete_document(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for delete_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def pre_get_chunk(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_chunk

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_get_chunk(self = None, response = None):
        '''Post-rpc interceptor for get_chunk

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_get_corpus(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_corpus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_get_corpus(self = None, response = None):
        '''Post-rpc interceptor for get_corpus

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_get_document(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_get_document(self = None, response = None):
        '''Post-rpc interceptor for get_document

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_chunks(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_chunks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_list_chunks(self = None, response = None):
        '''Post-rpc interceptor for list_chunks

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_corpora(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_corpora

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_list_corpora(self = None, response = None):
        '''Post-rpc interceptor for list_corpora

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_documents(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_documents

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_list_documents(self = None, response = None):
        '''Post-rpc interceptor for list_documents

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_query_corpus(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for query_corpus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_query_corpus(self = None, response = None):
        '''Post-rpc interceptor for query_corpus

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_query_document(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for query_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_query_document(self = None, response = None):
        '''Post-rpc interceptor for query_document

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_update_chunk(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for update_chunk

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_update_chunk(self = None, response = None):
        '''Post-rpc interceptor for update_chunk

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_update_corpus(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for update_corpus

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_update_corpus(self = None, response = None):
        '''Post-rpc interceptor for update_corpus

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_update_document(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for update_document

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_update_document(self = None, response = None):
        '''Post-rpc interceptor for update_document

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_get_operation(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_get_operation(self = None, response = None):
        '''Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response

    
    def pre_list_operations(self = None, request = None, metadata = None):
        '''Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RetrieverService server.
        '''
        return (request, metadata)

    
    def post_list_operations(self = None, response = None):
        '''Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the RetrieverService server but before
        it is returned to user code.
        '''
        return response


RetrieverServiceRestStub = <NODE:12>()

class RetrieverServiceRestTransport(_BaseRetrieverServiceRestTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('RetrieverServiceRestTransport',)
