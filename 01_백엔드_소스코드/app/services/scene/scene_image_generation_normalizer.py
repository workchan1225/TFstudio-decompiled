# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_image_generation_normalizer.pyc (Python 3.11)

from typing import Any, Dict, Iterable, List, Optional
from scene_asset_reference_builder import build_scene_asset_context, resolve_scene_asset_id
from scene_cast_orchestration import build_scene_cast_audit
from scene_identity_context import build_scene_binding_characters_from_unique_ids, build_scene_identity_binding_characters, extract_scene_registered_character_names, extract_scene_resolved_character_ids
from scene_staging_plan import build_scene_staging_audit
from scene_prompt_assembly import build_scene_prompt_assembly
from scene_decision import NARRATIVE_GENRE_KEYS
from scene_project_character_loader import resolve_effective_project_characters, resolve_effective_project_character_relationships
from scene_image_generation_types import SceneImageGenerationNormalizedRequest, SceneImageGenerationPipelineRequest

def _is_scene_batch_request_source(value = None):
    return _normalize_text(value).lower() == 'scene_batch'

_DRAMA_VISUAL_CATEGORIES = {
    'manga',
    'manhwa',
    'webtoon',
    'dramatic',
    'cinematic',
    'animation_3d',
    'animation_anime',
    'animation_webtoon'}

def _infer_content_category(style_visual_category = None, default = None):
    '''style_visual_category에서 content_category를 추론한다.

    informational_* 스타일은 항상 "informational" 반환.
    드라마 계열 스타일(animation_webtoon 등)은 "drama" 반환.
    매칭 없으면 default 반환.
    '''
    if not style_visual_category:
        normalized = str('').strip().lower()
        if not normalized:
            return default
        if None.startswith('informational'):
            return 'informational'
        for token in None:
            if token in normalized:
                return 'drama'
            return default


def build_scene_single_pipeline_request(*, scene, characters, character_relationships, character_images, engine, aspect_ratio, resolution, include_character_reference, template_id, style_template_id, project_id, content_type, content_category, auto_cinematic, auto_template_matching, project_genre, speaker_mode, custom_modifiers, total_scenes, previous_shots, use_ai_fallback, cinematic_override, consistency_strength, include_text_in_image, include_keyword_text, character_binding_mode, informational_realistic_background, colorful_background_enhancer, preserve_reference_character_style, reference_style_locked_character_keys, generation_session_id, scene_session_id, character_anchor_references, replaced_character_keys, replacement_scopes, previous_generated_scene_images, asset_library, scene_asset_references, scene_asset_selection, scene_interaction_bindings, use_flat_style_prompt_mode, cancel_check, period_setting, request_source):
    effective_characters = resolve_effective_project_characters(project_id = project_id, provided_characters = characters)
    effective_character_relationships = resolve_effective_project_character_relationships(project_id = project_id, provided_relationships = character_relationships)
# WARNING: Decompyle incomplete


def build_informational_pipeline_request(*, image_prompt, aspect_ratio, project_id, model_type, style_template_id, style_template, style_visual_category_hint, include_keyword_text, custom_keyword_text, narration_text, period_setting, temporal_context, characters, character_relationships, detected_characters, registered_characters_effective, resolved_character_ids, identity_source_signature, character_registry_signature, scene_actors, preserve_reference_character_style, informational_realistic_background, reference_style_locked_character_keys, replaced_character_keys, replacement_scopes, scene_asset_references, scene_asset_selection, scene_interaction_bindings, user_direction, request_intent, diversity_retry_level, scene_id, request_id, attempt_no, scene_index, total_scenes, skip_key_scene_extraction, request_source, scene_spec, speaker_mode, content_category):
    effective_characters = resolve_effective_project_characters(project_id = project_id, provided_characters = characters)
    effective_character_relationships = resolve_effective_project_character_relationships(project_id = project_id, provided_relationships = character_relationships)
    explicit_content_category = _normalize_text(content_category).lower()
# WARNING: Decompyle incomplete


def normalize_pipeline_request(request = None):
    if request.entrypoint == 'informational':
        return _normalize_informational_request(request)
    return None(request)


