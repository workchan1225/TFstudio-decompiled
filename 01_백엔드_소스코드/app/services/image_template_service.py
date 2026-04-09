# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_template_service.pyc (Python 3.11)

'''
ImageTemplateService

이미지 생성 프롬프트 템플릿 관리 서비스
- 템플릿 조회/생성/수정/삭제
- 변수 치환을 통한 프롬프트 생성
- 캐릭터/장면별 프롬프트 빌드
- AI 기반 템플릿 자동 생성
- 역사극/사극: 신분별 한복 자동 적용
'''
import json
import re
from typing import List, Dict, Optional
from models.image_prompt_template import ImagePromptTemplate
from models.project_image_settings import ProjectImageSettings
from services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from utils.joseon_costume_data import get_costume_by_class, detect_social_class, detect_gender, build_costume_prompt, get_all_social_classes
from utils.scene_context_analyzer import analyze_scene_context, get_dynamic_outfit, get_face_identity_prompt
from prompt.style_profile_filter import filter_style_template_visual_only as filter_style_template_visual_only_structured, strip_content_phrases_from_style as strip_content_phrases_from_style_structured
from scene.rule_loader import RuleLoader, detect_period_context as rule_detect_period_context
from  import db
HAIRSTYLE_CONSISTENCY_NEGATIVE = 'different hairstyle, changed hairstyle, altered hairstyle, different hair, changed hair, altered hair, longer hair, shorter hair, hair length change, hair grown out, hair cut shorter, different hair color, hair color change, dyed hair differently, darker hair, lighter hair, different styling, new hairdo, restyled hair, ponytail when should be down, hair down when should be up, straight when should be wavy, curly when should be straight, different hair accessories, missing hair pin, added hair decoration'
STYLE_TEMPLATE_CONTENT_PREFIXES = [
    'environment:',
    'background:',
    'setting:',
    'location:',
    'character:',
    'characters:',
    'costume:',
    'clothing:',
    'props:',
    'architecture:',
    'vehicle:']
STYLE_TEMPLATE_CONTENT_TERMS = [
    'environment',
    'background',
    'setting',
    'location',
    'clothing',
    'costume',
    'hanbok',
    'armor',
    'robe',
    'city',
    'village',
    'palace',
    'hanok',
    'hospital',
    'school',
    'subway',
    'apartment',
    'office',
    'street',
    'corridor',
    'skyscraper',
    'building',
    'modern setting',
    'historical setting',
    'futuristic setting']
STYLE_TEMPLATE_VISUAL_TERMS = [
    'style',
    'aesthetic',
    'linework',
    'brush',
    'render',
    'rendering',
    'color',
    'palette',
    'tone',
    'lighting',
    'shadow',
    'contrast',
    'mood',
    'atmosphere',
    'texture',
    'composition',
    'chiaroscuro',
    'cel-shading',
    'painterly',
    'illustration',
    'anime',
    'webtoon']

def detect_period_context(scene_description = None, project_genre = None):
    '''
    장면 설명/장르 기반으로 시대 컨텍스트를 판별한다.

    v1.8.0: RuleLoader에 위임 (SSOT)
    '''
    return rule_detect_period_context(scene_description, project_genre)


def extract_visual_only_style_template(template_text = None):
    '''스타일 텍스트에서 시각 스타일 요소만 추출한다.'''
    if not template_text:
        return ''
    structured = None(template_text)
    inline_sanitized = strip_content_phrases_from_style_structured(structured)
    result = re.sub('\\s{2,}', ' ', inline_sanitized.replace('\n', ' ')).strip(', .')
    return result


def _normalize_custom_style_prompt_template(template_text = None):
    '''커스텀 스타일 템플릿은 구조를 유지한 채 안전하게 정규화한다.'''
    if not template_text:
        return '{base_prompt}'
    normalized = None(template_text).replace('\r\n', '\n').replace('\r', '\n').strip()
    normalized = re.sub('\\n{3,}', '\n\n', normalized)
    normalized = re.sub('[ \\t]{2,}', ' ', normalized)
    if normalized.lstrip().startswith('{base_prompt}'):
        return normalized
    if None in normalized:
        normalized = normalized.replace('{base_prompt}', '').strip(', \n')
    if normalized:
        return '{base_prompt}\n\n' + normalized


def _sanitize_style_template_payload(data = None, template_type = None):
    '''Style 템플릿 payload에서 content-bearing 요소를 제거한다.'''
    if not data:
        return { }
    sanitized = None(data)
    if not template_type:
        pass
    if not sanitized.get('type'):
        resolved_type = ''.strip().lower()
        if resolved_type != 'style':
            return sanitized
        if not sanitized.get('visualCategory'):
            visual_category = None('').strip().lower()
            for field_name in ('promptTemplate', 'promptTemplateKo'):
                raw_value = sanitized.get(field_name)
                if not isinstance(raw_value, str):
                    continue
                if visual_category == 'custom':
                    cleaned_value = _normalize_custom_style_prompt_template(raw_value)
                else:
                    cleaned_value = extract_visual_only_style_template(raw_value)
                if cleaned_value:
                    if cleaned_value.strip() != raw_value.strip():
                        print(f'''[ImageTemplateService] Sanitized style template field: {field_name}''')
                    sanitized[field_name] = cleaned_value
                if visual_category == 'custom':
                    system_prompt = sanitized.get('systemPrompt')
                    if isinstance(system_prompt, str) and system_prompt.strip():
                        sanitized['systemPrompt'] = _normalize_custom_style_prompt_template(system_prompt)
                    elif sanitized.get('promptTemplate'):
                        sanitized['systemPrompt'] = sanitized['promptTemplate']
    return sanitized


def get_style_emphasis(visual_category = None):
    """
    스타일 카테고리에 맞는 강조 키워드 반환

    v1.7.1: style_emphasis.py의 상세 버전으로 통합 (캐릭터/씬 일관성 보장)

    Args:
        visual_category: 'realistic', 'animation', 'illustration', 'traditional', 'informational_*' 등

    Returns:
        {prefix, keywords, anti_keywords} 딕셔너리
    """
    get_detailed_style_emphasis = get_style_emphasis
    import app.services.prompt.style_emphasis
    return get_detailed_style_emphasis(visual_category)


class ImageTemplateService:
    '''이미지 프롬프트 템플릿 서비스'''
    get_templates = (lambda template_type = None, active_only = None: query = ImagePromptTemplate.queryif template_type:
query = query.filter_by(type = template_type)if active_only:
query = query.filter_by(is_active = True)templates = query.order_by(ImagePromptTemplate.type, ImagePromptTemplate.is_default.desc(), ImagePromptTemplate.name).all()templates())()
    get_template_by_id = (lambda template_id = None: template = ImagePromptTemplate.query.get(template_id)template.to_dict() if template else None)()
    get_default_template = (lambda template_type = None: template = ImagePromptTemplate.get_default(template_type)template.to_dict() if template else None)()
    get_template_id_by_name = (lambda template_type = None, name = None: template = ImagePromptTemplate.query.filter_by(type = template_type, name = name, is_active = True).first()template.id if template else None)()
    create_template = (lambda data = None: sanitized_data = _sanitize_style_template_payload(data)# WARNING: Decompyle incomplete
)()
    update_template = (lambda template_id = None, data = None:
