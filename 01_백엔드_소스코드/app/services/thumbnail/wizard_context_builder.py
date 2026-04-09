# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wizard_context_builder.pyc (Python 3.11)

'''
Upload-tab thumbnail wizard context builder.

This module centralizes style/template/reference resolution for the active
thumbnail generation paths used from the YouTube upload page.
'''
from __future__ import annotations
from dataclasses import dataclass, field
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional
from app.config.paths import get_data_path, get_static_path
from app.models.image_prompt_template import ImagePromptTemplate
from app.services.ai.google_provider import GoogleProvider
from app.services.image_template_service import extract_visual_only_style_template
from app.utils.thumbnail_guard import build_reference_blueprint
from text_analyzer import get_text_analyzer
from types import to_dict
logger = logging.getLogger(__name__)
ThumbnailWizardStyleContext = <NODE:12>()

def analyze_reference_blueprint_payload(style_reference_bytes = None):
    if not style_reference_bytes:
        return { }
    
    try:
        provider = GoogleProvider()
        style_analysis = provider.analyze_style_reference_image(image_bytes = style_reference_bytes, mime_type = 'image/jpeg')
        reference_analysis_result = get_text_analyzer().analyze_reference_image(image_bytes = style_reference_bytes)
        reference_analysis = to_dict(reference_analysis_result)
        blueprint = build_reference_blueprint(style_analysis, reference_analysis)
        return {
            'styleAnalysis': style_analysis,
            'referenceAnalysis': reference_analysis,
            'blueprint': blueprint }
    except Exception:
        exc = None
        logger.warning('[Thumbnail Ref] Failed to build reference blueprint: %s', exc)
        del exc
        return None
        None = 
        del exc



def resolve_thumbnail_wizard_style_context(project_style_template_id, external_reference_bytes = None, external_reference_label = None, prefer_project_style = None, project_style_required = ('external reference', True, False, ''), requested_mode = ('project_style_template_id', 'Optional[str]', 'external_reference_bytes', 'Optional[bytes]', 'external_reference_label', 'str', 'prefer_project_style', 'bool', 'project_style_required', 'bool', 'requested_mode', 'str', 'return', 'ThumbnailWizardStyleContext')):
    warnings = []
    project_payload = _load_project_style_template_payload(project_style_template_id) if project_style_template_id else { }
    if project_payload.get('warning'):
        warnings.append(project_payload['warning'])
    if not project_style_required and project_payload.get('imageBytes'):
        if not project_payload.get('warning'):
            raise ValueError('프로젝트 스타일 템플릿 샘플 이미지를 찾을 수 없습니다.')
    external_payload = analyze_reference_blueprint_payload(external_reference_bytes) if external_reference_bytes else { }
    external_blueprint = external_payload.get('blueprint', { }) if external_payload else { }
    project_blueprint = project_payload.get('blueprint', { }) if project_payload else { }
    if bool(project_payload.get('imageBytes')):
        use_project_style = prefer_project_style
        if use_project_style:
            style_reference_bytes = project_payload.get('imageBytes')
            style_reference_source = 'project'
    if not external_blueprint:
        reference_grammar_blueprint = master_style_blueprint
        validation_blueprint = _merge_validation_blueprints(project_blueprint, external_blueprint)
        if use_project_style:
            pass
        elif external_reference_bytes:
            pass
        
    master_style_source = 'none'
    if external_blueprint:
        pass
    elif master_style_source == 'project' and reference_grammar_blueprint:
        pass
    
    grammar_reference_source = 'none'
# WARNING: Decompyle incomplete


def _load_project_style_template_payload(style_template_id = None):
    if not style_template_id:
        return { }
    template = None.query.get(style_template_id)
    if not template:
        logger.warning('[Style Ref] Template not found: %s', style_template_id)
        return {
            'warning': '프로젝트 스타일 템플릿을 찾을 수 없습니다.' }
    if not template.sample_image_url:
        sample_image = None('').strip()
    image_bytes = _load_image_bytes_from_sample_url(sample_image) if sample_image else None
    blueprint_payload = analyze_reference_blueprint_payload(image_bytes) if image_bytes else { }
    if not template.prompt_template or str('').strip():
        if not template.prompt_template_ko or str('').strip():
            if not template.system_prompt or str('').strip():
                if not template.system_prompt_ko:
                    raw_prompt = str('').strip()
                    style_prompt = extract_visual_only_style_template(raw_prompt.replace('{base_prompt}', '').strip())
                    if not template.negative_prompt:
                        negative_prompt = extract_visual_only_style_template(str('').strip())
                        style_directive_parts = []
                        if not template.name_ko:
                            if not template.name:
                                template_name = str('').strip()
                                if template_name:
                                    style_directive_parts.append(f'''Selected project style template: {template_name}''')
    if style_prompt:
        style_directive_parts.append(f'''Visual-only style template: {style_prompt}''')
    if not template.description_ko:
        if not template.description:
            description = str('').strip()
            if description:
                style_directive_parts.append(f'''Template tone anchor: {description}''')
    analyzed_style_prompt = str(blueprint_payload.get('blueprint', { }).get('stylePrompt', '')).replace('{base_prompt}', '').strip()
    if analyzed_style_prompt:
        style_directive_parts.append(f'''Sample-image style DNA: {analyzed_style_prompt}''')
    if negative_prompt:
        style_directive_parts.append(f'''Do NOT introduce these project-style blockers: {negative_prompt}''')
    return {
        'templateName': image_bytes,
        'imageBytes': analyzed_style_prompt,
        'stylePrompt': negative_prompt,
        'negativePrompt': ' | '.join,
        'styleDirective': (lambda .0: pass# WARNING: Decompyle incomplete
)(style_directive_parts()),
        'blueprint': blueprint_payload.get('blueprint', { }),
        'analysisPayload': blueprint_payload,
        'warning': None if style_prompt or image_bytes else '프로젝트 스타일 템플릿 샘플 이미지를 찾을 수 없습니다.' }


