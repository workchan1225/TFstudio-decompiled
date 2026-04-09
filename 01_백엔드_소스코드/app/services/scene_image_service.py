# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_image_service.pyc (Python 3.11)

'''
Scene Image Service

대본 기반 장면 이미지 생성 서비스
- 챕터별 장면 분할
- 장면 프롬프트 생성 (템플릿 기반)
- 캐릭터 참조 이미지 생성
- 장면 이미지 일괄/개별 생성
'''
import os
import re
import sys
import json
import importlib
import base64
import uuid
import random
from typing import List, Dict, Optional, Any, Tuple, Callable, Set
from datetime import datetime
repair_broken_json = None

try:
    _json_repair_module = importlib.import_module('json_repair')
    repair_broken_json = getattr(_json_repair_module, 'repair_json', None)
except Exception:
    repair_broken_json = None

from models.project import Project
from models.settings import Settings
from models.image_prompt_template import ImagePromptTemplate
from google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from ai.google_provider import GoogleProvider
from image_template_service import ImageTemplateService, get_style_emphasis
from prompt.style_emphasis import apply_style_emphasis
from prompt.informational_style_contract import INFORMATIONAL_STYLE_PRIORITY_LOCK, build_informational_character_dimension_lock, build_informational_character_style_blueprint, build_informational_substyle_lock
from prompt.style_profile_filter import filter_style_template_visual_only as filter_style_template_visual_only_structured, strip_content_phrases_from_style as strip_content_phrases_from_style_structured
from prompt.scene_prompt_request_builder import build_scene_prompt_fallback_data, build_scene_prompt_request
from prompt.scene_prompt_response_parser import extract_scene_prompt_json_text, inspect_prompt_ko_quality
from prompt.scene_prompt_postprocessor import build_keyword_suffix, truncate_prompt_with_suffix_budget
from prompt.scene_diversity_guidance import build_scene_diversity_instruction, build_scene_diversity_profile, format_scene_diversity_diagnostics
from prompt.scene_style_mode_helper import resolve_flat_style_prompt_mode
from scene_character_selection_helper import extract_structured_prompt_context, normalize_keyword_text_config, select_scene_characters
from dialogue_line_parser import DialogueLineParser
from scene_cinematic_template_helper import apply_style_category_rules, run_template_and_cinematic_flow
from scene import CostumeGuideLoader, get_costume_guide, CharacterAnalyzerService, SceneSplitterService, ScenePromptComposer, SceneRedistributionService, CharacterReferenceGenerator
from scene.scene_actor_modeling import resolve_scene_actor_context
from scene.scene_cast_orchestration import apply_scene_cast_plan_to_actor_profile, build_scene_cast_plan, format_scene_cast_diagnostics
from scene.scene_framing_policy import format_scene_framing_diagnostics, resolve_scene_composition_subject_count
from scene.scene_identity_context import build_scene_identity_context, extract_scene_registered_character_names, extract_scene_resolved_character_ids
from scene.scene_prompt_conflict_guard import reconcile_scene_prompt_policies
from scene.scene_project_character_loader import resolve_effective_project_characters, resolve_effective_project_character_relationships
from scene.hybrid_background_policy import is_hybrid_background_capable_style as policy_is_hybrid_background_capable_style, rewrite_style_profile_for_hybrid
from scene.background_mode_policy import resolve_background_mode
from scene.reference_policy import REPLACEMENT_SCOPE_FULL_LOOK, extract_direct_reference_keys, extract_replaced_scope_map_from_character_images, filter_anchor_reference_map, normalize_replacement_scope_map, normalize_replaced_character_keys
from scene.reference_character_style_policy import resolve_reference_style_locked_keys
from scene.retry_policy import get_scene_request_timeout_seconds, get_scene_retry_policy
from scene.scene_prompt_name_normalizer import build_scene_prompt_alias_maps, collect_text_only_detected_character_names, normalize_reference_prompt_character_aliases
from scene.scene_prompt_post_assembly import apply_scene_prompt_post_assembly
from scene.scene_prompt_payload_assembler import assemble_multimodal_scene_payload, assemble_text_only_scene_payload
from scene.scene_generation_api_runner import build_scene_prompt_debug_lines, run_scene_generation_api_request
from scene.scene_generation_execution_runner_factory import SceneGenerationExecutionRequest, build_scene_generation_execution_kwargs
from scene.scene_generation_execution_flow import execute_scene_generation_flow
from scene.scene_generation_input_preparation import prepare_scene_generation_inputs
from scene.scene_result_builder import SceneResultBuilder
from scene.scene_keyword_manager import SceneKeywordManager
from scene.scene_generation_legacy_orchestrator import execute_scene_generation_legacy_orchestration
from scene.scene_generation_legacy_runner_factory import SceneGenerationLegacyRequest, build_scene_generation_legacy_runners
from scene.scene_generation_prompt_preparation import prepare_scene_generation_prompt, prepare_scene_keyword_text_config
from scene.scene_generation_reference_dispatch_flow import execute_scene_generation_reference_dispatch
from scene.scene_generated_image_postprocessor import build_scene_generation_response, postprocess_scene_generated_image
from scene.scene_multimodal_reference_builder import decode_data_url_part as decode_scene_multimodal_data_url_part, is_scene_derived_anchor_payload as is_scene_multimodal_scene_derived_anchor_payload, prepare_character_reference_image_parts, prepare_continuity_reference_image_parts, prepare_scene_multimodal_reference_context
from scene.scene_image_generation_reference_policy import resolve_scene_image_generation_reference_policy
from scene.scene_image_generation_text_policy import extract_keyword_tokens as extract_scene_generation_keyword_tokens, has_keyword_text_mode_enabled as resolve_scene_generation_keyword_text_mode_enabled, resolve_allow_text_rendering as resolve_scene_generation_allow_text_rendering, resolve_scene_image_generation_text_policy
from scene.line_index_matcher import calculate_line_index_range_for_scene as calculate_scene_line_index_range
from utils.cinematic_analyzer import analyze_scene_cinematics, get_cinematic_prompt_enhancement, CinematicDirection, analyze_emotional_intensity, get_crop_gravity_for_shot_type
from utils.scene_context_analyzer import get_dynamic_outfit, analyze_temporal_period
from utils.temporal_analyzer import get_temporal_analyzer, get_temporal_context_for_scene
from utils.whisk_prompt_optimizer import optimize_whisk_prompt, generate_negative_prompt
from utils.prompt_sanitizer import convert_negative_to_positive_guidance, sanitize_prompt_for_image_generation, get_policy_violation_message, apply_proactive_safety_check
from utils.nano_banana_optimizer import NanoBananaOptimizer, optimize_for_nano_banana
from supporting_character_service import SupportingCharacterService
from utils.korean_names import get_period_name_guidance, detect_period_from_text, infer_social_class, validate_name_for_period
from utils.action_verb_extractor import get_dynamic_pose_prompt, get_scene_intensity, get_disaster_actions, enhance_prompt_with_actions
from utils.scene_environment_analyzer import analyze_scene_environment, get_environment_prompt
from utils.character_interaction_analyzer import analyze_character_interaction, get_interaction_prompt, assign_screen_positions, extract_character_specific_actions, get_character_action_difference, extract_character_action_sentences
from utils.character_name_matcher import normalize_character_name, build_character_name_map, is_character_name_in_text, filter_characters_by_narration, is_flashback_character, filter_non_flashback_characters, is_future_reference_character, resolve_detected_characters, extract_partial_name
from utils.character_binding_mode import normalize_character_binding_mode
from utils.image_storage import scan_character_images_from_disk
HISTORICAL_CONTEXT_KEYWORDS = [
    '조선',
    '조선시대',
    '고려',
    '삼국시대',
    '신라',
    '백제',
    '고구려',
    '사극',
    '역사극',
    '야담',
    '한옥',
    '궁궐',
    '왕',
    '왕비',
    '양반',
    '선비',
    '도령',
    '낭자',
    '무림',
    '무협',
    '강호',
    '협객',
    '검객',
    '도사',
    '선협',
    'joseon',
    'goryeo',
    'sageuk',
    'historical korean',
    'korean dynasty',
    'period drama',
    'ancient korea',
    'traditional korean village',
    'martial arts world',
    'wuxia',
    'medieval',
    'feudal',
    'dynasty']
