# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_analyzer.pyc (Python 3.11)

'''
Script Analyzer

대본 분석 전문 모듈.
google_provider.py에서 분리.

v2.0: 장르별 분석 기준 시스템 통합
- 드라마 장르: 6단계 서사 구조, 심리학적 기제 검증
- 정보 장르: 리텐션 구조, 금지 표현, 공격적 훅 검증
'''
import re
import json
from typing import List, Dict, Any, Optional

try:
    from app.utils.script_genre_prompts import get_genre_analysis_prompt, get_genre_type, is_drama_genre, is_info_genre, validate_info_script
    GENRE_ANALYSIS_AVAILABLE = True
except ImportError:
    GENRE_ANALYSIS_AVAILABLE = False
    print('[ScriptAnalyzer] Warning: Genre analysis system not available')


class ScriptAnalyzer:
    '''
    스크립트 분석기

    대본의 논리적 일관성, 플롯 기법, 서사 구조 등을 분석.
    '''
    
    def __init__(self, genai, model):
        '''
        초기화

        Args:
            genai: Google Generative AI 인스턴스
            model: 기본 Gemini 모델
        '''
        self.genai = genai
        self.model = model

    
    def analyze_script(self, script, synopsis = None, chapter_info = None, model = None, previous_analysis = (None, None, None, None, None), genre = ('script', str, 'synopsis', str, 'chapter_info', list, 'model', str, 'previous_analysis', dict, 'genre', str, 'return', Dict[(str, Any)]), **kwargs):
        '''
        대본의 논리적 일관성, 플롯 기법, 서사 구조 등을 분석

        Args:
            script: 분석할 대본
            synopsis: 시놉시스 (참고용)
            chapter_info: 챕터 정보
            model: 사용할 모델
            previous_analysis: 이전 분석 결과 (비교용)
            genre: 장르 코드 (v2.0 - 장르별 분석 기준 적용)

        Returns:
            분석 결과 dict
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _split_script_for_analysis(self = None, script = None, max_chunk_size = None):
        '''하이브리드 방식으로 대본을 분석용 청크로 분할'''
        chunks = []
        chapter_pattern = '\\[챕터\\s*(\\d+)\\]'
        chapter_matches = list(re.finditer(chapter_pattern, script))
        if not chapter_matches:
            return self._split_by_size(script, max_chunk_size)
        current_chunk = {
            'content': None,
            'chapters': [],
            'chunk_index': 0 }
        for i, match in enumerate(chapter_matches):
            chapter_num = int(match.group(1))
            start_pos = match.start()
            if i + 1 < len(chapter_matches):
                end_pos = chapter_matches[i + 1].start()
            else:
                end_pos = len(script)
            chapter_content = script[start_pos:end_pos]
            if len(current_chunk['content']) + len(chapter_content) > max_chunk_size and current_chunk['content']:
                chunks.append(current_chunk)
                current_chunk = {
                    'content': chapter_content,
                    'chapters': [
                        chapter_num],
                    'chunk_index': len(chunks) }
                continue
            current_chunk['chapters'].append(chapter_num)
            if current_chunk['content']:
                chunks.append(current_chunk)
        if chapter_matches and chapter_matches[0].start() > 0:
            None[script:chapter_matches[0].start()].strip() = None
            if prefix:
                chunks[0]['content'] = prefix + '\n' + chunks[0]['content']
        return chunks

    
    def _split_by_size(self = None, script = None, max_size = None):
        '''글자수 기반 분할'''
        chunks = []
        paragraphs = script.split('\n\n')
        current = {
            'content': '',
            'chapters': [],
            'chunk_index': 0 }
        for para in paragraphs:
            if len(current['content']) + len(para) + 2 > max_size and current['content']:
                chunks.append(current)
                current = {
                    'content': para,
                    'chapters': [],
                    'chunk_index': len(chunks) }
                continue
            if current['content']:
                continue
            para = None
            if current['content']:
                chunks.append(current)
        return chunks

    
    def _analyze_single_chunk(self, chunk_content = None, synopsis = None, chapters = None, model_instance = (None,), genre = ('chunk_content', str, 'synopsis', str, 'chapters', list, 'genre', str, 'return', Dict[(str, Any)])):
        '''단일 청크 분석 (v2.0: 장르별 분석 기준 지원)'''
        
        try:
            chapter_str = ''
            if chapters:
                chapter_str = f'''\n(분석 대상 챕터: {', '.join(map(str, chapters))})\n'''
            genre_analysis_section = ''
            if genre and GENRE_ANALYSIS_AVAILABLE:
                genre_criteria = get_genre_analysis_prompt(genre)
                if genre_criteria:
                    genre_analysis_section = f'''\n## 장르별 분석 기준 ({genre}):\n{genre_criteria}\n'''
                    print(f'''[_analyze_single_chunk] Applied genre-specific criteria for: {genre}''')
            prompt_text = f'''당신은 전문 스토리 분석가입니다. 대본의 **서사 흐름과 구조**를 분석하고 JSON 형식으로 결과를 반환하세요.\n\n## 분석 대상 대본:\n{chunk_content}\n\n{f'''시놉시스 (참고용): {synopsis}''' if synopsis else ''}\n{chapter_str}\n\n## 분석 관점:\n### 1. 서사 흐름 분석\n- 서사 템포, 감정선 일관성, 정보 전달 타이밍\n\n### 2. 구조적 문제\n- 장면 전환, 인과관계, 캐릭터 동선\n\n### 3. 반복/중복\n- 의미 없는 장면/상황 반복\n\n### 4. 일관성 확인\n- 시간 순서, 설정 일관성\n{genre_analysis_section}\n## 응답 형식 (JSON만):\n{{\n  "overallScore": 0-100,\n  "issues": [\n    {{\n      "type": "서사 템포 불균형" | "감정선 단절" | "정보 전달 타이밍" | "장면 전환 문제" | "인과관계 오류" | "시간순서 오류" | "설정 모순" | "캐릭터 불일치" | "구조적 반복" | "장르 부적합",\n      "severity": "high" | "medium" | "low",\n      "chapter": 챕터 번호 또는 null,\n      "location": "문제 위치 요약",\n      "description": "문제 설명",\n      "suggestion": "개선 방향"\n    }}\n  ],\n  "strengths": ["강점1", "강점2"],\n  "structureAnalysis": {{\n    "introduction": "도입부 평가",\n    "development": "전개부 평가",\n    "crisis": "위기 평가",\n    "climax": "클라이맥스 평가",\n    "resolution": "결말 평가"\n  }},\n  "characterConsistency": [\n    {{"character": "캐릭터명", "score": 0-100, "note": "평가"}}\n  ],\n  "genreCompliance": {{\n    "score": 0-100,\n    "notes": "장르 적합성 평가"\n  }}\n}}'''
            response = model_instance.generate_content(prompt_text, generation_config = {
                'temperature': 0.1,
                'top_p': 0.9,
                'max_output_tokens': 50000 })
            content = response.text.strip()
            if '```json' in content:
                content = content.split('```json')[1].split('```')[0].strip()
            elif '```' in content:
                content = content.split('```')[1].split('```')[0].strip()
            return json.loads(content)
        except Exception:
            e = None
            print(f'''Google Gemini API Error (_analyze_single_chunk): {e}''')
            del e
            return None
            None = 
            del e


    
    def _merge_analysis_results(self = None, partial_results = None, genre = None):
