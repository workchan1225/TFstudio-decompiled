# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_multimodal_prompt_blocks.pyc (Python 3.11)

from typing import Any, Dict, List, Optional
from scene_generation_prompt_blocks import build_keyword_exact_once_rule_lines

def build_style_category_checklist(*, style_visual_category, use_informational_realistic_background, use_colorful_background_enhancer):
    if not style_visual_category:
        category = str('').strip().lower()
        if not category:
            return ''
        lines = [
            None,
            'STYLE CATEGORY CHECKLIST (MANDATORY):',
            f'''- Keep selected visual category fixed: {style_visual_category}''',
            '- Keep template visual DNA stable: palette temperature, shading language, and texture finish should match across scenes']
        if use_informational_realistic_background and category != 'realistic':
            lines.append('- Keep character rendering category fixed; hybrid exception allows photoreal background only')
        elif use_colorful_background_enhancer and category != 'realistic':
            lines.append('- Keep character rendering category fixed; colorful enhancer applies to background/environment only')
        else:
            lines.append('- Do not blend neighboring substyles or unrelated style families')
    if category.startswith('animation'):
        lines.append('- Maintain 2D animation/webtoon rendering with clean linework and cel-shading')
    elif category.startswith('illustration'):
        lines.append('- Maintain selected stylized illustration rendering (2D or stylized 2.5D per template); avoid photoreal live-action human rendering')
    elif category.startswith('traditional'):
        lines.append('- Maintain traditional painting aesthetics; avoid modern photoreal rendering')
    elif category.startswith('realistic') or category == 'realistic':
        lines.append('- Maintain photoreal live-action look; avoid anime/cartoon/illustration rendering')
    elif category.startswith('informational'):
        lines.append('- Keep characters in selected informational substyle consistently')
        if use_informational_realistic_background:
            lines.append('- Only background can be photorealistic; character layer stays in selected informational substyle')
    if use_informational_realistic_background and category != 'realistic':
        lines.extend([
            '- Hybrid mixed-media mode: keep characters stylized in selected category, render background photoreal',
            '- Keep a layered composite feel: stylized characters should read as intentionally placed over live-action background',
            '- Background must read as live-action at first glance; avoid line-art/cel-shaded/painterly treatment on environment surfaces',
            '- Preserve compositing quality (grounded contact shadows, occlusion, perspective consistency)',
            '- Preserve texture contrast between stylized character layer and photographic background'])
    elif use_colorful_background_enhancer and category != 'realistic':
        lines.extend([
            '- Colorful background mode: enrich environment color separation and local contrast while keeping characters in selected style',
            '- Keep location-consistent props and architecture; avoid random fantasy elements unrelated to scene context'])
    return '\n' + '\n'.join(lines) + '\n'


def build_hybrid_background_final_guard(*, preserve_reference_character_style):
    guard = '\n\nHYBRID FINAL RENDER PRIORITY (MANDATORY):\n- Character layer: keep selected style DNA stable (lineweight, shading language, palette)\n- Background layer: render as live-action photo realism (camera optics, real materials, natural exposure)\n- Layered look: characters should feel intentionally placed/composited over the real background plate\n- Environment exclusion: no painterly brush texture, no cel-shading bands, no anime/cartoon line-art on architecture/surfaces\n- If uncertain, preserve stylized character layer and push environment further toward photoreal live-action\n'
    if preserve_reference_character_style:
        guard += "- ABSOLUTE CHARACTER ISOLATION: Style-locked characters MUST maintain their reference image's exact rendering language. The template style influence is ZERO on these characters. Any stylization, simplification, or artistic reinterpretation of style-locked characters is a critical violation.\n"
    return guard


def build_colorful_background_final_guard():
    return '\n\nCOLORFUL BACKGROUND PRIORITY (MANDATORY):\n- Keep character layer exactly in selected style DNA\n- Enhance environment with richer but plausible color contrast and atmospheric color depth\n- Keep scene location cues coherent (architecture, props, era)\n- Avoid neon oversaturation, posterization, or abstract rainbow gradients\n- If uncertain, protect character style first and increase environment color richness moderately\n'


