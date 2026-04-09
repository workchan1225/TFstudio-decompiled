# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_text_cleaner.pyc (Python 3.11)

'''
Script Text Cleaner - 대본 텍스트 정제 유틸리티

Google STT/TTS 자막 생성 시 화자 태그, 지문, 챕터 마커 등을 제거하여
순수 대사 내용만 추출합니다.

주요 기능:
- 화자 태그 제거: [나레이션]:, 민수: 등
- 챕터 마커 제거: [챕터 1], ## Chapter 1 등
- 지문/행동 지시 제거: (웃으며), (한숨) 등
- 따옴표 정제: "대사" → 대사
- 이모지/특수문자 제거: 😀, ★, ◆ 등

사용법:
    from app.utils.script_text_cleaner import clean_script_for_subtitle

    # 대본에서 자막용 텍스트 추출
    clean_text = clean_script_for_subtitle(script_text)

    # 화자 태그만 제거
    text_without_tags = remove_speaker_tags(script_text)
'''
import re
import logging
from typing import List, Optional
logger = logging.getLogger(__name__)
JSON_KEYWORDS = {
    'data',
    'http',
    'json',
    'name',
    'type',
    'error',
    'https',
    'title',
    'value',
    'format',
    'script',
    'status',
    'content',
    'chapters',
    'provider',
    'description'}
NON_SPEAKER_LABELS = {
    '경고',
    '공지',
    '답변',
    '문답',
    '알림',
    '정보',
    '주의',
    '중요',
    '질문',
    '참고',
    'q&a',
    'a',
    'q',
    'qa',
    'tip',
    'note',
    'answer',
    'notice',
    'warning',
    'question'}
_BRACKET_SPEAKER_PATTERN = re.compile('^\\[\\s*([^\\]]+?)\\s*\\]\\s*[:：]\\s*(.*)$')
_KEYWORD_SPEAKER_PATTERN = re.compile('^((?:나레이션|내레이션|화자|발화자|speaker|narrator|host|mc)(?:\\s*[-#]?\\s*[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_]+)?)\\s*[:：]\\s*(.*)$', re.IGNORECASE)
_PLAIN_SPEAKER_PATTERN = re.compile('^([가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9][가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{0,23})\\s*[:：]\\s*(.*)$')
_QUOTE_PATTERN = re.compile('^["\\\'""]+|["\'""]+$')

def _is_probable_speaker_label(label = None):
    '''라벨이 화자명으로 보이는지 판단'''
    if not label:
        return False
    candidate = None.strip()
    if candidate or len(candidate) > 30:
        return False
    candidate_lower = None.lower()
    if candidate_lower in JSON_KEYWORDS:
        return False
    if None in NON_SPEAKER_LABELS:
        return False
    if None.search('(?:챕터|chapter|part|scene|episode|ep)\\s*[0-9ivxlcdm]+', candidate_lower):
        return False
    if None.match('^(?:제\\s*)?\\d+\\s*(?:장|화|부|막)$', candidate):
        return False
    if None in candidate or "'" in candidate:
        return False


def remove_inline_speaker_tags(text = None):
    '''문장 중간에 섞인 화자 태그 제거 ([화자]:, Narrator 1: 등)'''
    if not text:
        return text
    result = None
    bracket_pattern = re.compile('(^|[\\s\\("\\\'“”‘’.,!?;:])\\[\\s*([^\\]]{1,30})\\s*\\]\\s*[:：]\\s*')
    
    def _replace_bracket(match = None):
        prefix = match.group(1)
        label = match.group(2).strip()
        if _is_probable_speaker_label(label):
            return prefix
        return None.group(0)

    result = bracket_pattern.sub(_replace_bracket, result)
    keyword_inline_pattern = re.compile('(^|[\\s\\("\\\'“”‘’.,!?;:])((?:나레이션|내레이션|화자|발화자|speaker|narrator|host|mc)(?:\\s*[-#]?\\s*[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_]+)?)\\s*[:：]\\s*', re.IGNORECASE)
    
    def _replace_keyword(match = None):
        prefix = match.group(1)
        label = match.group(2).strip()
        if _is_probable_speaker_label(label):
            return prefix
        return None.group(0)

    result = keyword_inline_pattern.sub(_replace_keyword, result)
    return result


