# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: informational_image_service.pyc (Python 3.11)

'''
InformationalImageService - 정보성 콘텐츠 스타일 이미지 생성 서비스

핵심 기능:
1. 나레이션/대화에서 핵심 장면 추출 (AI)
2. 스타일 템플릿 강화 적용
3. 텍스트 제어 (키워드 오버레이 또는 텍스트 방지)
4. 이미지 생성 및 저장
'''
import re
import uuid
import base64
import hashlib
import logging
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple
from services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from utils.character_name_matcher import normalize_character_name, resolve_exact_character_identity_name, resolve_role_names_to_character_names
from scene.scene_image_generation_reference_policy import resolve_scene_image_generation_reference_policy
from scene.scene_reference_lock_resolver import resolve_reference_locked_character_names, resolve_replacement_scope_character_names
from scene.scene_single_subject_policy import build_single_registered_subject_lock, collapse_generic_human_subject_description, resolve_single_registered_subject_character, resolve_subject_display_name, rewrite_single_subject_role_aliases, should_apply_single_subject_lock
from scene.scene_actor_modeling import build_scene_actor_policy_lines, build_scene_actor_prompt_block, resolve_scene_actor_context
from scene.scene_asset_reference_builder import build_scene_asset_context, build_scene_asset_prompt_blocks
from scene.scene_cast_orchestration import apply_scene_cast_plan_to_actor_profile, build_scene_cast_plan, build_scene_cast_prompt_block, format_scene_cast_diagnostics
from scene.scene_identity_context import build_scene_identity_audit, build_scene_binding_characters_from_unique_ids, build_scene_identity_binding_characters, build_scene_identity_context, resolve_scene_identity_repair
from scene.scene_project_character_loader import resolve_effective_project_characters, resolve_effective_project_character_relationships
from scene.scene_staging_plan import build_scene_staging_plan, build_scene_staging_prompt_block
from scene.scene_expression_plan import build_scene_expression_plan, build_scene_expression_prompt_block
from scene.scene_prompt_conflict_guard import reconcile_scene_prompt_policies
from scene.scene_prompt_assembly import build_scene_prompt_assembly
from scene.scene_framing_policy import format_scene_framing_diagnostics, resolve_scene_composition_subject_count
from scene.scene_image_generation_text_policy import resolve_scene_image_generation_text_policy
from scene.scene_keyword_manager import SceneKeywordManager
from scene.scene_decision import build_public_scene_decision_summary, build_scene_decision, build_scene_decision_prompt_blocks
from scene.scene_prompt_block_plan import prepend_scene_prompt_blocks
from prompt.informational_style_contract import build_informational_style_lock, build_informational_character_style_blueprint, build_informational_final_style_enforcement, build_informational_scene_variation_lock
from prompt.informational_style_mode_builder import build_informational_style_mode_block
from prompt.informational_background_grounding import build_background_scene_fit_lock
from prompt.informational_template_filter import prepare_informational_style_template
from prompt.scene_multimodal_prompt_blocks import build_hybrid_background_final_guard, build_multimodal_reference_policy_lines, build_stickman_multimodal_checklist, build_style_category_checklist
from prompt.scene_generation_prompt_blocks import build_exact_character_count_instruction, build_face_separation_and_differentiation_instruction, build_keyword_exact_once_rule_lines, build_keyword_text_mode_prefix, build_multi_character_interaction_rules, build_no_text_symbol_lock_prefix
from prompt.informational_scene_dynamics import build_scene_dynamics_directive
logger = logging.getLogger(__name__)
ABSTRACT_STYLE_KEYWORDS = ('stickman', 'stick figure', 'minimalist', 'simple line', 'geometric', 'pixel art', '8-bit', '16-bit', 'retro game')

def _is_abstract_style(style_template = None):
    '''스타일 템플릿이 추상/비사실주의 스타일인지 판단'''
    pass
# WARNING: Decompyle incomplete


