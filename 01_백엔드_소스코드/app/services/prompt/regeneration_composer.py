# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: regeneration_composer.pyc (Python 3.11)

'''
RegenerationComposer - 재생성 전용 프롬프트 조립기

완화/재생성 시 앵커(캐릭터, 핵심 동작)를 보존하면서
변경 대상만 수정합니다.

핵심 원칙:
1. 앵커 보존: 캐릭터, 핵심 동작은 절대 변경 금지
2. 최소 변경: 위험 표현/direction만 적용
3. 일관성 검증: FidelityGate로 출력 검증
'''
import re
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field
from prompt_composer import PromptComposer, ComposedPrompt
from prompt_section import PromptSection, SectionPriority
AnchorContract = <NODE:12>()
RegenerationResult = <NODE:12>()

class RegenerationComposer(PromptComposer):
    pass
# WARNING: Decompyle incomplete


def regenerate_prompt_with_direction(original_prompt, direction, characters = dataclass, narration = dataclass, scope = None, style_template = (None, None, 'style', None, 'default'), genre = ('original_prompt', str, 'direction', str, 'characters', Optional[List[Dict]], 'narration', Optional[str], 'scope', str, 'style_template', Optional[Dict], 'genre', str, 'return', Dict)):
    """
    편의 함수: 방향 기반 프롬프트 재생성

    Args:
        original_prompt: 원본 프롬프트
        direction: 수정 방향
        characters: 캐릭터 목록
        narration: 나레이션
        scope: 변경 범위
        style_template: 스타일 템플릿
        genre: 장르

    Returns:
        Dict: {
            'promptEn': str,
            'originalPrompt': str,
            'anchorsPreserved': List[str],
            'anchorsLost': List[str],
            'consistencyScore': float,
            'isValid': bool,
            'warnings': List[str]
        }
    """
    composer = RegenerationComposer(original_prompt = original_prompt, style_template = style_template, genre = genre)
    result = composer.regenerate(direction = direction, characters = characters, narration = narration, scope = scope, preserve_anchors = True)
    return {
        'promptEn': result.prompt_en,
        'originalPrompt': result.original_prompt,
        'anchorsPreserved': result.anchors_preserved,
        'anchorsLost': result.anchors_lost,
        'consistencyScore': result.consistency_score,
        'isValid': result.is_valid,
        'warnings': result.warnings }


def validate_softened_prompt(original_prompt = None, softened_prompt = None, characters = None):
    '''
    편의 함수: 완화된 프롬프트 앵커 보존 검증

    Args:
        original_prompt: 원본 프롬프트
        softened_prompt: 완화된 프롬프트
        characters: 캐릭터 목록

    Returns:
        Dict: 검증 결과
    '''
    composer = RegenerationComposer(original_prompt = original_prompt)
    result = composer.soften_with_anchors(softened_prompt, characters)
    return {
        'isValid': result.is_valid,
        'consistencyScore': result.consistency_score,
        'anchorsPreserved': result.anchors_preserved,
        'anchorsLost': result.anchors_lost,
        'warnings': result.warnings }
