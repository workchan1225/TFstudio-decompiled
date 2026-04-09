# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: gemini_native_tts_service.pyc (Python 3.11)

'''
Gemini Native TTS Service
Google Gemini 2.5 TTS - 감정/나이대 표현 가능한 고급 음성 합성

지원 기능:
- 30개 음성 (Chirp3-HD와 동일)
- 감정 프리셋 (8개): 기본, 행복, 슬픔, 화남, 흥분, 차분, 신비, 극적
- 나이대 프리셋 (6개): 기본, 어린이, 청소년, 청년, 중년, 노년
- 커스텀 스타일 프롬프트 지원
- Flash/Pro 모델 선택
- 라인별 TTS 생성 (정확한 자막 타임코드)
'''
import html
import logging
import os
import sys
import re
import base64
import tempfile
import shutil
import subprocess
import wave
import struct
import time
import threading
from pathlib import Path
from typing import Optional, Dict, List, Any, Generator, Union
from app.utils.ffmpeg_wrapper import FFmpegWrapper
from app.utils.ffmpeg_utils import get_ffmpeg_executable
from app.utils.atomic_media_write import atomic_audio_output
from app.utils.audio_silence_utils import detect_all_silence_regions
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from app.utils.sequence_alignment import STTWord, align_script_with_stt, enforce_minimum_segment_duration, validate_and_fix_segment_overlaps
from app.utils.ssml_utils import detect_mixed_korean_english
logger = logging.getLogger(__name__)
DEFAULT_GEMINI_NATIVE_TTS_REQUEST_TIMEOUT_SEC = 2400

def _read_positive_int_env(name = None, default = None):
    raw_value = os.getenv(name)
# WARNING: Decompyle incomplete


class RateLimiter:
    '''Gemini TTS API Rate Limiter (분당 6건 = 10초당 1건 제한 대응)'''
    
    def __init__(self = None, min_interval_seconds = None):
        '''
        Args:
            min_interval_seconds: 요청 간 최소 간격 (초, 기본: 10초 - 6 RPM 안전 여유)
        '''
        self.min_interval = min_interval_seconds
        self.last_request_time = 0
        self.lock = threading.Lock()

    
    def wait_if_needed(self = None):
        '''
        Rate limit에 걸리지 않도록 필요시 대기
        6 RPM = 10초당 1건 (안전 여유 포함)

        Returns:
            대기한 시간 (초)
        '''
        self.lock
        now = time.time()
        elapsed = now - self.last_request_time
        if elapsed < self.min_interval and self.last_request_time > 0:
            wait_time = self.min_interval - elapsed
            logger.info(f'''[GeminiNativeTTS RateLimiter] Waiting {wait_time:.1f}s to maintain 10s interval''')
            time.sleep(wait_time)
            self.last_request_time = time.time()
            None(None, None)
            return 
        None(None, None)
        return 0
        with None:
            if not None.time():
                pass


_gemini_rate_limiter = RateLimiter(min_interval_seconds = 10)
GEMINI_NATIVE_AVAILABLE = False
_USE_NEW_SDK = False

try:
    from google import genai as new_genai
    from google.genai import types as genai_types
    GEMINI_NATIVE_AVAILABLE = True
    _USE_NEW_SDK = True
    logger.info('[Gemini Native TTS] google-genai SDK 로드 완료 (신규)')
except ImportError:
    from google.generativeai import generativeai as legacy_genai
    GEMINI_NATIVE_AVAILABLE = True
    _USE_NEW_SDK = False
    logger.info('[Gemini Native TTS] google-generativeai SDK 로드 완료 (레거시)')
except ImportError:
    logger.warning('[Gemini Native TTS] Google AI SDK가 설치되지 않았습니다.')


