# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: korean_names.pyc (Python 3.11)

'''
한국인 이름 유틸리티 (AI 동적 생성 기반)

v2.0.0: 하드코딩 데이터 제거 - AI가 대본 맥락 기반으로 동적 생성
- 이름 생성: AI가 대본/시대/배경을 분석하여 직접 생성
- 이름 정제: 괄호 제거 등 후처리만 제공
'''
import re
from typing import Dict, List

def clean_character_name(name = None):
    '''캐릭터 이름에서 괄호 및 괄호 안 내용 제거 (한문/영문 병기 제거)

    AI가 "관우 (關羽)" 또는 "관우 (Guan Yu)" 형식으로 생성할 경우 정제

    Args:
        name: 정제할 이름

    Returns:
        괄호와 괄호 안 내용이 제거된 이름

    Examples:
        >>> clean_character_name("관우 (關羽)")
        \'관우\'
        >>> clean_character_name("유비 (劉備)")
        \'유비\'
    '''
    if not name:
        return name
    name = None.sub('\\s*[\\(（\\[【][^\\)）\\]】]*[\\)）\\]】]', '', name)
    return name.strip()

SURNAMES = { }
COMPOUND_SURNAMES = { }
JOSEON_YADAM_NAMES = { }
JOSEON_INVALID_NAMES = []
PERIOD_NAME_PATTERNS = { }
PERIOD_KEYWORD_MAP = { }
MALE_NAMES = { }
FEMALE_NAMES = { }
UNISEX_NAMES = []
MALE_NAME_PATTERNS = []
FEMALE_NAME_PATTERNS = []
GENDER_MAP = { }

def get_weighted_surname():
    '''[DEPRECATED] AI가 대본 맥락 기반으로 성씨 결정'''
    return ''


def get_names_by_gender(gender = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 이름 결정'''
    return { }


def get_names_by_generation(birth_decade = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 이름 결정'''
    return {
        'male': [],
        'female': [] }


def age_to_decade(age_range = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 나이대 결정'''
    return ''


def get_random_fullname(gender = None, age_range = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 이름 생성'''
    return ''


def suggest_names(gender = None, count = None, age_range = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 이름 추천'''
    return []


def get_gender_by_name(name = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 성별 결정'''
    return 'unknown'


def validate_name_gender(name = None, expected_gender = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 검증'''
    return True


def correct_character_gender(character = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 교정'''
    return character


def replace_mismatched_name(character = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 교정'''
    return character


def validate_characters(characters = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 검증'''
    return characters


def get_name_suggestions_for_prompt(gender = None, age_range = None, count = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 이름 생성'''
    return ''


def detect_period_from_text(text = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 시대 감지'''
    return '현대'


def infer_social_class(role_text = None, period = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 신분 추론'''
    return 'common'


def get_period_name_guidance(period = None, gender = None, social_class = None, age_range = (None, None)):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 이름 생성'''
    return ''


def get_period_surnames(period = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 성씨 결정'''
    return []


def validate_name_for_period(name = None, period = None, gender = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 검증'''
    return {
        'valid': True,
        'reason': '',
        'suggested': None }


def get_joseon_yadam_name_examples(gender = None, social_class = None, count = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 이름 생성'''
    return []


def get_joseon_yadam_name_guidance(gender = None, social_class = None, role_desc = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 이름 생성'''
    return ''


def validate_joseon_name(name = None, gender = None, social_class = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 검증'''
    return {
        'valid': True,
        'reason': '',
        'suggested': [] }


def is_joseon_yadam_genre(genre = None):
    '''[DEPRECATED] AI가 대본 맥락 기반으로 장르 감지'''
    return False
