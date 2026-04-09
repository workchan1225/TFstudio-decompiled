# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: creative_modes.pyc (Python 3.11)

'''
창작 모드 시스템

대본 생성 시 창작 자유도를 조절하는 3가지 모드를 제공합니다:
- STRICT: 규칙 엄격 준수 (초보자, 일관성 중요할 때)
- BALANCED: 균형 모드 (기본값, 권장)
- CREATIVE: 자유로운 창작 (경험자, 실험적 콘텐츠)
'''
from enum import Enum
from typing import Dict
from dataclasses import dataclass

class CreativeMode(Enum):
    '''창작 모드'''
    STRICT = 'strict'
    BALANCED = 'balanced'
    CREATIVE = 'creative'

CreativeModeConfig = <NODE:12>()
CREATIVE_MODE_CONFIGS: Dict[(CreativeMode, CreativeModeConfig)] = {
    CreativeMode.CREATIVE: CreativeModeConfig(mode = CreativeMode.CREATIVE, name = 'Creative', korean_name = '자유 창작', description = '핵심 원칙만 유지하고 창의적으로 구성. 경험자나 실험적 콘텐츠에 권장.', hooking_flexibility = '자유 - 더 효과적인 방법이 있다면 자유롭게 선택', structure_flexibility = '자유 - 핵심 감정선만 유지, 창의적 구성', dialogue_freedom = '자유 - 캐릭터 성장과 변화 허용', experimental_allowed = True),
    CreativeMode.BALANCED: CreativeModeConfig(mode = CreativeMode.BALANCED, name = 'Balanced', korean_name = '균형', description = '규칙을 참고하되 자연스럽게 변형 가능. 대부분의 경우 권장.', hooking_flexibility = '권장 - 제안된 기법 중 시놉시스에 맞는 것 선택', structure_flexibility = '권장 - 스토리 서클 참고하되 유연하게 적용', dialogue_freedom = '보통 - 캐릭터 특성 내에서 자유롭게 표현', experimental_allowed = True),
    CreativeMode.STRICT: CreativeModeConfig(mode = CreativeMode.STRICT, name = 'Strict', korean_name = '규칙 준수', description = '모든 규칙을 엄격하게 준수합니다. 일관성이 중요하거나 초보자에게 권장.', hooking_flexibility = '필수 - 반드시 지정된 후킹 기법 사용', structure_flexibility = '필수 - 기승전결/스토리 서클 엄격 준수', dialogue_freedom = '제한 - 캐릭터 프로필에서 벗어나지 않음', experimental_allowed = False) }

def build_creative_mode_instruction(mode = None):
    """
    창작 모드에 따른 프롬프트 지침 생성

    Args:
        mode: 창작 모드 ('strict', 'balanced', 'creative')

    Returns:
        창작 모드 지침 문자열
    """
    mode = mode.lower() if isinstance(mode, str) else 'balanced'
    if mode == 'strict':
        return _build_strict_instruction()
    if None == 'creative':
        return _build_creative_instruction()
    return None()


def _build_strict_instruction():
    '''STRICT 모드 지침'''
    return '\n## 창작 모드: STRICT (규칙 준수)\n\n모든 지침을 **엄격하게** 따라야 합니다:\n\n### 후킹\n- 반드시 위에서 제시한 In Medias Res 구조와 후킹 기법을 **그대로** 사용하세요\n- 첫 번째 챕터의 티저-전환-본편 구조를 **정확히** 따르세요\n- 예시로 제공된 형식을 벗어나지 마세요\n\n### 구조\n- 기승전결/스토리 서클 구조를 **엄격히** 준수하세요\n- 각 챕터의 역할(기/승/전/결)을 명확히 구분하세요\n- 챕터 수를 정확히 맞추세요\n\n### 캐릭터 & 대사\n- 정의된 캐릭터 프로필에서 **절대** 벗어나지 마세요\n- 새로운 캐릭터를 임의로 추가하지 마세요\n- 대사 스타일을 일관되게 유지하세요\n\n### 금지 사항\n- 실험적 표현 금지\n- 예상치 못한 톤 변화 금지\n- 구조 변형 금지\n'


