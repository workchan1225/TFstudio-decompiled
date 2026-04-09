# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_keyword_manager.pyc (Python 3.11)

'''
SceneKeywordManager - 장면 키워드 관리 모듈

Phase 1: scene_redistribution_service.py에서 키워드 관련 로직 추출
Phase 2: 배치 키워드 재생성 추가 (N회 → 1회 AI 호출)

주요 역할:
- 키워드 추출/검증/정규화
- 크로스씬 키워드 다양성
- 배치 키워드 재생성 (토큰 최적화)
'''
import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple
from utils.character_name_matcher import normalize_character_name
from scene_character_selection_helper import normalize_keyword_text_config
_SceneKeywordCandidate = <NODE:12>()
_SceneKeywordPlanState = <NODE:12>()

class SceneKeywordManager:
    '''장면 키워드 추출, 검증, 재생성 관리'''
    _KEYWORD_QUALITY_THRESHOLD = 0.75
    _KEYWORD_TARGET_MIN_COUNT = 2
    _KEYWORD_MAX_COUNT = 3
    _KEYWORD_CANDIDATE_POOL_LIMIT = 6
    _KEYWORD_DEFAULT_REPEAT_LIMIT = 1
    _KEYWORD_REPEAT_SCENE_LIMIT = 2
    _KEYWORD_REPEAT_RESCUE_SOURCES = {
        'original',
        'ai_recovery'}
    _KEYWORD_SOURCE_PRIORITY = {
        'original': 1,
        'ai_recovery': 0.92,
        'python_fallback': 0.64,
        'emergency_fallback': 0.42,
        'python_rescue': 0.58,
        'emergency_rescue': 0.34 }
    _KEYWORD_EMOTION_CANDIDATES = [
        '복수',
        '분노',
        '슬픔',
        '기쁨',
        '희망',
        '절망',
        '사랑',
        '증오',
        '결의',
        '고통',
        '평화',
        '전쟁',
        '대결',
        '승리',
        '패배',
        '각성']
    _KEYWORD_REJECT_STOPWORDS = {
        '것',
        '곳',
        '그',
        '끝',
        '넷',
        '눈',
        '둘',
        '때',
        '말',
        '몇',
        '몸',
        '셋',
        '손',
        '수',
        '씬',
        '일',
        '각각',
        '거기',
        '건설',
        '것들',
        '결과',
        '경우',
        '관계',
        '그것',
        '그녀',
        '나중',
        '내일',
        '누구',
        '느낌',
        '다음',
        '대사',
        '동안',
        '마음',
        '많은',
        '매일',
        '매주',
        '먼저',
        '며칠',
        '모든',
        '모습',
        '무엇',
        '문제',
        '방법',
        '부분',
        '사람',
        '상황',
        '생각',
        '소리',
        '시작',
        '어디',
        '어떤',
        '어제',
        '언제',
        '얼굴',
        '여기',
        '오늘',
        '우리',
        '원인',
        '이것',
        '이번',
        '이유',
        '이전',
        '이후',
        '자막',
        '장면',
        '저것',
        '저기',
        '저희',
        '적은',
        '전체',
        '정도',
        '중간',
        '지난',
        '하나',
        '항상',
        '해결',
        '해설',
        '사람들',
        '여러분',
        '텍스트',
        '나레이션',
        '내레이션',
        '진행'}
    _KEYWORD_PREDICATE_SUFFIX_REGEX = re.compile('(?:합니다|됩니다|있습니다|입니다|였습니다|있으십니|십니다|십니|하고|하며|해서|하는|했다|한다|되는|된다|라고|라며)$')
    _KEYWORD_PARTICLE_SUFFIX_REGEX = re.compile('(?:에서|에게|으로|까지|부터|처럼|보다|은|는|이|가|을|를|와|과|도|만)$')
    _KEYWORD_NUMERIC_SUPPORT_UNIT_REGEX = re.compile('(?:원|만원|억원|천만원|달러|usd|krw|유로|엔|%|퍼센트|배|회|명|년|개월|월|일|시간|분|초|건|개|점)$', re.IGNORECASE)
    _SCENE_ROLE_HINTS = {
        'warning': ('경고', '위험', '위기', '긴급', '비상', '재난', '붕괴', '폭발', '대피', '통제', '정전'),
        'data': ('데이터', '기록', '문서', '보고', '계약', '증거', '통계', '차트', '수치', '분석', '파일'),
        'ui_status': ('화면', '모니터', '알림', '상태', '메시지', '접속', '오류', 'dashboard', 'status'),
        'environment': ('간판', '표지', '표식', '구역', '입구', '출구', 'notice', 'sign', 'label'),
        'emotional_anchor': tuple(_KEYWORD_EMOTION_CANDIDATES),
        'event_state': ('사건', '발생', '진행', '혼란', '붕괴', '추락', '충돌', '도킹', '폭우', '정전') }
    _KEYWORD_ROLE_HINTS = {
        'warning': ('경고', '주의', '위험', '위기', '긴급', '비상', '경보', '정전'),
        'data': ('문서', '기록', '보고', '증거', '데이터', '차트', '수치', '통계', '계약', '상태'),
        'ui_status': ('화면', '모니터', '알림', '메시지', '오류', '접속', 'status'),
        'environment': ('입구', '출구', '구역', '표지', '간판', 'label', 'sign') }
    _strip_json_fences = (lambda text = None: fenced_match = re.search('```(?:json)?\\s*([\\s\\S]*?)```', text, flags = re.IGNORECASE)if fenced_match:
fenced_match.group(1).strip()None.replace('```json', '').replace('```', '').strip())()
    _collect_character_name_filters = (lambda characters = None: raw_names = []normalized_names = set()seen_raw = set()if not isinstance(characters, list):
(raw_names, normalized_names)for character in None:
if not isinstance(character, dict):
continuefor key in ('name', 'nameKo', 'koreanName', 'displayName', 'englishName'):
if not character.get(key):
raw_name = str('').strip()if not raw_name:
continuecleaned_name = raw_name.lstrip('@').strip()if not cleaned_name:
continueraw_key = cleaned_name.lower()if raw_key not in seen_raw:
seen_raw.add(raw_key)raw_names.append(cleaned_name)normalized_name = normalize_character_name(cleaned_name)if normalized_name and len(normalized_name) >= 2:
normalized_names.add(normalized_name)split_tokens = re.split('[\\s\\-_]+', cleaned_name)()for token in split_tokens:
normalized_token = normalize_character_name(token)if normalized_token and len(normalized_token) >= 2:
normalized_names.add(normalized_token)(raw_names, normalized_names))()
    _normalize_blocked_character_names = (lambda character_name_blocklist = None: normalized_names = set()if not character_name_blocklist:
for raw_name in []:
if not raw_name:
normalized_name = normalize_character_name(str('').replace('@', '').strip())if normalized_name and len(normalized_name) >= 2:
normalized_names.add(normalized_name)normalized_names)()
    _format_blocked_character_names = (lambda character_name_blocklist = None: cleaned_names = []seen = set()if not character_name_blocklist:
for raw_name in []:
if not raw_name:
cleaned_name = str('').replace('@', '').strip()if not cleaned_name:
continuededupe_key = cleaned_name.lower()if dedupe_key in seen:
continueseen.add(dedupe_key)cleaned_names.append(cleaned_name)', '.join(cleaned_names[:12]) if cleaned_names else '없음')()
    _sanitize_keyword_text = (lambda candidate = None:
