# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tts_sync_service.pyc (Python 3.11)

'''
TTS 오디오 → SRT 동기화 서비스

Gemini TTS 2.5 등 타임포인트를 제공하지 않는 TTS 엔진에서
대량 생성된 오디오를 스크립트 라인과 동기화합니다.

핵심 전략:
- FFmpeg silencedetect 기반 무음 구간 탐지
- 무음 경계를 라인 분할점으로 활용
- 라인 수와 무음 수 불일치 시 비율 기반 보정

torch 의존성 없이 FFmpeg만으로 동작합니다.
'''
import logging
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from app.utils.audio_silence_utils import detect_all_silence_regions, get_audio_duration
logger = logging.getLogger(__name__)
SubtitleSegment = <NODE:12>()
QualityReport = <NODE:12>()
TTSSyncResult = <NODE:12>()

class TTSSyncService:
    '''
    FFmpeg silencedetect 기반 TTS 오디오 → SRT 동기화 서비스

    주요 기능:
    - 무음 구간 탐지하여 자연스러운 분할점 결정
    - 스크립트 라인과 오디오 구간 매칭
    - 신뢰도 계산 및 품질 리포트 생성
    '''
    DEFAULT_SILENCE_THRESHOLD_DB = -38
    DEFAULT_MIN_SILENCE_DURATION = 0.12
    DEFAULT_MIN_SEGMENT_DURATION = 0.35
    DEFAULT_MAX_SEGMENT_DURATION = 6
    DEFAULT_MAX_SEGMENT_CHARS = 40
    ORPHAN_MAX_CHARS = 10
    ORPHAN_MAX_WORDS = 2
    ORPHAN_MAX_DURATION = 0.95
    ORPHAN_MAX_GAP = 0.12
    DEFAULT_END_PADDING = 0.15
    SEGMENT_OVERLAP = 0.5
    SILENCE_SNAP_DISTANCE = 1.2
    MAX_EARLY_SNAP_SHIFT = 0.18
    MIN_LAST_SEGMENT_DURATION = 1
    SPLIT_POINT_DELAY = 0
    SENTENCE_END_PUNCTUATION = '.?!。？！'
    CLAUSE_PUNCTUATION = ',;:，；：'
    LOW_CONFIDENCE_THRESHOLD = 0.6
    HIGH_CONFIDENCE_THRESHOLD = 0.85
    
    def __init__(self):
        self._logger = logging.getLogger(f'''{__name__}.{self.__class__.__name__}''')

    
    def sync_audio_to_script(self, audio_path, script_lines, language, silence_threshold_db, min_silence_duration = None, min_segment_duration = None, end_padding = None, max_segment_duration = ('ko', None, None, None, None, None, None), max_segment_chars = ('audio_path', str, 'script_lines', List[str], 'language', str, 'silence_threshold_db', Optional[float], 'min_silence_duration', Optional[float], 'min_segment_duration', Optional[float], 'end_padding', Optional[float], 'max_segment_duration', Optional[float], 'max_segment_chars', Optional[int], 'return', TTSSyncResult)):
        '''
        오디오를 스크립트 라인과 동기화

        Args:
            audio_path: 오디오 파일 경로
            script_lines: 스크립트 라인 리스트 (줄바꿈 단위)
            language: 언어 코드 (ko, en, ja 등)
            silence_threshold_db: 무음 판정 임계값 (dB)
            min_silence_duration: 최소 무음 지속시간 (초)
            min_segment_duration: 최소 세그먼트 길이 (초)
            end_padding: 마지막 세그먼트 패딩 (초)
            max_segment_duration: 긴 세그먼트 분할 임계 길이 (초, 0 이하면 분할 비활성화)
            max_segment_chars: 긴 세그먼트 분할 임계 글자수 (0 이하면 분할 비활성화)

        Returns:
            TTSSyncResult: 동기화 결과
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _find_split_points_from_silence(self = None, silence_regions = None, audio_duration = None, num_lines = (None,), script_lines = ('silence_regions', List[Dict], 'audio_duration', float, 'num_lines', int, 'script_lines', Optional[List[str]], 'return', List[float])):
        '''
        글자수 비율 기반 분할점 + 무음 스냅

        전략:
        1. 글자수 비율로 이상적인 분할점 계산 (기본)
        2. 각 분할점 근처에 무음이 있으면 무음으로 스냅 (보조)
        3. 무음 스냅 시 무음 구간의 중간점 사용 (자연스러운 전환)

        Args:
            silence_regions: 무음 구간 리스트
            audio_duration: 오디오 전체 길이
            num_lines: 스크립트 라인 수
            script_lines: 스크립트 라인 리스트

        Returns:
            분할점 리스트 (초)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _uniform_split_points(self = None, audio_duration = None, num_lines = None):
        '''균등 분할점 생성'''
        pass
    # WARNING: Decompyle incomplete

    
    def _select_best_split_points(self = None, silence_endpoints = None, needed_splits = None, audio_duration = ('silence_endpoints', List[float], 'needed_splits', int, 'audio_duration', float, 'return', List[float])):
        '''
        충분한 무음 중에서 최적 분할점 선택

        전략: 균등 분할 지점에 가장 가까운 무음 선택
        '''
        if needed_splits <= 0:
            return []
        ideal_splits = None._uniform_split_points(audio_duration, needed_splits + 1)
        selected = []
        used_indices = set()
        for ideal in ideal_splits:
            best_idx = -1
            best_distance = float('inf')
            for idx, midpoint in enumerate(silence_endpoints):
                if idx in used_indices:
                    continue
                distance = abs(midpoint - ideal)
                if distance < best_distance:
                    best_distance = distance
                    best_idx = idx
                if best_idx >= 0:
                    selected.append(silence_endpoints[best_idx])
                    used_indices.add(best_idx)
            selected = sorted(set(selected))
            return selected[:needed_splits]

    
    def _interpolate_split_points(self = None, silence_endpoints = None, needed_splits = None, audio_duration = ('silence_endpoints', List[float], 'needed_splits', int, 'audio_duration', float, 'return', List[float])):
        '''
        무음이 부족할 때 보간하여 분할점 생성

        전략:
        1. 기존 무음 위치 유지
        2. 긴 구간은 균등 분할로 추가 분할점 생성
        '''
        if not silence_endpoints:
            return self._uniform_split_points(audio_duration, needed_splits + 1)
        all_points = None([
            0] + silence_endpoints + [
            audio_duration])
        additional_needed = needed_splits - len(silence_endpoints)
        if additional_needed <= 0:
            return silence_endpoints[:needed_splits]
        intervals = None
        for i in range(len(all_points) - 1):
            intervals.append({
                'start': all_points[i],
                'end': all_points[i + 1],
                'duration': all_points[i + 1] - all_points[i] })
            intervals.sort(key = (lambda x: x['duration']), reverse = True)
            new_splits = list(silence_endpoints)
            for interval in intervals:
                if additional_needed <= 0:
                    pass
                else:
                    avg_duration = audio_duration / (needed_splits + 1)
                    splits_for_interval = int(interval['duration'] / avg_duration)
                    if splits_for_interval > 1:
                        segment_len = interval['duration'] / splits_for_interval
                        for j in range(1, splits_for_interval):
                            if additional_needed <= 0:
                                pass
                            else:
                                new_point = interval['start'] + segment_len * j
                                new_splits.append(new_point)
                                additional_needed -= 1
                            return sorted(new_splits)[:needed_splits]

    
    def _char_weighted_split_points(self = None, script_lines = None, audio_duration = None):
