# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_generation_prompt_blocks.pyc (Python 3.11)

from typing import Iterable, List

def build_no_text_symbol_lock_prefix():
    return '[NO TEXT/SYMBOL LOCK - HIGHEST PRIORITY] Do NOT render ANY text, letters, numbers, digits, symbols, currency marks, percentages, labels, signs, subtitles, captions, logos, or watermarks anywhere in the image. The image must contain ZERO readable characters or symbolic marks of any kind. Never render square-bracket metadata tokens such as [Image 1], [Scene], [Character].'


def build_keyword_exact_once_rule_lines():
    return [
        'Render only the requested keywords as short in-scene text; selected keywords only, and do not invent additional keyword copies, narration, dialogue, or numeric data labels.',
        'Each selected keyword may appear at most once in the entire image.',
        'Never render the same keyword on multiple carriers.',
        'Use one carrier per keyword.',
        'If there are not enough natural carriers, omit lower-priority keywords instead of duplicating them.',
        'Total visible keyword/text instances must not exceed the number of selected keywords.',
        'If a keyword is already rendered once, do not render it again elsewhere in the image.']


def build_keyword_text_mode_prefix(keywords = None):
    quoted_keywords = (lambda .0: pass# WARNING: Decompyle incomplete
)(keywords())
    exact_once_rules = ' '.join(build_keyword_exact_once_rule_lines())
    return f'''[KEYWORD TEXT MODE ENABLED - STRUCTURAL POLICY] Target Korean keywords/phrases: {quoted_keywords}. Readable in-scene Korean text must appear. {exact_once_rules} If there are multiple keywords, assign one carrier per keyword and place each keyword on a different in-scene object/surface in different positions; never cluster all keywords on one sign. Text must be naturally embedded on a physical in-scene surface, never floating or subtitle-like. Keep the main character/action as the primary focus; keyword text is secondary scene dressing. Never render character names or @mentions as visible text. CHARACTER STYLE LOCK: Keep ALL characters in the SAME art style as their reference images. Do NOT change character rendering style because of text — text is additive, character style is immutable.'''


def build_exact_character_count_instruction(character_count = None):
    return f'''EXACTLY {character_count} CHARACTERS: render exactly {character_count} people, no more, no less. '''


def build_face_separation_and_differentiation_instruction(character_count = None, *, preserve_reference_anchors):
    if preserve_reference_anchors:
        return f'''FACE SEPARATION & DIFFERENTIATION ({character_count} characters): Each character MUST have a uniquely different face shape, apparent age cues, and overall silhouette. NEVER draw {character_count} people with the same face - they are DIFFERENT individuals. Preserve each referenced character\'s existing hairstyle silhouette and signature outfit palette. Differentiate through face geometry, accessories, pose, spacing, blocking, and expression instead of redesigning hair or wardrobe. Place characters at natural conversational distance - NO face merging or overlapping. '''
    return f'''{character_count} characters): Each character MUST have a uniquely different face shape, hairstyle silhouette, and apparent age. NEVER draw {character_count} people with the same face - they are DIFFERENT individuals. Vary hairstyle dramatically (updo vs braided vs loose vs short). Place characters at natural conversational distance - NO face merging or overlapping. '''


def build_multi_character_interaction_rules(character_count = None, *, all_characters_have_reference_images):
    base_block = f'''Interaction rules ({character_count} characters):\nCharacters look at EACH OTHER (not camera). Different expressions per character. Natural conversation poses.\n\nFACE SEPARATION LOCK (CRITICAL - NO FACE OVERLAP):\n- Each character\'s face MUST be clearly distinct and separated from other characters\' faces.\n- NO face merging, blending, or overlapping between any two characters.\n- Maintain MINIMUM visible gap between character heads/faces - no touching or fusing.\n- Each face must have its own clear boundary, distinct features, and independent expression.\n- Place characters at NATURAL conversational distance (arm\'s length or more apart).\n- If {character_count} characters in frame: use STAGGERED DEPTH placement (foreground/mid/background) to avoid crowding.\n- Characters may overlap in BODY only (e.g. one behind another), but faces must NEVER overlap or blend.'''
    if all_characters_have_reference_images:
        suffix = "\n\nREFERENCE IMAGE IDENTITY LOCK (CRITICAL - MATCH REFERENCE IMAGES):\n- Each character MUST look EXACTLY like their corresponding reference image above.\n- Do NOT exaggerate, alter, or invent facial features, hairstyle, or body proportions.\n- The reference images already define each character's unique identity — preserve them faithfully.\n- If two reference images look similar, still reproduce each EXACTLY as shown — do NOT artificially differentiate.\n- Use different expressions and poses per character, but keep their physical appearance locked to their reference."
    else:
        suffix = f'''\n\nVISUAL IDENTITY DIFFERENTIATION (CRITICAL - NO CLONE FACES):\n- Each character MUST have a UNIQUELY DIFFERENT face: vary face shape (round vs oval vs angular), eye size, nose shape, eyebrow thickness.\n- Distinguish characters through hairstyle silhouette, accessories, age cues, body-size ratio, pose, and placement; if any character is reference-backed, preserve that existing hairstyle silhouette instead of redesigning it.\n- NEVER draw {character_count} characters with the same face or the same overall visual identity - they are DIFFERENT people.\n- If reference images look similar, exaggerate differences in face shape, age appearance, accessories, and blocking before changing hair or wardrobe.\n- Use different accessories per character (hair ornaments, ribbons, pins, eyewear, props) to reinforce visual identity.'''
    return f'''{base_block}{suffix}'''
