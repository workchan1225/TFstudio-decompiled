# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: character_reference_generator.pyc (Python 3.11)

'''
CharacterReferenceGenerator - 캐릭터 참조 이미지 생성 서비스

scene_image_service.py에서 추출됨 (Phase 6 리팩토링)

주요 기능:
- 캐릭터 참조 이미지 생성
- 캐릭터 프롬프트 구성
- 캐릭터 스타일 참조 수집
- 프로젝트 메타데이터 기반 캐릭터 페이로드 보강
'''
import re
from copy import deepcopy
from typing import Dict, List, Any, Optional
from models.settings import Settings
from models.project import Project
POSE_VARIATIONS = [
    'facing slightly left',
    'facing slightly right',
    'three-quarter view',
    'profile view',
    'with hands clasped',
    'with arms crossed',
    'with one hand raised',
    'leaning slightly forward',
    'with subtle gesture',
    'with relaxed shoulders',
    'with attentive posture',
    'in contemplative stance']

class CharacterReferenceGenerator:
    '''캐릭터 참조 이미지 생성 서비스'''
    normalize_age_range_key = (lambda age_range = None: if not age_range:
text = str('').strip()if not text:
''age_match = None.search('(\\d{1,2})', text)if age_match:
age_match.group(1)lowered = None.lower()for token in ('young_child', 'child', 'teen', 'young', 'adult', 'middle', 'senior', 'elderly'):
if token in lowered:
None, tokenlowered[:20])()
    infer_informational_character_reference_visual_category = (lambda visual_category = None, style_template = None, style_modifier = staticmethod: pass# WARNING: Decompyle incomplete
)()
    should_skip_informational_style_keyword_reinforcement = (lambda effective_visual_category = None, style_keywords = None: pass# WARNING: Decompyle incomplete
)()
    enrich_character_reference_payload_from_project = (lambda character = None, project_id = None: if not isinstance(character, dict) or project_id:
characterif not character.get('id', ''):
target_id = None('').strip()if not character.get('uniqueId', ''):
target_unique_id = str('').strip()if not character.get('name', ''):
target_name = str('').strip().lower()if not target_id and target_unique_id and target_name:
charactertry:
project = Project.query.get(project_id)if project:
passmetadata = { } if not project.llm_generation_metadata else { }metadata_chars = metadata.get('characters', [])if not isinstance(metadata_chars, list):
charactermatched = Nonefor item in metadata_chars:
if not isinstance(item, dict):
continueif not item.get('id', ''):
item_id = str('').strip()if not item.get('uniqueId', ''):
item_unique_id = str('').strip()if not item.get('name', ''):
item_name = str('').strip().lower()if target_id:
if not target_id == item_id:
id_match = bool(target_id == item_unique_id)if target_unique_id:
if not target_unique_id == item_unique_id:
unique_match = bool(target_unique_id == item_id)if target_name:
name_match = bool(target_name == item_name)if id_match and unique_match or name_match:
matched = itemif not matched:
characterenriched = None(matched)enriched.update(character)if not enriched.get('socialStatus'):
if not matched.get('socialStatus'):
enriched['socialStatus'] = matched.get('social_status', '')if not enriched.get('role'):
if not matched.get('role'):
if not matched.get('characterRole'):
enriched['role'] = matched.get('character_role', '')if not enriched.get('personality'):
enriched['personality'] = matched.get('personality', '')if not enriched.get('clothing'):
if not matched.get('clothing'):
if not matched.get('outfit'):
enriched['clothing'] = matched.get('attire', '')print(f'''[CharacterRef] Enriched character payload from project metadata: {enriched.get('name', target_name)}, clothing={enriched.get('clothing', '')[:50]}''')enrichedexcept Exception:
e = Noneprint(f'''[CharacterRef] Warning: Failed to enrich payload from project metadata: {e}''')del eNoneNone = del e)()
    get_character_pose = (lambda role = None, social_status = None, age_range = staticmethod, scene_index = (0,): pass# WARNING: Decompyle incomplete
)()
    derive_expression_for_reference = (lambda personality = None, appearance_desc = None, role = staticmethod: pass# WARNING: Decompyle incomplete
)()
    generate_character_reference_prompt = (lambda character = None, style_prefix = None, style_keywords = staticmethod: name = character.get('name', 'Character')gender = character.get('gender', 'unknown')age_range = character.get('ageRange', '')appearance = character.get('appearance', '')clothing = character.get('clothing', '')gender_map = {
'male': 'man',
'female': 'woman' }gender_en = gender_map.get(gender, 'person')prompt_parts = [
style_prefix] if style_prefix else []prompt_parts.append(f'''Character reference sheet of a Korean {gender_en}''')if age_range:
prompt_parts.append(f''', {age_range}''')if appearance:
prompt_parts.append(f'''. {appearance[:200]}''')if clothing:
prompt_parts.append(f'''. Wearing {clothing[:100]}''')if style_keywords:
prompt_parts.append(f'''. {style_keywords}''')prompt_parts.append('. Multiple views (front, 3/4, side, back), white background. CRITICAL: The character MUST wear the EXACT SAME outfit in ALL views - same clothing, same colors, same accessories. Only the viewing angle changes, NOT the clothing or appearance.')''.join(prompt_parts))()
    _truncate_text_on_boundary = (lambda text = None, max_length = None, min_ratio = staticmethod: if not text:
cleaned = ''.strip()if cleaned or len(cleaned) <= max_length:
cleanedcandidate = None[:max_length + 1]min_boundary_idx = int(max_length * min_ratio)boundary_markers = [
'. ',
', ',
'; ',
' - ',
' ']boundary_idx = -1for marker in boundary_markers:
idx = candidate.rfind(marker)if idx >= min_boundary_idx:
boundary_idx = max(boundary_idx, idx)if boundary_idx == -1:
clipped = candidate[:max_length]else:
clipped = candidate[:boundary_idx]clipped.strip(' ,.'))()
    sanitize_character_reference_description = (lambda description = None: pass# WARNING: Decompyle incomplete
)()
    collect_character_style_reference_parts = (lambda style_template = None, visual_category = None, generation_session_id = staticmethod: parts = []if not style_template:
partsif None(style_template, 'style_prefix') and style_template.style_prefix:
parts.append(style_template.style_prefix)if hasattr(style_template, 'style_keywords') and style_template.style_keywords:
parts.append(style_template.style_keywords)if visual_category and visual_category.startswith('informational'):
parts.append('simple design, clean lines, minimal details')if visual_category and visual_category.startswith('traditional'):
parts.append('traditional painting style, folk art aesthetic')parts)()
    build_character_batch_style_instruction = (lambda generation_session_id = None, character_session_id = None, style_reference_count = staticmethod, visual_category = ('generation_session_id', Optional[str], 'character_session_id', Optional[str], 'style_reference_count', int, 'visual_category', Optional[str], 'return', str): metadata_parts = []if generation_session_id:
metadata_parts.append(f'''[CHARACTER GENERATION SESSION: {generation_session_id}]''')if character_session_id:
metadata_parts.append(f'''[CHARACTER SESSION: {character_session_id}]''')if style_reference_count > 0:
metadata_parts.append(f'''[STYLE REFERENCES: {style_reference_count}]''')style_lock_lines = [
'[CHARACTER STYLE LOCK CONTRACT]',
'- Draw all characters as if created by the SAME illustrator and production pipeline.',
'- Keep line weight, rendering language, shading behavior, and palette temperature unified across this batch.',
'- Never change global art style because of age, era, personality, role, or emotional descriptors.',
"- Preserve this character's unique identity and outfit silhouette while sharing only style DNA with references."]if visual_category:
if not visual_category.startswith('realistic'):
is_realistic = bool(visual_category == 'realistic')if not is_realistic:
style_lock_lines.extend([
'- Avoid retro anime/comic-book drift and avoid accidental old-generation rendering.',
'- Avoid hyper-realistic wrinkle over-emphasis that breaks stylized character consistency.'])if visual_category and visual_category.startswith('informational'):
style_lock_lines.append(f'''- Keep selected informational substyle \'{visual_category}\' stable across this batch.''')'\n'.join(metadata_parts + style_lock_lines))()
    build_character_identity_signature = (lambda payload = None, fallback_text = None: source = payload if isinstance(payload, dict) else { }if not source.get('gender'):
gender = str('').strip()if not source.get('ageRange'):
if not source.get('age_range'):
age_range = str('').strip()if not source.get('hairstyleEn'):
if not source.get('hairstyle'):
hair = str('').strip()if not source.get('distinctiveFeaturesEn'):
if not source.get('distinctiveFeatures'):
if not source.get('silhouetteHint'):
features = str('').strip()if not source.get('accessoriesEn'):
if not source.get('accessories'):
accessories = str('').strip()if not source.get('englishDescription'):
if not source.get('appearance'):
if not source.get('profile'):
if not fallback_text:
appearance = str('').strip()appearance = CharacterReferenceGenerator.sanitize_character_reference_description(appearance)signature_parts = []if gender:
signature_parts.append(f'''gender={gender}''')if age_range:
signature_parts.append(f'''age={age_range}''')if hair:
signature_parts.append(f'''hair={hair}''')if features:
signature_parts.append(f'''traits={features}''')if accessories:
signature_parts.append(f'''accessories={accessories}''')if appearance:
signature_parts.append('visual=' + CharacterReferenceGenerator._truncate_text_on_boundary(appearance, max_length = 120))if not signature_parts:
''None.join(signature_parts[:4]))()
    build_character_uniqueness_instruction = (lambda current_character_name = None, current_identity_signature = None, style_reference_parts = staticmethod, visual_category = ('',): if not visual_category:
normalized_category = str('').strip().lower()is_informational_style = normalized_category.startswith('informational')lines = [
'[CHARACTER IDENTITY UNIQUENESS CONTRACT]',
'- Keep global art style consistent, but this character MUST be a clearly different person from all style references.',
"- Preserve this character's own identity signature while using references only for line/render/palette style DNA."]if is_informational_style:
lines.extend([
'- For informational substyles, enforce uniqueness via silhouette, hairstyle block shape, outfit color blocking, and accessory cues.',
'- Do NOT force realistic facial landmark differences; keep minimal facial features aligned with selected informational style.'])else:
lines.extend([
'- NEVER clone or reuse face geometry from style reference characters.',
'- Ensure at least three facial landmarks differ from each reference (face shape, eye spacing, nose bridge, lip line, jaw/chin).'])if not style_reference_parts:
lines.append("- No style references attached in this request; keep this character's own identity signature stable.")if current_character_name:
lines.append(f'''- Target character: {current_character_name}''')if current_identity_signature:
lines.append(f'''- Target signature: {current_identity_signature}''')reference_lines = []for reference in style_reference_parts[:3]:
if not str(reference.get('name', 'style-reference')).strip():
name = 'style-reference'signature = str(reference.get('identity_signature', '')).strip()if signature:
reference_lines.append(f'''  - Do NOT match {name}: {signature}''')continuereference_lines.append(f'''  - Do NOT match {name}\'s face geometry or hairstyle silhouette''')if reference_lines:
lines.append('- Distinctiveness constraints against style references:')lines.extend(reference_lines)'\n'.join(lines))()


def enrich_character_payload(character = None, project_id = None):
    '''캐릭터 페이로드 보강 편의 함수'''
    return CharacterReferenceGenerator.enrich_character_reference_payload_from_project(character, project_id)


def get_character_pose(role = None, social_status = None, age_range = None, scene_index = (0,)):
    '''
    캐릭터 포즈 결정 편의 함수.

    Args:
        role: 캐릭터 역할
        social_status: 사회적 신분
        age_range: 나이 범위
        scene_index: 씬 인덱스 (포즈 변형용, 기본값 0)

    Returns:
        포즈 설명 문자열
    '''
    return CharacterReferenceGenerator.get_character_pose(role, social_status, age_range, scene_index)


def sanitize_character_description(description = None):
    '''캐릭터 설명 정제 편의 함수'''
    return CharacterReferenceGenerator.sanitize_character_reference_description(description)


def infer_informational_visual_category_for_character_reference(visual_category = None, style_template = None, style_modifier = None):
    '''정보성 캐릭터 참조용 서브스타일 추론 편의 함수'''
    return CharacterReferenceGenerator.infer_informational_character_reference_visual_category(visual_category = visual_category, style_template = style_template, style_modifier = style_modifier)


def should_skip_informational_keyword_reinforcement(effective_visual_category = None, style_keywords = None):
    '''정보성 서브스타일 불일치 키워드 보강 차단 편의 함수'''
    return CharacterReferenceGenerator.should_skip_informational_style_keyword_reinforcement(effective_visual_category = effective_visual_category, style_keywords = style_keywords)
