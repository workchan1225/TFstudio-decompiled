# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_analyzer_service.pyc (Python 3.11)

'''
Script Analyzer Service - Gemini AI를 사용한 대본 분석 및 형식 변환
'''
import re
import time
from collections import defaultdict
from app.utils.google_sdk import configure_legacy_genai
from app.models.settings import Settings
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from app.utils.speaker_normalizer import canonicalize_speaker_name as _canonicalize_speaker_name_util, is_likely_metadata_speaker_label as _is_likely_metadata_speaker_label_util
CHAPTER_MARKER_PATTERN = re.compile('^\\s*\\[(?:챕터|chapter|장)\\s*(\\d+)(?:\\s*[:：]\\s*([^\\]]+))?\\]\\s*[:：]?\\s*(.*)$|^\\s*\\[(?:제\\s*)?(\\d+)장(?:\\s*[:：]\\s*([^\\]]+))?\\]\\s*[:：]?\\s*(.*)$', re.IGNORECASE | re.MULTILINE)
CHAPTER_LINE_PATTERN = re.compile('^\\s*\\[(?:챕터|chapter|장)\\s*\\d+(?:\\s*[:：][^\\]]+)?\\]\\s*[:：]?\\s*.*$|^\\s*\\[(?:제\\s*)?\\d+장(?:\\s*[:：][^\\]]+)?\\]\\s*[:：]?\\s*.*$|^\\s*(?:챕터|chapter)\\s*\\d+\\s*[:：]\\s*.+$|^\\s*(?:제\\s*)?\\d+장\\s*[:：]\\s*.+$|^\\s*\\[(?:챕터|chapter|파트|part)\\]\\s*[:：]\\s*.+$', re.IGNORECASE)
SCRIPT_UPLOAD_ANALYZER_MODEL = 'gemini-2.5-flash'

class ScriptAnalyzerService:
    '''
    대본 분석 및 화자 태그 형식 변환 서비스

    주요 기능:
    - 대본에서 화자 추출
    - 다양한 형식을 표준 [화자명]: 대사 형식으로 변환
    '''
    
    def __init__(self = None, api_key = None):
        '''Initialize with Gemini API'''
        settings = Settings.get_or_create()
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = get_google_api_key_or_runtime_token(settings = settings)
        if not self.api_key:
            raise ValueError(get_google_configuration_error_message(settings = settings))
        self.genai = configure_legacy_genai(self.api_key)
        model_name = SCRIPT_UPLOAD_ANALYZER_MODEL
        self.model = self.genai.GenerativeModel(model_name)

    
    def _is_chapter_marker_line(self = None, line = None):
        '''
        주어진 줄이 챕터 마커인지 확인

        지원 형식:
        - [챕터 N]: 제목  또는  [챕터 N: 제목]
        - [chapter N]: Title
        - [N장]: 제목  또는  [제 N장]: 제목
        '''
        if not line or line.strip():
            return False
        return None(CHAPTER_LINE_PATTERN.match(line.strip()))

    
    def _extract_chapter_markers(self = None, script = None):
        '''
        대본에서 챕터 마커를 추출하고 플레이스홀더로 대체

        Returns:
            tuple: (챕터 마커가 플레이스홀더로 대체된 대본, {줄번호: 원본 챕터 마커})
        '''
        lines = script.split('\n')
        chapter_markers = { }
        processed_lines = []
        for i, line in enumerate(lines):
            if self._is_chapter_marker_line(line):
                chapter_markers[i] = line
                processed_lines.append(f'''___CHAPTER_MARKER_{i}___''')
                print(f'''[ScriptAnalyzerService] 챕터 마커 추출: line {i} = {line.strip()[:50]}''')
                continue
            processed_lines.append(line)
            return ('\n'.join(processed_lines), chapter_markers)

    
    def _restore_chapter_markers(self = None, script = None, chapter_markers = None):
        '''
        플레이스홀더를 원본 챕터 마커로 복원
        '''
        if not chapter_markers:
            return script
        result = None
        for line_num, original_marker in chapter_markers.items():
            placeholder = f'''___CHAPTER_MARKER_{line_num}___'''
            pattern = f'''\\[[^\\]]+\\]\\s*[:：]\\s*{re.escape(placeholder)}|{re.escape(placeholder)}'''
            result = re.sub(pattern, original_marker.strip(), result)
            print(f'''[ScriptAnalyzerService] 챕터 마커 복원: {original_marker.strip()[:50]}''')
            return result

    
    def _clean_chapter_narration_prefix(self = None, script = None):
        '''
        챕터 마커에 잘못 추가된 [나레이션]: 접두사 제거

        지원 형식:
        - [나레이션]: 챕터1: 제목 → [챕터1]: 제목
        - [나레이션]: chapter 1: Title → [chapter 1]: Title
        - [나레이션]: 1장: 제목 → [1장]: 제목
        - [나레이션]: 제1장: 제목 → [제1장]: 제목
        '''
        lines = script.split('\n')
        result = []
        pattern_chapter = re.compile('^\\[나레이션\\]\\s*[:：]\\s*(?:\\[)?(챕터|chapter)\\s*(\\d+)\\s*[:：]?\\s*(.*)$', re.IGNORECASE)
        pattern_jang = re.compile('^\\[나레이션\\]\\s*[:：]\\s*(?:\\[)?(제\\s*)?(\\d+)장\\s*[:：]?\\s*(.*)$', re.IGNORECASE)
        for line in lines:
            stripped = line.strip()
            match = pattern_chapter.match(stripped)
            if match:
                keyword = match.group(1)
                num = match.group(2)
                rest = match.group(3).strip()
                if rest:
                    result.append(f'''[{keyword}{num}]: {rest}''')
                else:
                    result.append(f'''[{keyword}{num}]''')
                print(f'''[ScriptAnalyzerService] 챕터 접두사 제거: {stripped[:50]} → {result[-1]}''')
                continue
            match = pattern_jang.match(stripped)
            if match:
                if not match.group(1):
                    prefix = ''
                    num = match.group(2)
                    rest = match.group(3).strip()
                chapter_label = f'''{prefix.strip()}{num}장''' if prefix else f'''{num}장'''
                if rest:
                    result.append(f'''[{chapter_label}]: {rest}''')
                else:
                    result.append(f'''[{chapter_label}]''')
                print(f'''[ScriptAnalyzerService] 챕터 접두사 제거: {stripped[:50]} → {result[-1]}''')
                continue
            result.append(line)
            return self._merge_speaker_tag_only_lines('\n'.join(result))

    
    def _canonicalize_speaker_name(self = None, speaker = None):
        '''
        화자명을 정규화하여 유사 표기(na레이션, narration, 내레이션 등)를 하나로 통일

        Note: 실제 로직은 app.utils.speaker_normalizer 모듈에서 공유됨
        '''
        return _canonicalize_speaker_name_util(speaker)

    
    def _is_likely_metadata_speaker_label(self = None, speaker = None, value = None):
        '''
        화자명이 메타데이터 키(예: 결제금액, title)일 가능성이 높은지 판별

        Note: 실제 로직은 app.utils.speaker_normalizer 모듈에서 공유됨
        '''
        return _is_likely_metadata_speaker_label_util(speaker, value)

    
    def _remove_parenthetical_stage_directions(self = None, text = None):
        '''
        대사 내 지문성 괄호 표현((웃으며), (한숨), (속으로) 등) 제거
        '''
        if not text:
            return ''
        cleaned = None
        cleaned = re.sub('\\((?:혼잣말로|속으로|조용히|천천히|급히|빠르게|느리게|작게|크게|낮게|높게)\\)', '', cleaned)
        cleaned = re.sub('\\([가-힣\\s]{1,15}(?:으며|며|면서)\\)', '', cleaned)
        cleaned = re.sub('\\([가-힣\\s]{1,15}(?:하다|한다|했다|치다|보다|듣다|먹다|마시다|걷다|뛰다|앉다|서다|눕다|열다|닫다|잡다|놓다|받다|주다|가다|오다|쉬다|자다|깨다)\\)', '', cleaned)
        cleaned = re.sub('\\((?:한숨|웃음|침묵|기침|신음|탄식|울음|비명|놀람|분노|슬픔|기쁨|당황|긴장|불안|초조|절망|희망|미소|눈물|한탄|고민|생각|회상|상상)\\)', '', cleaned)
        cleaned = re.sub('\\s{2,}', ' ', cleaned).strip()
        return cleaned

    
    def _remove_parenthetical_stage_directions_in_script(self = None, script = None):
        '''
        스크립트 전체에서 지문성 괄호 표현을 제거한다.
        '''
        if not script:
            return script
        lines = None.split('\n')
        cleaned_lines = []
        for line in lines:
            stripped = line.strip()
            if not stripped:
                cleaned_lines.append(line)
                continue
            if stripped.startswith('___CHAPTER_MARKER_') and stripped.endswith('___'):
                cleaned_lines.append(line)
                continue
            if self._is_chapter_marker_line(stripped):
                cleaned_lines.append(line)
                continue
            match = re.match('^(\\s*)\\[([^\\]]+)\\]\\s*[:：]\\s*(.*)$', line)
            if not match:
                cleaned_dialogue = self._remove_parenthetical_stage_directions(stripped)
                if cleaned_dialogue:
                    cleaned_lines.append(cleaned_dialogue)
                continue
            indent = match.group(1)
            speaker = self._canonicalize_speaker_name(match.group(2).strip())
            if not match.group(3):
                dialogue = self._remove_parenthetical_stage_directions(''.strip())
                if not dialogue:
                    continue
            cleaned_lines.append(f'''{indent}[{speaker}]: {dialogue}''')
            return '\n'.join(cleaned_lines)

    
    def _is_likely_non_dialogue_line_for_tag_merge(self = None, line = None):
