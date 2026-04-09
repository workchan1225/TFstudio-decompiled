# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_result_builder.pyc (Python 3.11)

'''
SceneResultBuilder - 장면 결과 조립 모듈

Phase 1: scene_redistribution_service.py의 main path와 chunked retry에서
중복된 결과 조립 로직을 통합.

주요 역할:
- Scene result dict 구성
- 캐릭터 감지/해석
- lineIndexRange 계산
- temporal context 할당
- fidelity score 부착
'''
import hashlib
import json
import re
from typing import Any, Dict, List, Optional
from scene_decision import NARRATIVE_GENRE_KEYS
from utils.character_name_matcher import normalize_character_name, resolve_exact_character_identity_name, resolve_detected_characters, resolve_role_names_to_character_names
from utils.temporal_analyzer import get_temporal_context_for_scene
from scene_anchor_metadata import attach_scene_anchor_metadata_to_structured_prompt, build_scene_anchor_payload
from scene_actor_modeling import build_scene_actor_profile, build_scene_actors
from scene_cast_orchestration import apply_scene_cast_plan_to_actor_profile, build_scene_cast_plan
from scene_decision import build_scene_decision, format_scene_decision_debug
from scene_expression_plan import build_scene_expression_plan
from scene_identity_context import build_scene_identity_audit, build_scene_identity_context
from scene_staging_plan import build_scene_staging_plan
from scene_prompt_conflict_guard import reconcile_scene_prompt_policies
from scene_prompt_composer import ScenePromptComposer
from scene_splitter_service import SceneSplitterService

class SceneResultBuilder:
    '''AI 응답 장면 데이터를 최종 결과 dict 리스트로 변환'''
    _GENERIC_IMAGE_PROMPT_PATTERNS = (re.compile('^a\\s+cinematic\\s+scene\\s+from\\s+chapter\\s+\\d+', flags = re.IGNORECASE), re.compile('atmospheric\\s+and\\s+visually\\s+engaging\\s+composition', flags = re.IGNORECASE), re.compile('^(horizontal|vertical)\\s+\\d+:\\d+.*cinematic', flags = re.IGNORECASE))
    build_result_scenes = (lambda scenes_data, chapter_index, chapter_title, chapter_content, target_scene_count, chapter_dialogue_lines, characters, normalized_binding_mode, local_upload_fallback_name, temporal_structure, fidelity_scores = None, speaker_mode = None, content_category = staticmethod, style_visual_category = (None, 'multi_speaker', '', '', 'redistribution'), route_name = ('scenes_data', List[Dict[(str, Any)]], 'chapter_index', int, 'chapter_title', str, 'chapter_content', str, 'target_scene_count', int, 'chapter_dialogue_lines', List[Dict[(str, Any)]], 'characters', Optional[List[Dict[(str, Any)]]], 'normalized_binding_mode', str, 'local_upload_fallback_name', Optional[str], 'temporal_structure', Optional[Dict[(str, Any)]], 'fidelity_scores', Optional[Dict[(int, float)]], 'speaker_mode', str, 'content_category', str, 'style_visual_category', str, 'route_name', str, 'return', List[Dict[(str, Any)]]): SceneRedistributionService = SceneRedistributionServiceimport scene_redistribution_service_effective_content_cat = str(content_category).strip().lower()if route_name == 'redistribution':
if speaker_mode == 'single_narrator' or _effective_content_cat not in NARRATIVE_GENRE_KEYS or str(style_visual_category).lower().startswith('informational'):
route_name = 'informational'result_scenes = []previous_scene_end_line_index = -1# WARNING: Decompyle incomplete
)()
    _build_scene_id = (lambda *:
