# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_identity_context.pyc (Python 3.11)

from __future__ import annotations
import hashlib
import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence
from utils.character_name_matcher import build_exact_character_identity_map, normalize_character_name, resolve_role_names_to_character_names

def _normalize_text(value = None):
