# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_prompt_conflict_guard.pyc (Python 3.11)

from __future__ import annotations
from typing import Any, Dict, List, Optional
_COMPOSITION_RULE_LABELS = {
    'object_focus_insert': 'object-focused insert frame',
    'reaction_layered_group': 'layered reaction group frame',
    'supporting_reaction_focus': 'supporting reaction frame' }
_ABSTRACT_GAZE_TOKENS = ('threat, objective, or counterpart', 'scene partner', 'event focal point or reaction chain', 'counterpart eyeline exchange')

def _normalize_text(value = None):
