# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from collections import OrderedDict
from typing import Dict, Type
from base import DiscussServiceTransport
from grpc import DiscussServiceGrpcTransport
from grpc_asyncio import DiscussServiceGrpcAsyncIOTransport
from rest import DiscussServiceRestInterceptor, DiscussServiceRestTransport
_transport_registry = OrderedDict()
_transport_registry['grpc'] = DiscussServiceGrpcTransport
_transport_registry['grpc_asyncio'] = DiscussServiceGrpcAsyncIOTransport
_transport_registry['rest'] = DiscussServiceRestTransport
__all__ = ('DiscussServiceTransport', 'DiscussServiceGrpcTransport', 'DiscussServiceGrpcAsyncIOTransport', 'DiscussServiceRestTransport', 'DiscussServiceRestInterceptor')
