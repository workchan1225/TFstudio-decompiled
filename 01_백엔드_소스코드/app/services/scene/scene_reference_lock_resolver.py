# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_reference_lock_resolver.pyc (Python 3.11)

from typing import Any, Dict, Iterable, List, Optional
from utils.character_name_matcher import normalize_character_name
from reference_policy import REPLACEMENT_SCOPE_FACE_ONLY, REPLACEMENT_SCOPE_FULL_LOOK, normalize_replacement_scope_map, normalize_replaced_character_keys

def resolve_reference_locked_character_names(*, characters, detected_names, explicit_locked_keys):
