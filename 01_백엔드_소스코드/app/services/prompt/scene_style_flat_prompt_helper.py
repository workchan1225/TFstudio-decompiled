# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_style_flat_prompt_helper.pyc (Python 3.11)

import re
from typing import Any, Dict, List, Optional
from scene.hybrid_background_policy import get_hybrid_priority_rule, rewrite_style_profile_for_hybrid
from hybrid_realism_sanitizer import remove_global_realism_clauses_for_hybrid
from scene_generation_prompt_blocks import build_keyword_exact_once_rule_lines
_SCENE_SECTION_MARKER_PATTERN = re.compile('\\[(Context|ACTION|Subject|Environment)\\]', flags = re.IGNORECASE)

def strip_nested_style_control_tags(prompt = None):
