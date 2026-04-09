# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_prompt_postprocessor.pyc (Python 3.11)

'''
Scene prompt post-processing helpers.
'''
import re
from typing import Any, Dict
from scene_generation_prompt_blocks import build_keyword_exact_once_rule_lines
_KEYWORD_PARTICLE_SUFFIX_REGEX = re.compile('(?:에서|으로|에게|처럼|보다|까지|부터|은|는|이|가|을|를|와|과|도|만|의|에)$')
_KEYWORD_META_STOPWORDS = {
    '챕',
    'end',
    'scene',
    'start',
    'action',
    'chapter',
    'context',
    'subject',
    'environment',
    '챕터',
    '도입부',
    '시작부',
    '페이지'}

def _sanitize_keyword_for_scene_text(raw_keyword = None):
    pass
# WARNING: Decompyle incomplete


def build_keyword_suffix(include_keyword_text = None, keyword_text_config = None):
    if not include_keyword_text or keyword_text_config:
        return {
            'suffix': '',
            'keywords': [],
            'position': 'center' }
    raw_keywords = None.get('keywords', [])
    if isinstance(raw_keywords, str):
        raw_keywords = [
            raw_keywords]
    cleaned_keywords = []
    seen = set()
    if not raw_keywords:
        for raw_keyword in []:
            keyword = _sanitize_keyword_for_scene_text(raw_keyword)
            if not keyword:
                continue
            if len(keyword) > 14:
                keyword = keyword[:14].strip()
            if len(keyword) < 2:
                continue
            dedupe_key = keyword.lower()
            if dedupe_key in seen:
                continue
            cleaned_keywords.append(keyword)
            seen.add(dedupe_key)
            if len(cleaned_keywords) >= 3:
                pass
            
            if not cleaned_keywords:
                return {
                    'suffix': '',
                    'keywords': [],
                    'position': keyword_text_config.get('position', 'center') }
            position = None(keyword_text_config.get('position', 'center')).strip().lower()
            position_frame_hints = {
                'top': 'in an upper-left or upper-right area (never dead-center)',
                'center': 'in a side-third area (left or right), never in the exact center',
                'bottom': 'in a lower-left or lower-right area, avoiding exact center' }
            if position not in position_frame_hints:
                position = 'center'
    frame_position = position_frame_hints[position]
    quoted_keywords = (lambda .0: pass# WARNING: Decompyle incomplete
)(cleaned_keywords())
    distribution_rule = 'If multiple keywords are requested, assign one carrier per keyword and place each keyword on a different small physical object/surface in different positions; never cluster all keywords on one sign. ' if len(cleaned_keywords) >= 2 else ''
    exact_once_rule = ' '.join(build_keyword_exact_once_rule_lines())
    suffix = f'''. [TEXT_CONTENT]: Render these exact Korean keywords once each: {quoted_keywords}. [TEXT_PLACEMENT]: Place the keyword text {frame_position} on a small physical in-world surface near the main action. [TEXT RENDER LOCK] {exact_once_rule} Do not omit, merge, paraphrase, replace, or expand them. Do not invent extra numbers, percentages, units, or supporting labels. Keep each keyword horizontal and fully legible (no split Hangul syllables). [CRITICAL - TEXT MUST BE INSIDE FRAME] The text-bearing object MUST be positioned clearly WITHIN the visible frame, not at edges or outside. Text should support the scene, not dominate the entire frame. Keep the main character/action as the visual focus. Never place keyword text at dead-center, and never cover the main character\'s face/body. [TEXT_HOLDER_OBJECT REQUIREMENT] Text MUST appear ON a physical object that exists in the scene world. {distribution_rule}Examples: plaque, notice card, desk label, pinned note, monitor corner label. [STRICTLY FORBIDDEN] NEVER render: floating text, subtitle bars, caption overlays, watermarks, UI elements, ticker text. NEVER place text in sky, empty space, or outside the frame boundaries. NEVER render text that looks like post-production addition or digital overlay. Never render character names or @mentions as visible text. NEVER render square-bracket metadata or control tokens such as [Context], [Scene], [Subject], [Action], [Environment]. NEVER render chapter/page markers (e.g., 챕터, 페이지) unless explicitly requested as a keyword. [TEXT_CONTENT_AND_STYLE] Render 1-3 short Korean noun keywords exactly as provided. Text must match the perspective, lighting, and material of its host surface. If the scene lacks suitable surfaces, ADD a plausible in-world sign or display to carry the text.'''
    return {
        'suffix': suffix,
        'keywords': cleaned_keywords,
        'position': position }


def truncate_prompt_with_suffix_budget(prompt = None, keyword_suffix = None, max_prompt_length = None):
    pass
# WARNING: Decompyle incomplete