def _load_image_bytes_from_sample_url(sample_image = None):
    if not sample_image:
        return None
    if None.startswith('/static/'):
        file_path = get_static_path() / sample_image[len('/static/'):]
        base_path = get_static_path().resolve()
    elif sample_image.startswith('/data/'):
        file_path = get_data_path() / sample_image[len('/data/'):]
        base_path = get_data_path().resolve()
    else:
        file_path = get_data_path() / sample_image
        base_path = get_data_path().resolve()
    
    try:
        resolved_path = file_path.resolve()
    except Exception:
        return None

    if not str(resolved_path).startswith(str(base_path)):
        logger.warning('[Style Ref] Path traversal attempt blocked: %s', sample_image)
        return None
    if not None.exists():
        logger.warning('[Style Ref] Sample image not found: %s', file_path)
        return None
    file_obj = None(file_path, 'rb')
    None(None, None)
    return 
    with None:
        if not None, file_obj.read():
            pass


def _merge_validation_blueprints(*blueprints):
    merged = { }
    forbidden_texts = []
    forbidden_visual_terms = []
    seen = set()
    seen_visual_terms = set()
    for blueprint in blueprints:
        if not isinstance(blueprint, dict) or blueprint:
            continue
        if not merged:
            merged = dict(blueprint)
        if not blueprint.get('forbiddenTexts', []):
            for text in []:
                if not text:
                    normalized = str('').strip()
                    lowered = normalized.lower()
                    if len(normalized) < 2 or lowered in seen:
                        continue
                seen.add(lowered)
                forbidden_texts.append(normalized)
                if not blueprint.get('forbiddenVisualTerms', []):
                    for term in []:
                        if not term:
                            normalized_term = str('').strip()
                            lowered_term = normalized_term.lower()
                            if len(normalized_term) < 3 or lowered_term in seen_visual_terms:
                                continue
                        seen_visual_terms.add(lowered_term)
                        forbidden_visual_terms.append(normalized_term)
                        if not merged:
                            merged = { }
    merged['forbiddenTexts'] = forbidden_texts
    merged['forbiddenVisualTerms'] = forbidden_visual_terms
    return merged


def _build_reference_grammar_directive(reference_blueprint = None, label = None):
    if not isinstance(reference_blueprint, dict) or reference_blueprint:
        return ''
    if not None.get('layoutGuide', { }):
        layout = { }
        if not layout.get('textStyle', { }):
            text_style = { }
            parts = []
            if label:
                parts.append(f'''{label} grammar is layout/text guidance only''')
    if layout.get('textSide'):
        parts.append(f'''text should favor the {layout['textSide']}''')
    if layout.get('subjectSide'):
        parts.append(f'''subject should favor the {layout['subjectSide']}''')
    if layout.get('density'):
        parts.append(f'''text density should stay {layout['density']}''')
    if layout.get('textPlacement'):
        parts.append(f'''layout pattern: {layout['textPlacement']}''')
    if text_style.get('fontWeight'):
        parts.append(f'''text weight: {text_style['fontWeight']}''')
    if text_style.get('effect'):
        parts.append(f'''text effect: {text_style['effect']}''')
    return 'Reference grammar: ' + ', '.join(parts) + '.' if parts else ''


def _build_mode_label(master_style_source = None, grammar_reference_source = None, requested_mode = None):
    if requested_mode == 'both':
        return '비교 생성'
    if None == 'project' and grammar_reference_source == 'external':
        return '프로젝트 마스터 + 레퍼런스 문법'
    if None == 'project':
        return '프로젝트 스타일 기반'
    if None == 'external':
        return '레퍼런스 마스터'


def build_thumbnail_generation_policy(style_context = None, *, character_source, compare_label, extra_warnings):