def _normalize_scene_single_request(request = None):
    if not request.payload:
        payload = { }
    scene = payload.get('scene') if isinstance(payload.get('scene'), dict) else { }
    characters = resolve_effective_project_characters(project_id = _normalize_text(payload.get('project_id')), provided_characters = _normalize_dict_list(payload.get('characters')))
    if not payload.get('character_relationships'):
        character_relationships = resolve_effective_project_character_relationships(project_id = _normalize_text(payload.get('project_id')), provided_relationships = _normalize_dict_list(payload.get('characterRelationships')))
        character_images = _normalize_dict_list(payload.get('character_images'))
        requested_style_template_id = _normalize_text(payload.get('style_template_id'))
        scene_override_style_template_id = _resolve_scene_override_style_template_id(scene)
        if not scene_override_style_template_id:
            style_template_id = requested_style_template_id
            requested_style_visual_category = _normalize_text(request.style_visual_category).lower()
            (style_visual_category, style_visual_category_source) = _resolve_style_visual_category_with_source(style_template_id = style_template_id, explicit_hint = requested_style_visual_category)
            if scene_override_style_template_id:
                style_template_source = 'scene_override'
            elif requested_style_template_id:
                style_template_source = 'request_payload'
            else:
                style_template_source = 'none'
    if not _normalize_text(scene.get('imagePrompt')):
        if not _normalize_text(scene.get('promptEn')):
            prompt_text = _normalize_text(scene.get('narrationText'))
            if not _normalize_text(scene.get('narrationText')):
                if not _normalize_text(scene.get('promptEn')):
                    narration_text = prompt_text
                    if not scene.get('sceneId'):
                        scene_id = _normalize_text(scene.get('id'))
                        raw_detected_characters = _normalize_name_list(scene.get('detectedCharacters'))
                        canonical_registered_characters = extract_scene_registered_character_names(scene)
                        canonical_resolved_character_ids = extract_scene_resolved_character_ids(scene)
                        if not _normalize_text(scene.get('era')):
                            period_setting = _normalize_text(payload.get('period_setting'))
                            if not _normalize_text(payload.get('content_category')).lower():
                                content_category = _normalize_text(request.content_category).lower()
                                if not _normalize_text(payload.get('speaker_mode')):
                                    if not _normalize_text(request.speaker_mode):
                                        speaker_mode = 'multi_speaker'
    preserve_reference_character_style = bool(payload.get('preserve_reference_character_style') if 'preserve_reference_character_style' in payload else request.preserve_reference_character_style)
    if not payload.get('request_source'):
        suppress_scene_assets = _is_scene_batch_request_source(payload.get('requestSource'))
        include_character_reference = bool(payload.get('include_character_reference', True))
    informational_realistic_background = bool(payload.get('informational_realistic_background') if 'informational_realistic_background' in payload else request.informational_realistic_background)
    colorful_background_enhancer = bool(payload.get('colorful_background_enhancer'))
    include_keyword_text = bool(payload.get('include_keyword_text'))
    include_text_in_image = bool(payload.get('include_text_in_image'))
    reference_style_locked_character_keys = _normalize_key_list(payload.get('reference_style_locked_character_keys'))
    (total_reference_images, usable_reference_images) = _count_reference_images(character_images, image_keys = ('imageDataUrl', 'imagePath'))
# WARNING: Decompyle incomplete


def _normalize_informational_request(request = None):
    if not request.payload:
        payload = { }
        characters = resolve_effective_project_characters(project_id = _normalize_text(payload.get('project_id')), provided_characters = _normalize_dict_list(payload.get('characters')))
        if not payload.get('character_relationships'):
            character_relationships = resolve_effective_project_character_relationships(project_id = _normalize_text(payload.get('project_id')), provided_relationships = _normalize_dict_list(payload.get('characterRelationships')))
            style_template_id = _normalize_text(payload.get('style_template_id'))
            if not _normalize_text(payload.get('style_visual_category_hint')).lower():
                requested_style_visual_category = _normalize_text(request.style_visual_category).lower()
                (style_visual_category, style_visual_category_source) = _resolve_style_visual_category_with_source(style_template_id = style_template_id, explicit_hint = requested_style_visual_category)
    style_template_source = 'request_payload' if style_template_id else 'none'
    inferred_content_category = _infer_content_category(style_visual_category = style_visual_category)
    if not _normalize_text(request.speaker_mode):
        if not request.payload and _normalize_text({ }.get('speaker_mode')):
            inferred_speaker_mode = 'single_narrator'
            prompt_text = _normalize_text(payload.get('image_prompt'))
            if not _normalize_text(payload.get('narration_text')):
                narration_text = prompt_text
                raw_detected_characters = _normalize_name_list(payload.get('detected_characters'))
                scene_id = _normalize_text(payload.get('scene_id'))
                canonical_registered_characters = _normalize_name_list(payload.get('registered_characters_effective'))
                canonical_resolved_character_ids = _normalize_name_list(payload.get('resolved_character_ids'))
    preserve_reference_character_style = bool(payload.get('preserve_reference_character_style') if 'preserve_reference_character_style' in payload else request.preserve_reference_character_style)
    if not payload.get('request_source'):
        suppress_scene_assets = _is_scene_batch_request_source(payload.get('requestSource'))
    informational_realistic_background = bool(payload.get('informational_realistic_background') if 'informational_realistic_background' in payload else request.informational_realistic_background)
    include_keyword_text = bool(payload.get('include_keyword_text'))
    reference_style_locked_character_keys = _normalize_key_list(payload.get('reference_style_locked_character_keys'))
    (total_reference_images, usable_reference_images) = _count_reference_images(characters, image_keys = ('imageDataUrl', 'imagePath', 'referenceImage', 'imageUrl'))
# WARNING: Decompyle incomplete


def _resolve_style_visual_category_with_source(*, style_template_id, explicit_hint):
