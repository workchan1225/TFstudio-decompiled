# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: genre_categories.pyc (Python 3.11)

'''
장르 카테고리 시스템

장르를 카테고리로 분류하고, 각 카테고리에 맞는 In Medias Res 전략을 매핑합니다.
모든 장르에 In Medias Res 기법이 적용되며, 장르별로 최적의 유형이 자동 선택됩니다.
'''
from typing import Dict, List, Optional, Tuple
from enum import Enum

class InMediasResType(Enum):
    '''In Medias Res 유형'''
    CLIMAX_TEASER = 'climax_teaser'
    RESULT_FIRST = 'result_first'
    QUESTION_HOOK = 'question_hook'
    FLASH_FORWARD = 'flash_forward'

GENRE_CATEGORIES: Dict[(str, Dict)] = {
    'dramatic': {
        'genres': [
            'DRAMATIC',
            'CONFESSION',
            'TOUCHING',
            'LIFE_LESSONS',
            'LIFE_CHALLENGE',
            'TRUE_STORY',
            'DISASTER_APOCALYPSE',
            'YOUTH_DRAMA',
            'MUNCHKIN',
            'COMEDY'],
        'in_medias_res_type': InMediasResType.CLIMAX_TEASER,
        'description': '클라이맥스의 가장 충격적인 순간을 먼저 보여주고, "어떻게 이런 일이?" 하며 과거로 돌아감',
        'teaser_duration': '5-10초',
        'transition_phrase': '어떻게 이런 일이 벌어졌을까요? 이야기는 [시간] 전으로 돌아갑니다...' },
    'revenge': {
        'genres': [
            'REVENGE'],
        'in_medias_res_type': InMediasResType.RESULT_FIRST,
        'description': '복수가 완성된 통쾌한 순간을 먼저 보여주고, 어떻게 이렇게 됐는지 과거로 돌아감',
        'teaser_duration': '5-10초',
        'transition_phrase': '이 통쾌한 순간이 오기까지... 모든 것은 [시간] 전에 시작되었습니다.' },
    'mystery': {
        'genres': [
            'MYSTERY',
            'CONSPIRACY',
            'THRILLER',
            'HORROR'],
        'in_medias_res_type': InMediasResType.QUESTION_HOOK,
        'description': '강렬한 의문을 먼저 제기하고, 그 답을 찾아가는 구조',
        'teaser_duration': '3-8초',
        'transition_phrase': '그 답을 찾기 위해, 처음으로 돌아가 봅시다...' },
    'heartwarming': {
        'genres': [
            'HEARTWARMING',
            'FAMILY'],
        'in_medias_res_type': InMediasResType.RESULT_FIRST,
        'description': '화해하고 감동받는 순간을 먼저 보여주고, 어떻게 이런 변화가 일어났는지 과거로',
        'teaser_duration': '5-10초',
        'transition_phrase': '이 감동적인 순간이 오기까지... 사실 처음엔 그렇지 않았습니다.' },
    'informational': {
        'genres': [
            'ENCYCLOPEDIA',
            'LIFE_TIPS',
            'LIFE_KNOWLEDGE',
            'OFFICE_SURVIVAL',
            'MONEY_SENSE',
            'ECONOMICS',
            'RELATIONSHIP_EQ',
            'PSYCHOLOGY',
            'LIFE_CHOICES',
            'KNOWLEDGE_BITE',
            'SCIENCE',
            'DOCUMENTARY',
            'NEWS_REPORT',
            'REVIEW_ANALYSIS',
            'SPACE',
            'SOCIAL_ISSUES',
            'NATURAL_DISASTER'],
        'in_medias_res_type': InMediasResType.QUESTION_HOOK,
        'description': '핵심 질문이나 충격적 사실로 시작하여 답을 찾아가는 구조',
        'teaser_duration': '3-8초',
        'transition_phrase': '그 답을 지금부터 알려드리겠습니다...' },
    'historical': {
        'genres': [
            'JOSEON_FOLKTALE',
            'HISTORY',
            'WAR_MILITARY',
            'HISTORICAL',
            'NATIONAL_PRIDE',
            'THREE_KINGDOMS'],
        'in_medias_res_type': InMediasResType.FLASH_FORWARD,
        'description': '비극적이거나 감동적인 결말을 암시하고, 그 이야기의 시작으로 돌아감',
        'teaser_duration': '5-10초',
        'transition_phrase': '이 순간이 오기까지... 이야기는 [시간] 전으로 거슬러 올라갑니다.' },
    'fantasy': {
        'genres': [
            'SF_FANTASY',
            'EPIC_FANTASY'],
        'in_medias_res_type': InMediasResType.CLIMAX_TEASER,
        'description': '가장 스펙터클한 장면을 먼저 보여주고, 세계관과 시작을 설명',
        'teaser_duration': '5-10초',
        'transition_phrase': '어떻게 이런 세계가 펼쳐졌을까요? 모든 것은 여기서 시작되었습니다...' },
    'variety': {
        'genres': [
            'VARIETY'],
        'in_medias_res_type': InMediasResType.QUESTION_HOOK,
        'description': '재미있는 결과나 반전을 먼저 암시하고, 과정을 보여줌',
        'teaser_duration': '3-5초',
        'transition_phrase': '어떻게 이런 결과가 나왔을까요?' } }
