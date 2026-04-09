# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_generated_image_postprocessor.pyc (Python 3.11)

import base64
from dataclasses import dataclass, field
from io import BytesIO
from typing import Any, Callable, Dict, List, Optional, Sequence
SceneKeywordOverlayMetadata = <NODE:12>()
SceneGeneratedImagePostprocessResult = <NODE:12>()

def resolve_scene_keyword_overlay_metadata(*, keyword_text_mode_enabled, keyword_text_config, narration_text, prompt_en, detected_character_names, characters, normalize_keyword_text_config_fn, has_keyword_text_mode_enabled_fn, recover_keyword_text_with_python_fallback_fn, collect_character_name_tokens_for_prompt_fn):
    diagnostics = []
    overlay_config_for_postprocess = None
    keyword_overlay_keywords = []
    if not keyword_text_mode_enabled:
        return SceneKeywordOverlayMetadata(overlay_config_for_postprocess = None, keyword_overlay_keywords = [], diagnostics = [])
    overlay_config = normalize_keyword_text_config_fn(keyword_text_config)
    if not has_keyword_text_mode_enabled_fn(True, overlay_config):
        if not narration_text:
            fallback_overlay_config = recover_keyword_text_with_python_fallback_fn(narration_text = prompt_en, character_name_blocklist = collect_character_name_tokens_for_prompt_fn(detected_character_names = detected_character_names, characters = characters))
            if has_keyword_text_mode_enabled_fn(True, fallback_overlay_config):
                overlay_config = fallback_overlay_config
    if has_keyword_text_mode_enabled_fn(True, overlay_config) and isinstance(overlay_config, dict):
        overlay_config_for_postprocess = overlay_config
        raw_overlay_keywords = overlay_config.get('keywords', [])
    return SceneKeywordOverlayMetadata(overlay_config_for_postprocess = overlay_config_for_postprocess, keyword_overlay_keywords = keyword_overlay_keywords, diagnostics = diagnostics)


def apply_lighting_normalization_to_scene_image(image_data = None, mime_type = None):
    Image = Image
    import PIL
    process_lighting_normalization = process_lighting_normalization
    import app.utils.split_screen_blender
    img_buffer = BytesIO(image_data)
    pil_image = Image.open(img_buffer)
    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert('RGB')
    (processed_image, lighting_applied) = process_lighting_normalization(pil_image, threshold = 8, strength = 0.7)
    if not lighting_applied:
        return (image_data, mime_type, False)
    output_buffer = None()
    processed_image.save(output_buffer, format = 'JPEG', quality = 95)
    return (output_buffer.getvalue(), 'image/jpeg', True)


def postprocess_scene_generated_image(*, image_parts_for_response, cinematic_info, is_informational_style, aspect_ratio, fixed_output_size, keyword_text_mode_enabled, keyword_text_config, narration_text, prompt_en, detected_character_names, characters, ensure_not_cancelled_fn, get_crop_gravity_for_shot_type_fn, adjust_image_aspect_ratio_fn, normalize_keyword_text_config_fn, has_keyword_text_mode_enabled_fn, recover_keyword_text_with_python_fallback_fn, collect_character_name_tokens_for_prompt_fn, apply_lighting_normalization_fn):
    diagnostics = []
    for part in image_parts_for_response:
        if not hasattr(part, 'inline_data') or part.inline_data:
            continue
        ensure_not_cancelled_fn('before_response_postprocess')
        image_data = part.inline_data.data
        mime_type = part.inline_data.mime_type
        shot_type = cinematic_info.get('shot_type', 'medium shot') if isinstance(cinematic_info, dict) else 'medium shot'
        crop_gravity = get_crop_gravity_for_shot_type_fn(shot_type)
        diagnostics.append(f'''[SceneImage] Crop gravity: {crop_gravity} (shot_type: {shot_type})''')
        (image_data, mime_type) = adjust_image_aspect_ratio_fn(image_data, mime_type, aspect_ratio, crop_gravity, target_size = fixed_output_size, allow_white_letterbox_detection = True, max_letterbox_crop_ratio = 0.12 if is_informational_style else 0.3)
    except Exception:
        adjust_err = None
        diagnostics.append(f'''[SceneImage] Aspect ratio adjustment failed: {adjust_err}, using original image''')
        adjust_err = None
        del adjust_err
    except:
        adjust_err = None
        del adjust_err
    overlay_metadata = resolve_scene_keyword_overlay_metadata(keyword_text_mode_enabled = keyword_text_mode_enabled, keyword_text_config = keyword_text_config, narration_text = narration_text, prompt_en = prompt_en, detected_character_names = detected_character_names, characters = characters, normalize_keyword_text_config_fn = normalize_keyword_text_config_fn, has_keyword_text_mode_enabled_fn = has_keyword_text_mode_enabled_fn, recover_keyword_text_with_python_fallback_fn = recover_keyword_text_with_python_fallback_fn, collect_character_name_tokens_for_prompt_fn = collect_character_name_tokens_for_prompt_fn)
    diagnostics.extend(overlay_metadata.diagnostics)
    if is_informational_style:
        diagnostics.append('[SceneImage] Informational style: lighting-norm post-processing disabled')
    else:
        (image_data, mime_type, lighting_applied) = apply_lighting_normalization_fn(image_data, mime_type)
        if lighting_applied:
            diagnostics.append('[SceneImage] Image post-processing applied: lighting-norm')
        else:
            except Exception:
                blend_err = None
                diagnostics.append(f'''[SceneImage] Image post-processing skipped: {blend_err}''')
                blend_err = None
                del blend_err
            except:
                blend_err = None
                del blend_err
            keyword_overlay_applied = bool(overlay_metadata.overlay_config_for_postprocess)
            if keyword_overlay_applied:
                diagnostics.append(f'''[SceneImage] Keyword text: AI in-scene rendering mode active, PIL overlay disabled (keywords: {overlay_metadata.keyword_overlay_keywords})''')
    image_b64 = base64.b64encode(image_data).decode('utf-8')
    
    return None, SceneGeneratedImagePostprocessResult(image_data_url = f'''data:{mime_type};base64,{image_b64}''', keyword_overlay_applied = keyword_overlay_applied, keyword_overlay_keywords = overlay_metadata.keyword_overlay_keywords, diagnostics = diagnostics)
    raise ValueError('이미지 생성 실패: 응답에 이미지가 없습니다.')


def build_scene_generation_response(*, image_data_url, prompt, scene_prompt, final_prompt, negative_prompt, used_character_references, requested_engine, effective_engine, requested_model_name, effective_model_name, pro_timeout_fallback_applied, pro_timeout_fallback_reason, request_timeout_seconds, keyword_text_overlay_applied, keyword_text_overlay_keywords):
    return {
        'imageDataUrl': image_data_url,
        'prompt': prompt,
        'scenePrompt': scene_prompt,
        'finalPrompt': final_prompt,
        'negativePrompt': negative_prompt,
        'usedCharacterReferences': used_character_references,
        'requestedEngine': requested_engine,
        'effectiveEngine': effective_engine,
        'requestedModelName': requested_model_name,
        'effectiveModelName': effective_model_name,
        'proTimeoutFallbackApplied': pro_timeout_fallback_applied,
        'proTimeoutFallbackReason': pro_timeout_fallback_reason,
        'requestTimeoutSeconds': request_timeout_seconds,
        'keywordTextOverlayApplied': keyword_text_overlay_applied,
        'keywordTextOverlayKeywords': keyword_text_overlay_keywords }
