# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: edge_engine.pyc (Python 3.11)

'''
Edge TTS 엔진

Microsoft Edge의 무료 TTS 서비스를 사용하는 엔진 구현체입니다.
API 키가 필요하지 않습니다.
'''
import os
import logging
from typing import Dict, Any, Optional
from pathlib import Path
from base_tts_engine import BaseTTSEngine, TTSResult, TTSEngineConfig
from line_regeneration_mixin import LineRegenerationMixin
logger = logging.getLogger(__name__)

class EdgeEngine(LineRegenerationMixin, BaseTTSEngine):
    pass
# WARNING: Decompyle incomplete
