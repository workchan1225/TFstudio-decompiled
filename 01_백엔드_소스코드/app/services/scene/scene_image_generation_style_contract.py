# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_image_generation_style_contract.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Set
from app.services.prompt.scene_style_mode_helper import resolve_flat_style_prompt_mode
from scene_decision import build_scene_decision_prompt_blocks
from scene_image_generation_types import SceneImageGenerationNormalizedRequest, SceneImageGenerationStyleContract
from style_template_capability_registry import resolve_style_template_capabilities

def resolve_scene_image_generation_style_contract(normalized_request = None):
    if not normalized_request.style_visual_category:
        style_visual_category = str('').strip().lower()
        capabilities = resolve_style_template_capabilities(style_template_id = normalized_request.style_template_id, visual_category = style_visual_category)
        is_informational_style = style_visual_category.startswith('informational')
        is_animation_style = style_visual_category.startswith('animation')
        is_illustration_style = style_visual_category.startswith('illustration')
        is_traditional_style = style_visual_category.startswith('traditional')
        if not is_animation_style:
            if not is_illustration_style:
                is_animation_baseline_style = is_traditional_style
                requested_hybrid_background = bool(normalized_request.informational_realistic_background)
                requested_colorful_background = bool(normalized_request.colorful_background_enhancer)
                if requested_hybrid_background:
                    effective_hybrid_background = bool(capabilities.supports_hybrid_background)
                    if requested_colorful_background:
                        if not effective_hybrid_background:
                            effective_colorful_background = bool(capabilities.supports_colorful_background)
                            if effective_hybrid_background:
                                background_mode = 'hybrid_realistic'
                            elif effective_colorful_background:
                                background_mode = 'colorful_background'
                            else:
                                background_mode = 'template_default'
    requested_reference_lock = bool(normalized_request.preserve_reference_character_style)
# WARNING: Decompyle incomplete


def _resolve_reference_usability_state(normalized_request = None):
    if normalized_request.include_character_reference and normalized_request.scene_character_count <= 0 or normalized_request.usable_reference_images <= 0:
        return 'none'
    if None.usable_reference_images < normalized_request.scene_character_count:
        return 'partial'


def _resolve_effective_locked_keys(*, requested_reference_lock, requested_locked_keys, scene_decision, effective_reference_lock, reference_usability_state):
