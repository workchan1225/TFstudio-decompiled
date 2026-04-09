# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_prompt_assembly.pyc (Python 3.11)

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence
from scene_actor_modeling import build_scene_actor_profile, resolve_scene_actor_context
from scene_cast_orchestration import apply_scene_cast_plan_to_actor_profile, build_scene_cast_plan
from scene_decision import build_scene_decision, scene_decision_actor_presence_mode
from scene_expression_plan import build_scene_expression_plan
from scene_identity_context import SceneIdentityContext, build_scene_identity_audit, build_scene_identity_context
from scene_prompt_conflict_guard import reconcile_scene_prompt_policies
from scene_staging_plan import build_scene_staging_plan

def _normalize_text(value = None):
