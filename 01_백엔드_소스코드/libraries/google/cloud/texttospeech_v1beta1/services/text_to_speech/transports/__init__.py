# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from collections import OrderedDict
from typing import Dict, Type
from base import TextToSpeechTransport
from grpc import TextToSpeechGrpcTransport
from grpc_asyncio import TextToSpeechGrpcAsyncIOTransport
from rest import TextToSpeechRestInterceptor, TextToSpeechRestTransport
_transport_registry = OrderedDict()
_transport_registry['grpc'] = TextToSpeechGrpcTransport
_transport_registry['grpc_asyncio'] = TextToSpeechGrpcAsyncIOTransport
_transport_registry['rest'] = TextToSpeechRestTransport
__all__ = ('TextToSpeechTransport', 'TextToSpeechGrpcTransport', 'TextToSpeechGrpcAsyncIOTransport', 'TextToSpeechRestTransport', 'TextToSpeechRestInterceptor')
