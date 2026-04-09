# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subtitle_runtime_style_resolver.pyc (Python 3.11)

'''
Runtime subtitle/title style resolver shared by preview, sample and final render paths.
'''
from __future__ import annotations
from typing import Any, Dict, Literal, Mapping
from app.constants.subtitle_style_defaults import merge_with_defaults
from app.constants.title_layer_defaults import merge_title_layer_with_defaults
Orientation = Literal[('landscape', 'portrait')]
LANDSCAPE_BASE_WIDTH = 1920
PORTRAIT_BASE_WIDTH = 1080
SUBTITLE_FONT_SCALE_MULTIPLIER = 1.22188
ALIGNMENT_MAP = {
    'top': {
        'left': 7,
        'center': 8,
        'right': 9 },
    'center': {
        'left': 4,
        'center': 5,
        'right': 6 },
    'middle': {
        'left': 4,
        'center': 5,
        'right': 6 },
    'bottom': {
        'left': 1,
        'center': 2,
        'right': 3 } }
POS_ALIGNMENT_MAP = {
    'left': 4,
    'center': 5,
    'right': 6 }

def get_orientation(video_width = None, video_height = None):
    return 'portrait' if video_width < video_height else 'landscape'


def _normalize_percent(value = None, default = None, minimum = None, maximum = (0, 100)):
    
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        numeric = float(default)

    return max(minimum, min(maximum, numeric))


def _normalize_scale_value(value = None, default = None):
    
    try:
        return float(value)
    except (TypeError, ValueError):
        return 



def _scale_length(value = None, scale_factor = None, default = None, minimum = (0, 0)):
    numeric = _normalize_scale_value(value, default)
    return max(int(minimum), int(round(numeric * scale_factor)))


def _calculate_render_scale(video_width = None, orientation = None):
    base_width = PORTRAIT_BASE_WIDTH if orientation == 'portrait' else LANDSCAPE_BASE_WIDTH
    if base_width <= 0:
        return 1
    return None(0.01, float(video_width) / float(base_width))


def infer_vertical_position(position_y_percent = None):
    numeric = _normalize_percent(position_y_percent, 50)
    if numeric <= 33:
        return 'top'
    if None >= 66:
        return 'bottom'


def calculate_runtime_position(*, video_width, video_height, position_x_percent, position_y_percent, horizontal_margin_percent, font_size_px):
    margin_percent = _normalize_percent(horizontal_margin_percent, 2.5, 0, 50)
    margin_px = int(video_width * margin_percent / 100)
    raw_x = int(video_width * _normalize_percent(position_x_percent, 50) / 100)
    clamped_x = max(margin_px, min(raw_x, video_width - margin_px))
    raw_y = int(video_height * _normalize_percent(position_y_percent, 90) / 100)
    estimated_height = max(1, int(font_size_px * 1.5))
    min_y = int(estimated_height / 2)
    max_y = int(video_height - estimated_height / 2)
    clamped_y = max(min_y, min(raw_y, max_y))
    return {
        'rawX': raw_x,
        'rawY': raw_y,
        'marginPx': margin_px,
        'clampedX': clamped_x,
        'clampedY': clamped_y,
        'estimatedHeightPx': estimated_height }


def calculate_runtime_wrap_width(*, video_width, orientation, horizontal_margin_percent, max_width_percent):
    margin_percent = _normalize_percent(horizontal_margin_percent, 2.5, 0, 50) / 100
    usable_percent = max(0, 1 - margin_percent * 2)
    width_correction = 1.2 if orientation == 'portrait' else 1.15
    user_max_width_percent = _normalize_percent(max_width_percent, 100, 0, 100) / 100
    return max(1, int(video_width * usable_percent * width_correction * user_max_width_percent))


def calculate_runtime_padding(*, font_size_px, enable_stroke, stroke_width_px):
    base_padding = 15
    outline_value = stroke_width_px if enable_stroke and stroke_width_px > base_padding else base_padding
    x_padding = max(1, int(round(outline_value)))
    y_padding = max(1, min(2, int(round(font_size_px * 0.02))))
    y_padding = min(y_padding, max(1, x_padding - 1))
    return {
        'outlineValue': outline_value,
        'x': x_padding,
        'y': y_padding }


def _resolve_runtime_style(style_settings = None, *, orientation, video_width, video_height, kind):
    if kind == 'title':
        if not style_settings:
            merged_style = merge_title_layer_with_defaults(dict({ }), orientation)
            merged_style.setdefault('useCustomPosition', True)
            merged_style.setdefault('position', infer_vertical_position(merged_style.get('positionY', 10)))
        elif not style_settings:
            merged_style = dict(style_settings({ }), orientation)
            merged_style.setdefault('position', infer_vertical_position(merged_style.get('positionY', 90)))
            render_scale = _calculate_render_scale(video_width, orientation)
    visual_scale = render_scale * SUBTITLE_FONT_SCALE_MULTIPLIER if kind == 'subtitle' else 1
    font_size_px = max(1, _scale_length(merged_style.get('fontSize', 54), visual_scale, default = 54, minimum = 1))
    stroke_width_px = _scale_length(merged_style.get('strokeWidth', 0), visual_scale)
    shadow_blur_px = _scale_length(merged_style.get('shadowBlur', 0), visual_scale)
    shadow_offset_x_px = _scale_length(merged_style.get('shadowOffsetX', 0), visual_scale)
    shadow_offset_y_px = _scale_length(merged_style.get('shadowOffsetY', 0), visual_scale)
    letter_spacing_px = _scale_length(merged_style.get('letterSpacing', 0), visual_scale)
    if not merged_style.get('position'):
        position = infer_vertical_position(merged_style.get('positionY', 50))
        alignment = merged_style.get('alignment', 'center')
    runtime_position = calculate_runtime_position(video_width = video_width, video_height = video_height, position_x_percent = merged_style.get('positionX', 50), position_y_percent = merged_style.get('positionY', 90 if kind == 'subtitle' else 10), horizontal_margin_percent = merged_style.get('horizontalMargin', 2.5), font_size_px = font_size_px)
    wrap_width_px = calculate_runtime_wrap_width(video_width = video_width, orientation = orientation, horizontal_margin_percent = merged_style.get('horizontalMargin', 2.5), max_width_percent = merged_style.get('maxWidth', 100 if kind == 'subtitle' else 90))
    padding = calculate_runtime_padding(font_size_px = font_size_px, enable_stroke = merged_style.get('enableStroke', kind == 'title'), stroke_width_px = stroke_width_px)
    runtime_style = dict(merged_style)
# WARNING: Decompyle incomplete


def resolve_runtime_subtitle_style(style_settings = None, *, video_width, video_height):
    orientation = get_orientation(video_width, video_height)
    return _resolve_runtime_style(style_settings, orientation = orientation, video_width = video_width, video_height = video_height, kind = 'subtitle')


def resolve_runtime_title_layer_style(layer_settings = None, *, orientation, video_width, video_height):
    return _resolve_runtime_style(layer_settings, orientation = orientation, video_width = video_width, video_height = video_height, kind = 'title')
