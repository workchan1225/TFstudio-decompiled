# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: temporal_analyzer.pyc (Python 3.11)

'''
시간적 구조 분석기 (Temporal Analyzer)

씬 분할 전에 전체 대본의 시간적 구조를 AI로 사전 분석합니다.
- 회상/현재/미래 구간 식별
- 각 구간별 캐릭터 나이 계산
- 회상 시작/종료 지점 명확화
- 폴백 분석 (AI 실패 시)

v1.1: 모델 alias 적용, 404 즉시 fallback, is_fallback 플래그 추가
'''
import re
import json
import ast
import asyncio
import logging
from typing import Dict, List, Any, Optional, Tuple
from app.config.model_aliases import get_model_name, get_fallback_chain

try:
    from json_repair import repair_json as repair_broken_json
except Exception:
    repair_broken_json = None

logger = logging.getLogger(__name__)

class TemporalAnalysisError(Exception):
    '''시간적 분석 관련 예외'''
    pass

TEMPORAL_PATTERNS = {
    'flashback_start': {
        'patterns_ko': [
            ('(\\d+)년\\s*전', 'years_ago'),
            ('수십\\s*년\\s*전', 'decades_ago'),
            ('몇\\s*년\\s*전', 'few_years_ago'),
            ('오래\\s*전', 'long_ago'),
            ('(\\d+)세\\s*때', 'age_at')],
        'keywords_ko': [
            '회상',
            '과거',
            '어린 시절',
            '젊은 시절',
            '그때',
            '옛날',
            '추억',
            '기억이 떠올',
            '그 시절',
            '그 해',
            '그 날',
            '과거로 돌아가',
            '되돌아가',
            '회고',
            '그리워하며',
            '전쟁터',
            '전쟁 중',
            '참전',
            '어렸을 때',
            '젊었을 때'],
        'priority': 10 },
    'flashback_end': {
        'patterns_ko': [
            ('다시\\s*(현재|오늘날|지금)', 'back_to_present'),
            ('(\\d+)년이?\\s*(지나|흘러)', 'years_passed'),
            ('세월이\\s*(지나|흘러)', 'time_passed'),
            ('시간이\\s*(지나|흘러)', 'time_passed')],
        'keywords_ko': [
            '현재로 돌아',
            '현실로 돌아',
            '지금은',
            '현재 시점',
            '오늘날',
            '지금 생각해보면',
            '현재의',
            '꿈에서 깨',
            '생각에서 빠져나',
            '추억에서 깨',
            '고개를 들어',
            '눈을 떴다',
            '정신을 차리',
            '노인이 된',
            '늙은',
            '주름진',
            '백발이 된'],
        'priority': 9 } }
AGE_ESTIMATION_DEFAULTS = {
    '어린 시절': 10,
    '어렸을 때': 10,
    '소년 시절': 12,
    '소녀 시절': 12,
    '청소년': 15,
    '젊은 시절': 25,
    '젊었을 때': 25,
    '청년': 25,
    '청춘': 25,
    '수십 년 전': 30,
    '몇 년 전': 5,
    '오래 전': 20 }

class TemporalAnalyzer:
    '''시간적 구조 분석기'''
    MAX_RETRIES = 2
    TIMEOUT_SECONDS = 25
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    
    async def analyze_temporal_structure(self, chapter_content = None, characters = None, model_type = None, api_key = ('standard', None, None), provider = ('chapter_content', str, 'characters', List[Dict], 'model_type', str, 'api_key', str, 'provider', Any, 'return', Dict[(str, Any)])):
        """
        전체 대본의 시간적 구조를 분석합니다.

        Args:
            chapter_content: 챕터 전체 내용
            characters: 캐릭터 정보 리스트 [{name, ageRange, gender, ...}]
            model_type: 모델 타입 ('standard' 또는 'pro-hq')
            api_key: Gemini API 키

        Returns:
            {
                'temporal_segments': [...],
                'detected_flashbacks': [...],
                'timeline_consistency_check': bool,
                'warnings': []
            }
        """
        pass
    # WARNING: Decompyle incomplete

    
    async def _analyze_with_retry(self, chapter_content = None, characters = None, model_type = None, api_key = (None,), provider = ('chapter_content', str, 'characters', List[Dict], 'model_type', str, 'api_key', str, 'provider', Any, 'return', Dict[(str, Any)])):
        '''재시도 로직 포함 AI 분석 (404 에러 시 즉시 fallback)'''
        pass
    # WARNING: Decompyle incomplete

    
    async def _call_ai_analysis(self, chapter_content = None, characters = None, model_type = None, api_key = (None,), provider = ('chapter_content', str, 'characters', List[Dict], 'model_type', str, 'api_key', str, 'provider', Any, 'return', Dict[(str, Any)])):
        '''AI API 호출 (provider 경유 → MediaGenerator의 _strip_property_ordering 적용)'''
        pass
    # WARNING: Decompyle incomplete

    
    def _extract_json_from_response(self = None, response = None):
        '''응답에서 JSON 추출'''
        if not response:
            raise ValueError('Empty response')
        last_error = None
        for candidate in self._collect_json_candidates(response):
            parsed = self._load_json_candidate(candidate)
        except json.JSONDecodeError:
            exc = None
            last_error = exc
            exc = None
            del exc
            continue
            exc = None
            del exc
        if isinstance(parsed, dict):
            
            return None, parsed
    # WARNING: Decompyle incomplete

    
    def _collect_json_candidates(self = None, response = None):
        if not response:
            text = str('').strip()
            if not text:
                return []
            candidates = [
                None]
            for match in re.finditer('```(?:json)?\\s*([\\s\\S]*?)\\s*```', text, flags = re.IGNORECASE):
                if not match.group(1):
                    block = str('').strip()
                    if block:
                        candidates.append(block)
                candidates.extend(self._extract_balanced_json_objects(text))
                deduped = []
                seen = set()
                for candidate in candidates:
                    if not candidate:
                        normalized = str('').strip()
                        if normalized or normalized in seen:
                            continue
                    seen.add(normalized)
                    deduped.append(normalized)
                    return deduped

    
    def _extract_balanced_json_objects(self = None, text = None):
        candidates = []
        start_index = None
        depth = 0
        in_string = False
        string_quote = ''
        escape_next = False
    # WARNING: Decompyle incomplete

    
    def _load_json_candidate(self = None, candidate_text = None):
        if not candidate_text:
            candidate = str('').strip().lstrip('﻿')
            candidate = re.sub('^\\s*json\\s*', '', candidate, flags = re.IGNORECASE).strip()
            candidate = candidate.rstrip(';').strip()
            if not candidate:
                if not candidate_text:
                    raise json.JSONDecodeError('Empty JSON candidate', '', 0)
        parse_attempts = [
            candidate,
            self._strip_trailing_commas(candidate)]
    # WARNING: Decompyle incomplete

    _strip_trailing_commas = (lambda text = None:
