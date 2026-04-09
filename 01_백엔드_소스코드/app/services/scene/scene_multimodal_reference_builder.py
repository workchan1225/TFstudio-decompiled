# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_multimodal_reference_builder.pyc (Python 3.11)

import base64
import io
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set, Tuple
from utils.character_name_matcher import normalize_character_name
from reference_character_style_policy import resolve_reference_style_locked_keys
from reference_policy import REPLACEMENT_SCOPE_FULL_LOOK, extract_direct_reference_keys, extract_replaced_scope_map_from_character_images, filter_anchor_reference_map, normalize_replacement_scope_map, normalize_replaced_character_keys
SceneMultimodalReferenceContext = <NODE:12>()
PreparedCharacterReferenceParts = <NODE:12>()
PreparedContinuityReferenceParts = <NODE:12>()

def decode_data_url_part(data_url = dataclass):
    if not data_url and isinstance(data_url, str) or data_url.startswith('data:image'):
        return None
    
    try:
        (header, b64_data) = data_url.split(',', 1)
        mime_type = header.split(':')[1].split(';')[0]
        return {
            'bytes': base64.b64decode(b64_data),
            'mime_type': mime_type }
    except Exception:
        return None



def is_scene_derived_anchor_payload(anchor_payload = None):
    if not isinstance(anchor_payload, dict):
        return False
    anchor_role = None(anchor_payload.get('anchorRole', '')).strip().lower()
    if anchor_role in frozenset({'previous_generated', 'first_completed_scene'}):
        return True
    scene_id = None(anchor_payload.get('sceneId', '')).strip()
    return bool(scene_id)


def prepare_scene_multimodal_reference_context(*, character_images, character_anchor_references, preserve_reference_character_style, reference_style_locked_character_keys, replaced_character_keys, replacement_scopes):
    if not character_images:
        filtered_character_images = []
        direct_reference_keys = extract_direct_reference_keys(filtered_character_images)
        replaced_scope_map = normalize_replacement_scope_map(replacement_scopes)
        replaced_reference_keys = normalize_replaced_character_keys(replaced_character_keys)
        replaced_reference_keys.update(replaced_scope_map.keys())
        replaced_from_images = extract_replaced_scope_map_from_character_images(filtered_character_images)
        replaced_reference_keys.update(replaced_from_images.keys())
        for key, scope in replaced_from_images.items():
            replaced_scope_map.setdefault(key, scope)
            for key in replaced_reference_keys:
                replaced_scope_map.setdefault(key, REPLACEMENT_SCOPE_FULL_LOOK)
                full_look_replaced_keys = replaced_scope_map.items()()
                reference_style_locked_keys = resolve_reference_style_locked_keys(preserve_reference_character_style = preserve_reference_character_style, replaced_scope_map = replaced_scope_map, explicit_locked_keys = reference_style_locked_character_keys, direct_reference_keys = direct_reference_keys)
                if not character_anchor_references:
                    anchor_reference_map = { }.items()()
                    anchor_reference_map = filter_anchor_reference_map(anchor_reference_map, direct_reference_keys, replaced_reference_keys)
                    diagnostics = []
                    if direct_reference_keys or replaced_reference_keys:
                        diagnostics.append(f'''[SceneImage] Reference policy: direct={sorted(direct_reference_keys)}, replaced={sorted(replaced_reference_keys)}, full_look={sorted(full_look_replaced_keys)}, reference_style_lock={sorted(reference_style_locked_keys)}, anchor_after_filter={sorted(anchor_reference_map.keys())}''')
    return SceneMultimodalReferenceContext(direct_reference_keys = direct_reference_keys, replaced_scope_map = replaced_scope_map, replaced_reference_keys = replaced_reference_keys, full_look_replaced_keys = full_look_replaced_keys, reference_style_locked_keys = reference_style_locked_keys, anchor_reference_map = anchor_reference_map, diagnostics = diagnostics)


