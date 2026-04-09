# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_semantic_contract.pyc (Python 3.11)

from __future__ import annotations
from typing import Any, Dict, Optional
_SCENE_FAMILY_TO_TYPE = {
    'character_relation': 'emotion_dialogue',
    'emotion_reaction': 'emotion_dialogue',
    'response_action': 'action_focus',
    'event_observation': 'crowd_establishing',
    'environment_context': 'crowd_establishing',
    'explainer_scene': 'explanation_presentation',
    'evidence_explanation': 'explanation_presentation',
    'comparison': 'explanation_presentation' }
_SCENE_TYPE_TO_FAMILY = {
    'emotion_dialogue': 'character_relation',
    'action_focus': 'response_action',
    'crowd_establishing': 'environment_context',
    'explanation_presentation': 'explainer_scene',
    'character_focus': 'scene' }

def _normalize_text(value = None):
