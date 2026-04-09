# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tone_dampening_enforcer.pyc (Python 3.11)

"""
ToneDampeningEnforcer - AI 대본 과장/형용사 완화 시스템

장르별로 적절한 완화 레벨을 적용하여 AI 대본의 과장된 표현을 제어.
기존 ToneEnforcer와 함께 사용 가능.

사용법:
    from app.services.prompt.constraints.tone_dampening_enforcer import ToneDampeningEnforcer

    enforcer = ToneDampeningEnforcer()
    prompt = enforcer.build_dampening_prompt('LIFE_KNOWLEDGE')
    temperature = enforcer.get_temperature_override('LIFE_KNOWLEDGE', 0.9)
"""
import re
from typing import Dict, List, Optional
from dataclasses import dataclass
from app.utils.tone_dampening_config import DampeningLevel, DampeningLevelConfig, get_dampening_level, get_level_config, get_temperature_for_genre
from app.config.feature_flags import FeatureFlags
DampeningResult = <NODE:12>()

class ToneDampeningEnforcer:
    '''
    톤 완화 Enforcer

    AI 대본 생성 시 과장된 표현을 완화하는 규칙을 적용합니다.
    장르에 따라 자동으로 적절한 완화 레벨을 적용합니다.
    '''
    
    def __init__(self):
        self._cache = { }

    
    def get_config_for_genre(self = None, genre = None):
        '''
        장르에 맞는 설정 반환 (캐싱)

        Args:
            genre: 장르 코드

        Returns:
            DampeningLevelConfig
        '''
        if genre not in self._cache:
            level = get_dampening_level(genre)
            self._cache[genre] = get_level_config(level)
        return self._cache[genre]

    
    def build_dampening_prompt(self = None, genre = None, override_level = None):
        """
        완화 지침 프롬프트 생성

        Args:
            genre: 장르 코드
            override_level: 수동 레벨 지정 ('none', 'minimal', 'moderate', 'strong')

        Returns:
            AI에게 전달할 완화 지침 프롬프트 (빈 문자열 = 완화 없음)
        """
        if not FeatureFlags.is_enabled('TONE_DAMPENING'):
            return ''
        if None:
            
            try:
                level = DampeningLevel(override_level)
            except ValueError:
                level = get_dampening_level(genre)
            except:
                level = get_dampening_level(genre)

            if level == DampeningLevel.NONE:
                return ''
            config = None(level)
            return config.prompt_instruction

    
    def get_temperature_override(self = None, genre = None, base_temperature = None):
        '''
        장르에 맞는 temperature 반환

        Args:
            genre: 장르 코드
            base_temperature: 기본 temperature

        Returns:
            조정된 temperature
        '''
        if not FeatureFlags.is_enabled('TONE_DAMPENING'):
            return base_temperature
        return None(genre, base_temperature)

    
    def normalize_output(self = None, text = None, genre = None, override_level = (None,)):
        '''
        출력 후 정규화 (선택적 후처리)

        이 기능은 TONE_DAMPENING_POST_PROCESS 플래그가 활성화된 경우에만 동작합니다.

        Args:
            text: 생성된 대본 텍스트
            genre: 장르 코드
            override_level: 수동 레벨 지정

        Returns:
            DampeningResult - 처리 결과
        '''
        if not FeatureFlags.is_enabled('TONE_DAMPENING_POST_PROCESS'):
            return DampeningResult(original_text = text, processed_text = text, changes_made = 0, patterns_found = [], level_applied = DampeningLevel.NONE)
        if None:
            
            try:
                level = DampeningLevel(override_level)
            except ValueError:
                level = get_dampening_level(genre)
            except:
                level = get_dampening_level(genre)

            if level == DampeningLevel.NONE:
                return DampeningResult(original_text = text, processed_text = text, changes_made = 0, patterns_found = [], level_applied = level)
            config = None(level)
            processed_text = text
            changes = 0
            found_patterns = []
            for pattern in config.forbidden_patterns:
                if pattern in processed_text:
                    found_patterns.append(pattern)
                for old, new in config.replacement_rules.items():
                    if old in processed_text:
                        count = processed_text.count(old)
                        processed_text = processed_text.replace(old, new)
                        changes += count
                    if config.exclamation_policy == 'forbid':
                        narration_pattern = '(\\[나레이션\\]:[^!]*?)!'
                        (processed_text, sub_count) = re.subn(narration_pattern, '\\1.', processed_text)
                        changes += sub_count
                    elif config.exclamation_policy == 'reduce':
                        (processed_text, sub_count) = re.subn('!{2,}', '!', processed_text)
                        changes += sub_count
        return DampeningResult(original_text = text, processed_text = processed_text, changes_made = changes, patterns_found = found_patterns, level_applied = level)

    
    def get_dampening_level_for_genre(self = None, genre = None):
        """
        장르의 완화 레벨 문자열 반환

        Args:
            genre: 장르 코드

        Returns:
            레벨 문자열 ('none', 'minimal', 'moderate', 'strong')
        """
        level = get_dampening_level(genre)
        return level.value

    
    def get_available_levels(self = None):
        '''사용 가능한 완화 레벨 목록'''
        return DampeningLevel()

    
    def is_enabled(self = None):
        '''톤 완화 기능 활성화 여부'''
        return FeatureFlags.is_enabled('TONE_DAMPENING')

    
    def validate_dampening(self = None, text = None, genre = None):
        '''
        텍스트의 과장 표현 검증

        Args:
            text: 검증할 텍스트
            genre: 장르 코드

        Returns:
            검증 결과 딕셔너리
        '''
        level = get_dampening_level(genre)
        config = get_level_config(level)
        violations = []
        found_patterns = []
        for pattern in config.forbidden_patterns:
            count = text.count(pattern)
            if count > 0:
                found_patterns.append({
                    'pattern': pattern,
                    'count': count })
                violations.append({
                    'type': 'forbidden_pattern',
                    'pattern': pattern,
                    'count': count,
                    'message': f'''금지 패턴 발견: "{pattern}" ({count}회)''' })
            if level == DampeningLevel.STRONG:
                exclamation_count = len(re.findall('\\[나레이션\\]:[^!]*!', text))
                if exclamation_count > 0:
                    violations.append({
                        'type': 'exclamation_violation',
                        'count': exclamation_count,
                        'message': f'''나레이션에서 느낌표 사용: {exclamation_count}회''' })
        is_valid = len(violations) == 0
        return {
            'is_valid': is_valid,
            'level_applied': level.value,
            'violations': violations,
            'patterns_found': found_patterns,
            'score': max(0, 1 - len(violations) * 0.1) }
