# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: googlecloud_engine.pyc (Python 3.11)

'''
Google Cloud TTS 엔진

Google Cloud Text-to-Speech API (표준 음성)를 사용하는 엔진 구현체입니다.
API 키가 필요합니다.
'''
import os
import logging
from typing import Dict, Any, Optional
from pathlib import Path
from base_tts_engine import BaseTTSEngine, TTSResult, TTSEngineConfig
from line_regeneration_mixin import LineRegenerationMixin
logger = logging.getLogger(__name__)

class GoogleCloudEngine(LineRegenerationMixin, BaseTTSEngine):
    pass
# WARNING: Decompyle incomplete
