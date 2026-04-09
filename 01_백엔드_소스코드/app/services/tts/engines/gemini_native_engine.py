# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gemini_native_engine.pyc (Python 3.11)

'''
Gemini Native TTS 엔진

Google Gemini 네이티브 TTS를 사용하는 엔진 구현체입니다.
API 키가 필요합니다.
'''
import os
import logging
from typing import Dict, Any, Optional
from pathlib import Path
from base_tts_engine import BaseTTSEngine, TTSResult, TTSEngineConfig
from line_regeneration_mixin import LineRegenerationMixin
logger = logging.getLogger(__name__)

class GeminiNativeEngine(LineRegenerationMixin, BaseTTSEngine):
    pass
# WARNING: Decompyle incomplete