def _build_balanced_instruction():
    '''BALANCED 모드 지침'''
    return '\n## 창작 모드: BALANCED (균형) - 권장\n\n규칙을 참고하되 자연스럽게 적용하세요:\n\n### 후킹\n- 제안된 In Medias Res 기법 중 **시놉시스에 가장 맞는 것**을 선택하세요\n- 티저-전환-본편 구조를 참고하되, 이야기 흐름에 맞게 조절 가능\n- 핵심은 "첫 3초에 시청자 사로잡기"입니다\n\n### 구조\n- 스토리 서클을 참고하되 **유연하게** 적용하세요\n- 감정 흐름이 자연스럽다면 약간의 변형 허용\n- 핵심 기승전결 흐름만 유지하세요\n\n### 캐릭터 & 대사\n- 캐릭터 특성 내에서 자유롭게 표현하세요\n- 대화가 자연스럽다면 약간의 성격 변화 허용\n- 캐릭터 간 케미를 살려주세요\n\n### 허용 사항\n- 시놉시스에 맞는 창의적 해석\n- 더 효과적인 전환 문구 사용\n- 감정선에 맞는 속도 조절\n'


def _build_creative_instruction():
    '''CREATIVE 모드 지침'''
    return '\n## 창작 모드: CREATIVE (자유 창작)\n\n핵심 원칙만 지키고 **창의적으로** 작성하세요:\n\n### 후킹\n- 제안된 기법은 **참고**용입니다\n- 이 이야기에 더 효과적인 시작 방식이 있다면 자유롭게 사용하세요\n- 목표: 첫 3초에 시청자가 스크롤을 멈추게 하는 것\n\n### 구조\n- 핵심 감정선(기대-갈등-해소)만 유지하세요\n- 챕터 구성, 속도, 전환은 **자유롭게** 설계하세요\n- 실험적인 구조도 환영합니다 (예: 역순 전개, 병렬 스토리)\n\n### 캐릭터 & 대사\n- 캐릭터가 성장하고 변화하는 모습을 보여주세요\n- 예상치 못한 캐릭터 반응도 허용됩니다\n- 대사에 개성과 깊이를 더하세요\n\n### 권장 사항\n- 클리셰를 피하고 신선한 접근을 시도하세요\n- 감정적 임팩트를 극대화하세요\n- 시청자를 놀라게 하세요\n\n### 유일한 제약\n- 시청자 이탈 방지 원칙만 지키세요\n- TTS 호환성 규칙(나레이션 200자, 괄호 지문 금지)은 유지\n'


def get_creative_mode_config(mode = None):
    """
    창작 모드 설정 반환

    Args:
        mode: 모드 문자열 ('strict', 'balanced', 'creative')

    Returns:
        CreativeModeConfig 객체
    """
    mode = mode.lower() if isinstance(mode, str) else 'balanced'
    mode_enum = {
        'strict': CreativeMode.STRICT,
        'balanced': CreativeMode.BALANCED,
        'creative': CreativeMode.CREATIVE }.get(mode, CreativeMode.BALANCED)
    return CREATIVE_MODE_CONFIGS[mode_enum]


def is_experimental_allowed(mode = None):
    '''
    실험적 표현 허용 여부 확인

    Args:
        mode: 모드 문자열

    Returns:
        허용 여부
    '''
    config = get_creative_mode_config(mode)
    return config.experimental_allowed


def get_mode_description(mode = None):
    '''
    창작 모드 설명 반환 (UI 표시용)

    Args:
        mode: 모드 문자열

    Returns:
        설명 문자열
    '''
    config = get_creative_mode_config(mode)
    return f'''{config.korean_name}: {config.description}'''


def get_all_modes_for_ui():
    '''
    UI 드롭다운용 모든 모드 정보 반환

    Returns:
        [{value, label, description}, ...] 형식의 리스트
    '''
    return [
        {
            'value': 'strict',
            'label': 'Strict (규칙 준수)',
            'description': '모든 규칙을 엄격하게 준수합니다' },
        {
            'value': 'balanced',
            'label': 'Balanced (균형) - 권장',
            'description': '규칙을 참고하되 자연스럽게 변형 가능' },
        {
            'value': 'creative',
            'label': 'Creative (자유 창작)',
            'description': '핵심 원칙만 유지하고 창의적으로 구성' }]