def build_stickman_multimodal_checklist(*, use_informational_realistic_background):
    checklist = '\n\nSTICKMAN CHECKLIST (MANDATORY):\n- Characters are flat 2D stickman with black outlines and white round faces\n- Character faces use only dot eyes and simple line mouth\n- Character body has no volume, no sculpting, no CGI look\n- No 3D/cartoon clay/plastic style on characters\n'
    if use_informational_realistic_background:
        checklist += '- Background can be photorealistic, but character layer must remain flat 2D stickman\n'
    return checklist


def build_flat_mode_compact_reference_rules(*, has_reference_images, reference_style_locked_names, keyword_text_mode_enabled):
    compact_rules = []
    if has_reference_images:
        if reference_style_locked_names:
            joined_reference_style_names = ', '.join(reference_style_locked_names)
            compact_rules.extend([
                '- Reference images are identity anchors; for non-style-locked characters, only face geometry, hairstyle silhouette, and signature outfit colors are binding.',
                f'''- STYLE-LOCKED REFERENCES: {joined_reference_style_names}. Preserve their reference-image character rendering style (linework, shading, texture, palette handling).''',
                '- CHARACTER PRESERVATION (ABSOLUTE): Keep each style-locked reference character exactly as in the uploaded reference image (same facial features, hairstyle silhouette, outfit design/colors, body proportions, and rendering language). Do NOT stylize, simplify, repaint, or reinterpret style-locked characters with template profile cues.',
                '- STYLE TARGET SPLIT: Apply template style influence to environment/background and lighting mood only; do NOT repaint style-locked characters into template style.',
                '- Keep exactly one instance of each referenced character in one unified scene.',
                '- Ignore reference background, composition, and camera layout for non-style-locked characters.',
                '- Never output collage, split panels, floating portraits, or character turnaround sheets.'])
        else:
            compact_rules.extend([
                '- Reference images are soft identity anchors only (broad face geometry, age range, gender, and hairstyle silhouette).',
                '- Character rendering MUST follow the selected template style, including face/hair/outfit linework and texture finish.',
                '- Do NOT preserve photo-like skin pores, wrinkle micro-detail, or camera-real hair strands from references.',
                '- Keep exactly one instance of each referenced character in one unified scene.',
                '- Ignore reference background, composition, and camera layout.',
                '- Never output collage, split panels, floating portraits, or character turnaround sheets.'])
    if keyword_text_mode_enabled:
        exact_once_rules = ' '.join(build_keyword_exact_once_rule_lines())
        compact_rules.append(f'''- Render only the requested keywords as naturally embedded environmental text. {exact_once_rules} If multiple keywords are requested, assign one carrier per keyword and distribute them across different in-scene objects/positions instead of clustering them on one sign. Never use subtitle bars/floating overlays. Add one small in-scene sign/card/monitor if needed.''')
    if not compact_rules:
        return ''
    compact_rules_text = None.join(compact_rules)
    return f'''ADDITIONAL REFERENCE RULES (COMPACT):\n{compact_rules_text}'''


def build_multimodal_reference_policy_lines(*, reference_style_locked_names, full_look_replaced_names, single_style_locked_human_mode, scene_actor_profile):
    pass
# WARNING: Decompyle incomplete