class InformationalImageService:
    __module__ = __name__
    __qualname__ = 'InformationalImageService'
    __doc__ = '정보성 이미지 생성 전문 서비스'
    NO_TEXT_SUFFIX = ''
    COMPACT_RETRY_PROMPT_MAX_CHARS = 2400
    COMPACT_RETRY_REFERENCE_LIMIT = 2
    KEYWORD_POSITION_HINTS = {
        'top': 'upper composition area',
        'center': 'center composition area, offset to a side safe zone away from the main character silhouette',
        'bottom': 'lower composition area' }
    KEYWORD_LAYOUT_VARIANTS = {
        'top': [
            'top-left safe margin on a rigid in-world surface',
            'top-right safe margin with slight perspective skew',
            'upper-center but offset away from the main subject silhouette'],
        'center': [
            'center-left safe zone integrated on a physical display surface',
            'center-right safe zone with clear negative space around letters',
            'mid-frame offset panel aligned to scene perspective'],
        'bottom': [
            'lower-left anchored label area on a practical object',
            'lower-right anchored caption surface attached to scene prop',
            'bottom-center physical strip/card with realistic depth'] }
    KEYWORD_ZONE_VARIANTS = {
        'top': [
            'upper-left third grid zone',
            'upper-right third grid zone',
            'upper-center offset zone (not dead center)'],
        'center': [
            'middle-left third grid zone',
            'middle-right third grid zone',
            'mid-frame offset side lane'],
        'bottom': [
            'lower-left third grid zone',
            'lower-right third grid zone',
            'bottom-center offset lane (away from subject)'] }
    KEYWORD_DEPTH_VARIANTS = {
        'top': [
            'background wall/sign plane',
            'upper-mid hanging surface plane',
            'mid-depth mounted display plane'],
        'center': [
            'mid-depth practical object plane',
            'foreground side prop plane',
            'background side panel plane with clear separation from subject'],
        'bottom': [
            'foreground desk/floor prop plane',
            'mid-depth lower wall/card plane',
            'near-ground practical signage plane'] }
    SCENE_ARCHETYPE_KEYWORDS = {
        'office_studio': ('office', 'studio', 'desk', 'meeting', 'presentation', 'monitor', 'chart', 'report', '사무실', '스튜디오', '책상', '회의', '발표', '모니터', '차트', '리포트'),
        'document_desk': ('document', 'paper', 'contract', 'invoice', 'letter', 'book', 'notebook', 'clipboard', '문서', '종이', '계약서', '영수증', '편지', '책', '노트', '클립보드'),
        'street_outdoor': ('street', 'road', 'crosswalk', 'storefront', 'billboard', 'alley', 'plaza', 'station', '거리', '도로', '횡단보도', '상점', '간판', '골목', '광장', '역'),
        'home_interior': ('home', 'living room', 'kitchen', 'bedroom', 'sofa', 'table', 'fridge', '집', '거실', '주방', '침실', '소파', '테이블', '냉장고'),
        'retail_cafe': ('cafe', 'coffee', 'restaurant', 'menu', 'counter', 'shop', '카페', '커피', '식당', '메뉴', '카운터', '매장'),
        'industrial_lab': ('factory', 'lab', 'machine', 'control panel', 'terminal', 'equipment', 'warehouse', '공장', '실험실', '기계', '제어판', '터미널', '장비', '창고'),
        'nature_open': ('mountain', 'forest', 'river', 'beach', 'field', 'park', 'sky', 'cloud', '산', '숲', '강', '바다', '들판', '공원', '하늘', '구름') }
    SCENE_ARCHETYPE_LAYOUT_BONUS = {
        'office_studio': {
            'center': [
                'mid-right panel anchored to monitor perspective lines',
                'mid-left desk-side plate aligned to table edge perspective'],
            'top': [
                'upper-right wall display corner away from presenter silhouette'] },
        'document_desk': {
            'center': [
                'desk-corner paper label zone aligned to tabletop perspective'],
            'bottom': [
                'lower-third document strip zone with natural desk shadow'] },
        'street_outdoor': {
            'top': [
                'upper storefront sign lane following facade perspective'],
            'center': [
                'side billboard lane with traffic-safe visual clearance'] },
        'industrial_lab': {
            'center': [
                'control-panel side lane with machine-aligned perspective'],
            'bottom': [
                'lower equipment label strip near console base'] } }
    CARRIER_HINTS_BY_ERA = {
        'past_fantasy': 'a surface that naturally exists in the scene (wooden sign, stone tablet, scroll, banner, wall plaque)',
        'modern_daily': 'a surface that naturally exists in the scene (signboard, poster, screen, bulletin board, wall sign, nameplate)',
        'future_sf': 'a surface that naturally exists in the scene (digital display, LED panel, holographic sign, control screen)' }
    ILLUSTRATION_STYLE_HINT_TOKENS = ('stickman', 'stick figure', 'webtoon', 'cartoon', 'comic', 'anime', 'manga', '2d', 'illustration', 'illustrated', 'line art', 'flat color', 'minimal', 'simple line')
    PHOTOREAL_STYLE_HINT_TOKENS = ('photoreal', 'photo-real', 'real photograph', 'realistic photo', 'hyperreal', 'hyper-real', 'dslr', 'cinematic photo', 'ultra realistic')
    _normalize_reference_image_path = (lambda raw_path = None: if not raw_path:
normalized_path = str('').replace('\\', '/').strip()if not normalized_path:
''if None.match('^/[A-Za-z]:/', normalized_path):
normalized_path = normalized_path[1:]if normalized_path.startswith('/data/'):
normalized_path = normalized_path[6:]elif normalized_path.startswith('data/'):
normalized_path = normalized_path[5:]if not normalized_path.startswith('/') and normalized_path.startswith('//'):
normalized_path = normalized_path.lstrip('/')normalized_path)()
    _build_keyword_config_from_custom_text = (lambda custom_keyword_text = None:
