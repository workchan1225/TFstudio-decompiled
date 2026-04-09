# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: style_template_capability_registry.pyc (Python 3.11)

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Literal, Optional
CharacterDimensionMode = Literal[('flat_2d', 'pseudo_3d', 'photoreal')]
StyleScopePolicy = Literal[('full_frame', 'split_subject_background', 'background_only_when_reference_locked', 'template_visual_dna_only')]
BackgroundRenderMode = Literal[('template_default', 'hybrid_realistic_supported', 'colorful_background_supported')]
HYBRID_CAPABLE_PREFIXES = ('informational', 'animation', 'illustration')
HYBRID_BLOCKED_PREFIXES = ('realistic', 'traditional')
PSEUDO_3D_VISUAL_CATEGORIES = {
    'informational_isometric'}
StyleTemplateCapabilities = <NODE:12>()
STYLE_TEMPLATE_CAPABILITY_OVERRIDES_BY_ID: 'Dict[str, Dict[str, Any]]' = { }
STYLE_TEMPLATE_CAPABILITY_OVERRIDES_BY_VISUAL_CATEGORY: 'Dict[str, Dict[str, Any]]' = {
    'informational_isometric': {
        'supports_hybrid_background': True,
        'supports_colorful_background': True,
        'character_dimension_mode': 'pseudo_3d',
        'style_scope_policy': 'split_subject_background',
        'background_render_mode': 'hybrid_realistic_supported' } }

def resolve_style_template_capabilities(*, style_template_id, visual_category):
    normalized_template_id = _normalize_text(style_template_id)
    normalized_category = _normalize_text(visual_category).lower()
    base = _build_default_capabilities(style_template_id = normalized_template_id, visual_category = normalized_category)
    category_override = STYLE_TEMPLATE_CAPABILITY_OVERRIDES_BY_VISUAL_CATEGORY.get(normalized_category, { })
    template_override = STYLE_TEMPLATE_CAPABILITY_OVERRIDES_BY_ID.get(normalized_template_id, { })
    payload = dict(base)
    payload.update(category_override)
    payload.update(template_override)
# WARNING: Decompyle incomplete


def supports_hybrid_background(visual_category = None, *, style_template_id):
    return resolve_style_template_capabilities(style_template_id = style_template_id, visual_category = visual_category).supports_hybrid_background


def supports_colorful_background(visual_category = None, *, style_template_id):
    return resolve_style_template_capabilities(style_template_id = style_template_id, visual_category = visual_category).supports_colorful_background


def _build_default_capabilities(*, style_template_id, visual_category):
    if visual_category in PSEUDO_3D_VISUAL_CATEGORIES:
        character_dimension_mode = 'pseudo_3d'
    elif visual_category.startswith('realistic'):
        character_dimension_mode = 'photoreal'
    else:
        character_dimension_mode = 'flat_2d'
    if bool(visual_category):
        if visual_category.startswith(HYBRID_CAPABLE_PREFIXES):
            hybrid_supported = not visual_category.startswith(HYBRID_BLOCKED_PREFIXES)
            if hybrid_supported:
                style_scope_policy = 'split_subject_background'
                background_render_mode = 'hybrid_realistic_supported'
            else:
                style_scope_policy = 'full_frame'
                background_render_mode = 'template_default'
    return {
        'style_template_id': style_template_id,
        'visual_category': visual_category,
        'supports_hybrid_background': hybrid_supported,
        'supports_colorful_background': hybrid_supported,
        'allow_reference_lock': True,
        'character_dimension_mode': character_dimension_mode,
        'style_scope_policy': style_scope_policy,
        'background_render_mode': background_render_mode }


def _normalize_text(value = None):
    pass
# WARNING: Decompyle incomplete