_GENRE_TO_CATEGORY: Dict[(str, str)] = { }

def _build_genre_to_category_map():
    '''장르 → 카테고리 역매핑 생성'''
    for category, data in GENRE_CATEGORIES.items():
        for genre in data['genres']:
            _GENRE_TO_CATEGORY[genre] = category
            return None

_build_genre_to_category_map()

def get_genre_category(genre = None):
    """
    장르의 카테고리 반환

    Args:
        genre: 장르 코드 (예: 'DRAMATIC', 'ENCYCLOPEDIA')

    Returns:
        카테고리 이름 (예: 'dramatic', 'informational')
        찾지 못하면 'dramatic' 반환 (기본값)
    """
    return _GENRE_TO_CATEGORY.get(genre, 'dramatic')


def get_in_medias_res_type(genre = None):
    '''
    장르에 맞는 In Medias Res 유형 반환

    Args:
        genre: 장르 코드

    Returns:
        InMediasResType enum 값
    '''
    category = get_genre_category(genre)
    category_data = GENRE_CATEGORIES.get(category, GENRE_CATEGORIES['dramatic'])
    return category_data['in_medias_res_type']


def get_category_data(genre = None):
    '''
    장르의 카테고리 전체 데이터 반환

    Args:
        genre: 장르 코드

    Returns:
        카테고리 데이터 딕셔너리
    '''
    category = get_genre_category(genre)
    return GENRE_CATEGORIES.get(category, GENRE_CATEGORIES['dramatic'])


def get_transition_phrase(genre = None):
    '''
    장르에 맞는 시간 역행 전환 문구 반환

    Args:
        genre: 장르 코드

    Returns:
        전환 문구 문자열
    '''
    category_data = get_category_data(genre)
    return category_data.get('transition_phrase', '어떻게 이런 일이 벌어졌을까요?')


def get_teaser_duration(genre = None):
    """
    장르에 맞는 티저 권장 길이 반환

    Args:
        genre: 장르 코드

    Returns:
        티저 길이 (예: '5-10초')
    """
    category_data = get_category_data(genre)
    return category_data.get('teaser_duration', '5-10초')


def get_all_genres_in_category(category = None):
    '''
    카테고리에 속한 모든 장르 반환

    Args:
        category: 카테고리 이름

    Returns:
        장르 코드 리스트
    '''
    category_data = GENRE_CATEGORIES.get(category, { })
    return category_data.get('genres', [])


def is_drama_category(genre = None):
    '''드라마/스토리텔링 계열인지 확인'''
    category = get_genre_category(genre)
    return category in ('dramatic', 'revenge', 'mystery', 'heartwarming', 'historical', 'fantasy')


def is_informational_category(genre = None):
    '''정보/교육 계열인지 확인'''
    category = get_genre_category(genre)
    return category in ('informational', 'variety')

