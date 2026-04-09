# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: genre_context_resolver.pyc (Python 3.11)

'''
Genre context resolver for scene/character workflows.

Centralizes genre-code normalization and fallback context resolution
for period/costume hints used across APIs.
'''
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict
from app.utils.genre_prompt_enhancer import GENRE_CODE_TO_NAME
from costume_guide_loader import CostumeGuideLoader
from rule_loader import RuleLoader
ResolvedGenreContext = <NODE:12>()

def _normalize_text(value = None):