HISTORICAL_GENRES = [
    'JOSEON_FOLKTALE',
    'HISTORICAL',
    'MUHYUP',
    'THREE_KINGDOMS']

def filter_style_template_visual_only(template_text = None):
    if not template_text:
        return ''
    filtered = None(template_text)
    if template_text or filtered != ''.strip():
        print('[SceneImage] Structured style profile filtering applied')
    return filtered


def filter_content_phrases_from_style(template_text = None):
    if not template_text:
        return ''
    filtered = None(template_text)
    if template_text or filtered != ''.strip():
        print('[SceneImage] Structured inline content filtering applied')
    return filtered


def extract_location_context_lock(prompt_text = None):
    '''Extract primary location from LOCATION CONTEXT LOCK tag.'''
    if not prompt_text:
        return ''
    match = None.search('\\[LOCATION\\s+CONTEXT\\s+LOCK:\\s*Primary\\s+location\\s+is\\s*([^\\].]+)', prompt_text, flags = re.IGNORECASE)
    if not match:
        return ''
    return None.group(1).strip()


def build_location_conflict_negative(location_context = None):
    '''Build negative prompt hints to block obvious location drift.'''
    pass
# WARNING: Decompyle incomplete


def filter_negative_for_historical_context(negative_prompt = None, period_context = None):
