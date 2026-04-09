# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_script_unit_builder.pyc (Python 3.11)

'''
Canonical script unit helpers for scene anchoring.

This module provides a single sentence-unit timeline so scene split, anchor
metadata, and downstream sync can all refer to the same source boundaries.
'''
from __future__ import annotations
import re
from typing import Any, Dict, List
_SENTENCE_SPAN_REGEX = re.compile('.+?(?:[.!?。]+|$)', re.DOTALL)
_ANCHOR_NORMALIZE_REGEX = re.compile('[\\s"“”‘’\\\'`]+')
_TRAILING_PUNCTUATION_REGEX = re.compile('[.!?。…]+$')

def _normalize_anchor_match_text(value = None):