def build_multimodal_prompt_with_context(*, style_instruction, enhanced_prompt, char_list_mapped, composition_hint, consistency_instruction, style_priority_mode, style_priority_reference_line, style_target_split_line, full_look_ignore_line, reference_ignore_line, full_look_lock_block, reference_style_lock_block, extra_people_policy_line, actor_visibility_policy_line, identity_separation_policy_line, subordinate_extras_policy_line):
    if style_priority_mode:
        return f'''{style_instruction}\n\nScene Description:\n{enhanced_prompt}\n\n---\n{char_list_mapped}\n\n{composition_hint}\n\n**Character Consistency (Style Priority):**\n{style_priority_reference_line}\n- Keep hairstyle silhouette and signature outfit colors stable across scenes\n{style_target_split_line}\n{full_look_ignore_line}\n{full_look_lock_block}\n{reference_style_lock_block}\n- {extra_people_policy_line.lstrip('- ').strip()}\n- {actor_visibility_policy_line.lstrip('- ').strip()}\n- {identity_separation_policy_line.lstrip('- ').strip()}\n- {subordinate_extras_policy_line.lstrip('- ').strip()}\n- Generate one unified scene from one camera perspective; each referenced character appears once\n- Do not render character names, labels, or identifying text in the output\n- Never create character sheets, model sheets, turnaround layouts, or multi-angle reference boards\n- Never place a detached portrait, side panel, or standing figure strip beside the main scene\n\nOutput: One cohesive scene with consistent style rendering, no text, no watermark, no collage or split panels.\n\n{consistency_instruction}'''
    return f'''{None}\n\nScene Description:\n{enhanced_prompt}\n\n---\n{char_list_mapped}\n\n{composition_hint}\n\n**Character Consistency:**\n- Match facial features, hairstyle, body type, and signature outfit identity from reference images\n- Keep hairstyle silhouette and core outfit color palette consistent across scenes\n- Allow only minor cloth movement/wrinkle variation (no major outfit redesign)\n- Each character must be instantly recognizable as the same person from their reference\n\n**CRITICAL - Gaze Direction & Body Orientation:**\n- Characters MUST face the object/person they are interacting with in the scene description\n- If leaning against something (wall, glass, door), character MUST face that object\n- If looking at someone, character\'s eyes and body MUST be oriented toward that person\n- If described as "watching" or "looking at" something, gaze MUST be directed at that target\n- Body orientation should match the described action (e.g., "leaning on glass wall" = facing the wall)\n\n**CRITICAL - Reference Image Usage Rules:**\n- Reference images are for APPEARANCE CONSISTENCY ONLY - extract FACE FEATURES from them\n- Transfer ONLY identity-level face geometry (face shape, eyes, nose, mouth)\n{style_target_split_line}\n{reference_ignore_line}\n{full_look_lock_block}\n{reference_style_lock_block}\n- DO NOT include multiple views (front/side/back) in the output\n- DO NOT create turnaround sheets or character model sheets\n- DO NOT show split-screen or side-by-side comparison layouts\n- DO NOT copy the reference image composition directly\n- DO NOT place the reference image or character portrait on the side of the scene\n- DO NOT create collage-style output with reference portrait visible\n- Generate ONE cohesive scene with characters naturally positioned in context\n- The output must be a SINGLE unified scene, not a collage\n\n**CRITICAL - FORBIDDEN COMPOSITIONS (v1.7.2):**\n- ❌ NEVER create "3-panel character turnaround" layout (front view | scene | side view)\n- ❌ NEVER show the same character multiple times from different angles (front, side, back)\n- ❌ NEVER create character model sheets or reference sheets\n- ❌ NEVER split the image into panels showing different views of the same person\n- ❌ NEVER create "emotional face overlay" composition (large close-up face in foreground with scene in background)\n- ❌ NEVER show a character\'s face overlaid or superimposed on the scene\n- ❌ NEVER create "memory/reflection" style with face floating over background\n- ❌ NEVER make characters appear semi-transparent or ghostly unless explicitly described\n- ❌ NEVER create picture-in-picture or floating portrait layouts\n- ✅ ALWAYS generate ONE SINGLE SCENE with ONE camera angle\n- ✅ Each character appears ONLY ONCE in the image\n- ✅ Characters must be fully integrated into the scene, performing the described action\n\n**CRITICAL - CHARACTER CONSISTENCY:**\n- Referenced characters (with @ prefix in CHARACTER section) must match their reference images EXACTLY\n- DO NOT duplicate any referenced character - each referenced character appears EXACTLY ONCE\n- {extra_people_policy_line.lstrip('- ').strip()}\n- {actor_visibility_policy_line.lstrip('- ').strip()}\n- {identity_separation_policy_line.lstrip('- ').strip()}\n- {subordinate_extras_policy_line.lstrip('- ').strip()}\n- Background extras must look CLEARLY DIFFERENT from referenced characters (different age, clothing, build)\n- Referenced characters should be the visual focus; extras should be secondary\n\nOutput: A single cohesive scene (NOT a collage with portrait), no text, no watermarks, no character name labels, no name tags, no identifying text.\n⚠️ IMPORTANT: The character names (like @김철수, @영희) are INTERNAL REFERENCES ONLY - NEVER render these names as visible text, labels, or tags in the image.\n\n{consistency_instruction}'''


