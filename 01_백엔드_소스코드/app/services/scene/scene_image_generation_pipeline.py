# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_image_generation_pipeline.pyc (Python 3.11)

from typing import Any, Dict, List
from scene_decision import build_public_scene_decision_summary
from scene_image_generation_mode_resolver import resolve_scene_image_generation_mode
from scene_image_generation_normalizer import normalize_pipeline_request
from scene_image_generation_style_contract import resolve_scene_image_generation_style_contract
from scene_image_generation_types import SceneImageGenerationPipelineRequest, SceneImageGenerationPipelineResolution, SceneImageGenerationStyleContract

class SceneImageGenerationPipelineService:
    '''Shared orchestration entrypoint for scene image generation flows.'''
    generate = (lambda request = None: normalized_request = normalize_pipeline_request(request)resolution = SceneImageGenerationPipelineService.resolve(normalized_request)style_contract = resolve_scene_image_generation_style_contract(normalized_request)effective_payload = SceneImageGenerationPipelineService._sanitize_payload_for_scene_batch(request.payload)# WARNING: Decompyle incomplete
)()
    resolve = (lambda normalized_request = None: resolve_scene_image_generation_mode(normalized_request))()
    _is_scene_batch_request_source = (lambda value = None:
