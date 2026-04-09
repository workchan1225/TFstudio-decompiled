# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: elevenlabs_engine.pyc (Python 3.11)

'''
ElevenLabs TTS Engine

ElevenLabs API를 사용해 단일 줄 TTS를 생성합니다.
'''
import base64
import json
import os
import requests
from typing import Dict, List, Optional, Tuple
from app.utils.atomic_media_write import atomic_audio_output
from base_tts_engine import BaseTTSEngine, TTSResult, TTSEngineConfig
from line_regeneration_mixin import LineRegenerationMixin

class ElevenLabsErrorCode:
    QUOTA_EXCEEDED = 'ELEVENLABS_QUOTA_EXCEEDED'
    API_ERROR = 'ELEVENLABS_API_ERROR'
    TIMEOUT = 'ELEVENLABS_TIMEOUT'


class ElevenLabsEngine(LineRegenerationMixin, BaseTTSEngine):
    pass
# WARNING: Decompyle incomplete
