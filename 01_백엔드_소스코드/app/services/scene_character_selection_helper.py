# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_character_selection_helper.pyc (Python 3.11)

'''
Helpers for scene-level character selection and structured prompt context handling.
'''
import re
from typing import Callable, Dict, List, Optional, Tuple
from utils.korean_pos_analyzer import KIWI_AVAILABLE, is_noun_only, clean_keyword_to_pure_noun
from utils.character_name_matcher import detect_characters_in_text, extract_partial_name, filter_non_scene_characters, is_character_name_in_text, normalize_character_name, resolve_detected_characters, resolve_partial_name_to_full, resolve_role_names_to_character_names
from utils.character_binding_mode import normalize_character_binding_mode
from scene.scene_identity_context import extract_scene_registered_character_names
DEFAULT_SCENE_REFERENCE_LIMIT = 2
MAX_SCENE_REFERENCE_LIMIT = 4
MIN_SCORE_FOR_THIRD_REFERENCE = 7
MIN_SCORE_FOR_THIRD_REFERENCE_STRUCTURED = 5
MIN_SCORE_FOR_FOURTH_REFERENCE = 9
MIN_SCORE_FOR_FOURTH_REFERENCE_STRUCTURED = 7
MAX_KEYWORD_COUNT = 3
MAX_KEYWORD_LENGTH = 8
VALID_KEYWORD_POSITIONS = {
    'top',
    'bottom',
    'center'}
_KEYWORD_SPLIT_REGEX = re.compile('[\\n,;|]+')
_KEYWORD_LABEL_PREFIX_REGEX = re.compile('^(?:표지판|간판|배너|모니터|라벨|텍스트|키워드|keyword|text|label|sign|banner|screen|title|subtitle)\\s*\\d*\\s*[:：]\\s*', flags = re.IGNORECASE)
_ADJECTIVE_KEYWORD_SET = {
    '큰',
    '강한',
    '나쁜',
    '낮은',
    '높은',
    '느린',
    '빠른',
    '약한',
    '작은',
    '좋은',
    '간단한',
    '급격한',
    '급속한',
    '따뜻한',
    '명확한',
    '복잡한',
    '불안한',
    '새로운',
    '심각한',
    '안전한',
    '오래된',
    '위험한',
    '중요한',
    '차가운',
    '차분한',
    '화려한',
    '지속적인',
    '효과적인'}
_ADJECTIVE_SUFFIX_REGEX = re.compile('(?:적인|스러운|스런|같은)$')
_PREDICATE_SUFFIX_REGEX = re.compile('(?:하는|하며|해서|하고|했던|하던|된다|되는|된다면|했다|한다|였다|었다|라고|라며|스럽게|하게|됩니다|합니다|있습니다|였습니다|입니다|십니다|십니|되다|되어|되며|된|되|하다|하여|하면|함)$')
_PARTICLE_SUFFIX_REGEX = re.compile('(?:에서|에게|으로|까지|부터|처럼|보다|은|는|이|가|을|를|와|과|도|만)$')
_NON_NOUN_STOPWORDS = {
    '것',
    '끝',
    '눈',
    '때',
    '말',
    '몸',
    '손',
    '챕',
    '건설',
    '것들',
    '결과',
    '결심',
    '결정',
    '경우',
    '계획',
    '관계',
    '나중',
    '내일',
    '느낌',
    '다음',
    '다짐',
    '대사',
    '동안',
    '마음',
    '먼저',
    '모습',
    '문제',
    '방법',
    '부분',
    '사람',
    '상황',
    '생각',
    '소리',
    '시작',
    '실행',
    '어제',
    '얼굴',
    '오늘',
    '우리',
    '원인',
    '이번',
    '이유',
    '이전',
    '이후',
    '자막',
    '저희',
    '전체',
    '정도',
    '준비',
    '중간',
    '지난',
    '진행',
    '해결',
    '해설',
    '사람들',
    '여러분',
    '텍스트',
    '나레이션',
    '내레이션',
    'end',
    'scene',
    'start',
    'action',
    'chapter',
    'context',
    'subject',
    'environment',
    '챕터',
    '도입부',
    '시작부',
    '페이지'}
_SENTENCE_PARTICLE_REGEX = re.compile('(?:을|를|이|가|은|는|에서|으로|에게|한테|께서)')
_SENTENCE_ENDING_REGEX = re.compile('(?:다|요|니다|습니다|세요|까요|네요|ㅂ니다)$')
_ACTION_PHRASE_REGEX = re.compile('(?:을|를)\\s*(?:다짐|시작|계획|준비|결심|각오|결정|실행|진행)')
_STATE_PHRASE_REGEX = re.compile('(?:중$|중에$|하며$|하면서$)')
_MODIFIER_ENDING_REGEX = re.compile('(?:하는|하던|했던|되는|되던|된)\\s')
_ADJ_PHRASE_REGEX = re.compile('(?:적인|스러운|스런)\\s')

def _is_sentence_like(keyword = None):
    '''키워드가 명백한 문장인지 기본 체크만 수행합니다.

    복잡한 품사 분석은 AI에 위임하고, 여기서는 명백한 문장 패턴만 감지합니다.
    - 구두점 포함
    - 길이 초과 (15자 이상)
    - 조사 2개 이상

    Args:
        keyword: 검사할 키워드

    Returns:
        명백한 문장이면 True, 그 외는 False (AI 판단에 위임)
    '''
    if not keyword:
        return False
    if None in keyword and '.' in keyword and '!' in keyword or '?' in keyword:
        return True
    if None(keyword) > 15:
        return True
    particle_count = None(_SENTENCE_PARTICLE_REGEX.findall(keyword))
    if particle_count >= 2:
        return True


def _normalize_name_text(value = None):
