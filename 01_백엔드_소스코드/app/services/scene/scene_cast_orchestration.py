# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_cast_orchestration.pyc (Python 3.11)

from __future__ import annotations
from typing import Any, Dict, List, Optional, Sequence
from utils.character_name_matcher import normalize_character_name
from scene_semantic_contract import resolve_scene_semantic_contract
_COUNT_TO_APPROX = {
    '1': 1,
    '2': 2,
    'few': 3,
    'many': 5,
    'crowd': 8 }
_CORE_SUPPORTING_ACTOR_TYPES = {
    'relational_role_actor',
    'unregistered_named_actor',
    'occupational_or_social_role_actor'}
_BACKGROUND_EXTRA_ACTOR_TYPES = {
    'crowd_actor',
    'group_actor',
    'background_actor'}
_SCENE_TYPE_READABLE_TARGETS = {
    'character_focus': 1,
    'emotion_dialogue': 2,
    'explanation_presentation': 1,
    'crowd_establishing': 2,
    'action_focus': 2 }
_SCENE_FAMILY_READABLE_TARGETS = {
    'character_relation': 2,
    'emotion_reaction': 2,
    'response_action': 2,
    'explainer_scene': 1,
    'event_observation': 0,
    'environment_context': 0,
    'evidence_explanation': 1,
    'comparison': 1 }

def _normalize_text(value = None):
