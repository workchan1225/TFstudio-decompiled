# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: audio_silence_utils.pyc (Python 3.11)

'''
오디오 트리밍 유틸리티

TTS 생성 후 세그먼트 끝부분을 고정 시간만큼 트리밍합니다.
자막 자동 생성 모드에서 자연스러운 음성 연결을 위해 사용됩니다.

주요 함수:
- trim_trailing_fixed(): 뒤쪽 고정 시간 트리밍 (0.6초)
- should_trim_trailing(): 트리밍 여부 판단 (마침표 체크)
'''
import subprocess
import sys
import re
import os
import struct
import math
import logging
from collections import OrderedDict
from pathlib import Path
from threading import Lock
from typing import Tuple, Optional, List, Dict
from app.utils.ffmpeg_utils import get_ffmpeg_executable, get_ffprobe_executable
logger = logging.getLogger(__name__)
_PEAKS_CACHE_MAX_ENTRIES = 256
_peaks_cache: 'OrderedDict[Tuple[str, float, int], Tuple[List[float], float]]' = OrderedDict()
_peaks_cache_lock = Lock()

def _get_cached_peaks(cache_key = None):
    _peaks_cache_lock
    cached = _peaks_cache.get(cache_key)
# WARNING: Decompyle incomplete


def _set_cached_peaks(cache_key = None, value = None):
    _peaks_cache_lock
    _peaks_cache[cache_key] = value
    _peaks_cache.move_to_end(cache_key)
    if len(_peaks_cache) > _PEAKS_CACHE_MAX_ENTRIES:
        _peaks_cache.popitem(last = False)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def get_audio_peaks(audio_path = None, num_peaks = None):
    '''
    FFmpeg로 오디오 파형 peaks 데이터와 duration 추출

    WaveSurfer.js의 peaks 로딩에 사용 (전체 파일 다운로드 없이 파형 렌더링 가능)

    Args:
        audio_path: 오디오 파일 경로
        num_peaks: 반환할 peaks 데이터 개수 (기본 2000)

    Returns:
        (peaks_list, duration_seconds)
        peaks_list: 0~1 사이 float 값의 리스트
    '''
    pass
# WARNING: Decompyle incomplete


def get_audio_duration(audio_path = None):
    '''
    오디오 파일의 전체 길이 조회 (초)

    Args:
        audio_path: 오디오 파일 경로

    Returns:
        오디오 길이 (초), 실패 시 0.0
    '''
    pass
# WARNING: Decompyle incomplete


def trim_trailing_fixed(audio_path = None, output_path = None, trim_seconds = None):
    '''
    오디오 뒤쪽을 고정 시간만큼 트리밍

    복잡한 무음 감지 없이 단순히 뒤쪽 N초를 제거합니다.
    Google TTS는 약 0.5~0.8초의 뒤쪽 무음을 추가하므로,
    0.6초 고정 트리밍으로 대부분의 불필요한 무음을 제거할 수 있습니다.

    Args:
        audio_path: 입력 오디오 파일 경로
        output_path: 출력 오디오 파일 경로
        trim_seconds: 트리밍할 시간 (초, 기본 0.6)

    Returns:
        (출력 파일 경로, 실제 트리밍량) 튜플
        에러 발생 시 (원본 경로, 0.0) 반환
    '''
    pass
# WARNING: Decompyle incomplete


def should_trim_trailing(text = None):
    '''
    뒤쪽 트리밍 여부 판단

    텍스트가 마침표, 물음표, 느낌표 등으로 끝나면 문장이 완결된 것이므로
    자연스러운 휴지가 필요해 트리밍하지 않습니다.
    문장부호로 끝나지 않으면 다음 문장과 이어지는 것이므로 트리밍합니다.

    Args:
        text: 현재 세그먼트 텍스트

    Returns:
        트리밍이 필요하면 True, 아니면 False
    '''
    if not text:
        return False
    text_stripped = None.strip()
    if not text_stripped:
        return False
    last_char = None[-1]
    punctuation_chars = '.?!。？！'
    if last_char in punctuation_chars:
        return False


def detect_trailing_silence(audio_path = None, threshold_db = None, min_silence_duration = None):
    '''
    오디오 끝부분의 무음 길이 감지

    FFmpeg silencedetect 필터를 사용하여 오디오 끝부분의 무음 구간 길이를 감지합니다.

    Args:
        audio_path: 오디오 파일 경로
        threshold_db: 무음 판정 임계값 (dB, 기본값 -40dB)
        min_silence_duration: 최소 무음 지속시간 (초, 기본값 0.05초)

    Returns:
        끝부분 무음 길이 (초), 무음이 없으면 0.0
    '''
    pass
# WARNING: Decompyle incomplete


def detect_all_silence_regions(audio_path = None, threshold_db = None, min_silence_duration = None):
    '''
    전체 오디오에서 모든 무음 구간 감지

    FFmpeg silencedetect 필터를 사용하여 오디오 전체의 무음 구간을 감지합니다.

    Args:
        audio_path: 오디오 파일 경로
        threshold_db: 무음 판정 임계값 (dB, 기본값 -40dB)
        min_silence_duration: 최소 무음 지속시간 (초, 기본값 0.5초)

    Returns:
        무음 구간 리스트: [{"start": float, "end": float, "duration": float}, ...]
        감지 실패 시 빈 리스트 반환
    '''
    pass
# WARNING: Decompyle incomplete


def trim_trailing_silence(audio_path = None, output_path = None, max_silence = None, threshold_db = (0.2, -25)):
    '''
    오디오 끝부분 무음 트리밍

    끝부분의 무음 구간을 max_silence 이하로 줄입니다.
    예: 원본이 0.5초 무음이고 max_silence가 0.2초면, 0.3초를 잘라냅니다.

    Args:
        audio_path: 입력 오디오 파일 경로
        output_path: 출력 오디오 파일 경로
        max_silence: 최대 허용 무음 길이 (초, 기본값 0.2초)
        threshold_db: 무음 판정 임계값 (dB, 기본값 -40dB)

    Returns:
        (출력 파일 경로, 줄인 시간) 튜플
        트리밍이 필요 없거나 실패하면 (audio_path, 0.0) 반환
    '''
    pass
# WARNING: Decompyle incomplete


def detect_leading_silence(audio_path = None, threshold_db = None, min_silence_duration = None):
    '''
    오디오 앞부분의 무음 길이 감지

    Args:
        audio_path: 오디오 파일 경로
        threshold_db: 무음 판정 임계값 (dB, 기본값 -40dB)
        min_silence_duration: 최소 무음 지속시간 (초, 기본값 0.05초)

    Returns:
        앞부분 무음 길이 (초), 무음이 없으면 0.0
    '''
    pass
# WARNING: Decompyle incomplete


def trim_both_silence(audio_path = None, output_path = None, max_silence = None, threshold_db = (0.1, -25)):
    '''
    오디오 앞뒤 무음 트리밍

    앞부분과 끝부분의 무음 구간을 max_silence 이하로 줄입니다.

    Args:
        audio_path: 입력 오디오 파일 경로
        output_path: 출력 오디오 파일 경로
        max_silence: 최대 허용 무음 길이 (초, 기본값 0.1초)
        threshold_db: 무음 판정 임계값 (dB, 기본값 -40dB)

    Returns:
        (출력 파일 경로, 앞부분 트리밍량, 끝부분 트리밍량) 튜플
    '''
    pass
# WARNING: Decompyle incomplete


def trim_by_timepoints(audio_path = None, output_path = None, first_word_start = None, last_word_end = (0.1,), max_silence = ('audio_path', str, 'output_path', str, 'first_word_start', float, 'last_word_end', float, 'max_silence', float, 'return', Tuple[(str, float, float)])):
    '''
    강제 트리밍 테스트

    앞부분: 0.1초 강제 트리밍
    뒷부분: 0.2초 강제 트리밍

    Args:
        audio_path: 입력 오디오 파일 경로
        output_path: 출력 오디오 파일 경로
        first_word_start: 첫 단어 시작 시간 (초) - 사용 안함
        last_word_end: 마지막 단어 종료 시간 (초) - 사용 안함
        max_silence: 최대 허용 무음 길이 (초) - 사용 안함

    Returns:
        (출력 파일 경로, 앞부분 트리밍량, 끝부분 트리밍량) 튜플
    '''
    pass
# WARNING: Decompyle incomplete


def should_trim_silence(current_text = None, next_text = None):
    '''
    무음 트리밍 여부 판단

    현재 세그먼트가 문장부호로 끝나면 완전한 문장이므로 무음 유지.
    문장부호로 끝나지 않으면 다음 문장과 자연스럽게 이어져야 하므로 무음 줄임.

    예:
    - "시작되었습니다." → 마침표로 끝남 → 무음 유지 (False)
    - "시작되었습니다. 믿기" → "믿기"로 끝남 → 무음 줄임 (True)
    - "홋카이도의 아름다운" → 문장부호 없음 → 무음 줄임 (True)

    Args:
        current_text: 현재 세그먼트 텍스트
        next_text: 다음 세그먼트 텍스트

    Returns:
        트리밍해야 하면 True, 아니면 False
    '''
    if not current_text:
        return False
    current_text_stripped = None.strip()
    if not current_text_stripped:
        return False
    last_char = None[-1]
    punctuation_chars = '.?!。？！'
    if last_char in punctuation_chars:
        logger.debug(f'''[should_trim_silence] No trim: ends with \'{last_char}\'''')
        return False
    None.debug(f'''[should_trim_silence] Trim needed: ends with \'{last_char}\'''')
    return True
