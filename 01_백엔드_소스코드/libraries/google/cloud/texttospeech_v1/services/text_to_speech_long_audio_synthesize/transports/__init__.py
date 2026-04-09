# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from collections import OrderedDict
from typing import Dict, Type
from base import TextToSpeechLongAudioSynthesizeTransport
from grpc import TextToSpeechLongAudioSynthesizeGrpcTransport
from grpc_asyncio import TextToSpeechLongAudioSynthesizeGrpcAsyncIOTransport
from rest import TextToSpeechLongAudioSynthesizeRestInterceptor, TextToSpeechLongAudioSynthesizeRestTransport
_transport_registry = OrderedDict()
_transport_registry['grpc'] = TextToSpeechLongAudioSynthesizeGrpcTransport
_transport_registry['grpc_asyncio'] = TextToSpeechLongAudioSynthesizeGrpcAsyncIOTransport
_transport_registry['rest'] = TextToSpeechLongAudioSynthesizeRestTransport
__all__ = ('TextToSpeechLongAudioSynthesizeTransport', 'TextToSpeechLongAudioSynthesizeGrpcTransport', 'TextToSpeechLongAudioSynthesizeGrpcAsyncIOTransport', 'TextToSpeechLongAudioSynthesizeRestTransport', 'TextToSpeechLongAudioSynthesizeRestInterceptor')
