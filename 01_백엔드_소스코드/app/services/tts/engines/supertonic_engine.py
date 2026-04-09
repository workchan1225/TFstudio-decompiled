# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: supertonic_engine.pyc (Python 3.11)

'''
Supertonic TTS engine.

Local ONNX Supertonic inference for unified line regeneration API.
'''
import logging
from typing import Any, Dict
from base_tts_engine import BaseTTSEngine, TTSResult, TTSEngineConfig
from line_regeneration_mixin import LineRegenerationMixin
logger = logging.getLogger(__name__)

class SupertonicEngine(LineRegenerationMixin, BaseTTSEngine):
    pass
# WARNING: Decompyle incomplete