def prepare_character_reference_image_parts(*, character_images, include_character_reference, characters, anchor_reference_map, content_category, project_image_loader, max_image_size):
    diagnostics = []
    image_parts = []
    char_names_for_prompt = []
    used_reference_characters = []
    if not character_images:
        filtered_character_images = []
        if not filtered_character_images or include_character_reference:
            return PreparedCharacterReferenceParts(image_parts = image_parts, char_names_for_prompt = char_names_for_prompt, reference_image_count = 0, used_reference_characters = used_reference_characters, diagnostics = diagnostics)
        None.append(f'''[SceneImage] Processing {len(filtered_character_images)} character reference images for multimodal input''')
        char_age_lookup = _build_character_age_lookup(characters)
        seen_character_names = set()
        for idx, char_img in enumerate(filtered_character_images):
            if not isinstance(char_img, dict):
                continue
            char_name = str(char_img.get('characterName', f'''Character {idx + 1}''')).strip()
            normalized_char_name = normalize_character_name(char_name)
            anchor_payload = anchor_reference_map.get(normalized_char_name)
            img_data_url = char_img.get('imageDataUrl')
            if img_data_url and isinstance(anchor_payload, dict):
                if is_scene_derived_anchor_payload(anchor_payload):
                    diagnostics.append(f'''[SceneImage] Skipping scene-derived anchor image for {char_name} (face-only reference policy)''')
                else:
                    img_data_url = anchor_payload.get('imageDataUrl')
                    if not img_data_url:
                        anchor_image_path = anchor_payload.get('imagePath')
                        if anchor_image_path and project_image_loader:
                            img_data_url = project_image_loader(anchor_image_path)
                            if img_data_url:
                                diagnostics.append(f'''[SceneImage] Loaded anchor reference image from path for {char_name}''')
                    if img_data_url:
                        diagnostics.append(f'''[SceneImage] Using anchor reference image for {char_name}''')
            if img_data_url and char_img.get('imagePath') and project_image_loader:
                img_data_url = project_image_loader(char_img.get('imagePath'))
            if not img_data_url:
                decoded = decode_data_url_part(str(''))
                if not decoded:
                    continue
            img_bytes = decoded['bytes']
            mime_type = decoded['mime_type']
            if len(img_bytes) > max_image_size:
                diagnostics.append(f'''[SceneImage] Reference image {idx} is {len(img_bytes) / 1024 / 1024:.2f}MB, resizing...''')
                resized = _resize_reference_image_bytes(image_bytes = img_bytes, mime_type = mime_type, max_image_size = max_image_size)
                if not resized:
                    diagnostics.append(f'''[SceneImage] Resize failed, skipping: unable to fit reference image {idx}''')
                    continue
                img_bytes = resized['bytes']
                mime_type = resized['mime_type']
                diagnostics.append(f'''[SceneImage] Resized to {len(img_bytes) / 1024:.1f}KB''')
            scene_safe_reference = _derive_scene_safe_reference_crop(image_bytes = img_bytes, mime_type = mime_type, content_category = content_category)
            if scene_safe_reference:
                img_bytes = scene_safe_reference['bytes']
                mime_type = scene_safe_reference['mime_type']
                diagnostics.append(f'''[SceneImage] Derived scene-safe single-view reference crop for {char_name} from multi-view lineup sheet''')
            if normalized_char_name in seen_character_names:
                diagnostics.append(f'''[SceneImage] Skipping duplicate character: {char_name}''')
                continue
            seen_character_names.add(normalized_char_name)
            age_info = char_age_lookup.get(normalized_char_name, '')
            image_parts.append({
                'bytes': img_bytes,
                'mime_type': mime_type,
                'name': char_name,
                'age_info': age_info })
            char_names_for_prompt.append(char_name)
            used_reference_characters.append(char_name)
            diagnostics.append(f'''[SceneImage] Prepared reference image for {char_name}''')
            except Exception:
                exc = None
                diagnostics.append(f'''[SceneImage] Warning: Failed to process reference image {idx}: {exc}''')
                exc = None
                del exc
                continue
                exc = None
                del exc
            return PreparedCharacterReferenceParts(image_parts = image_parts, char_names_for_prompt = char_names_for_prompt, reference_image_count = len(image_parts), used_reference_characters = used_reference_characters, diagnostics = diagnostics)