def build_multimodal_reference_image_instruction(*, ref_num, char_name, age_info, is_style_locked):
    if not char_name:
        clean_name = str('').strip().lstrip('@')
    age_suffix = f''' ({age_info})''' if age_info or str('').strip() else ''
    if is_style_locked:
        return f'''[Reference image {ref_num} for @{clean_name}{age_suffix}]\n⚠️⚠️⚠️ STYLE-LOCKED CHARACTER: {clean_name} ⚠️⚠️⚠️\n- This character\'s visual style is ABSOLUTE and CANNOT be changed.\n- PRESERVE EXACTLY: rendering style, linework, shading, color palette, texture from reference.\n- If reference is photorealistic photo: keep EXACT photographic quality - natural skin, realistic lighting, camera depth.\n- If reference is illustration/cartoon: keep EXACT illustration quality - same linework, same shading.\n- ANY template/style influence on this character is FORBIDDEN.\n- Template style applies to BACKGROUND and ENVIRONMENT ONLY.'''
    return f'''{ref_num} for @{clean_name}{age_suffix}]'''


def build_multimodal_continuity_reference_instruction(*, source, name):
    return f'''CONTINUITY REFERENCE ({source}): {name}. Use for style and identity continuity only.'''


def build_multimodal_final_reminder(*, style_priority_mode, char_count_for_reminder, reference_style_locked_names, art_style_consistency_instruction):
    reference_style_lock_reminder = ''
    reference_style_ignore_line = '- Ignore reference art style, clothing details, background, and composition layout.'
    style_consistency_line = '- Keep style rendering consistent with [STYLE LOCK] and [VISUAL STYLE CONTRACT].'
    style_priority_reminder_title = 'REMINDER: The images above are FACE REFERENCES ONLY.'
    style_priority_identity_line = '- Extract identity-level facial geometry and apply it to this new scene.'
    standard_reminder_title = 'REMINDER: The images above are FACE REFERENCE ONLY.'
    standard_reminder_identity_line = '- Extract the FACIAL FEATURES (face shape, eyes, nose, mouth) from these reference images'
    if reference_style_locked_names:
        joined_reference_style_names = ', '.join(reference_style_locked_names)
        reference_style_lock_reminder = f'''- REFERENCE STYLE LOCK: {joined_reference_style_names} must keep reference-image character rendering style (linework, shading, texture, palette handling).\n'''
        reference_style_ignore_line = '- For non-style-locked characters, ignore reference art style, clothing details, background, and composition layout.'
        style_consistency_line = '- STYLE TARGET SPLIT: Apply template style influence to environment/background and lighting mood only; keep style-locked characters in reference-image rendering style.'
        style_priority_reminder_title = 'REMINDER: Style-locked references are identity + rendering-style anchors; non-style-locked references are face anchors only.'
        style_priority_identity_line = '- For non-style-locked characters, extract identity-level facial geometry and apply it to this new scene.'
        standard_reminder_title = 'REMINDER: Style-locked references are identity + rendering-style anchors; non-style-locked references are face references only.'
        standard_reminder_identity_line = '- For non-style-locked characters, extract the FACIAL FEATURES (face shape, eyes, nose, mouth) from these reference images'
    if style_priority_mode:
        return f'''\n{style_priority_reminder_title}\n{style_priority_identity_line}\n- Keep exactly one instance of each referenced character ({char_count_for_reminder} main character(s)).\n{reference_style_ignore_line}\n{reference_style_lock_reminder}{style_consistency_line}\n- Output must be one unified scene with no labels, name tags, or collage panels.\n'''
    reference_face_only_ignore_line = None
    if reference_style_locked_names:
        reference_face_only_ignore_line = '- Transfer ONLY facial identity; for non-style-locked characters, ignore reference clothing, pose, background, and art style'
    return f'''\n{standard_reminder_title}\n{standard_reminder_identity_line}\n- Generate a NEW scene where the character appears with matching facial features\n{reference_face_only_ignore_line}\n{reference_style_lock_reminder}- For non-style-locked characters, ignore reference clothing/pose/background/style details.\n- DO NOT duplicate the character or show them looking at themselves\n- DO NOT include the reference image as a portrait or side panel\n- Create exactly ONE instance of each referenced character in the scene\n- ⚠️ {char_count_for_reminder} main character(s) must match references. Background extras allowed if mentioned in scene.\n- Keep each referenced character\'s hairstyle silhouette and signature outfit colors consistent with reference.\n- ❌ NEVER create "3-panel character turnaround" (front view | scene | side view layout)\n- ❌ NEVER show the same character from multiple angles (front, side, back views)\n- ❌ NEVER create character model sheets or reference sheets\n- ❌ NEVER create "emotional face overlay" (large close-up face in foreground with scene in background)\n- ❌ NEVER create picture-in-picture, collage, or multi-panel composition\n- ❌ NEVER include character names, name labels, name tags, or identifying text in the image\n- ✅ Generate ONE SINGLE UNIFIED SCENE from ONE camera angle\n\n{art_style_consistency_instruction}\n'''


