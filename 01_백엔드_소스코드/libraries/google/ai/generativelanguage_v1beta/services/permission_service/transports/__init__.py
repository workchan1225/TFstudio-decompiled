# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from collections import OrderedDict
from typing import Dict, Type
from base import PermissionServiceTransport
from grpc import PermissionServiceGrpcTransport
from grpc_asyncio import PermissionServiceGrpcAsyncIOTransport
from rest import PermissionServiceRestInterceptor, PermissionServiceRestTransport
_transport_registry = OrderedDict()
_transport_registry['grpc'] = PermissionServiceGrpcTransport
_transport_registry['grpc_asyncio'] = PermissionServiceGrpcAsyncIOTransport
_transport_registry['rest'] = PermissionServiceRestTransport
__all__ = ('PermissionServiceTransport', 'PermissionServiceGrpcTransport', 'PermissionServiceGrpcAsyncIOTransport', 'PermissionServiceRestTransport', 'PermissionServiceRestInterceptor')
