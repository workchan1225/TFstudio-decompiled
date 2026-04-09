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
from google.ai.generativelanguage_v1beta.types import cached_content as gag_cached_content
from google.ai.generativelanguage_v1beta.types import cache_service
from google.ai.generativelanguage_v1beta.types import cached_content
from base import DEFAULT_CLIENT_INFO, CacheServiceTransport
from grpc import CacheServiceGrpcTransport

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



class CacheServiceGrpcAsyncIOTransport(CacheServiceTransport):
    pass
# WARNING: Decompyle incomplete

__all__ = ('CacheServiceGrpcAsyncIOTransport',)