IN_MEDIAS_RES_INSTRUCTIONS: Dict[(InMediasResType, Dict)] = {
    InMediasResType.FLASH_FORWARD: {
        'name': '미래 암시',
        'korean_name': '미래 장면 먼저',
        'instruction': '\n**첫 번째 챕터 구조 (미래 암시)**:\n\n[미래 장면 - 5-10초]\n비극적이거나 감동적인 결말을 암시하세요:\n- 임금의 눈물\n- 영웅의 최후\n- 역사적 순간의 시작\n\n[현재로 복귀]\n"이 순간이 오기까지..."\n"이 비극의 시작은 [X년] 전으로 거슬러 올라갑니다"\n\n[과거 시점 시작]\n이야기의 시작점부터 전개하세요\n미래 장면을 향해 이야기가 흘러가야 합니다\n',
        'example': '\n[나레이션]: 영조 임금은 그날 밤, 조용히 눈물을 흘렸습니다.\n[나레이션]: "이 아이가 정녕 내 아들이란 말인가..."\n[나레이션]: 조선 역사상 가장 비극적인 순간이 다가오고 있었습니다.\n\n[나레이션]: 이 비극의 시작은 10년 전으로 거슬러 올라갑니다...\n' },
    InMediasResType.QUESTION_HOOK: {
        'name': '질문형',
        'korean_name': '질문으로 시작',
        'instruction': '\n**첫 번째 챕터 구조 (질문형)**:\n\n[핵심 질문 - 3-8초]\n시청자가 답을 알고 싶어하는 강렬한 질문으로 시작:\n- "왜 90%의 사람들이 이 실수를 반복할까요?"\n- "당신이 매일 먹는 이것, 왜 전문의들은 피할까요?"\n- "그날 밤 무슨 일이 있었을까요?"\n\n[힌트 제공]\n질문에 대한 힌트를 살짝 보여주세요\n완전한 답은 주지 마세요\n\n[탐색/설명 시작]\n답을 찾아가는 여정 또는 설명을 시작하세요\n마지막에 명확한 답이 제시되어야 합니다\n',
        'example': '\n[나레이션]: 왜 90%의 사람들이 이 실수를 반복할까요?\n[나레이션]: 전문가들도 처음엔 몰랐던 이 사실,\n[나레이션]: 오늘 이 영상에서 그 답을 알려드립니다.\n\n[나레이션]: 첫 번째 이유는 생각보다 단순합니다...\n' },
    InMediasResType.RESULT_FIRST: {
        'name': '결과 먼저',
        'korean_name': '결과 먼저 제시',
        'instruction': '\n**첫 번째 챕터 구조 (결과 먼저)**:\n\n[결과 제시 - 5-10초]\n주인공의 현재 상태(결과)를 먼저 보여주세요:\n- 복수가 완성된 통쾌한 순간\n- 화해하고 감동받는 순간\n- 성공하거나 변화된 모습\n\n[호기심 유발]\n"이 모든 것은 [X]에서 시작되었습니다"\n"처음엔 이렇지 않았습니다..."\n\n[과거로 이동]\n변화가 시작된 시점부터 이야기를 풀어가세요\n',
        'example': '\n[영희]: "어머니, 이 서류 보이세요?"\n[시어머니]: "그, 그건..."\n[영희]: "30년간 저한테 숨기셨던 것들이에요."\n[시어머니]: "영희야, 그건 오해란다. 내가 설명할게..."\n[영희]: "설명? 이제 와서요? 다 끝났어요, 어머니."\n[나레이션]: 무릎 꿇은 시어머니 앞에서, 30년간의 복수가 완성되는 순간이었습니다.\n\n[나레이션]: 어떻게 이런 일이 일어났을까요?\n[나레이션]: 모든 것은 6개월 전에 시작되었습니다...\n' },
    InMediasResType.CLIMAX_TEASER: {
        'name': '클라이맥스 티저',
        'korean_name': '클라이맥스 먼저',
        'instruction': '\n**첫 번째 챕터 구조 (클라이맥스 티저)**:\n\n[티저 - 5-10초]\n이야기의 가장 충격적이고 감정적인 순간을 먼저 보여주세요:\n- 눈물, 분노, 충격의 순간\n- 대결의 절정\n- 충격적인 폭로/발견\n- 결과는 보여주지 말고 "순간"만 전달\n\n[전환]\n"어떻게 이런 일이 벌어졌을까요?"\n"모든 것은 [X개월/년] 전에 시작되었습니다..."\n\n[본편 시작]\n평범했던 일상, 주인공 소개부터 시작\n마지막 챕터에서 티저 장면이 다시 등장해야 함\n',
        'example': '\n[민지]: "어머니, 이게 뭔지 아세요?"\n[시어머니]: "그, 그건... 어디서 났어?"\n[민지]: "어머니가 숨긴 곳에서요. 제 몫의 유산 증서죠."\n[시어머니]: "그건 오해야! 내가 보관만..."\n[민지]: "보관? 10년간 없다고 거짓말하신 게 보관이에요?"\n[나레이션]: 그 순간, 시어머니는 바닥에 무릎을 꿇었습니다.\n\n[나레이션]: 어떻게 이런 일이 벌어졌을까요?\n[나레이션]: 이야기는 6개월 전으로 돌아갑니다...\n' } }

def get_in_medias_res_instruction(genre = None):
    '''
    장르에 맞는 In Medias Res 상세 지침 반환

    Args:
        genre: 장르 코드

    Returns:
        상세 지침 문자열
    '''
    imr_type = get_in_medias_res_type(genre)
    instruction_data = IN_MEDIAS_RES_INSTRUCTIONS.get(imr_type, IN_MEDIAS_RES_INSTRUCTIONS[InMediasResType.CLIMAX_TEASER])
    return instruction_data['instruction']


def get_in_medias_res_example(genre = None):
    '''
    장르에 맞는 In Medias Res 예시 반환

    Args:
        genre: 장르 코드

    Returns:
        예시 문자열
    '''
    imr_type = get_in_medias_res_type(genre)
    instruction_data = IN_MEDIAS_RES_INSTRUCTIONS.get(imr_type, IN_MEDIAS_RES_INSTRUCTIONS[InMediasResType.CLIMAX_TEASER])
    return instruction_data.get('example', '')
