# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_generation_reference_dispatch_flow.pyc (Python 3.11)

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Sequence, Set
from scene_asset_reference_builder import build_scene_asset_context
from scene_identity_context import build_scene_identity_binding_characters, build_scene_identity_context, extract_scene_registered_character_names, extract_scene_resolved_character_ids, resolve_scene_identity_repair
SceneGenerationReferenceDispatchResult = <NODE:12>()

def _normalize_name_key(value = None):
