# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: retry_policy.pyc (Python 3.11)

import os
from typing import Any, Dict
DEFAULT_PRO_TIMEOUT_SECONDS = 250
DEFAULT_NANOBANANA2_TIMEOUT_SECONDS = 250
DEFAULT_STANDARD_TIMEOUT_SECONDS = 70

def _read_positive_int_env(name = None, default = None):
    raw_value = os.getenv(name)
# WARNING: Decompyle incomplete


def get_scene_retry_policy(engine = None):
    '''엔진별 이미지 생성 재시도 정책 반환.

    max_retries=2: 최초 1회 + 재시도 1회 = 총 2회 시도
    - 일시적 네트워크 오류, 타임아웃, 503 서비스 불가 시 1회 재시도
    - 정책 위반(policy_violation)은 재시도하지 않음
    - retry는 스타일/상호작용/시선의 핵심 의미를 유지하고 카메라/디테일 축만 변형해야 함
    '''
    return {
        'max_retries': 2,
        'base_wait': 2,
        'service_unavailable_base_wait': 5,
        'preserve_axes': [
            'style_mode',
            'character_render_mode',
            'background_render_mode',
            'scene_semantics',
            'interaction_plan',
            'gaze_targets',
            'subject_count'],
        'variation_axes': [
            'camera_geometry',
            'action_beat',
            'detail_focus',
            'lighting_placement'] }


def get_scene_request_timeout_seconds(engine = None):
