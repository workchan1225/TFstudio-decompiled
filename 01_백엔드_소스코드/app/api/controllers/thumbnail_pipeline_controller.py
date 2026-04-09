# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thumbnail_pipeline_controller.pyc (Python 3.11)

'''
Thumbnail Pipeline Controller
5단계 파이프라인 기반 AI 썸네일 생성 API

Endpoints:
- POST /api/thumbnail-pipeline/analyze       - Stage 1: 레퍼런스 분석
- POST /api/thumbnail-pipeline/validate      - Stage 2: 콘텐츠 검증
- POST /api/thumbnail-pipeline/generate-prompt - Stage 3: 프롬프트 생성
- POST /api/thumbnail-pipeline/optimize      - Stage 4: 프롬프트 최적화
- POST /api/thumbnail-pipeline/generate      - Stage 5: 이미지 생성
- POST /api/thumbnail-pipeline/execute       - 전체 파이프라인 실행
'''
from flask import Blueprint, request, jsonify
import logging
import base64
import os
from app.services.thumbnail import get_thumbnail_pipeline, get_text_analyzer, get_content_analyzer, get_content_processor, get_prompt_generator, get_prompt_optimizer, get_image_generator, to_dict, UserContentInput, SubjectImage, AdditionalText, FloatingText, StylePreferences, PipelineStep
from app.services.thumbnail.pipeline import PipelineConfig
from dataclasses import asdict
from app.utils.thumbnail_guard import build_reference_blueprint, normalize_design_analysis
logger = logging.getLogger(__name__)
thumbnail_pipeline_bp = Blueprint('thumbnail_pipeline', __name__)

def _load_image_from_source(source = None):
    '''
    이미지 소스(URL, 파일 경로, Base64)에서 PIL Image 로드

    Args:
        source: 이미지 URL, 로컬 파일 경로, 또는 Base64 데이터

    Returns:
        PIL.Image 또는 None (실패 시)
    '''
    Image = Image
    import PIL
    import requests
    BytesIO = BytesIO
    import io
    Path = Path
    import pathlib
    if not source:
        return None
    
    try:
        if source.startswith('data:image'):
            if ',' in source:
                base64_data = source.split(',')[1]
            else:
                base64_data = source
            image_bytes = base64.b64decode(base64_data)
            return Image.open(BytesIO(image_bytes))
        if None.startswith('http://') or source.startswith('https://'):
            response = requests.get(source, timeout = 30)
            response.raise_for_status()
            return Image.open(BytesIO(response.content))
        if None.startswith('/data/') or source.startswith('data/'):
            
            try:
                get_data_path = get_data_path
                import app.config.paths
                data_dir = get_data_path()
                if source.startswith('/data/'):
                    rel_path = source[6:]
                else:
                    rel_path = source[5:]
                abs_path = Path(data_dir) / rel_path
                if abs_path.exists():
                    return Image.open(abs_path)
                None.warning(f'''File not found: {abs_path}''')
                return None
            except Exception:
                e = None
                logger.error(f'''Failed to resolve data path: {e}''')
                
                try:
                    e = None
                    del e
                    return None
                    e = None
                    del e
                    
                    try:
                        if os.path.exists(source):
                            return Image.open(source)
                        None.warning(f'''Cannot load image from source: {source[:100]}...''')
                        return None
                    except Exception:
                        e = None
                        logger.error(f'''Failed to load image from source: {e}''')
                        e = None
                        del e
                        return None
                        e = None
                        del e





