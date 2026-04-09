# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shorts_analyzer.pyc (Python 3.11)

'''
Shorts Highlight Analyzer

Gemini API를 사용하여 자막 텍스트에서 YouTube Shorts에 적합한
하이라이트 구간을 분석하고 추출합니다.
'''
import json
import re
import uuid
from typing import List, Dict, Any, Optional
from app.utils.google_sdk import get_legacy_genai, configure_legacy_genai

class ShortsHighlightAnalyzer:
    '''
    쇼츠 하이라이트 분석기

    자막 텍스트를 분석하여 감정적 장면, 핵심 대사, 클라이맥스 등을
    자동으로 식별합니다.
    '''
    CRITERIA_DESCRIPTIONS = {
        'emotional': '감정적으로 강렬한 장면 (슬픔, 기쁨, 분노, 감동 등)',
        'key_dialogue': '스토리의 핵심이 되는 중요한 대사',
        'climax': '긴장감이 최고조에 달하는 클라이맥스 장면',
        'comedy': '재미있거나 유머러스한 장면',
        'action': '역동적이거나 액션이 있는 장면',
        'twist': '반전이나 놀라운 전개가 있는 장면' }
    
    def __init__(self = None, api_key = None, model = None):
        '''
        초기화

        Args:
            api_key: Google API 키
            model: 사용할 Gemini 모델
        '''
        self.api_key = api_key
        self.model_name = model
        self._configure_genai()

    
    def _configure_genai(self):
        '''Gemini API 설정'''
        configure_legacy_genai(self.api_key)
        genai = get_legacy_genai()
        self.model = genai.GenerativeModel(self.model_name)

    
    def analyze(self, subtitle_text, total_duration, min_duration = None, max_duration = None, count = None, criteria = (15, 60, 3, None, None), custom_prompt = ('subtitle_text', str, 'total_duration', float, 'min_duration', int, 'max_duration', int, 'count', int, 'criteria', List[str], 'custom_prompt', str, 'return', List[Dict[(str, Any)]])):
        '''
        자막 텍스트에서 하이라이트 구간 분석

        Args:
            subtitle_text: 타임스탬프가 포함된 자막 텍스트
            total_duration: 전체 영상 길이 (초)
            min_duration: 최소 쇼츠 길이 (초)
            max_duration: 최대 쇼츠 길이 (초)
            count: 추출할 하이라이트 개수
            criteria: 분석 기준 리스트
            custom_prompt: 사용자 커스텀 편집 방향 (예: "코미디 하이라이트만 추출해줘")

        Returns:
            하이라이트 구간 리스트
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_response(self = None, response_text = None, expected_count = None):
        '''
        Gemini 응답 파싱

        Args:
            response_text: Gemini API 응답 텍스트
            expected_count: 예상 하이라이트 개수

        Returns:
            파싱된 하이라이트 리스트
        '''
        json_match = re.search('```json\\s*(.*?)\\s*```', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            json_match = re.search('\\{[\\s\\S]*"highlights"[\\s\\S]*\\}', response_text)
            if json_match:
                json_str = json_match.group(0)
            else:
                print(f'''[ShortsHighlightAnalyzer] No JSON found in response: {response_text[:500]}''')
                return []
            
            try:
                data = json.loads(json_str)
                highlights = data.get('highlights', [])
                result = []
                for idx, h in enumerate(highlights[:expected_count]):
                    unique_id = f'''h{idx + 1}_{uuid.uuid4().hex[:8]}'''
                    highlight = {
                        'id': unique_id,
                        'start_time': h.get('start_time', '00:00:00'),
                        'end_time': h.get('end_time', '00:00:30'),
                        'start_seconds': self._time_to_seconds(h.get('start_time', '00:00:00')),
                        'end_seconds': self._time_to_seconds(h.get('end_time', '00:00:30')),
                        'score': float(h.get('score', 0.5)),
                        'type': h.get('type', 'unknown'),
                        'reason': h.get('reason', ''),
                        'transcript': h.get('transcript', '')[:100] }
                    result.append(highlight)
                    return result
                    except json.JSONDecodeError:
                        e = None
                        print(f'''[ShortsHighlightAnalyzer] JSON parse error: {e}''')
                        print(f'''[ShortsHighlightAnalyzer] Raw JSON: {json_str[:500]}''')
                        del e
                        return None
                        None = 
                        del e


    _time_to_seconds = (lambda time_str = None: try:
parts = time_str.split(':')if len(parts) == 3:
hours = int(parts[0])minutes = int(parts[1])seconds = float(parts[2])hours * 3600 + minutes * 60 + secondsif None(parts) == 2:
minutes = int(parts[0])seconds = float(parts[1])minutes * 60 + secondsNone(time_str)except (ValueError, IndexError):
0)()
    
    def analyze_with_context(self = None, subtitle_text = None, total_duration = None, genre = (None, None), target_audience = ('subtitle_text', str, 'total_duration', float, 'genre', str, 'target_audience', str, 'return', List[Dict[(str, Any)]]), **kwargs):
        '''
        장르 및 타겟 오디언스를 고려한 분석

        Args:
            subtitle_text: 자막 텍스트
            total_duration: 전체 영상 길이
            genre: 콘텐츠 장르 (드라마, 코미디, 다큐멘터리 등)
            target_audience: 타겟 오디언스 (일반, 10대, 성인 등)
            **kwargs: 추가 분석 옵션

        Returns:
            하이라이트 구간 리스트
        '''
        genre_criteria_map = {
            'drama': [
                'emotional',
                'key_dialogue',
                'climax'],
            'comedy': [
                'comedy',
                'key_dialogue'],
            'documentary': [
                'key_dialogue',
                'climax'],
            'action': [
                'action',
                'climax',
                'twist'],
            'horror': [
                'climax',
                'twist',
                'emotional'],
            'romance': [
                'emotional',
                'key_dialogue'] }
        criteria = kwargs.get('criteria')
    # WARNING: Decompyle incomplete
