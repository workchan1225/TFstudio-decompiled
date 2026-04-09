# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grpc_asyncio.pyc (Python 3.11)

import inspect
import json
import logging as std_logging
import pickle
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
import warnings
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials
from google.auth.transport.grpc import SslCredentials
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToJson
import google.protobuf.message as google
import grpc
from grpc.experimental import aio
import proto
from google.ai.generativelanguage_v1beta.types import retriever, retriever_service
from base import DEFAULT_CLIENT_INFO, RetrieverServiceTransport
from grpc import RetrieverServiceGrpcTransport

try:
    from google.api_core import client_logging
    CLIENT_LOGGING_SUPPORTED = True
except ImportError:
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

class _LoggingClientAIOInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    
    async def intercept_unary_unary(self, continuation, client_call_details, request):
        pass
    # WARNING: Decompyle incomplete



class RetrieverServiceGrpcAsyncIOTransport(RetrieverServiceTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('RetrieverServiceGrpcAsyncIOTransport',)
