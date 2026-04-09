# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: informational_style_mode_builder.pyc (Python 3.11)

import re
from typing import Dict

def build_informational_style_mode_block(*, style_portion, preserve_reference_character_style, informational_realistic_background, allow_clothing_override, is_modern_period_style_conflict):
    style_name = _extract_style_name(style_portion)
    if preserve_reference_character_style:
        if informational_realistic_background:
            return {
                'style_prefix': '[STYLE MODE: hybrid | characters=reference-locked | background=photorealistic]\n\n',
                'style_declaration': '',
                'log_message': '[InformationalImage] 스타일 적용: 캐릭터=참조 유지, 배경=실사 (간소화 마커, 상세는 Step 4.5)' }
        style_prefix = None + 'CHARACTERS: Wardrobe may change to follow user direction.\n' if allow_clothing_override else '' + f'''BACKGROUND: Apply {style_name} VISUAL STYLE ONLY (line art, colors, shading, rendering technique).\n''' + "BACKGROUND CONTENT: Keep buildings, environment, setting as described in scene prompt - do NOT change to match style's era/setting.\n" + f'''Do NOT apply {style_name} style to characters - keep identity/rendering anchored to reference images.\n\n'''
        return {
            'style_prefix': style_prefix,
            'style_declaration': '',
            'log_message': f'''[InformationalImage] 스타일 적용: 캐릭터=참조 유지, 배경={style_name}''' }
    if None:
        return {
            'style_prefix': f'''[STYLE MODE: hybrid | characters={style_name} | background=photorealistic]\n\n''',
            'style_declaration': f''' [Character art style: {style_name} on characters ONLY. Background MUST be photorealistic photograph quality]''',
            'log_message': f'''[InformationalImage] 스타일 적용: 캐릭터={style_name}, 배경=실사 (간소화 마커, 상세는 Step 4.5)''' }
    if None:
        return {
            'style_prefix': f'''[MODERN ERA CONTENT LOCK]\nApply selected style as VISUAL RENDERING LANGUAGE ONLY (linework, palette, shading, texture).\nDo NOT import era-specific motifs or historical setting cues from the style template.\nMANDATORY CONTENT ERA: modern contemporary clothing, architecture, props, and lighting.\nRendering style reference: {style_portion[:200]}\n[END MODERN ERA CONTENT LOCK]\n\n''',
            'style_declaration': ' [Art rendering: keep selected style texture/palette only; content era remains strictly modern]',
            'log_message': '[InformationalImage] 스타일 적용: 렌더링만 유지 + 현대 콘텐츠 강제' }
    return {
        'style_prefix': None,
        'style_declaration': f''' [Art style: {style_portion[:80]}]''',
        'log_message': '[InformationalImage] 스타일 적용: 전체 (캐릭터 포함)' }


def _extract_style_name(style_portion = None):