def remove_inline_chapter_markers(text = None):
    '''문장 중간에 섞인 챕터/파트 마커 제거 ([챕터 1], [Scene 2] 등)'''
    if not text:
        return text
    result = None
    inline_patterns = [
        '\\[\\s*챕터\\s*\\d+(?:\\s*[:：][^\\]]*?)?\\s*\\]',
        '\\[\\s*chapter\\s*\\d+(?:\\s*[:：][^\\]]*?)?\\s*\\]',
        '\\[\\s*chap(?:ter)?\\.?\\s*\\d+(?:\\s*[:：][^\\]]*?)?\\s*\\]',
        '\\[\\s*(?:part|scene|episode|ep)\\s*[0-9ivxlcdm]+(?:\\s*[:：][^\\]]*?)?\\s*\\]',
        '\\[\\s*(?:제\\s*)?\\d+\\s*(?:장|화|부|막)(?:\\s*[:：][^\\]]*?)?\\s*\\]']
    for pattern in inline_patterns:
        result = re.sub(pattern, ' ', result, flags = re.IGNORECASE)
        result = re.sub('\\s{2,}', ' ', result)
        return result.strip()


def normalize_newlines(text = None):
    '''
    줄바꿈 정규화
    - \\n (이스케이프된 줄바꿈)을 실제 줄바꿈으로 변환
    - Windows CRLF를 LF로 변환

    Args:
        text: 원본 텍스트

    Returns:
        정규화된 텍스트
    '''
    if not text:
        return text
    text = None.replace('\\n', '\n')
    text = text.replace('\r\n', '\n')
    text = text.replace('\r', '\n')
    return text


def remove_speaker_tags(text = None):
    '''
    대본에서 화자 태그를 제거하고 대사만 추출

    지원 형식:
    - [화자명]: 대사 → 대사
    - 화자명: 대사 → 대사
    - [narration]: dialogue → dialogue

    Args:
        text: 화자 태그가 포함된 대본 텍스트

    Returns:
        화자 태그가 제거된 텍스트
    '''
    if not text:
        return text
    text = None(text)
    result_lines = []
    for line in text.split('\n'):
        stripped = line.strip()
        if not stripped:
            result_lines.append('')
            continue
        bracket_match = _BRACKET_SPEAKER_PATTERN.match(stripped)
        if bracket_match:
            speaker = bracket_match.group(1).strip()
            dialogue = bracket_match.group(2).strip()
            if not _is_probable_speaker_label(speaker):
                result_lines.append(stripped)
                continue
            result_lines.append(dialogue)
            continue
        keyword_match = _KEYWORD_SPEAKER_PATTERN.match(stripped)
        if keyword_match:
            speaker = keyword_match.group(1).strip()
            dialogue = keyword_match.group(2).strip()
            if not _is_probable_speaker_label(speaker):
                result_lines.append(stripped)
                continue
            result_lines.append(dialogue)
            continue
        plain_match = _PLAIN_SPEAKER_PATTERN.match(stripped)
        if plain_match:
            speaker = plain_match.group(1).strip()
            dialogue = plain_match.group(2).strip()
            if not _is_probable_speaker_label(speaker):
                result_lines.append(stripped)
                continue
            result_lines.append(dialogue)
            continue
        result_lines.append(stripped)
        result = '\n'.join(result_lines)
        result = re.sub('\\n{3,}', '\n\n', result)
        return result.strip()


def remove_chapter_markers(text = None):
    '''
    챕터 마커 제거

    지원 형식:
    - [챕터 N], [챕터N], [챕터]
    - [Chapter N], [chapter N], [chapter]
    - [N장], [장 N]
    - [파트 N], [Part N], [파트], [part]
    - 챕터 N:, 챕터 N (단독 줄)
    - ## 챕터 N (마크다운)

    Args:
        text: 챕터 마커가 포함된 텍스트

    Returns:
        챕터 마커가 제거된 텍스트
    '''
    pass
# WARNING: Decompyle incomplete


def remove_parenthetical_directions(text = None):
