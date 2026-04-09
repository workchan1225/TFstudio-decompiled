# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_length_calculator.pyc (Python 3.11)

'''
대본 길이 계산 유틸리티

시간 기반 대본 길이 선택 및 챕터 분배를 위한 함수들.
Gemini 2.5 Pro의 토큰 제한(32,000 출력 토큰)을 고려한 안전 상한선 적용.

기준:
- 한글 나레이션 평균 속도: 분당 700자 (TTS 1.0x 속도)
- 최대 출력: 40,000자 (토큰 안전 마진 적용)
'''
from typing import Dict, Tuple, List, Optional
from dataclasses import dataclass
CHARS_PER_MINUTE = 700
MAX_CHARS = 40000
MIN_CHARS = 1000
SLIDER_STEP = 1000
ScriptLengthPreset = <NODE:12>()
TIME_PRESETS: List[ScriptLengthPreset] = [
    ScriptLengthPreset(label = '10분', minutes = 10, chars = 7000),
    ScriptLengthPreset(label = '20분', minutes = 20, chars = 14000),
    ScriptLengthPreset(label = '40분', minutes = 40, chars = 28000),
    ScriptLengthPreset(label = '1시간', minutes = 60, chars = 40000)]

def minutes_to_chars(minutes = None):
    '''
    영상 시간(분)을 예상 글자수로 변환

    Args:
        minutes: 영상 시간 (분)

    Returns:
        예상 글자수 (최대 40,000자)
    '''
    chars = minutes * CHARS_PER_MINUTE
    return min(chars, MAX_CHARS)


def chars_to_minutes(chars = None):
    '''
    글자수를 예상 영상 시간(분)으로 변환

    Args:
        chars: 글자수

    Returns:
        예상 영상 시간 (분, 소수점 1자리)
    '''
    return round(chars / CHARS_PER_MINUTE, 1)


def get_chars_per_chapter(total_chars = None, chapter_count = None):
    '''
    챕터당 글자수 계산

    Args:
        total_chars: 총 글자수
        chapter_count: 챕터 수 (5~8)

    Returns:
        챕터당 글자수
    '''
    if chapter_count < 5 or chapter_count > 8:
        raise ValueError(f'''챕터 수는 5~8 사이여야 합니다: {chapter_count}''')
    return total_chars // chapter_count


def validate_script_length(chars = None):
    '''
    대본 길이 유효성 검증

    Args:
        chars: 글자수

    Returns:
        (유효 여부, 오류 메시지)
    '''
    if chars < MIN_CHARS:
        return (False, f'''최소 {MIN_CHARS:,}자 이상이어야 합니다.''')
    if None > MAX_CHARS:
        return (False, f'''최대 {MAX_CHARS:,}자를 초과할 수 없습니다. (Gemini 토큰 제한)''')


def snap_to_slider_step(chars = None):
    '''
    슬라이더 스텝(1000자)에 맞게 반올림

    Args:
        chars: 글자수

    Returns:
        1000 단위로 반올림된 글자수
    '''
    snapped = round(chars / SLIDER_STEP) * SLIDER_STEP
    return max(MIN_CHARS, min(snapped, MAX_CHARS))


def get_recommended_chapter_count(chars = None):
    '''
    글자수에 따른 권장 챕터 수

    Args:
        chars: 글자수

    Returns:
        권장 챕터 수 (5~8)
    '''
    if chars <= 7000:
        return 5
    if None <= 14000:
        return 6
    if None <= 28000:
        return 7


def get_length_info(chars = None, chapter_count = None):
    '''
    대본 길이에 대한 종합 정보 반환

    Args:
        chars: 총 글자수
        chapter_count: 챕터 수

    Returns:
        {
            "total_chars": 총 글자수,
            "estimated_minutes": 예상 시간(분),
            "chapter_count": 챕터 수,
            "chars_per_chapter": 챕터당 글자수,
            "display_time": 표시용 시간 문자열,
            "is_valid": 유효 여부,
            "error": 오류 메시지
        }
    '''
    (is_valid, error) = validate_script_length(chars)
    estimated_minutes = chars_to_minutes(chars)
    if estimated_minutes >= 60:
        hours = int(estimated_minutes // 60)
        mins = int(estimated_minutes % 60)
        display_time = f'''{hours}시간''' if mins == 0 else f'''{hours}시간 {mins}분'''
    else:
        display_time = f'''약 {int(estimated_minutes)}분'''
    return {
        'total_chars': chars,
        'estimated_minutes': estimated_minutes,
        'chapter_count': chapter_count,
        'chars_per_chapter': get_chars_per_chapter(chars, chapter_count) if is_valid else 0,
        'display_time': display_time,
        'is_valid': is_valid,
        'error': error }


def get_presets_for_api():
    '''
    API 응답용 프리셋 목록 반환

    Returns:
        프리셋 목록 (딕셔너리 형태)
    '''
    return TIME_PRESETS()