def prepare_continuity_reference_image_parts(*, engine, previous_generated_scene_images, anchor_reference_map, project_image_loader, used_reference_characters, max_parts):
    if not used_reference_characters:
        collected_used_reference_characters = list([])
        diagnostics = []
        continuity_image_parts = []
        if not str(engine).startswith('nanobanana'):
            return PreparedContinuityReferenceParts(continuity_image_parts = continuity_image_parts, used_reference_characters = collected_used_reference_characters, diagnostics = diagnostics)
        if None:
            diagnostics.append('[SceneImage] Previous-scene image references disabled - AI creates from script context')
    skipped_anchor_scene_refs = 0
    for anchor_payload in anchor_reference_map.values():
        if not isinstance(anchor_payload, dict):
            continue
        if is_scene_derived_anchor_payload(anchor_payload):
            skipped_anchor_scene_refs += 1
            continue
        anchor_data_url = anchor_payload.get('imageDataUrl', '')
        if not anchor_data_url:
            anchor_image_path = anchor_payload.get('imagePath')
            if anchor_image_path and project_image_loader:
                if not project_image_loader(anchor_image_path):
                    anchor_data_url = ''
                    decoded = decode_data_url_part(anchor_data_url)
                    if not decoded:
                        continue
        if not str(anchor_payload.get('characterName', 'anchor-character')).strip():
            anchor_name = 'anchor-character'
            continuity_image_parts.append({
                'bytes': decoded['bytes'],
                'mime_type': decoded['mime_type'],
                'name': anchor_name,
                'source': 'character-anchor' })
            if anchor_name not in collected_used_reference_characters:
                collected_used_reference_characters.append(anchor_name)
        if skipped_anchor_scene_refs:
            diagnostics.append(f'''[SceneImage] Skipped scene-derived character anchors for this scene: {skipped_anchor_scene_refs}''')
    if len(continuity_image_parts) > max_parts:
        continuity_image_parts = continuity_image_parts[:max_parts]
    if continuity_image_parts:
        previous_scene_ref_count = (lambda .0: pass# WARNING: Decompyle incomplete
)(continuity_image_parts())
        anchor_ref_count = (lambda .0: pass# WARNING: Decompyle incomplete
)(continuity_image_parts())
        diagnostics.append(f'''[SceneImage] Added continuity references: previous-scenes={previous_scene_ref_count}, character-anchors={anchor_ref_count}, total={len(continuity_image_parts)}''')
    return PreparedContinuityReferenceParts(continuity_image_parts = continuity_image_parts, used_reference_characters = collected_used_reference_characters, diagnostics = diagnostics)


def _build_character_age_lookup(characters = None):
    char_age_lookup = { }
    if not characters:
        for char in []:
            if not isinstance(char, dict):
                continue
            char_name_key = normalize_character_name(char.get('name', ''))
            if not char_name_key:
                continue
            age_range = char.get('ageRange', '')
            gender = char.get('gender', '')
            char_age_lookup[char_name_key] = f'''{age_range}, {gender}''' if age_range else gender
            return char_age_lookup


def _resize_reference_image_bytes(*, image_bytes, mime_type, max_image_size):
    
    try:
        Image = Image
        import PIL
    except Exception:
        return None

# WARNING: Decompyle incomplete


def _derive_scene_safe_reference_crop(*, image_bytes, mime_type, content_category):
    pass
# WARNING: Decompyle incomplete


def _should_apply_scene_safe_reference_crop(content_category = None):
