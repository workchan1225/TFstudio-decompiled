# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_redistribution_service.pyc (Python 3.11)

'''
SceneRedistributionService - 장면 재분배 서비스

scene_image_service.py에서 추출됨 (Phase 5 리팩토링)

주요 기능:
- 챕터 내용을 AI가 분석하고 장면으로 분할
- 장면 수 재조정 (분할/병합)
- JSON 응답 파싱 및 복구
'''
import re
import json
from copy import deepcopy
from typing import Dict, List, Any, Optional, Tuple
from models.settings import Settings
from services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from utils.character_name_matcher import normalize_character_name
from utils.temporal_analyzer import get_temporal_analyzer, get_temporal_context_for_scene
from utils.character_binding_mode import normalize_character_binding_mode
from line_index_matcher import build_even_line_index_range, calculate_line_index_range_for_scene as calculate_scene_line_index_range, normalize_keyword_text_for_matching
from scene_anchor_metadata import attach_scene_anchor_metadata_to_structured_prompt, build_scene_anchor_payload
from scene_script_unit_builder import build_chapter_sentence_units
from prompt.scene_diversity_guidance import build_scene_split_diversity_hints, build_diversity_hint_prompt_section, build_scene_diversity_profile, validate_scene_diversity
from prompt.scene_split_prompt_builder import SceneSplitPromptBuilder
from scene_keyword_manager import SceneKeywordManager
from scene_result_builder import SceneResultBuilder

try:
    from json_repair import repair_json as repair_broken_json
except ImportError:
    repair_broken_json = None


class SceneRedistributionService:
    '''챕터를 장면으로 분할하고 재분배하는 서비스'''
    _STRICT_SENTENCE_COVERAGE_THRESHOLD = 1
    _SEMANTIC_SENTENCE_COVERAGE_THRESHOLD = 0.85
    _GROUNDED_SENTENCE_RANGE_COVERAGE_THRESHOLD = 0.999
    _TEMPORAL_MARKER_REGEX = re.compile('(\\d+\\s*년\\s*전|\\d+\\s*년\\s*후|\\d+\\s*세\\s*때|다시\\s*(현재|지금|오늘날)|현재로\\s*돌아|현실로\\s*돌아)', re.IGNORECASE)
    _TEMPORAL_FLASHBACK_HINTS = ('회상', '과거', '어린 시절', '젊은 시절', '그때', '옛날', '추억', '기억이 떠올', '그 시절', '과거로 돌아', '되돌아가')
    _TEMPORAL_RETURN_HINTS = ('현재로 돌아', '현재 시점', '오늘날', '지금은', '현실로 돌아', '세월이 지나', '세월이 흘러', '시간이 지나', '시간이 흘러')
    _resolve_scene_segment_split_reason = (lambda scene = None, default_split_reason = None:
