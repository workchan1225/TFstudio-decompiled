# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: zoom_motion_config.pyc (Python 3.11)

'''
줌/모션 효과 중앙 설정

세그먼트 길이별 자동 조절 파라미터 및 떨림 방지 임계값 관리.
모든 줌 관련 상수는 이 모듈에서 중앙 관리.
'''
ZOOM_MIN = 1
ZOOM_MAX_ALLOWED = 1.5
DURATION_ZOOM_MAP = [
    (2, 1.08),
    (5, 1.15),
    (10, 1.25),
    (30, 1.35),
    (60, 1.5)]
LONG_SEGMENT_THRESHOLD = 60
LONG_SEGMENT_ZOOM_DURATION = 30
LONG_SEGMENT_ZOOM_END = 1.5
MIN_ZOOM_CHANGE_PER_SECOND = 0.01
MAX_ZOOM_CHANGE_PER_SECOND = 0.15

def get_optimal_zoom_end(duration = None, user_zoom_end = None):
    '''
    세그먼트 길이에 따른 최적 zoomEnd 계산.

    짧은 세그먼트에서는 작은 줌 변화로 떨림을 방지하고,
    긴 세그먼트에서는 더 큰 줌 변화를 허용.

    Args:
        duration: 세그먼트 길이 (초)
        user_zoom_end: 사용자 지정 zoomEnd (기본 1.3)

    Returns:
        조절된 zoomEnd (떨림 방지 적용)
    '''
    target_zoom = min(user_zoom_end, ZOOM_MAX_ALLOWED)
    if duration >= LONG_SEGMENT_THRESHOLD:
        return LONG_SEGMENT_ZOOM_END
    allowed_zoom = None
    for max_dur, zoom_end in DURATION_ZOOM_MAP:
        if duration <= max_dur:
            allowed_zoom = zoom_end
        
        allowed_zoom = DURATION_ZOOM_MAP[-1][1]
        return min(target_zoom, allowed_zoom)


def calculate_zoom_for_long_segment(duration = None):
    """
    60초 이상 세그먼트의 줌 설정 계산.

    긴 세그먼트에서는 30초간 줌 효과 후 나머지는 정지 상태 유지.

    Args:
        duration: 세그먼트 길이 (초)

    Returns:
        dict: {
            'zoom_duration': 실제 줌 효과 지속 시간,
            'zoom_end': 최종 줌 레벨,
            'hold_duration': 줌 정지 유지 시간,
            'is_long_segment': 긴 세그먼트 여부
        }
    """
    if duration < LONG_SEGMENT_THRESHOLD:
        return {
            'zoom_duration': duration,
            'zoom_end': get_optimal_zoom_end(duration),
            'hold_duration': 0,
            'is_long_segment': False }
    return {
        'zoom_duration': None,
        'zoom_end': LONG_SEGMENT_ZOOM_END,
        'hold_duration': duration - LONG_SEGMENT_ZOOM_DURATION,
        'is_long_segment': True }


def validate_zoom_speed(zoom_start = None, zoom_end = None, duration = None):
    '''
    줌 속도 검증 및 zoomEnd 자동 조절.

    초당 줌 변화량이 MAX_ZOOM_CHANGE_PER_SECOND를 초과하면
    zoomEnd를 자동으로 축소하여 떨림 방지.

    Args:
        zoom_start: 시작 줌 레벨
        zoom_end: 목표 줌 레벨
        duration: 세그먼트 길이 (초)

    Returns:
        조절된 zoomEnd (속도 제한 적용)
    '''
    zoom_change = abs(zoom_end - zoom_start)
    speed = zoom_change / max(duration, 0.1)
    if speed > MAX_ZOOM_CHANGE_PER_SECOND:
        max_change = MAX_ZOOM_CHANGE_PER_SECOND * duration
        if zoom_end > zoom_start:
            return zoom_start + max_change
        return None - max_change


def get_adjusted_zoom_params(duration = None, user_zoom_start = None, user_zoom_end = None, is_zoom_out = (1, 1.3, False)):
    """
    최종 줌 파라미터 계산 (모든 조절 적용).

    세그먼트 길이 기반 최적 줌 + 속도 검증 + 긴 세그먼트 처리를 통합.

    Args:
        duration: 세그먼트 길이 (초)
        user_zoom_start: 사용자 지정 시작 줌
        user_zoom_end: 사용자 지정 종료 줌
        is_zoom_out: zoom_out 효과 여부 (True면 시작이 더 큼)

    Returns:
        dict: {
            'zoom_start': 최종 시작 줌,
            'zoom_end': 최종 종료 줌,
            'zoom_duration': 줌 효과 지속 시간,
            'hold_duration': 정지 유지 시간,
            'is_long_segment': 긴 세그먼트 여부
        }
    """
    optimal_zoom_end = get_optimal_zoom_end(duration, user_zoom_end)
    validated_zoom_end = validate_zoom_speed(user_zoom_start, optimal_zoom_end, duration)
    long_config = calculate_zoom_for_long_segment(duration)
    if is_zoom_out:
        final_start = max(validated_zoom_end, user_zoom_start)
        final_end = min(validated_zoom_end, user_zoom_start)
        final_end = max(final_end, ZOOM_MIN)
    else:
        final_start = user_zoom_start
        final_end = validated_zoom_end
    return {
        'zoom_start': final_start,
        'zoom_end': final_end,
        'zoom_duration': long_config['zoom_duration'],
        'hold_duration': long_config['hold_duration'],
        'is_long_segment': long_config['is_long_segment'] }
