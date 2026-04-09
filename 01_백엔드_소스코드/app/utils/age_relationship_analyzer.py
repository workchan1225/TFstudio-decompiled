# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: age_relationship_analyzer.pyc (Python 3.11)

'''
나이 기반 캐릭터 관계 분석 유틸리티

캐릭터의 나이대 정보를 분석하여:
1. 나이 숫자 추출 (예: "60대 후반 ~ 70대 초반" -> 67)
2. 캐릭터 간 관계 추론 (부모/자녀, 형제자매 등)
3. AI 프롬프트용 관계 힌트 생성
'''
import re
from typing import Optional, Dict, List, Tuple

class AgeBasedRelationship:
    '''나이 기반 관계 분류 상수'''
    PARENT_CHILD = 'parent_child'
    GRANDPARENT = 'grandparent_child'
    SIBLING = 'sibling'
    SIMILAR_AGE = 'similar_age'
    UNKNOWN = 'unknown'


def _apply_modifier(decade = None, modifier = None):
    '''나이대에 수식어 적용'''
    modifiers = {
        '초반': 2,
        '중반': 5,
        '후반': 8,
        '이상': 5 }
    offset = modifiers.get(modifier, 5)
    return decade + offset


def extract_age_number(age_range = None):
    '''
    나이 문자열에서 대표 나이 숫자를 추출한다.

    다양한 형식 지원:
    - "60대 후반 ~ 70대 초반" -> 67 (중간값)
    - "50대" -> 55 (중간값)
    - "30대 초반" -> 32
    - "30대 중반" -> 35
    - "30대 후반" -> 38
    - "25세" -> 25
    - "70대 이상" -> 75

    Args:
        age_range: 나이 범위 문자열

    Returns:
        추정된 나이 숫자 (int) 또는 None
    '''
    if not age_range:
        return None
    text = None.strip().lower()
    range_match = re.search('(\\d+)대?\\s*(?:후반)?\\s*[~\\-]\\s*(\\d+)대?\\s*(?:초반)?', text)
    if range_match:
        start_decade = int(range_match.group(1))
        end_decade = int(range_match.group(2))
        start_age = _apply_modifier(start_decade, '후반')
        end_age = _apply_modifier(end_decade, '초반')
        return (start_age + end_age) // 2
    decade_match = None.search('(\\d+)대(?:\\s*(초반|중반|후반|이상))?', text)
# WARNING: Decompyle incomplete


def _get_parent_child_roles(parent_gender = None, child_gender = None):
    '''부모-자녀 역할 조합'''
    if parent_gender == 'male':
        pass
    elif parent_gender == 'female':
        pass
    
    parent = '부모'
    if child_gender == 'male':
        pass
    elif child_gender == 'female':
        pass
    
    child = '자녀'
    return [
        (parent, child)]


def _get_grandparent_roles(grandparent_gender = None, grandchild_gender = None):
    '''조부모-손자녀 역할 조합'''
    if grandparent_gender == 'male':
        pass
    elif grandparent_gender == 'female':
        pass
    
    gp = '조부모'
    if grandchild_gender == 'male':
        pass
    elif grandchild_gender == 'female':
        pass
    
    gc = '손자녀'
    return [
        (gp, gc)]


def _get_sibling_roles(older_gender = None, younger_gender = None):
    '''형제자매 역할 조합'''
    if older_gender == 'male':
        older = '형' if younger_gender == 'male' else '오빠'
    elif older_gender == 'female':
        older = '누나' if younger_gender == 'male' else '언니'
    else:
        older = '형/언니'
    younger = '동생'
    return [
        (older, younger)]


