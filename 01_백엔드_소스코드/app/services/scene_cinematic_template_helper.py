# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_cinematic_template_helper.pyc (Python 3.11)

'''
Helpers for style-category adjustment, template matching, and cinematic merge.
'''
from typing import Any, Dict, List, Optional
from models.image_prompt_template import ImagePromptTemplate
from utils.cinematic_analyzer import analyze_informational_content
from scene.background_mode_policy import resolve_background_mode

def _normalize_name_for_match(name = None):
    if not name:
        normalized = str('').strip()
        if normalized.startswith('@'):
            normalized = normalized[1:]
    normalized = normalized.replace('[', '').replace(']', '')
    normalized = ' '.join(normalized.split())
    return normalized.lower()


def _collect_scene_text_for_informational(scene = None, narration = None):
