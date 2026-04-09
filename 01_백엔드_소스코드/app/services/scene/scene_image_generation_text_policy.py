# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_image_generation_text_policy.pyc (Python 3.11)

from typing import Any, Dict, List, Optional
from scene_image_generation_types import SceneImageGenerationTextPolicy

def extract_keyword_tokens(keyword_text_config = None):
    if not isinstance(keyword_text_config, dict):
        return []
    raw_keywords = None.get('keywords')
    if isinstance(raw_keywords, str):
        candidates = [
            raw_keywords]
    elif isinstance(raw_keywords, (list, tuple, set)):
        candidates = list(raw_keywords)
    else:
        candidates = []
    cleaned_keywords = []
    seen = set()
    for candidate in candidates:
        if not candidate:
            keyword = str('').strip()
            if not keyword:
                continue
        keyword = ' '.join(keyword.split())
        dedupe_key = keyword.lower()
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)
        cleaned_keywords.append(keyword)
        return cleaned_keywords


def has_keyword_text_mode_enabled(include_keyword_text = None, keyword_text_config = None):
