# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grpc.pyc (Python 3.11)

import json
import logging as std_logging
import pickle
from typing import Callable, Dict, Optional, Sequence, Tuple, Union
import warnings
from google.api_core import gapic_v1, grpc_helpers
import google.auth as google
from google.auth import credentials as ga_credentials
from google.auth.transport.grpc import SslCredentials
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToJson
import google.protobuf.message as google
import grpc
import proto
from google.ai.generativelanguage_v1beta.types import cached_content as gag_cached_content
from google.ai.generativelanguage_v1beta.types import cache_service
from google.ai.generativelanguage_v1beta.types import cached_content
from base import DEFAULT_CLIENT_INFO, CacheServiceTransport

try:
    from google.api_core import client_logging
    CLIENT_LOGGING_SUPPORTED = True
except ImportError:
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

class _LoggingClientInterceptor(grpc.UnaryUnaryClientInterceptor):
    
    def intercept_unary_unary(self, continuation, client_call_details, request):
        if CLIENT_LOGGING_SUPPORTED:
            pass
        logging_enabled = _LOGGER.isEnabledFor(std_logging.DEBUG)
        if logging_enabled:
            request_metadata = client_call_details.metadata
            if isinstance(request, proto.Message):
                request_payload = type(request).to_json(request)
            elif isinstance(request, google.protobuf.message.Message):
                request_payload = MessageToJson(request)
            else:
                request_payload = f'''{type(request).__name__}: {pickle.dumps(request)}'''
            request_metadata = request_metadata()
            grpc_request = {
                'payload': request_payload,
                'requestMethod': 'grpc',
                'metadata': dict(request_metadata) }
            _LOGGER.debug(f'''Sending request for {client_call_details.method}''', extra = {
                'serviceName': 'google.ai.generativelanguage.v1beta.CacheService',
                'rpcName': client_call_details.method,
                'request': grpc_request,
                'metadata': grpc_request['metadata'] })
        response = continuation(client_call_details, request)
        if logging_enabled:
            response_metadata = response.trailing_metadata()
            metadata = (lambda .0: [ (k, str(v)) for k, v in .0 ])(response_metadata()) if response_metadata else None
            result = response.result()
            if isinstance(result, proto.Message):
                response_payload = type(result).to_json(result)
            elif isinstance(result, google.protobuf.message.Message):
                response_payload = MessageToJson(result)
            else:
                response_payload = f'''{type(result).__name__}: {pickle.dumps(result)}'''
            grpc_response = {
                'payload': response_payload,
                'metadata': metadata,
                'status': 'OK' }
            _LOGGER.debug(f'''Received response for {client_call_details.method}.''', extra = {
                'serviceName': 'google.ai.generativelanguage.v1beta.CacheService',
                'rpcName': client_call_details.method,
                'response': grpc_response,
                'metadata': grpc_response['metadata'] })
        return response



class CacheServiceGrpcTransport(CacheServiceTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('CacheServiceGrpcTransport',)
