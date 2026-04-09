# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_anchor_metadata.pyc (Python 3.11)

'''
Canonical scene anchor metadata helpers.

These helpers turn AI scene payloads into canonical, source-backed metadata that
downstream consumers can trust more than free-form narration text.
'''
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from scene_script_unit_builder import build_chapter_sentence_units, infer_sentence_range_from_anchor, normalize_sentence_range, select_sentence_units_for_range

def _normalize_line_index_range(line_index_range = None):
    if not isinstance(line_index_range, dict):
        return { }
    start = None.get('start')
    end = line_index_range.get('end')
    if not isinstance(start, int) or isinstance(end, int):
        return { }
    if None > end:
        end = start
        start = end
    return {
        'start': start,
        'end': end }


def _build_script_unit_selection(*, chapter_index, chapter_content, sentence_range, fallback_anchor_sentence, fallback_narration_text):
    sentence_units = build_chapter_sentence_units(chapter_index, chapter_content)
    normalized_sentence_range = normalize_sentence_range(sentence_range, len(sentence_units))
    anchor_source = 'chapter_sentence_range'
    if not normalized_sentence_range:
        normalized_sentence_range = infer_sentence_range_from_anchor(anchor_sentence = fallback_anchor_sentence, narration_text = fallback_narration_text, sentence_units = sentence_units)
        if normalized_sentence_range:
            anchor_source = 'anchor_sentence_match'
        else:
            anchor_source = 'scene_payload'
    selected_units = select_sentence_units_for_range(sentence_units, normalized_sentence_range)
    return {
        'sentenceUnits': sentence_units,
        'selectedUnits': selected_units,
        'sentenceRange': normalized_sentence_range,
        'anchorSource': anchor_source,
        'canonicalTextApplied': bool(selected_units) }


def derive_canonical_scene_text(chapter_content = None, sentence_range = None, fallback_narration_text = None, fallback_anchor_sentence = ('chapter_content', 'str', 'sentence_range', 'Any', 'fallback_narration_text', 'str', 'fallback_anchor_sentence', 'str', 'return', 'Tuple[str, str, Dict[str, int], bool]')):
