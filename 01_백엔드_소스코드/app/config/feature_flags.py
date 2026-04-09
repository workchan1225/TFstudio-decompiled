# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: feature_flags.pyc (Python 3.11)

"""
Feature Flags - 기능 토글 시스템

새 기능의 점진적 롤아웃 및 롤백을 위한 플래그 관리.
환경변수 또는 런타임 설정으로 제어 가능.

사용법:
    from app.config.feature_flags import FeatureFlags

    if FeatureFlags.is_enabled('TONE_DAMPENING'):
        # 톤 완화 로직 적용
"""
import os
from typing import Dict, Optional
from dataclasses import dataclass, field
from datetime import datetime
FeatureFlag = <NODE:12>()

class FeatureFlags:
    '''
    Feature Flag 관리자

    환경변수로 오버라이드 가능:
        FEATURE_FLAG_TONE_DAMPENING=0  # 비활성화
        FEATURE_FLAG_TONE_DAMPENING=1  # 활성화
    '''
    FLAGS: Dict[(str, FeatureFlag)] = {
        'TONE_DAMPENING': FeatureFlag(name = 'TONE_DAMPENING', description = 'AI 대본 과장/형용사 완화 기능', default_enabled = True, metadata = {
            'version': '1.0.0',
            'owner': 'script-team' }),
        'TONE_DAMPENING_POST_PROCESS': FeatureFlag(name = 'TONE_DAMPENING_POST_PROCESS', description = '출력 후 정규화 레이어 (실험적)', default_enabled = False, metadata = {
            'version': '1.0.0',
            'experimental': True }),
        'TONE_DAMPENING_METRICS': FeatureFlag(name = 'TONE_DAMPENING_METRICS', description = '톤 완화 지표 수집', default_enabled = True),
        'SHORTS_V2_ENABLED': FeatureFlag(name = 'SHORTS_V2_ENABLED', description = 'Shorts V2 문장 기반 쇼츠 생성 기능', default_enabled = True, metadata = {
            'version': '2.0.0',
            'owner': 'shorts-team' }),
        'SCRAPLING_ENABLED': FeatureFlag(name = 'SCRAPLING_ENABLED', description = 'Scrapling 기반 웹 수집 기능 활성화', default_enabled = False, metadata = {
            'version': '0.4.1',
            'owner': 'platform-team',
            'risk': 'tos_and_antibot_review_required' }) }
    _runtime_overrides: Dict[(str, bool)] = { }
    is_enabled = (lambda cls = None, flag_name = None: env_key = f'''FEATURE_FLAG_{flag_name}'''env_value = os.environ.get(env_key)# WARNING: Decompyle incomplete
)()
    get_flag = (lambda cls = None, flag_name = None: cls.FLAGS.get(flag_name))()
    set_enabled = (lambda cls = None, flag_name = None, enabled = classmethod: cls._runtime_overrides[flag_name] = enabled)()
    reset_overrides = (lambda cls: cls._runtime_overrides.clear())()
    get_all_flags = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