def build_multimodal_negative_prompt_suffix(*, use_informational_realistic_background):
    if use_informational_realistic_background:
        return 'face overlay, face superimposed, floating face, ghostly face, picture-in-picture, collage, multi-panel, split composition, emotional close-up overlay, memory overlay, character name labels, name tags, text labels, identifying text, written names, character turnaround, model sheet, reference sheet, 3-panel layout, front view side view, multiple angles of same person, character sheet, inconsistent character rendering, character style drift'
    return 'face overlay, face superimposed, floating face, ghostly face, picture-in-picture, collage, multi-panel, split composition, emotional close-up overlay, memory overlay, character name labels, name tags, text labels, identifying text, written names, character turnaround, model sheet, reference sheet, 3-panel layout, front view side view, multiple angles of same person, character sheet, inconsistent art style, mixed art styles, style variation, different rendering styles'


def build_reference_style_locked_negative_extensions(*, single_style_locked_human_mode):
    extensions = [
        'duplicate same person, same character twice, two copies of same character, cloned person, split-self composition, mirror duplicate, before-after dual self']
    if single_style_locked_human_mode:
        extensions.append('second person, extra person, additional human figure, extra character, multiple people, bystander person, background person, crowd member')
    return extensions


def build_text_only_character_dedup_instruction(*, character_count, positions):
    pass
# WARNING: Decompyle incomplete


def build_text_only_negative_prompt_suffix(*, use_informational_realistic_background):
    if use_informational_realistic_background:
        return 'duplicate person, same person twice, clone, doppelganger, mirror reflection of person, person appearing multiple times, face overlay, face superimposed, floating face, ghostly face, picture-in-picture, collage, multi-panel, split composition, emotional close-up overlay, character name labels, name tags, text labels, identifying text, written names, character turnaround, model sheet, reference sheet, 3-panel layout, front view side view, multiple angles of same person, character sheet, inconsistent character rendering, character style drift'
    return 'duplicate person, same person twice, clone, doppelganger, mirror reflection of person, person appearing multiple times, face overlay, face superimposed, floating face, ghostly face, picture-in-picture, collage, multi-panel, split composition, emotional close-up overlay, character name labels, name tags, text labels, identifying text, written names, character turnaround, model sheet, reference sheet, 3-panel layout, front view side view, multiple angles of same person, character sheet, inconsistent art style, mixed art styles, style variation, different rendering styles'


def build_text_only_forbidden_composition_instruction(*, art_style_consistency_instruction):
    return f'''\n\n**FORBIDDEN COMPOSITIONS (MANDATORY):**\n- ❌ NEVER create character sheet, model sheet, turnaround sheet, or reference board layouts\n- ❌ NEVER show the same character from multiple angles (front, side, back) in one image\n- ❌ NEVER create "emotional face overlay" (large close-up face in foreground with scene in background)\n- ❌ NEVER show a character\'s face overlaid or superimposed on the scene\n- ❌ NEVER create "memory/reflection" style with face floating over background\n- ❌ NEVER create picture-in-picture or floating portrait layouts\n- ❌ NEVER place a detached portrait, side insert, or standing figure strip beside the main scene\n- ✅ ALWAYS compose as a single, cohesive scene from ONE camera perspective\n- ✅ All characters must be fully integrated into the scene, not overlaid on it\n- The output must be ONE unified image, not a collage or multi-panel composition.\n\n{art_style_consistency_instruction}'''
