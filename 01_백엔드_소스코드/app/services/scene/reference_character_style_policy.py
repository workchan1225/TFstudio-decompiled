# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reference_character_style_policy.pyc (Python 3.11)

from typing import Any, Dict, Iterable, List, Optional, Set
from utils.character_name_matcher import normalize_character_name
from reference_policy import REPLACEMENT_SCOPE_FULL_LOOK
_STYLE_CONSISTENCY_NEGATIVE_MARKERS = ('inconsistent art style', 'mixed art styles', 'style variation', 'different rendering styles', 'changing visual style', 'inconsistent character rendering', 'character style drift', 'different character rendering styles', 'changing character visual style')
_REFERENCE_LOCK_REALISM_BLOCKERS = ('photorealistic', 'real human face detail', 'realistic skin texture', 'volumetric skin shading', 'painterly realism', 'photograph', 'real photo', 'photography', '3d render', 'cgi', 'real person', 'real human', 'stock photo', 'photorealistic character face', 'realistic human character', 'real-person character skin', 'realistic character eyes')

def normalize_reference_style_locked_keys(raw_keys = None):
    normalized = set()
    if not raw_keys:
        return normalized
    for raw_key in None:
        if not raw_key:
            key = normalize_character_name(str(''))
            if key:
                normalized.add(key)
        return normalized


def resolve_reference_style_locked_keys(preserve_reference_character_style = None, replaced_scope_map = None, explicit_locked_keys = None, direct_reference_keys = (None, None)):