class GeminiNativeTTSService:
    __module__ = __name__
    __qualname__ = 'GeminiNativeTTSService'
    __doc__ = 'Gemini Native TTS 서비스 (감정/나이대 표현)'
    BULK_LINE_MAX_CHARS = 40
    BULK_DEFAULT_CHUNK_SIZE = 1000
    BULK_MIN_CHUNK_SIZE = 180
    BULK_MAX_CHUNK_SIZE = 1000
    BULK_SEMANTIC_UNIT_MAX_CHARS = 120
    BULK_FORCE_ALIGNMENT_MIN_CONFIDENCE = 0.72
    BULK_STT_AUTO_RETRY_COUNT = 1
    BULK_STT_RETRY_MIN_CONFIDENCE = 0.7
    BULK_STT_RETRY_MIN_MATCH_RATE = 0.92
    BULK_STT_RETRY_MAX_LOW_CONF_RATIO = 0.3
    BULK_SILENCE_REFINE_MAX_BOUNDARY_SHIFT = 0.25
    BULK_SILENCE_REFINE_MAX_CANDIDATE_DISTANCE = 0.6
    BULK_SPEECH_RELAXED_MODE = True
    BULK_SPEECH_RELAXED_START_PADDING = 0.02
    BULK_SPEECH_RELAXED_END_PADDING = 0.06
    BULK_SPEECH_RELAXED_SEARCH_PADDING = 0.12
    BULK_SPEECH_RELAXED_MIN_DURATION = 0.45
    BULK_SPEECH_RELAXED_MIN_GAP = 0.01
    FORCED_ALIGNMENT_CONFIDENCE = 0.85
    MIN_SPLIT_TAIL_CHARS = 8
    ADJACENT_TEXT_OVERLAP_MIN_WORDS = 2
    ADJACENT_TEXT_OVERLAP_MAX_WORDS = 5
    OVERLAP_TOKEN_STRIP_CHARS = '"\'`.,!?;:()[]{}<>-_/\\|~…“”‘’「」『』《》【】'
    MODELS = {
        'flash': 'gemini-2.5-flash-preview-tts',
        'pro': 'gemini-2.5-pro-preview-tts' }
    EMOTION_PRESETS = {
        'neutral': {
            'prompt': '',
            'label': '기본',
            'label_en': 'Neutral',
            'icon': 'sentiment_neutral',
            'color': 'gray' },
        'happy': {
            'prompt': 'Say this in a cheerful, happy tone with enthusiasm and joy',
            'label': '행복한',
            'label_en': 'Happy',
            'icon': 'sentiment_very_satisfied',
            'color': 'yellow' },
        'sad': {
            'prompt': 'Say this with a somber, melancholic tone expressing deep sadness',
            'label': '슬픈',
            'label_en': 'Sad',
            'icon': 'sentiment_dissatisfied',
            'color': 'blue' },
        'angry': {
            'prompt': 'Say this with an intense, angry tone showing frustration and intensity',
            'label': '화난',
            'label_en': 'Angry',
            'icon': 'mood_bad',
            'color': 'red' },
        'excited': {
            'prompt': 'Say this with high energy and excitement, very upbeat and enthusiastic',
            'label': '흥분된',
            'label_en': 'Excited',
            'icon': 'celebration',
            'color': 'orange' },
        'calm': {
            'prompt': 'Say this in a calm, soothing, peaceful voice with gentle delivery',
            'label': '차분한',
            'label_en': 'Calm',
            'icon': 'spa',
            'color': 'cyan' },
        'mysterious': {
            'prompt': 'Say this in a mysterious, intriguing whisper with an air of secrecy',
            'label': '신비로운',
            'label_en': 'Mysterious',
            'icon': 'psychology',
            'color': 'purple' },
        'dramatic': {
            'prompt': 'Say this with dramatic emphasis, theatrical gravitas and intensity',
            'label': '극적인',
            'label_en': 'Dramatic',
            'icon': 'theater_comedy',
            'color': 'pink' } }
    AGE_PRESETS = {
        'default': {
            'prompt': '',
            'label': '기본',
            'label_en': 'Default',
            'icon': 'person',
            'color': 'gray' },
        'child': {
            'prompt': 'Speak like a young child around 8-10 years old with a bright, innocent voice',
            'label': '어린이 (8-10세)',
            'label_en': 'Child (8-10)',
            'icon': 'child_care',
            'color': 'pink' },
        'teen': {
            'prompt': 'Speak like a teenager around 15-17 years old with youthful energy',
            'label': '청소년 (15-17세)',
            'label_en': 'Teen (15-17)',
            'icon': 'face',
            'color': 'purple' },
        'young_adult': {
            'prompt': 'Speak like a young adult in their 20s with a fresh, energetic voice',
            'label': '청년 (20대)',
            'label_en': 'Young Adult (20s)',
            'icon': 'person',
            'color': 'blue' },
        'middle_aged': {
            'prompt': 'Speak like a mature adult in their 40s-50s with a seasoned, authoritative voice',
            'label': '중년 (40-50대)',
            'label_en': 'Middle-aged (40-50s)',
            'icon': 'person_3',
            'color': 'teal' },
        'elderly': {
            'prompt': 'Speak like an elderly person in their 70s with a wise, gentle, weathered voice',
            'label': '노년 (70대+)',
            'label_en': 'Elderly (70s+)',
            'icon': 'elderly',
            'color': 'amber' } }
# WARNING: Decompyle incomplete
