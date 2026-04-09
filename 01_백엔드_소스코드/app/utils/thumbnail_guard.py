# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thumbnail_guard.pyc (Python 3.11)

'''
Thumbnail generation guard helpers.

These helpers keep reference thumbnails style-only, derive concise hook text,
and validate generated thumbnails for reference text leakage and low-signal text.
'''
from __future__ import annotations
import difflib
import re
from typing import Any, Dict, Iterable, List, Sequence
YEAR_PATTERN = re.compile('(?<!\\d)(?:19|20)\\d{2}(?:\\s*[./-]\\s*\\d{1,2}){0,2}(?:\\s*년|\\s*월|\\s*일)?(?!\\d)')
DATE_PATTERN = re.compile('(?<!\\d)\\d{1,2}\\s*월\\s*\\d{1,2}\\s*일(?!\\d)')
SOURCE_PREFIX_PATTERN = re.compile('^\\s*(?:보고서|리포트|출처|자료|속보|단독|특보|브리핑|보도|발표|제보|공식)\\s*[:：]\\s*', re.IGNORECASE)
BRACKETED_SOURCE_PATTERN = re.compile('^\\s*[\\[(【<][^)\\]】>]{0,20}(?:출처|자료|공식|속보|보고서|뉴스)[^)\\]】>]{0,20}[)\\]】>]\\s*', re.IGNORECASE)
MULTISPACE_PATTERN = re.compile('\\s+')
PUNCT_SPLIT_PATTERN = re.compile('[|:/\\n\\r\\-]+|[?？！!]+')
QUOTES_PATTERN = re.compile('[\\"“”‘’]')
GENERIC_NOISE_TERMS = ('국립기상과학원', '기상청', 'weather', 'report', 'official', 'source', 'thumbnail')
HOOK_PRIORITY_TERMS = ('위기', '위험', '붕괴', '배신', '폭로', '경고', '잃', '무너', '태풍', '파산', '삭제', '고백', '마지막', '이유', '왜', '더', '결국', '알고', '뒤집')
STOPWORDS = {
    '같은',
    '그런',
    '대체',
    '대한',
    '되는',
    '없는',
    '에게',
    '에서',
    '으로',
    '이런',
    '있는',
    '저런',
    '정말',
    '진짜',
    '하는',
    '그러나',
    '그리고',
    '하지만',
    '왜'}
TEXT_ISSUE_TYPES = {
    'extraneous_text',
    'text_duplication',
    'year_or_date_leak',
    'reference_text_leak',
    'invalid_hook_sentence',
    'reference_visual_copy',
    'reference_text_similarity_leak'}
THUMBNAIL_HOOK_TEXT_MAX_LENGTH = 40
NON_BLOCKING_ISSUE_TYPES = {
    'weak_situation_clarity'}
TOKEN_PATTERN = re.compile('[A-Za-z0-9가-힣]+')
VISUAL_TERM_STOPWORDS = {
    'close-up',
    'bold',
    'mood',
    'text',
    'close',
    'large',
    'scene',
    'style',
    'layout',
    'object',
    'people',
    'person',
    'cartoon',
    'closeup',
    'objects',
    'setting',
    'subject',
    'dramatic',
    'lighting',
    'character',
    'thumbnail',
    'background',
    'characters',
    'composition',
    'illustration',
    'professional',
    'photorealistic'}

def _normalize_text(value = None):