def infer_relationship_by_age(age1 = None, age2 = None, gender1 = None, gender2 = (None, None)):
    """
    두 캐릭터의 나이 차이로 가능한 관계 추론

    Args:
        age1: 첫 번째 캐릭터 나이
        age2: 두 번째 캐릭터 나이
        gender1: 첫 번째 캐릭터 성별 ('male' | 'female')
        gender2: 두 번째 캐릭터 성별 ('male' | 'female')

    Returns:
        {
            'age_difference': int,  # 나이 차이 (절대값)
            'older_index': int,     # 나이 많은 쪽 (1 또는 2)
            'relationship_type': str,  # 'parent_child', 'grandparent', 'sibling', 'similar_age'
            'possible_roles': List[Tuple[str, str]],  # [(char1 역할, char2 역할), ...]
            'hint_text': str,       # AI 프롬프트용 힌트 텍스트
        }
    """
    diff = abs(age1 - age2)
    older_index = 1 if age1 >= age2 else 2
    older_gender = gender1 if older_index == 1 else gender2
    younger_gender = gender2 if older_index == 1 else gender1
    result = {
        'age_difference': diff,
        'older_index': older_index,
        'relationship_type': AgeBasedRelationship.UNKNOWN,
        'possible_roles': [],
        'hint_text': '' }
    if diff >= 40:
        result['relationship_type'] = AgeBasedRelationship.GRANDPARENT
        roles = _get_grandparent_roles(older_gender, younger_gender)
        result['possible_roles'] = roles
        result['hint_text'] = f'''나이 차이 {diff}세로, {roles[0][0]}/{roles[0][1]} 관계 가능성이 높습니다.'''
    elif diff >= 20:
        result['relationship_type'] = AgeBasedRelationship.PARENT_CHILD
        roles = _get_parent_child_roles(older_gender, younger_gender)
        result['possible_roles'] = roles
        result['hint_text'] = f'''나이 차이 {diff}세로, {roles[0][0]}/{roles[0][1]} 관계 가능성이 높습니다.'''
    elif diff < 5:
        result['relationship_type'] = AgeBasedRelationship.SIBLING
        roles = _get_sibling_roles(older_gender, younger_gender)
        result['possible_roles'] = roles
        result['hint_text'] = f'''나이 차이 {diff}세로, 형제자매 또는 또래 관계입니다.'''
    else:
        result['relationship_type'] = AgeBasedRelationship.SIMILAR_AGE
        result['possible_roles'] = [
            ('선배/언니/형', '후배/동생')]
        result['hint_text'] = f'''나이 차이 {diff}세로, 선후배/친척/지인 관계입니다.'''
    return result


def analyze_character_relationships(characters = None):
    """
    여러 캐릭터 간의 관계를 나이 기반으로 분석

    Args:
        characters: 캐릭터 정보 목록 [{'name': ..., 'ageRange': ..., 'gender': ...}, ...]

    Returns:
        {
            'relationships': [  # 모든 쌍별 관계
                {
                    'char1': '박선영',
                    'char2': '이서진',
                    'char1_age': 67,
                    'char2_age': 55,
                    'relationship': {...}
                },
                ...
            ],
            'age_hierarchy': ['박선영', '이서진', ...],  # 나이순 정렬
            'age_hierarchy_text': str,  # 나이순 정렬 텍스트
            'family_hints': str,  # AI 프롬프트용 힌트 텍스트
        }
    """
    if characters or len(characters) < 2:
        return {
            'relationships': [],
            'age_hierarchy': [],
            'age_hierarchy_text': '',
            'family_hints': '' }
    char_ages = None
    for char in characters:
        name = char.get('name', '').lstrip('@')
        age = extract_age_number(char.get('ageRange', ''))
        gender = char.get('gender')
        age_range_original = char.get('ageRange', '')
        if age:
            char_ages.append({
                'name': name,
                'age': age,
                'gender': gender,
                'age_range_original': age_range_original,
                'original': char })
        if len(char_ages) < 2:
            return {
                'relationships': [],
                'age_hierarchy': [],
                'age_hierarchy_text': '',
                'family_hints': '' }
        None.sort(key = (lambda x: x['age']), reverse = True)
        age_hierarchy = char_ages()
        age_hierarchy_lines = []
        for i, c in enumerate(char_ages, 1):
            char_name = c['name']
            if not c['age_range_original']:
                age_display = f'''{c['age']}세'''
                age_hierarchy_lines.append(f'''{i}. @{char_name} ({age_display})''')
                continue
                age_hierarchy_text = '\n'.join(age_hierarchy_lines)
                relationships = []
                hints = []
                for i in range(len(char_ages)):
                    for j in range(i + 1, len(char_ages)):
                        char1 = char_ages[i]
                        char2 = char_ages[j]
                        rel = infer_relationship_by_age(char1['age'], char2['age'], char1['gender'], char2['gender'])
                        relationships.append({
                            'char1': char1['name'],
                            'char2': char2['name'],
                            'char1_age': char1['age'],
                            'char2_age': char2['age'],
                            'relationship': rel })
                        hints.append(f'''@{char1['name']}({char1['age']}세)가 @{char2['name']}({char2['age']}세)보다 {rel['age_difference']}세 연상입니다.''')
    return {
        'relationships': relationships,
        'age_hierarchy': age_hierarchy,
        'age_hierarchy_text': age_hierarchy_text,
        'family_hints': '\n'.join(hints) if hints else '' }
