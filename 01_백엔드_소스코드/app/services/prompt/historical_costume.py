# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: historical_costume.pyc (Python 3.11)

'''
역사극 한복 처리 모듈

역사극/사극 스타일 감지 및 신분별 한복 프롬프트 생성
- joseon_costume_data.py의 함수들을 래핑
- 중복 로직 통합
'''
from typing import Dict, List, Optional, Tuple
from utils.joseon_costume_data import get_costume_by_class, detect_social_class, detect_gender, build_costume_prompt as _build_costume_prompt, get_all_social_classes
HISTORICAL_KEYWORDS = [
    'Historical Sageuk',
    'Joseon Folktale',
    '역사극',
    '사극',
    '조선야담',
    '민화',
    'historical korean',
    'joseon dynasty',
    'goryeo',
    '고려',
    '조선시대']

def is_historical_style(template = None):
    '''
    템플릿이 역사극/사극 스타일인지 확인

    Args:
        template: ImagePromptTemplate 객체 또는 dict

    Returns:
        역사극 스타일 여부
    '''
    pass
# WARNING: Decompyle incomplete


def build_costume_description(characters = None, scene_description = None, language = None):
    """
    캐릭터 목록에 대해 신분별 한복 설명 생성 (@캐릭터명 형식 사용)

    Args:
        characters: 캐릭터 정보 리스트
            - name: 캐릭터 이름
            - gender: 성별
            - profile: 캐릭터 설명
            - appearance: 외모 설명
            - englishDescription: 영문 설명
        scene_description: 장면 설명 (신분 감지 보조용)
        language: 언어 ('en' 또는 'ko')

    Returns:
        한복 설명 문자열
    """
    if not characters:
        return ''
    costume_descriptions = None
    for char in characters:
        char_name = char.get('name', 'Character')
        gender = char.get('gender', 'unknown')
        char_description = ' '.join(None(filter, [
            char.get('profile', ''),
            char.get('appearance', ''),
            char.get('englishDescription', ''),
            char_name,
            scene_description]))
        (social_class, confidence) = detect_social_class(char_description)
        costume_prompt = _build_costume_prompt(character_description = char_description, social_class = social_class, gender = gender, language = language)
        if costume_prompt:
            costume_descriptions.append(f'''@{char_name} {costume_prompt}''')
        if costume_descriptions:
            return 'Costume: ' + '. '.join(costume_descriptions)
        return None


def get_character_costume(character = None, scene_description = None, language = None):
    '''
    단일 캐릭터의 한복 프롬프트 생성

    Args:
        character: 캐릭터 정보
        scene_description: 장면 설명
        language: 언어

    Returns:
        한복 프롬프트 문자열
    '''
    char_name = character.get('name', 'Character')
    gender = character.get('gender', 'unknown')
    char_description = ' '.join(None(filter, [
        character.get('profile', ''),
        character.get('appearance', ''),
        character.get('englishDescription', ''),
        char_name,
        scene_description]))
    (social_class, confidence) = detect_social_class(char_description)
    return _build_costume_prompt(character_description = char_description, social_class = social_class, gender = gender, language = language)

__all__ = [
    'HISTORICAL_KEYWORDS',
    'is_historical_style',
    'build_costume_description',
    'get_character_costume',
    'get_costume_by_class',
    'detect_social_class',
    'detect_gender',
    'get_all_social_classes']
