# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: whisk_prompt_optimizer.pyc (Python 3.11)

'''
Whisk 프롬프트 최적화 유틸리티 (v2 - 간소화 버전)

스킬업데이트.txt 기반 간결한 감정 중심 프롬프트 생성:
- 복잡한 설명 대신 감정/분위기 중심
- Subject 참조 형식 지원
- 짧고 명확한 스타일 태그
'''
import re
from typing import Dict, List, Optional, Tuple
NEGATIVE_PROMPT_BASE = 'Western face, Caucasian, blonde hair, blue eyes, text overlay, watermark, split screen, two-panel layout, side-by-side comparison, diptych, collage, multi-panel, 50/50 composition, divided image, left-right split, room corner dividing scene'

def generate_negative_prompt(context = None):
    """
    Negative prompt 생성 (간소화)

    Args:
        context: 'general', 'historical', 'modern'

    Returns:
        Negative prompt 문자열
    """
    base = NEGATIVE_PROMPT_BASE
    if context == 'historical':
        return f'''{base}, modern architecture, contemporary clothing'''
    if None == 'modern':
        return f'''{base}, historical costume, period clothing'''


def detect_content_type(prompt = None, narration = None):
    '''
    콘텐츠 유형 감지 (정보성 vs 드라마틱)
    '''
    pass
# WARNING: Decompyle incomplete


def add_subject_references(prompt = None, characters = None):
    '''
    Subject 참조 형식 추가

    @캐릭터이름 → Subject 1 (name), Subject 2 (name) 형식으로 변환
    '''
    if not prompt or characters:
        return prompt
    result = None
    subject_num = 1
    for char in characters:
        char_name = char.get('name', '')
        if char_name and f'''@{char_name}''' in result:
            gender = char.get('gender', 'male')
            gender_word = 'man' if gender == 'male' else 'woman'
            result = result.replace(f'''@{char_name}''', f'''Subject {subject_num} ({char_name})''')
            subject_num += 1
        return result


def add_face_preservation_marker(prompt = None):
    '''
    얼굴 보존 마커 추가 (짧고 간결하게)
    '''
    if not prompt:
        return prompt
    if None in prompt.lower() or 'subject images' in prompt.lower():
        return prompt
    return f'''{None.rstrip('.')}. Maintain the exact facial structures from the subject images.'''


def get_style_tag(content_type = None):
    '''
    간결한 스타일 태그 반환
    '''
    if content_type == 'informational':
        return 'Clean, professional style. Natural lighting.'


def optimize_whisk_prompt(prompt, characters, narration = None, setting = None, force_ethnicity = None, remove_conflicts = (None, '', '', True, True, True), add_markers = ('prompt', str, 'characters', List[Dict], 'narration', str, 'setting', str, 'force_ethnicity', bool, 'remove_conflicts', bool, 'add_markers', bool, 'return', Dict[(str, str)])):
    """
    Whisk 프롬프트 간소화 최적화

    복잡한 표현 대신 감정 중심의 간결한 프롬프트 생성

    Args:
        prompt: 원본 프롬프트
        characters: 캐릭터 정보 목록
        narration: 나레이션 텍스트
        setting: 배경/시대 설정
        force_ethnicity: 인종 강화 (현재는 간단히 Korean만 유지)
        remove_conflicts: 스타일 충돌 제거 (간소화로 대부분 불필요)
        add_markers: 얼굴 보존 마커 추가

    Returns:
        {
            'optimized_prompt': 최적화된 프롬프트,
            'negative_prompt': Negative prompt,
            'content_type': 콘텐츠 유형,
            'changes_made': 적용된 변경 목록
        }
    """
    pass
# WARNING: Decompyle incomplete


def quick_optimize(prompt = None):
    '''
    빠른 최적화 (프롬프트, negative prompt 반환)
    '''
    result = optimize_whisk_prompt(prompt)
    return (result['optimized_prompt'], result['negative_prompt'])


def get_korean_ethnicity_prefix(gender = None, age = None):
    '''
    한국인 인종 프리픽스 생성 (간소화)
    '''
    if 'elderly' in age.lower() and '노인' in age and '할머니' in age or '할아버지' in age:
        return f'''elderly Korean {'man' if gender == 'male' else 'woman'}'''
    return f'''{'man' if gender == 'male' else 'woman'}'''
