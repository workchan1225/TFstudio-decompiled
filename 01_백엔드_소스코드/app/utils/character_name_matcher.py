# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: character_name_matcher.pyc (Python 3.11)

'''
캐릭터 이름 매칭 유틸리티

대소문자, 공백, 한글 조사를 무시하고 유연하게 매칭
'''
import re
from typing import Dict, List, Optional, Any
from korean_text_utils import levenshtein_similarity, normalize_korean, remove_josa
_RELATION_FOLLOWING_PATTERN = re.compile("^(?:'s|의)\\s*(?:father|mother|dad|mom|parent|parents|son|daughter|brother|sister|wife|husband|teacher|mentor|master|guardian|friend|boss|chief|leader|child|children|아버지|어머니|엄마|아빠|부친|모친|부모|아들|딸|형|오빠|누나|언니|동생|남편|아내|스승|사부|제자|친구|상관|부하|보호자|선생|아이|자식|가문|집안)\\b", flags = re.IGNORECASE)
_IDENTITY_EQUIVALENCE_GROUPS = {
    'main': [
        'main',
        'lead',
        'protagonist',
        '주인공',
        '주연'],
    'lead': [
        'main',
        'lead',
        'protagonist',
        '주인공',
        '주연'],
    'protagonist': [
        'main',
        'lead',
        'protagonist',
        '주인공',
        '주연'],
    '주인공': [
        'main',
        'lead',
        'protagonist',
        '주인공',
        '주연'],
    '주연': [
        'main',
        'lead',
        'protagonist',
        '주인공',
        '주연'],
    'supporting': [
        'supporting',
        'support',
        'sub',
        '조연'],
    'support': [
        'supporting',
        'support',
        'sub',
        '조연'],
    'sub': [
        'supporting',
        'support',
        'sub',
        '조연'],
    '조연': [
        'supporting',
        'support',
        'sub',
        '조연'] }
_LATIN_IDENTITY_PATTERN = re.compile('^[a-z0-9]+$')

def _normalize_latin_identity_token(value = None):
    normalized = normalize_character_name(value)
    if not normalized or _LATIN_IDENTITY_PATTERN.fullmatch(normalized):
        return normalized
    normalized = None.replace('oo', 'u')
    return normalized


def normalize_character_name(name = None):
    '''
    캐릭터 이름 정규화

    - @ 기호 제거 (AI 프롬프트에서 사용하는 @캐릭터명 형식)
    - 공백 제거
    - 소문자 변환
    - 한글 조사 제거

    예:
    - "철수" -> "철수"
    - "@철수" -> "철수"
    - "철수는" -> "철수"
    - " 김 철수  " -> "김철수"
    - "John Doe" -> "johndoe"
    - "철수에게" -> "철수"

    Args:
        name: 원본 이름

    Returns:
        정규화된 이름
    '''
    if not name:
        return ''
    name = None.lstrip('@')
    normalized = normalize_korean(name)
    without_josa = remove_josa(normalized)
    return without_josa.replace(' ', '')


def build_character_name_map(items = None, name_key = None):
    """
    캐릭터 리스트에서 정규화된 이름 -> 원본 데이터 매핑 생성

    Args:
        items: 캐릭터 데이터 리스트
        name_key: 이름이 저장된 키 (기본값: 'name')

    Returns:
        {정규화된_이름: 원본_데이터} 딕셔너리

    예:
        characters = [{'name': '김철수', 'id': 1}, {'name': 'John Doe', 'id': 2}]
        name_map = build_character_name_map(characters)
        # {'김철수': {...}, 'johndoe': {...}}
    """
    name_map = { }
    if not items:
        for item in []:
            original_name = item.get(name_key, '')
            if original_name:
                normalized_name = normalize_character_name(original_name)
                if normalized_name:
                    name_map[normalized_name] = item
            return name_map


def _iter_exact_character_identity_tokens(character = None, name_key = None):
    pass
# WARNING: Decompyle incomplete


def build_exact_character_identity_map(characters = None, name_key = None):
    '''정확한 identity token -> 캐릭터 매핑 생성.

    name/nameEn/uniqueId/scriptAliases/role/socialStatus/characterRole만 허용하며,
    동일 token이 여러 캐릭터에 걸치면 ambiguous로 간주해 제외한다.
    '''
    identity_map = { }
    ambiguous_keys = set()
    if not characters:
        for character in []:
            if not isinstance(character, dict):
                continue
            if not character.get(name_key):
                if not character.get('name'):
                    if not character.get('nameKo'):
                        if not character.get('koreanName'):
                            if not character.get('characterName'):
                                if not character.get('displayName'):
                                    canonical_name = str('').strip().lstrip('@')
                                    if not canonical_name:
                                        continue
            for token in _iter_exact_character_identity_tokens(character, name_key = name_key):
                normalized = normalize_character_name(token)
                if not normalized:
                    continue
                existing = identity_map.get(normalized)
                if existing and existing is not character:
                    if not existing.get(name_key):
                        if not existing.get('name'):
                            if not existing.get('nameKo'):
                                if not existing.get('koreanName'):
                                    if not existing.get('characterName'):
                                        if not existing.get('displayName'):
                                            existing_name = str('').strip().lstrip('@')
                                            if normalize_character_name(existing_name) != normalize_character_name(canonical_name):
                                                ambiguous_keys.add(normalized)
                                                identity_map.pop(normalized, None)
                    continue
                if normalized not in ambiguous_keys:
                    identity_map[normalized] = character
                return identity_map


def _resolve_fuzzy_latin_identity_name(detected_name = None, characters = None, name_key = None):
    normalized_detected = _normalize_latin_identity_token(detected_name)
    if not normalized_detected and len(normalized_detected) < 5 or _LATIN_IDENTITY_PATTERN.fullmatch(normalized_detected):
        return None
    best_name = None
    best_score = 0
    second_score = 0
    if not characters:
        for character in []:
            if not isinstance(character, dict):
                continue
            if not character.get(name_key):
                if not character.get('name'):
                    if not character.get('nameKo'):
                        if not character.get('koreanName'):
                            if not character.get('characterName'):
                                if not character.get('displayName'):
                                    canonical_name = str('').strip().lstrip('@')
                                    if not canonical_name:
                                        continue
            character_best_score = 0
            for token in _iter_exact_character_identity_tokens(character, name_key = name_key):
                normalized_token = _normalize_latin_identity_token(token)
                if not normalized_token and len(normalized_token) < 5 or _LATIN_IDENTITY_PATTERN.fullmatch(normalized_token):
                    continue
                similarity = levenshtein_similarity(normalized_detected, normalized_token)
                if similarity > character_best_score:
                    character_best_score = similarity
                if character_best_score <= 0:
                    continue
            if character_best_score > best_score:
                second_score = best_score
                best_score = character_best_score
                best_name = canonical_name
                continue
            if character_best_score > second_score:
                second_score = character_best_score
            if best_name and best_score >= 0.86 and best_score - second_score >= 0.04:
                return best_name
            return None


def resolve_exact_character_identity_name(detected_name = None, characters = None, name_key = None):