analyze_reference = (lambda : pass# WARNING: Decompyle incomplete
)()
validate_content = (lambda : try:
if not request.get_json():
data = { }subject_image = data.get('subject_image', '')main_text = data.get('main_text', '')sub_text = data.get('sub_text', '')cta_text = data.get('cta_text', '')floating_texts_data = data.get('floating_texts', [])style_tones = data.get('style_tones', [])emotional_keywords = data.get('emotional_keywords', [])floating_texts = []for ft in floating_texts_data:
floating_texts.append(FloatingText(id = ft.get('id', ''), text = ft.get('text', ''), position = ft.get('position', 'top-left'), fontSize = ft.get('fontSize', 24), color = ft.get('color', '#FFFFFF'), backgroundColor = ft.get('backgroundColor', ''), rotation = ft.get('rotation', 0)))content = UserContentInput(subject_image = SubjectImage(source = subject_image, description = '', subjects = [], mood = ''), additional_text = AdditionalText(main_text = main_text, sub_text = sub_text, cta_text = cta_text, floating_texts = floating_texts), style_preferences = StylePreferences(tone = style_tones, emotional_keywords = emotional_keywords, target_audience = '', color_preference = ''))processor = get_content_processor()result = processor.validate_and_process(content)jsonify({
'success': True,
'validated': result.validated,
'validation_errors': result.validation_errors,
'content': to_dict(result) })except Exception:
e = Nonelogger.error(f'''Validate content failed: {e}''', exc_info = True)del eNoneNone = del e)()
generate_prompt = (lambda : pass# WARNING: Decompyle incomplete
)()
optimize_prompt = (lambda : try:
if not request.get_json():
data = { }prompt = data.get('prompt')iterations = data.get('iterations', 3)if not prompt:
(jsonify({
'success': False,
'error': 'prompt가 필요합니다' }), 400)optimizer = None()result = optimizer.optimize_prompt(prompt, iterations)jsonify({
'success': True,
'optimization': to_dict(result) })except Exception:
e = Nonelogger.error(f'''Optimize prompt failed: {e}''', exc_info = True)del eNoneNone = del e)()
generate_image = (lambda : pass# WARNING: Decompyle incomplete
)()
execute_pipeline = (lambda : try:
if not request.get_json():
data = { }reference_image_path = data.get('reference_image')reference_image_url = data.get('reference_image_url')reference_image_base64 = data.get('reference_image_base64')reference_image_bytes = Noneif reference_image_base64:
if ',' in reference_image_base64:
reference_image_base64 = reference_image_base64.split(',')[1]reference_image_bytes = base64.b64decode(reference_image_base64)subject_image = data.get('subject_image', reference_image_path)main_text = data.get('main_text', '')sub_text = data.get('sub_text', '')cta_text = data.get('cta_text', '')floating_texts_data = data.get('floating_texts', [])style_tones = data.get('style_tones', [])emotional_keywords = data.get('emotional_keywords', [])person_references = data.get('person_references', [])floating_texts = []for ft in floating_texts_data:
floating_texts.append(FloatingText(id = ft.get('id', ''), text = ft.get('text', ''), position = ft.get('position', 'top-left'), fontSize = ft.get('fontSize', 24), color = ft.get('color', '#FFFFFF'), backgroundColor = ft.get('backgroundColor', ''), rotation = ft.get('rotation', 0)))config_data = data.get('config', { })config = PipelineConfig(skip_optimization = config_data.get('skip_optimization', False), optimization_iterations = config_data.get('optimization_iterations', 3), model_type = config_data.get('model_type', 'nanobanana-pro'), resolution = config_data.get('resolution', '1280x720'), project_id = config_data.get('project_id'), auto_save = config_data.get('auto_save', True))pipeline = get_thumbnail_pipeline()result = pipeline.execute(reference_image_path = reference_image_path, reference_image_url = reference_image_url, reference_image_bytes = reference_image_bytes, subject_image_source = subject_image, main_text = main_text, sub_text = sub_text, cta_text = cta_text, floating_texts = floating_texts, style_tones = style_tones, emotional_keywords = emotional_keywords, config = config, person_reference_paths = person_references)jsonify({
'success': result.success,
'result': to_dict(result),
'error': result.error })except Exception:
e = Nonelogger.error(f'''Execute pipeline failed: {e}''', exc_info = True)del eNoneNone = del e)()
skip_optimization = (lambda : try:
if not request.get_json():
data = { }prompt = data.get('prompt')if not prompt:
(jsonify({
'success': False,
'error': 'prompt가 필요합니다' }), 400)optimizer = None()result = optimizer.skip_optimization(prompt)jsonify({
'success': True,
'optimization': to_dict(result) })except Exception:
e = Nonelogger.error(f'''Skip optimization failed: {e}''', exc_info = True)del eNoneNone = del e)()
analyze_content_image = (lambda : try:
if not request.get_json():
data = { }image_path = data.get('image_path')image_url = data.get('image_url')image_base64 = data.get('image_base64')style_context = data.get('style_context', '')image_bytes = Noneif image_base64:
if ',' in image_base64:
image_base64 = image_base64.split(',')[1]image_bytes = base64.b64decode(image_base64)if not image_path and image_url and image_bytes:
(jsonify({
'success': False,
'error': 'image_path, image_url, 또는 image_base64 중 하나가 필요합니다' }), 400)analyzer = None()result = analyzer.analyze_content_image(image_path = image_path, image_url = image_url, image_bytes = image_bytes, style_context = style_context)if not result.detected:
(jsonify({
'success': False,
'error': '콘텐츠 이미지 분석 실패' }), 500)None({
'success': True,
'analysis': asdict(result) })except Exception:
e = Nonelogger.error(f'''Analyze content image failed: {e}''', exc_info = True)del eNoneNone = del e)()
generate_midjourney_prompt = (lambda : pass# WARNING: Decompyle incomplete
)()
