# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from collections import OrderedDict
from typing import Dict, Type
from base import CacheServiceTransport
from grpc import CacheServiceGrpcTransport
from grpc_asyncio import CacheServiceGrpcAsyncIOTransport
from rest import CacheServiceRestInterceptor, CacheServiceRestTransport
_transport_registry = OrderedDict()
_transport_registry['grpc'] = CacheServiceGrpcTransport
_transport_registry['grpc_asyncio'] = CacheServiceGrpcAsyncIOTransport
_transport_registry['rest'] = CacheServiceRestTransport
__all__ = ('CacheServiceTransport', 'CacheServiceGrpcTransport', 'CacheServiceGrpcAsyncIOTransport', 'CacheServiceRestTransport', 'CacheServiceRestInterceptor')
