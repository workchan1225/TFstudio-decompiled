# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chirp3_hd_tts_service.pyc (Python 3.11)

'''
Google Cloud Chirp 3 HD TTS Service
고품질 30가지 음성 스타일 + SSML mark 태그 기반 타임포인트 지원

지원 기능:
- 30개 Chirp3-HD 음성 (ko-KR, en-US)
- 속도 조절 (0.25 ~ 2.0)
- 숨 돌리기 태그: [pause short], [pause], [pause long]
- SSML mark 태그로 타임포인트 추출 (자막 생성용)
- 긴 텍스트 자동 청크 분할 (5000바이트 제한)
'''
import logging
import sys
import os
import re
import tempfile
import shutil
import subprocess
import threading
import time
from pathlib import Path
from typing import Optional, Dict, List, Any, Tuple, Generator
from app.utils.atomic_media_write import atomic_audio_output
from app.utils.ffmpeg_wrapper import FFmpegWrapper
from app.utils.ffmpeg_utils import get_ffmpeg_executable
from app.utils.parallel_tts_executor import ParallelTTSExecutor, TTSTask, TTSResult
from app.utils.ssml_utils import wrap_english_with_phoneme_tag, escape_ssml
from app.services.google_auth_service import create_google_tts_client
logger = logging.getLogger(__name__)
_CHIRP3_HD_COOLDOWN_LOCK = threading.Lock()
_CHIRP3_HD_LAST_SYNTHESIS_COMPLETED_AT = 0

def _wait_for_chirp3_hd_cooldown(delay_seconds = None):
