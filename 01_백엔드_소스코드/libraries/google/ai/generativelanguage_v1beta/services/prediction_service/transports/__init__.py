# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from collections import OrderedDict
from typing import Dict, Type
from base import PredictionServiceTransport
from grpc import PredictionServiceGrpcTransport
from grpc_asyncio import PredictionServiceGrpcAsyncIOTransport
from rest import PredictionServiceRestInterceptor, PredictionServiceRestTransport
_transport_registry = OrderedDict()
_transport_registry['grpc'] = PredictionServiceGrpcTransport
_transport_registry['grpc_asyncio'] = PredictionServiceGrpcAsyncIOTransport
_transport_registry['rest'] = PredictionServiceRestTransport
__all__ = ('PredictionServiceTransport', 'PredictionServiceGrpcTransport', 'PredictionServiceGrpcAsyncIOTransport', 'PredictionServiceRestTransport', 'PredictionServiceRestInterceptor')
