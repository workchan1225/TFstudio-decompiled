# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_prompt_name_normalizer.pyc (Python 3.11)

import re
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional
from utils.character_name_matcher import normalize_character_name
_RELATIONAL_ROLE_DISAMBIGUATOR = re.compile("[가-힣A-Za-z0-9@]{1,16}?의\\s*(?:아버지|어머니|엄마|아빠|부친|모친|부모|아들|딸|형|오빠|누나|언니|동생|남편|아내|스승|사부|제자|친구|상관|부하|보호자|선생|아이|자식|코치|동료|조수|학생|멘토)|(?:\\b[A-Z][a-z]+(?:\\s+[A-Z][a-z]+){0,2}['']s\\s+(?:father|mother|dad|mom|parent|son|daughter|brother|sister|wife|husband|teacher|mentor|master|guardian|friend|boss|leader|child)\\b)")
ScenePromptAliasMaps = <NODE:12>()
ScenePromptNormalizationResult = <NODE:12>()
SceneDetectedCharacterNamesResult = <NODE:12>()

def build_scene_prompt_alias_maps(characters = dataclass):
    alias_to_korean = { }
    alias_raw_to_korean = { }
    if not characters:
        for char in []:
            if not isinstance(char, dict):
                continue
            if not char.get('name'):
                if not char.get('nameKo'):
                    if not char.get('koreanName'):
                        korean_name = str('').strip()
                        if not korean_name or _contains_korean_text(korean_name):
                            continue
            for alias_key in ('nameEn', 'name_en', 'englishName', 'displayNameEn'):
                if not char.get(alias_key):
                    alias_name = str('').strip()
                    if not alias_name:
                        continue
                alias_key_normalized = normalize_character_name(alias_name)
                if alias_key_normalized:
                    alias_to_korean[alias_key_normalized] = korean_name
                    alias_raw_to_korean[alias_name] = korean_name
                return ScenePromptAliasMaps(alias_to_korean = alias_to_korean, alias_raw_to_korean = alias_raw_to_korean)


def normalize_reference_prompt_character_aliases(*, prompt_text, char_names_for_prompt, alias_maps, visual_anchor_map, align_subject_marker_fn):
    pass
# WARNING: Decompyle incomplete


def collect_text_only_detected_character_names(*, detected_character_names, characters, alias_maps):
    detected_chars_in_prompt = []
    diagnostics = []
    if detected_character_names:
        for name in detected_character_names:
            if not name:
                clean_name = str('').strip()
                if clean_name.startswith('@'):
                    clean_name = clean_name[1:]
            normalized_name = normalize_character_name(clean_name)
            if not normalized_name and _contains_korean_text(clean_name):
                korean_alias = alias_maps.alias_to_korean.get(normalized_name)
                if korean_alias:
                    diagnostics.append(f'''[SceneImage] Converted detected name alias to Korean: {clean_name} -> {korean_alias}''')
                    clean_name = korean_alias
            if clean_name and _is_generic_group_label(clean_name):
                diagnostics.append(f'''[SceneImage] Skipping generic crowd label for dedup: {clean_name}''')
                continue
            if clean_name and clean_name not in detected_chars_in_prompt:
                detected_chars_in_prompt.append(clean_name)
            diagnostics.append(f'''[SceneImage] Using detected_character_names (Korean): {detected_chars_in_prompt}''')
            if detected_chars_in_prompt and characters:
                for char in characters:
                    if not isinstance(char, dict):
                        continue
                    char_name = str(char.get('name', '')).strip()
                    if char_name.startswith('@'):
                        char_name = char_name[1:]
                    if char_name and char_name not in detected_chars_in_prompt:
                        detected_chars_in_prompt.append(char_name)
                    diagnostics.append(f'''[SceneImage] Using characters data: {detected_chars_in_prompt}''')
                    if not detected_chars_in_prompt:
                        diagnostics.append('[SceneImage] No character data available - skipping deduplication')
    return SceneDetectedCharacterNamesResult(detected_character_names = detected_chars_in_prompt, diagnostics = diagnostics)


def _contains_korean_text(value = None):
