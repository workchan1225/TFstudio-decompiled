# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from collections import OrderedDict
from typing import cast, Dict, Tuple
from base import OperationsTransport
from rest import OperationsRestTransport
_transport_registry: Dict[(str, OperationsTransport)] = OrderedDict()
_transport_registry['rest'] = cast(OperationsTransport, OperationsRestTransport)
__all__: Tuple[(str, ...)] = ('OperationsTransport', 'OperationsRestTransport')

try:
    from rest_asyncio import AsyncOperationsRestTransport
    __all__ += ('AsyncOperationsRestTransport',)
    _transport_registry['rest_asyncio'] = cast(OperationsTransport, AsyncOperationsRestTransport)
    return None
except ImportError:
    return None
