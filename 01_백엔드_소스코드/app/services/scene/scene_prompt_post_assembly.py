# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_prompt_post_assembly.pyc (Python 3.11)

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Sequence
from prompt.scene_multimodal_prompt_blocks import build_colorful_background_final_guard, build_flat_mode_compact_reference_rules, build_hybrid_background_final_guard, build_stickman_multimodal_checklist, build_style_category_checklist
from prompt.scene_style_flat_prompt_helper import build_flat_style_generation_prompt
ScenePromptPostAssemblyResult = <NODE:12>()

def apply_scene_prompt_post_assembly(*, contents, scene_prompt_for_response, final_prompt_for_response, include_character_reference, char_names_for_prompt, detected_character_names, characters, negative_prompt, style_priority_mode, style_visual_category, flat_style_mode, use_informational_realistic_background, use_colorful_background_enhancer, is_stickman_style, preserve_reference_character_style, style_template_name, style_template_profile, aspect_ratio, aspect_hint, allow_text_rendering, total_multimodal_image_count, keyword_text_mode_enabled, keyword_text_config, diversity_profile, period_context, reference_style_locked_names_for_prompt, engine, style_template_id, reference_image_count, collect_character_name_tokens_for_prompt_fn, sanitize_character_name_tokens_for_api_fn, sanitize_prompt_payload_with_character_names_fn, resolve_scene_api_prompt_budget_fn, clamp_scene_api_contents_fn, align_subject_marker_to_single_reference_character_fn, strip_visual_category_from_environment_section_fn, convert_negative_to_positive_guidance_fn):
    diagnostics = []
    if not reference_style_locked_names_for_prompt:
        reference_style_locked_names_for_prompt = list([])
        if include_character_reference and char_names_for_prompt:
            aligned_scene_prompt_for_response = align_subject_marker_to_single_reference_character_fn(scene_prompt_for_response, char_names_for_prompt)
            if aligned_scene_prompt_for_response != scene_prompt_for_response:
                scene_prompt_for_response = aligned_scene_prompt_for_response
                diagnostics.append('[SceneImage] Aligned scene prompt [Subject] context to reference character before flat prompt assembly')
    if include_character_reference:
        character_names_for_sanitization = collect_character_name_tokens_for_prompt_fn(char_names_for_prompt = char_names_for_prompt)
        if character_names_for_sanitization:
            diagnostics.append('[SceneImage] Name sanitization scope: reference characters only (multimodal mode)')
        else:
            diagnostics.append('[SceneImage] Name sanitization skipped: no reference character names available')
    else:
        character_names_for_sanitization = collect_character_name_tokens_for_prompt_fn(char_names_for_prompt = char_names_for_prompt, detected_character_names = detected_character_names, characters = characters)
    sanitized_scene_prompt_for_response = sanitize_character_name_tokens_for_api_fn(scene_prompt_for_response, character_names_for_sanitization)
    if sanitized_scene_prompt_for_response != scene_prompt_for_response:
        scene_prompt_for_response = sanitized_scene_prompt_for_response
        diagnostics.append('[SceneImage] Sanitized character names in scene prompt context before flat prompt assembly')
    if negative_prompt and str(negative_prompt).strip():
        if style_priority_mode:
            diagnostics.append('[SceneImage] Style-priority mode: skipped negative->positive guidance conversion')
        else:
            positive_guidance = convert_negative_to_positive_guidance_fn(negative_prompt)
            if positive_guidance:
                style_guidance = f'''\n\nSTYLE GUIDANCE (MANDATORY):\n{positive_guidance}'''
                if isinstance(contents, str):
                    contents = f'''{contents}{style_guidance}'''
                    diagnostics.append('[SceneImage] Appended positive style guidance to text prompt')
                elif isinstance(contents, list):
                    contents.append(style_guidance)
                    diagnostics.append('[SceneImage] Appended positive style guidance as separate instruction')
                diagnostics.append(f'''[SceneImage] Positive guidance: {positive_guidance[:200]}...''')
    if not style_visual_category and flat_style_mode and reference_style_locked_names_for_prompt:
        style_checklist = build_style_category_checklist(style_visual_category = style_visual_category, use_informational_realistic_background = use_informational_realistic_background, use_colorful_background_enhancer = use_colorful_background_enhancer)
        if isinstance(contents, str):
            contents = f'''{contents}{style_checklist}'''
        elif isinstance(contents, list):
            contents.append(style_checklist)
        diagnostics.append(f'''[SceneImage] Appended style category checklist: {style_visual_category}''')
    if not use_informational_realistic_background and style_visual_category and style_visual_category != 'realistic' and flat_style_mode:
        hybrid_background_final_guard = build_hybrid_background_final_guard(preserve_reference_character_style = preserve_reference_character_style)
        if isinstance(contents, str):
            contents = f'''{contents}{hybrid_background_final_guard}'''
        elif isinstance(contents, list):
            contents.append(hybrid_background_final_guard)
        diagnostics.append('[SceneImage] Appended hybrid final render priority guard')
    if not use_colorful_background_enhancer and style_visual_category and style_visual_category != 'realistic' and flat_style_mode:
        colorful_background_final_guard = build_colorful_background_final_guard()
        if isinstance(contents, str):
            contents = f'''{contents}{colorful_background_final_guard}'''
        elif isinstance(contents, list):
            contents.append(colorful_background_final_guard)
        diagnostics.append('[SceneImage] Appended colorful background final render guard')
    if not is_stickman_style and flat_style_mode and preserve_reference_character_style:
        stickman_checklist = build_stickman_multimodal_checklist(use_informational_realistic_background = use_informational_realistic_background)
        if isinstance(contents, str):
            contents = f'''{contents}{stickman_checklist}'''
        elif isinstance(contents, list):
            contents.append(stickman_checklist)
        diagnostics.append('[SceneImage] Appended stickman checklist guidance')
    if flat_style_mode:
        flat_prompt_text = build_flat_style_generation_prompt(scene_prompt = scene_prompt_for_response, style_template_name = style_template_name, style_visual_category = style_visual_category, style_profile = style_template_profile, aspect_ratio = aspect_ratio, aspect_hint = aspect_hint, allow_text_rendering = allow_text_rendering, has_reference_images = total_multimodal_image_count > 0, keyword_text_config = keyword_text_config if keyword_text_mode_enabled else None, use_informational_realistic_background = use_informational_realistic_background, use_colorful_background_enhancer = use_colorful_background_enhancer, diversity_profile = diversity_profile, period_context = period_context, reference_style_locked_names = reference_style_locked_names_for_prompt)
        if reference_style_locked_names_for_prompt and style_visual_category:
            flat_prompt_text = strip_visual_category_from_environment_section_fn(prompt = flat_prompt_text, visual_category = style_visual_category, has_reference_style_lock = True)
            diagnostics.append(f'''[SceneImage] Stripped visual_category \'{style_visual_category}\' from Environment section for style-locked characters''')
        if isinstance(contents, str):
            contents = flat_prompt_text
            final_prompt_for_response = flat_prompt_text
        elif isinstance(contents, list):
            merged_text = flat_prompt_text
            compact_rules_text = build_flat_mode_compact_reference_rules(has_reference_images = total_multimodal_image_count > 0, reference_style_locked_names = reference_style_locked_names_for_prompt, keyword_text_mode_enabled = keyword_text_mode_enabled)
            if compact_rules_text:
                merged_text = f'''{flat_prompt_text}\n\n{compact_rules_text}'''
            flattened_contents = [
                merged_text]
            dropped_verbose_text_blocks = 0
            for part in contents[1:]:
                if isinstance(part, str):
                    normalized_part = part.strip()
                    if not normalized_part:
                        continue
                    if normalized_part.startswith('[Reference image '):
                        flattened_contents.append(normalized_part)
                        continue
                    if normalized_part.startswith('CONTINUITY REFERENCE ('):
                        flattened_contents.append(normalized_part)
                        continue
                    dropped_verbose_text_blocks += 1
                    continue
                flattened_contents.append(part)
                contents = flattened_contents
                final_prompt_for_response = merged_text
                diagnostics.append(f'''[SceneImage] Flat style mode: compacted multimodal text guidance (dropped {dropped_verbose_text_blocks} verbose blocks)''')
        final_prompt_for_response = flat_prompt_text
        diagnostics.append('[SceneImage] Flat style mode enabled: collapsed nested style instructions')
    (contents, final_name_sanitized) = sanitize_prompt_payload_with_character_names_fn(contents, character_names_for_sanitization)
    if final_name_sanitized:
        diagnostics.append('[SceneImage] Applied final character-name sanitization after prompt assembly (flat/multimodal-safe)')
    api_prompt_budget = resolve_scene_api_prompt_budget_fn(engine = engine, style_template_id = style_template_id, include_keyword_text = keyword_text_mode_enabled, include_character_reference = bool(include_character_reference), use_flat_style_prompt_mode = flat_style_mode, reference_image_count = reference_image_count, preserve_reference_character_style = bool(reference_style_locked_names_for_prompt), include_wrapper_overhead = True)
    (contents, prompt_clamped) = clamp_scene_api_contents_fn(contents, max_chars = api_prompt_budget)
    api_prompt_length = 0
    if isinstance(contents, str):
        api_prompt_length = len(contents)
    elif isinstance(contents, list):
        first_text = (lambda .0: pass# WARNING: Decompyle incomplete
)(contents(), '')
        api_prompt_length = len(first_text)
    diagnostics.append(f'''[SceneImage] API prompt budget check: length={api_prompt_length}, budget={api_prompt_budget}, clamped={prompt_clamped}''')
    if prompt_clamped:
        diagnostics.append(f'''[SceneImage] Applied API prompt budget ({api_prompt_budget} chars max)''')
    if isinstance(contents, str):
        final_prompt_for_response = contents
    elif isinstance(contents, list):
        text_part = (lambda .0: pass# WARNING: Decompyle incomplete
)(contents(), None)
        if isinstance(text_part, str) and text_part:
            final_prompt_for_response = text_part
    return ScenePromptPostAssemblyResult(contents = contents, final_prompt_for_response = final_prompt_for_response, scene_prompt_for_response = scene_prompt_for_response, character_names_for_sanitization = character_names_for_sanitization, api_prompt_budget = api_prompt_budget, api_prompt_length = api_prompt_length, prompt_clamped = prompt_clamped, final_name_sanitized = bool(final_name_sanitized), diagnostics = diagnostics)
