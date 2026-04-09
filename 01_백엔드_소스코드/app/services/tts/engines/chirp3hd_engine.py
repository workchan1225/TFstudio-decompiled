# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chirp3hd_engine.pyc (Python 3.11)

'''
Chirp 3 HD TTS 엔진

Google Cloud Text-to-Speech (Chirp3-HD)를 사용하는 엔진 구현체입니다.
기존 Chirp3HDTTSService를 래핑하여 BaseTTSEngine 인터페이스를 제공합니다.
'''
import logging
from typing import Dict, Any, Optional
from base_tts_engine import BaseTTSEngine, TTSResult, TTSEngineConfig
from line_regeneration_mixin import LineRegenerationMixin
logger = logging.getLogger(__name__)

class Chirp3HDEngine(LineRegenerationMixin, BaseTTSEngine):
    pass
# WARNING: Decompyle incomplete
