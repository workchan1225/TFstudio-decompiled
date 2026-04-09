# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: background_mode_policy.pyc (Python 3.11)

'''Background mode policy helpers.

Ensures only one background-enhancement mode is active at once.
'''
from typing import Optional, TypedDict
from style_template_capability_registry import supports_colorful_background, supports_hybrid_background

class BackgroundModeDecision(TypedDict):
    use_colorful_background_enhancer: bool = 'BackgroundModeDecision'


def is_colorful_background_capable_style(visual_category = None):
    '''Colorful enhancer uses the same eligible style families as hybrid mode.'''
    return supports_colorful_background(visual_category)


def resolve_background_mode(visual_category = None, requested_hybrid_realistic_background = None, requested_colorful_background_enhancer = None):
