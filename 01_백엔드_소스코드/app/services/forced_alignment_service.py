# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: forced_alignment_service.pyc (Python 3.11)

'''
Forced Alignment Service for Chirp3-HD Subtitle Generation

Chirp3-HD 음성은 SSML <mark> 태그를 지원하지 않아 타임포인트를 직접 추출할 수 없습니다.
따라서 Forced Alignment 기술을 사용하여 대본과 오디오를 정렬합니다.

지원 방식:
1. aeneas (기본): 정확한 단어/문장 정렬
2. WhisperX (fallback): 음성 인식 + 정렬
'''
import os
import sys
import tempfile
import logging
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from app.utils.ffmpeg_utils import probe_media_duration
logger = logging.getLogger(__name__)
SubtitleSegment = <NODE:12>()

class ForcedAlignmentService:
    '''Forced Alignment 서비스'''
    
    def __init__(self):
        self._aeneas_available = None
        self._whisperx_available = None

    aeneas_available = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    whisperx_available = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def generate_subtitles_from_audio(self = None, audio_path = None, script_text = None, language = ('ko',)):
