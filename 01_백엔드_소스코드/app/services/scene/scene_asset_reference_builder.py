# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_asset_reference_builder.pyc (Python 3.11)

import re
from typing import Any, Dict, List, Optional, Sequence
MAX_STATIC_PROP_REFERENCE_COUNT = 3
MAX_INTERACTIVE_REFERENCE_COUNT = 2
MAX_INTERACTION_BINDING_COUNT = 2
_INTERACTION_LABELS = {
    'use': 'uses',
    'operate': 'operates',
    'hold': 'holds',
    'drink_from': 'drinks from',
    'exercise_with': 'exercises with',
    'sit_on': 'sits on',
    'push': 'pushes',
    'type_on': 'types on',
    'open': 'opens',
    'carry': 'carries' }

def _is_record(value = None):
    return isinstance(value, dict)


def _normalize_text(value = None):
