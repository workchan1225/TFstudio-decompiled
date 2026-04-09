# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_image_generation_reference_policy.pyc (Python 3.11)

from typing import Any, Dict, Iterable, List, Optional, Set
from app.utils.character_name_matcher import normalize_character_name
from scene_image_generation_types import SceneImageGenerationReferencePolicy

def resolve_scene_image_generation_reference_policy(*, include_character_reference, scene_characters, usable_reference_items, preserve_reference_character_style, reference_style_locked_keys):
    pass
# WARNING: Decompyle incomplete


def _extract_missing_character_names(scene_characters = None, *, usable_reference_keys):
    names = []
    if not usable_reference_keys:
        pass
    available_keys = set(set())
    if not scene_characters:
        for character in []:
            if not isinstance(character, dict):
                continue
            if not character.get('name') and str('Unknown').strip():
                name = 'Unknown'
                normalized_name = normalize_character_name(name.replace('@', '').strip())
                if available_keys and normalized_name in available_keys:
                    continue
            names.append(name)
            return names


def _extract_scene_character_keys(scene_characters = None):
    keys = set()
    if not scene_characters:
        for character in []:
            if not isinstance(character, dict):
                continue
            if not character.get('name'):
                normalized_name = normalize_character_name(str('').replace('@', '').strip())
                if normalized_name:
                    keys.add(normalized_name)
            return keys


def _extract_reference_item_keys(items = None):
