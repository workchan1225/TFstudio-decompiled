# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_image_generation_mode_resolver.pyc (Python 3.11)

from scene_image_generation_types import SceneImageGenerationMode, SceneImageGenerationNormalizedRequest, SceneImageGenerationPipelineResolution

def resolve_scene_image_generation_mode(normalized_request = None):
    if not normalized_request.scene_decision and { }.get('renderMode'):
        decision_render_mode = str('').strip()
        has_informational_visual_category = 'style_visual_category' in normalized_request.mode_hints
    resolved_mode = 'informational' if decision_render_mode == 'informational' and normalized_request.request.entrypoint == 'informational' or has_informational_visual_category else 'scene'
    inferred_mode = 'informational' if normalized_request.mode_hints else 'scene'
    mode_reasons = list(normalized_request.mode_hints)
    if decision_render_mode:
        mode_reasons.append('scene_decision_render_mode')
    if not mode_reasons:
        mode_reasons.append('default_scene')
# WARNING: Decompyle incomplete
