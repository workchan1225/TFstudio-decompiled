# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: upload_title_generator.pyc (Python 3.11)

'''Script-backed title generation with event anchoring and coherence gates.'''
from __future__ import annotations
import json
import logging
import re
from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Literal, Optional, Sequence, Tuple
from app.services.scene.scene_script_unit_builder import build_chapter_sentence_units
from app.utils.google_sdk import configure_legacy_genai, is_legacy_sdk_available
from app.utils.thumbnail_guard import sanitize_thumbnail_hook_text
from app.utils.title_pattern_profile import build_title_style_instruction, compute_title_stimulus_score, get_aggressive_ratio, get_title_style_metadata, normalize_title_style_profile
logger = logging.getLogger(__name__)
TitleContext = Literal[('script_titles', 'youtube_metadata', 'thumbnail')]
_CHAPTER_LINE_PATTERN = re.compile('^\\s*\\[(?:챕터|chapter|장)\\s*(\\d+)(?:\\s*[:：]\\s*([^\\]]+))?\\]\\s*[:：]?\\s*(.*)$|^\\s*\\[(?:제\\s*)?(\\d+)장(?:\\s*[:：]\\s*([^\\]]+))?\\]\\s*[:：]?\\s*(.*)$', re.IGNORECASE)
_TOKEN_PATTERN = re.compile('[0-9]+|[A-Za-z]{2,}|[가-힣]{2,}')
_GENERIC_STOPWORDS = {
    '더',
    '전',
    '한',
    '후',
    '가장',
    '계속',
    '관련',
    '그것',
    '그녀',
    '그들',
    '까지',
    '내용',
    '다시',
    '대본',
    '대한',
    '대해',
    '됐다',
    '때문',
    '바로',
    '부터',
    '에게',
    '에서',
    '영상',
    '으로',
    '이건',
    '이미',
    '이번',
    '이후',
    '있는',
    '장면',
    '저건',
    '정도',
    '정말',
    '조금',
    '처럼',
    '통해',
    '하게',
    '하나',
    '하는',
    '하며',
    '하면',
    '했다',
    '그래서',
    '그러나',
    '그리고',
    '스토리',
    '이야기',
    '왜',
    '결국',
    '당장',
    '보니',
    '순간',
    '알고',
    '오늘',
    '이유',
    '지금',
    '진짜',
    '마지막',
    '몰랐던',
    '숨겨진',
    '하지만'}
_HOOK_STOPWORDS = {
    '전에',
    '왜',
    '결국',
    '경고',
    '늦기',
    '반전',
    '보니',
    '비밀',
    '순간',
    '알고',
    '이유',
    '지금',
    '진짜',
    '충격',
    '놓치면',
    '마지막',
    '몰랐던',
    '숨겨진'}
_CONFLICT_MARKERS = ('갈등', '대립', '싸움', '충돌', '위기', '문제', '실수', '사고', '붕괴', '파산', '배신', '오해', '무너', '끊', '잃', '위험', '경고', '혼란', '절망', '후회')
_REVERSAL_MARKERS = ('알고 보니', '인 줄 알았', '하지만', '그런데', '반전', '사실', '진실', '숨겨', '뒤집')
_LOSS_MARKERS = ('잃', '무너', '무너진', '파산', '위기', '붕괴', '끊', '떠나', '배신', '추락', '실패')
_SECRET_MARKERS = ('비밀', '숨겨', '몰랐', '진실', '정체', '배후', '내막', '실체')
_URGENCY_MARKERS = ('지금', '오늘', '당장', '늦기 전에', '마지막', '놓치면', '시간', '더 늦')
_EMOTION_MARKERS = ('눈물', '오열', '침묵', '분노', '충격', '절망', '후회', '공포', '두려움', '무너진')
_RELATIONSHIP_MARKERS = ('가족', '부모', '엄마', '아빠', '딸', '아들', '부부', '친구', '형제', '자식')
_EVENT_MIN_SCORE = 2.2
_DEFAULT_MODEL = 'gemini-2.5-flash'
_THUMBNAIL_MAX_LEN = 32
_START_WORD_SKIP = {
    '왜',
    '결국',
    '늦기',
    '알고',
    '지금',
    '진짜',
    '마지막',
    '숨겨진'}
_THUMBNAIL_FLOATING_POSITIONS = ('top-right', 'bottom-right', 'top-left', 'bottom-left')
_THUMBNAIL_FLOATING_BG = ('#111827', '#D90429', '#7E22CE', '#0F766E')
_THUMBNAIL_FLOATING_TEXT = ('#FFFFFF', '#FDE047', '#E5E7EB')
UploadTitleEventCard = <NODE:12>()
UploadTitleCandidate = <NODE:12>()
UploadTitleGenerationResult = <NODE:12>()

def generate_upload_title_result(source_text = None, *, count, genre, title_style_profile, title_style_mix, content_format, context, api_key, model_name):
