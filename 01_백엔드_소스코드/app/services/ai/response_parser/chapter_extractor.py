# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chapter_extractor.pyc (Python 3.11)

'''
Chapter Extractor

AI 응답에서 챕터 구조 추출.
google_provider.py의 JSON 파싱 및 챕터 분리 로직에서 분리.
'''
import re
import json
import logging
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
logger = logging.getLogger(__name__)
ChapterData = <NODE:12>()

class ChapterExtractor:
    '''
    챕터 추출기

    AI 응답에서 챕터 구조를 추출하고 파싱.
    JSON 형식과 마커 기반 형식 모두 지원.
    '''
    CHAPTER_PATTERNS = [
        '\\[(?:챕터|chapter|Chapter|장)\\s*(\\d+)\\](?:\\s*[:：]\\s*)?([^\\n]*)?',
        '(?:챕터|Chapter)\\s+(\\d+)\\s*[:：]\\s*([^\\n]+)',
        '(?:장|Chapter)\\s+(\\d+)\\s*[:：]\\s*([^\\n]+)']
    
    def __init__(self):
        '''초기화'''
        self._compiled_patterns = self.CHAPTER_PATTERNS()

    
    def extract_from_json(self = None, response_text = None):
        '''
        JSON 응답에서 챕터 추출

        Args:
            response_text: AI 응답 텍스트

        Returns:
            (챕터 리스트, 성공 여부)
        '''
        json_text = self._extract_json_block(response_text)
        if not json_text:
            return ([], False)
        
        try:
            data = json.loads(json_text)
            chapters_data = None
            if isinstance(data, dict):
                if 'chapters' in data:
                    chapters_data = data['chapters']
                elif 'script' in data and isinstance(data['script'], dict):
                    chapters_data = data['script'].get('chapters', [])
                elif 'result' in data and isinstance(data['result'], dict):
                    chapters_data = data['result'].get('chapters', [])
                elif isinstance(data, list):
                    chapters_data = data
            if not chapters_data:
                return ([], False)
            chapters = None
            for idx, chapter in enumerate(chapters_data):
                if isinstance(chapter, dict):
                    title = chapter.get('title', f'''챕터 {idx + 1}''')
                    title = re.sub('^:\\s*', '', title.strip())
                    content = chapter.get('content', chapter.get('text', ''))
                    speakers = self._extract_speakers_from_content(content)
                    chapters.append(ChapterData(title = title, content = content, index = idx, speakers = speakers))
                return (chapters, bool(chapters))
                except json.JSONDecodeError:
                    e = None
                    logger.warning(f'''JSON parse error: {e}''')
                    del e
                    return None
                    None = 
                    del e


    
    def extract_from_markers(self = None, response_text = None):
        '''
        마커 기반 텍스트에서 챕터 추출

        Args:
            response_text: AI 응답 텍스트

        Returns:
            (챕터 리스트, 성공 여부)
        '''
        if not response_text:
            return ([], False)
        chapters = None
        chapter_starts = []
        for pattern in self._compiled_patterns:
            for match in pattern.finditer(response_text):
                chapter_num = int(match.group(1))
                title = match.group(2).strip() if match.group(2) else f'''챕터 {chapter_num}'''
                title = re.sub('^:\\s*', '', title)
                chapter_starts.append({
                    'index': match.start(),
                    'end': match.end(),
                    'num': chapter_num,
                    'title': title })
                if not chapter_starts:
                    return ([], False)
                chapter_starts = (lambda .0: pass# WARNING: Decompyle incomplete
)(chapter_starts().values(), key = (lambda x: x['index']))
                for i, start_info in enumerate(chapter_starts):
                    content_start = start_info['end']
                    if i + 1 < len(chapter_starts):
                        content_end = chapter_starts[i + 1]['index']
                    else:
                        content_end = len(response_text)
                    content = response_text[content_start:content_end].strip()
                    speakers = self._extract_speakers_from_content(content)
                    chapters.append(ChapterData(title = start_info['title'], content = content, index = i, speakers = speakers))
                    return (chapters, bool(chapters))

    
    def extract_chapters(self = None, response_text = None):
        '''
        자동으로 적절한 방식으로 챕터 추출

        Args:
            response_text: AI 응답 텍스트

        Returns:
            챕터 리스트
        '''
        (chapters, success) = self.extract_from_json(response_text)
        if success:
            return chapters
        (chapters, success) = None.extract_from_markers(response_text)
        if success:
            return chapters
        return [
            None(title = '전체', content = self._clean_response_text(response_text), index = 0, speakers = self._extract_speakers_from_content(response_text))]

    
    def _extract_json_block(self = None, text = None):
        '''
        텍스트에서 JSON 블록 추출

        마크다운 코드 블록이나 순수 JSON 탐지.
        '''
        if not text:
            return None
        code_block_match = None.search('```(?:json)?\\s*([\\s\\S]*?)```', text)
        if code_block_match:
            return code_block_match.group(1).strip()
        json_match = None.search('(\\{[\\s\\S]*\\}|\\[[\\s\\S]*\\])', text)
        if json_match:
            return json_match.group(1)

    
    def _clean_response_text(self = None, text = None):
        '''응답 텍스트 정리'''
        if not text:
            return ''
        text = None.sub('```(?:json)?[\\s\\S]*?```', '', text)
        text = re.sub('\\n{3,}', '\n\n', text)
        return text.strip()

    
    def _extract_speakers_from_content(self = None, content = None):
        '''내용에서 화자 추출'''
        if not content:
            return []
        speakers = None()
        pattern = '\\[([^\\]]+)\\]\\s*:'
        for match in re.finditer(pattern, content):
            speaker = match.group(1).strip()
            if speaker and speaker.lower() not in ('chapters', 'title', 'content'):
                speakers.add(speaker)
            return list(speakers)

    
    def normalize_chapter_title(self = None, title = None, original_title = None):
