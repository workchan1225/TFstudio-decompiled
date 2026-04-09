# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hybrid_background_policy.pyc (Python 3.11)

'''Hybrid realistic-background policy helpers.

Centralizes style eligibility and prompt-scoping rules for mixed-media mode
(stylized characters + photorealistic background).
'''
import re
from typing import Optional
from style_template_capability_registry import supports_hybrid_background
HYBRID_BACKGROUND_ELIGIBLE_PREFIXES = ()

def is_hybrid_background_capable_style(visual_category = None):
    '''Return whether a visual category supports hybrid background mode.'''
    return supports_hybrid_background(visual_category)


def rewrite_style_profile_for_hybrid(style_profile = None):
    '''Narrow global anti-realism clauses to character scope for hybrid mode.

    This keeps legacy style templates intact for OFF mode while preventing
    instruction conflicts when background photorealism is explicitly enabled.
    '''
    if not style_profile:
        text = str('')
        if not text:
            return text
        rewritten = None
        replacements = (('\\bNO\\s+realistic\\s+features\\b', 'NO photorealistic character features'), ('\\bNO\\s+3D\\s+shading\\b', 'NO 3D shading on characters'), ('\\bcel[\\-\\s]*shad(?:ed|ing)\\b', 'cel-shading on characters only'), ('\\bflat\\s+(?:color|shading)\\b', 'flat shading on characters only'), ('\\blinework\\b', 'linework on characters only'), ('\\boutline\\s+style\\b', 'outline style on characters only'), ('\\billustration\\s+style\\b', 'illustration style for characters only'), ('\\banimation\\s+style\\b', 'animation style for characters only'))
        for pattern, replacement in replacements:
            rewritten = re.sub(pattern, replacement, rewritten, flags = re.IGNORECASE)
            return rewritten


def get_hybrid_priority_rule():
    '''Return a single conflict-resolution rule for hybrid mode.'''
    return 'If any instruction conflicts, prioritize stylized characters and photorealistic environment/background rendering.'
