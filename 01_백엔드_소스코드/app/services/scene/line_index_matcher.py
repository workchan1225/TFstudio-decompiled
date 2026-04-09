# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: line_index_matcher.pyc (Python 3.11)

'''
Scene line-index matching utilities.

Responsibilities:
- Normalize mixed keywordText payloads (str/dict/list) into matchable text.
- Match scene narration/anchors to chapter dialogue line ranges.
- Provide deterministic even-split fallback range allocation.
'''
import re
from difflib import SequenceMatcher
from typing import Any, Dict, List, Optional, Set
_STOPWORDS: Set[str] = {
    '가',
    '과',
    '는',
    '도',
    '로',
    '를',
    '만',
    '에',
    '와',
    '은',
    '을',
    '의',
    '이',
    '같이',
    '까지',
    '부터',
    '에서',
    '으로',
    '처럼',
    '그리고',
    'a',
    'an',
    'in',
    'of',
    'on',
    'or',
    'to',
    'and',
    'for',
    'the',
    'with'}
_WINDOW_MATCH_MAX_SIZE = 6
_WINDOW_ONLY_MATCH_MIN_SCORE = 0.5

def normalize_keyword_text_for_matching(raw_keyword_text = None):
    '''Convert keywordText payloads into a single plain string for matching.'''
    pass
# WARNING: Decompyle incomplete


def _normalize_for_match(text = None):
    pass
# WARNING: Decompyle incomplete


def _extract_tokens(text = None):
    pass
# WARNING: Decompyle incomplete


def _build_context_sentences(match_context = None, normalized_context = None):
    context_sentences = []
    for sentence in re.split('[\\n.!?。！？]+', match_context):
        normalized_sentence = _normalize_for_match(sentence)
        if normalized_sentence:
            context_sentences.append(normalized_sentence)
        if normalized_context and normalized_context not in context_sentences:
            context_sentences.append(normalized_context)
    return context_sentences


def _score_match_text(candidate_text = None, *, normalized_context, context_sentences, context_tokens, keyword_tokens):
    pass
# WARNING: Decompyle incomplete


def _find_best_window_match(chapter_lines = None, *, start_search_idx, normalized_context, context_sentences, context_tokens, keyword_tokens):
    best_window = None
    if start_search_idx < 0 or start_search_idx >= len(chapter_lines):
        return None
# WARNING: Decompyle incomplete


def calculate_line_index_range_for_scene(narration_text, chapter_index = None, dialogue_lines = None, previous_scene_end_line_index = None, anchor_sentence = (-1, '', ''), keyword_text = ('narration_text', str, 'chapter_index', int, 'dialogue_lines', List[Dict[(str, Any)]], 'previous_scene_end_line_index', int, 'anchor_sentence', str, 'keyword_text', Any, 'return', Dict[(str, int)])):
    """Calculate lineIndex range matched to a scene's narration context."""
    pass
# WARNING: Decompyle incomplete


def build_even_line_index_range(chapter_lines = None, scene_index = None, total_scene_count = None):
    '''Estimate deterministic line range by evenly splitting chapter lines.'''
    if chapter_lines and total_scene_count < 1 or scene_index < 0:
        return { }
    total_lines = None(chapter_lines)
    lines_per_scene = total_lines // total_scene_count
    remainder = total_lines % total_scene_count
    start_idx = 0
    for i in range(scene_index):
        start_idx += lines_per_scene + 1 if i < remainder else 0
    scene_lines = lines_per_scene + 1 if scene_index < remainder else 0
    if scene_index == total_scene_count - 1:
        end_idx = total_lines - 1
    else:
        end_idx = start_idx + scene_lines - 1
    if start_idx >= total_lines:
        return { }
    start_line = None[start_idx].get('lineIndex')
    end_line = chapter_lines[min(end_idx, total_lines - 1)].get('lineIndex')
    if not isinstance(start_line, int) or isinstance(end_line, int):
        return { }
    return {
        'start': None,
        'end': end_line }
