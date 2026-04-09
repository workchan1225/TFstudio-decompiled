# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: informational_template_filter.pyc (Python 3.11)

import re
from typing import Any, Callable, Dict, List, Optional

def prepare_informational_style_template(*, style_template, preserve_reference_character_style, informational_realistic_background, period_setting, style_visual_category, reference_locked_names, build_template_unique_identity_key_fn):
    if not style_template:
        resolved_template = str('')
        injected_unique_id = ''
        if '{unique_id}' in resolved_template:
            injected_unique_id = build_template_unique_identity_key_fn(reference_locked_names)
            resolved_template = resolved_template.replace('{unique_id}', injected_unique_id)
    filtered_template = resolved_template
    character_filter_before_length = len(filtered_template)
    if preserve_reference_character_style:
        filtered_template = _filter_character_directives(filtered_template)
    character_filter_after_length = len(filtered_template)
    environment_filter_result = _filter_environment_directives(filtered_template = filtered_template, resolved_template = resolved_template, informational_realistic_background = informational_realistic_background, period_setting = period_setting, style_visual_category = style_visual_category)
    filtered_template = environment_filter_result['filtered_template']
    style_portion = _extract_style_portion(filtered_template = filtered_template, preserve_reference_character_style = preserve_reference_character_style)
    return {
        'resolved_template': resolved_template,
        'filtered_template': filtered_template,
        'style_portion': style_portion,
        'injected_unique_id': injected_unique_id,
        'character_filter_before_length': character_filter_before_length,
        'character_filter_after_length': character_filter_after_length,
        'environment_filter_before_length': environment_filter_result['before_length'],
        'environment_filter_after_length': environment_filter_result['after_length'],
        'environment_filter_applied': environment_filter_result['applied'],
        'environment_filter_reason': environment_filter_result['reason'],
        'is_modern_period_style_conflict': environment_filter_result['is_modern_period_style_conflict'] }


def _filter_character_directives(template_text = None):
    if not template_text:
        filtered_template = str('')
        character_patterns = [
            'Characters:\\s*[^.]+?(?=\\s*(?:Quality|Mood|Style|Technique|Colors|IMPORTANT|Background|\\.|$))',
            'Characters:\\s*[^\\n]+',
            'CHARACTER\\s*\\([^)]*\\)\\s*:.*?(?=BACKGROUND|CRITICAL:|$)',
            '-\\s*Character\\s+MUST\\s+be\\s+simple[^-\\n]*',
            '-\\s*Character\\s+MUST\\s+be\\s+stickman[^-\\n]*',
            '[Ss]imple\\s+stickman/?webtoon\\s+character[^.]*\\.',
            '[Ss]imple\\s+stickman[^.]*environment[^.]*\\.',
            '[Ss]tickman[^.]*character[^.]*\\.',
            '-\\s*Face:\\s*[Rr]ound\\s+WHITE[^-\\n]*',
            '-\\s*Body:\\s*[Ss]tick-figure[^-\\n]*',
            '-\\s*Style:\\s*[Mm]inimal[^-\\n]*',
            '-\\s*Expression:[^-\\n]*simple[^-\\n]*',
            '-\\s*NO\\s+realistic\\s+features[^-\\n]*',
            '-\\s*NO\\s+3D\\s+shading[^-\\n]*',
            '-\\s*Strong\\s+contrast:\\s*simple\\s+character[^-\\n]*',
            '\\([^)]*Cyanide[^)]*\\)',
            'webtoon/cartoon\\s+aesthetic',
            'minimal,\\s*clean,\\s*webtoon']
        for pattern in character_patterns:
            filtered_template = re.sub(pattern, '', filtered_template, flags = re.IGNORECASE | re.DOTALL)
            filtered_template = re.sub('CRITICAL:\\s*-?\\s*(?=-|$)', '', filtered_template)
            filtered_template = re.sub('-\\s*-', '-', filtered_template)
            filtered_template = re.sub('\\n\\s*\\n', '\n', filtered_template)
            filtered_template = re.sub('\\s+', ' ', filtered_template).strip()
            return filtered_template


def _filter_environment_directives(*, filtered_template, resolved_template, informational_realistic_background, period_setting, style_visual_category):
    pass
# WARNING: Decompyle incomplete


def _sanitize_abstract_character_rendering_for_hybrid(template_text = None, *, style_visual_category, resolved_template):
    pass
# WARNING: Decompyle incomplete


def _extract_style_portion(*, filtered_template, preserve_reference_character_style):
    if not filtered_template:
        style_portion = str('')
        for placeholder in ('{base_prompt}', '{scene_description}', '{concept}'):
            style_portion = style_portion.replace(placeholder, '')
            style_portion = re.sub('\\{[^}]+\\}', '', style_portion)
            style_portion = re.sub(',\\s*,', ',', style_portion)
            style_portion = re.sub('\\s+', ' ', style_portion).strip().strip(',').strip()
            if preserve_reference_character_style:
                style_portion = re.sub('Characters:\\s*[^.]+?(?=\\s*(?:Quality|Mood|Style|Technique|Colors|IMPORTANT|Background|\\.|$))', '', style_portion, flags = re.IGNORECASE)
                style_portion = re.sub('Characters:\\s*[^\\n]+', '', style_portion, flags = re.IGNORECASE)
                style_portion = re.sub('\\s+', ' ', style_portion).strip()
    return style_portion
