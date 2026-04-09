# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: timestamp_validator.pyc (Python 3.11)

'''
타임스탬프 검증 및 수정 유틸리티

VAD+STT 자막 생성 시 타임스탬프 일관성을 보장합니다.

주요 기능:
- 개별 세그먼트 검증 (start < end)
- 순차 일관성 검증 (prev.end <= curr.start)
- 이상치 감지 (큰 점프, 역전)
- 3-Pass 수정 알고리즘

사용법:
    from app.utils.timestamp_validator import fix_timestamps_3pass, validate_all

    # 검증만
    result = validate_all(segments)
    if not result.is_valid:
        print(result.issues)

    # 검증 + 수정
    fixed_segments = fix_timestamps_3pass(segments, audio_duration=100.0)
'''
import logging
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum
logger = logging.getLogger(__name__)

def log_debug(msg = None):
    '''디버그 로깅'''
    print(f'''[TimestampValidator] {msg}''')
    logger.info(msg)


class IssueType(Enum):
    '''타임스탬프 문제 유형'''
    END_BEFORE_START = 'end_before_start'
    OVERLAP = 'overlap'
    LARGE_GAP = 'large_gap'
    NEGATIVE_TIME = 'negative_time'
    EXCEEDS_DURATION = 'exceeds_duration'
    ZERO_DURATION = 'zero_duration'

TimestampIssue = <NODE:12>()
ValidationResult = <NODE:12>()

def validate_segment_timing(segment = None):
    """
    개별 세그먼트 타이밍 검증

    Args:
        segment: {'start': float, 'end': float, 'text': str, ...}

    Returns:
        (is_valid, issue) - 유효하면 (True, None), 문제 있으면 (False, issue)
    """
    start = segment.get('start', 0)
    end = segment.get('end', 0)
    if start < 0:
        return (False, TimestampIssue(index = -1, issue_type = IssueType.NEGATIVE_TIME, description = f'''Negative start time: {start}''', original_start = start, original_end = end, severity = 'error'))
    if None < 0:
        return (False, TimestampIssue(index = -1, issue_type = IssueType.NEGATIVE_TIME, description = f'''Negative end time: {end}''', original_start = start, original_end = end, severity = 'error'))
    if None < start:
        return (False, TimestampIssue(index = -1, issue_type = IssueType.END_BEFORE_START, description = f'''End ({end}) before start ({start})''', original_start = start, original_end = end, severity = 'critical'))
    if None == start:
        return (False, TimestampIssue(index = -1, issue_type = IssueType.ZERO_DURATION, description = f'''Zero duration segment at {start}''', original_start = start, original_end = end, severity = 'warning'))


def validate_sequence_order(segments = None):
    '''
    순차 일관성 검증 - 세그먼트 간 순서 및 겹침 체크

    Args:
        segments: 세그먼트 리스트

    Returns:
        (is_valid, issues)
    '''
    if len(segments) < 2:
        return (True, [])
    issues = None
    for i in range(1, len(segments)):
        prev = segments[i - 1]
        curr = segments[i]
        prev_end = prev.get('end', 0)
        curr_start = curr.get('start', 0)
        if curr_start < prev_end:
            overlap_amount = prev_end - curr_start
            issues.append(TimestampIssue(index = i, issue_type = IssueType.OVERLAP, description = f'''Segment {i} overlaps with previous by {overlap_amount:.3f}s (prev_end={prev_end:.3f}, curr_start={curr_start:.3f})''', original_start = curr_start, original_end = curr.get('end', 0), severity = 'error' if overlap_amount > 1 else 'warning'))
        return (len(issues) == 0, issues)


def detect_timestamp_anomalies(segments = None, max_gap_seconds = None, audio_duration = None):
    '''
    타임스탬프 이상치 감지 - 큰 점프, 범위 초과 등

    Args:
        segments: 세그먼트 리스트
        max_gap_seconds: 최대 허용 갭 (초)
        audio_duration: 오디오 전체 길이 (선택적)

    Returns:
        발견된 이상치 리스트
    '''
    issues = []
# WARNING: Decompyle incomplete


def validate_all(segments = None, audio_duration = None, max_gap_seconds = None):
