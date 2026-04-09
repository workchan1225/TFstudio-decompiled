# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from collections import OrderedDict
from typing import Dict, Type
from base import TextServiceTransport
from grpc import TextServiceGrpcTransport
from grpc_asyncio import TextServiceGrpcAsyncIOTransport
from rest import TextServiceRestInterceptor, TextServiceRestTransport
_transport_registry = OrderedDict()
_transport_registry['grpc'] = TextServiceGrpcTransport
_transport_registry['grpc_asyncio'] = TextServiceGrpcAsyncIOTransport
_transport_registry['rest'] = TextServiceRestTransport
__all__ = ('TextServiceTransport', 'TextServiceGrpcTransport', 'TextServiceGrpcAsyncIOTransport', 'TextServiceRestTransport', 'TextServiceRestInterceptor')
