# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: whisk_controller.pyc (Python 3.11)

'''
Whisk Automation Controller

Handles Google Whisk web automation for image synthesis.

Registration in app/__init__.py:
    from app.api.controllers import whisk_controller_bp
    app.register_blueprint(whisk_controller_bp)

Endpoints (11):
- GET /api/whisk/auth/status - Check Whisk authentication status
- POST /api/whisk/login - Start Whisk login (opens browser, non-blocking)
- POST /api/whisk/login/complete - Complete login (save session, close browser)
- POST /api/whisk/logout - Logout from Whisk
- POST /api/whisk/start-generation - Start image generation (opens browser to Whisk)
- POST /api/whisk/projects/<project_id>/run-batch - Run batch image generation
- POST /api/whisk/stop-generation - Stop ongoing generation
- GET /api/whisk/projects/<project_id>/batch-stats - Get batch generation statistics
- POST /api/whisk/projects/<project_id>/open-characters-folder - Open characters folder
- POST /api/whisk/projects/<project_id>/analyze-scenes - AI-based scene prompt generation
'''
from flask import Blueprint, jsonify, request
import logging
import os
import sys
import subprocess
import re
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.models.whisk_automation import WhiskCredentials, WhiskGenerationTask
from app.models.project import Project, Character
from flask import Response, current_app
from app.models.image_prompt_template import ImagePromptTemplate
from app.config.paths import get_projects_path
from app.utils.folder_utils import open_folder_foreground
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from app import db
logger = logging.getLogger(__name__)
whisk_controller_bp = Blueprint('whisk', __name__)

def _normalize_whisk_character_key(value):
    if not value:
        normalized = str('').strip()
        if normalized.startswith('char_'):
            normalized = normalized[5:]
    return normalized


def _build_project_character_name_map(project, characters):
    char_name_map = { }
    if not getattr(project, 'video_settings', None):
        video_settings = Project._ensure_video_settings_dict({ })
    scene_generation = video_settings.get('sceneGeneration', { }) if isinstance(video_settings, dict) else { }
    analyzed_characters = scene_generation.get('analyzedCharacters', []) if isinstance(scene_generation, dict) else []
    if isinstance(analyzed_characters, list):
        for character in analyzed_characters:
            if not isinstance(character, dict):
                continue
            if not character.get('uniqueId'):
                unique_id = _normalize_whisk_character_key(character.get('id'))
                if not character.get('name'):
                    name = str('').strip()
                    if unique_id and name and unique_id not in char_name_map:
                        char_name_map[unique_id] = name
            if not characters:
                for character in []:
                    if not getattr(character, 'unique_id', None):
                        if not getattr(character, 'uniqueId', None):
                            unique_id = _normalize_whisk_character_key(getattr(character, 'id', None))
                            if not getattr(character, 'name', ''):
                                name = str('').strip()
                                if unique_id and name and unique_id not in char_name_map:
                                    char_name_map[unique_id] = name
                    return char_name_map

get_whisk_auth_status = (lambda : try:
is_generation_browser_open = is_generation_browser_openimport app.services.whisk_automation_servicebrowser_open = is_generation_browser_open()creds = WhiskCredentials.query.first()if not creds:
(jsonify({
'isAuthenticated': False,
'accountEmail': None,
'lastAuthCheck': None,
'browserOpen': browser_open }), 200)result = None.to_dict()result['browserOpen'] = browser_open(jsonify(result), 200)except Exception:
e = Nonelogger.error(f'''Failed to get Whisk status: {e}''', exc_info = True)del eNoneNone = del e)()
start_whisk_login = (lambda : try:
get_generation_service = get_generation_serviceclear_generation_service = clear_generation_servicereset_whisk_log = reset_whisk_logwhisk_log = whisk_logimport app.services.whisk_automation_servicereset_whisk_log()whisk_log('[API] ========== LOGIN FLOW START (using generation_service) ==========')service = get_generation_service()result = service.start_generation_flow()if result.get('success'):
(jsonify({
'status': 'success',
'message': result.get('message', 'Browser opened'),
'isAuthenticated': result.get('isAuthenticated', False),
'needsLogin': result.get('needsLogin', False),
'reused': result.get('reused', False) }), 200)clear_generation_service()(jsonify({
'status': 'error',
'error': result.get('error', 'Failed to open browser') }), 400)except ImportError:
e = Nonelogger.error(f'''Whisk automation dependencies not installed: {e}''')del eNoneNone = del eexcept Exception:
e = Nonelogger.error(f'''Whisk login failed: {e}''', exc_info = True)del eNoneNone = del e)()
complete_whisk_login = (lambda : try:
get_generation_service = get_generation_servicewhisk_log = whisk_logimport app.services.whisk_automation_serviceservice = get_generation_service()whisk_log('[API] ========== LOGIN COMPLETE (using generation_service) ==========')if not service.driver:
(jsonify({
'status': 'error',
'error': 'Browser not open. Please click "설정 시작" first.' }), 400)try:
current_url = service.driver.current_urlwhisk_log(f'''[API] Current URL: {current_url}''')if 'accounts.google.com' in current_url:
(jsonify({
'status': 'error',
'error': 'Google 로그인이 완료되지 않았습니다. Chrome 창에서 로그인을 완료해주세요.' }), 400)is_authenticated = None in current_urlif is_authenticated:
WhiskCredentials = WhiskCredentialsimport app.models.whisk_automationcreds = WhiskCredentials.query.first()if not creds:
creds = WhiskCredentials()db.session.add(creds)creds.mark_authenticated()db.session.commit()whisk_log('[API] Authentication confirmed and saved')(jsonify({
'status': 'success',
'isAuthenticated': is_authenticated,
'accountEmail': None }), 200)except Exception:
e = Nonewhisk_log(f'''[API] Error checking login status: {e}''', level = 'error')try:
del eNoneNone = del etry:
passexcept ImportError:
e = Nonelogger.error(f'''Whisk automation dependencies not installed: {e}''')del eNoneNone = del eexcept Exception:
e = Nonelogger.error(f'''Complete login failed: {e}''', exc_info = True)del eNoneNone = del e)()
whisk_logout = (lambda : try:
creds = WhiskCredentials.query.first()if creds:
creds.clear_session()db.session.commit()try:
clear_login_service = clear_login_serviceclear_generation_service = clear_generation_serviceimport app.services.whisk_automation_serviceclear_login_service()clear_generation_service()logger.info('Whisk browser closed on logout')try:
passexcept Exception:
e = Nonelogger.warning(f'''Could not close browser on logout: {e}''')try:
e = Nonedel ee = Nonedel etry:
(jsonify({
'status': 'success',
'message': 'Logged out successfully' }), 200)except Exception:
e = Nonelogger.error(f'''Whisk logout failed: {e}''', exc_info = True)del eNoneNone = del e)()
get_whisk_browser_status = (lambda : try:
is_generation_browser_open = is_generation_browser_openget_generation_service = get_generation_serviceimport app.services.whisk_automation_serviceis_open = is_generation_browser_open()current_url = Noneif is_open:
try:
service = get_generation_service()if service.driver:
current_url = service.driver.current_urltry:
passexcept Exception:
try:
passtry:
(jsonify({
'isBrowserOpen': is_open,
'currentUrl': current_url }), 200)except Exception:
e = Nonelogger.error(f'''Failed to check browser status: {e}''')del eNoneNone = del e)()
start_whisk_generation = (lambda : try:
request = requestimport flaskget_generation_service = get_generation_serviceget_whisk_log_file = get_whisk_log_filewhisk_log = whisk_logreset_whisk_log = reset_whisk_logimport app.services.whisk_automation_servicereset_whisk_log()whisk_log('[API] ========== START GENERATION FLOW ==========')whisk_log('[API] start-generation endpoint called')if not request.get_json():
data = { }prompt = data.get('prompt')whisk_log(f'''[API] Prompt: {prompt[:50] if prompt else 'None'}...''')service = get_generation_service()whisk_log(f'''[API] Service obtained: {id(service)}, driver exists: {service.driver is not None}''')whisk_log('[API] Calling start_generation_flow...')result = service.start_generation_flow(prompt)whisk_log(f'''[API] start_generation_flow result: {result}''')if result.get('success'):
(jsonify({
'status': 'success',
'message': result.get('message', 'Browser opened'),
'promptCopied': result.get('promptCopied', False),
'reused': result.get('reused', False),
'needsLogin': result.get('needsLogin', False) }), 200)(None({
'status': 'error',
'error': result.get('error', 'Failed to open browser') }), 400)except ImportError:
e = Nonewhisk_log = whisk_logimport app.services.whisk_automation_servicewhisk_log(f'''[API] Whisk automation dependencies not installed: {e}''', 'error')except Exception:
passdel eNoneNone = del eexcept Exception:
e = Nonewhisk_log = whisk_logimport app.services.whisk_automation_servicewhisk_log(f'''[API] Start generation failed: {e}''', 'error')except Exception:
passdel eNoneNone = del e)()
run_whisk_batch_generation = (lambda project_id: try:
request = requestimport flaskget_generation_service = get_generation_serviceimport app.services.whisk_automation_serviceproject = Project.query.get_or_404(project_id)if not request.get_json():
data = { }prompts = data.get('prompts', [])if not prompts:
(jsonify({
'error': 'No prompts provided' }), 400)projects_dir = None()download_dir = str(projects_dir / project_id / 'whisk_images')service = get_generation_service()result = service.run_batch_generation(prompts, download_dir)if result.get('success'):
(jsonify({
'status': 'success',
'total': result.get('total', 0),
'completed': result.get('completed', 0),
'failed': result.get('failed', 0),
'results': result.get('results', []) }), 200)(None({
'status': 'error',
'error': result.get('error', 'Batch generation failed'),
'total': result.get('total', 0),
'completed': result.get('completed', 0),
'failed': result.get('failed', 0),
'results': result.get('results', []) }), 400)except ImportError:
e = Nonelogger.error(f'''Whisk automation dependencies not installed: {e}''')del eNoneNone = del eexcept Exception:
e = Nonelogger.error(f'''Batch generation failed: {e}''', exc_info = True)del eNoneNone = del e)()
proceed_whisk_generation = (lambda project_id: logger.info(f'''[API] proceed-generation called for project: {project_id}''')try:
request = requestimport flaskget_generation_service = get_generation_serviceimport app.services.whisk_automation_serviceproject = Project.query.get_or_404(project_id)logger.info(f'''[API] Project validated: {project.title}''')if not request.get_json():
data = { }prompts = data.get('prompts', [])logger.info(f'''[API] Received {len(prompts)} prompts''')if not prompts:
logger.warning('[API] No prompts provided')(jsonify({
'error': 'No prompts provided' }), 400)projects_dir = None()download_dir = str(projects_dir / project_id / 'whisk_images')logger.info(f'''[API] Download dir: {download_dir}''')service = get_generation_service()logger.info(f'''[API] Service obtained, driver exists: {service.driver is not None}''')if not service.driver:
logger.error('[API] Browser not open!')(jsonify({
'status': 'error',
'error': 'Browser not open. Please click "생성 시작" first.' }), 400)None.info('[API] Calling run_batch_generation_in_place...')result = service.run_batch_generation_in_place(prompts, download_dir, project_id)logger.info(f'''[API] Batch result: success={result.get('success')}, completed={result.get('completed')}, failed={result.get('failed')}''')if result.get('success'):
(jsonify({
'status': 'success',
'total': result.get('total', 0),
'completed': result.get('completed', 0),
'failed': result.get('failed', 0),
'results': result.get('results', []) }), 200)(None({
'status': 'error',
'error': result.get('error', 'Generation failed'),
'total': result.get('total', 0),
'completed': result.get('completed', 0),
'failed': result.get('failed', 0),
'results': result.get('results', []) }), 400)except ImportError:
e = Nonelogger.error(f'''Whisk automation dependencies not installed: {e}''')del eNoneNone = del eexcept Exception:
e = Nonelogger.error(f'''Proceed generation failed: {e}''', exc_info = True)del eNoneNone = del e)()
get_generation_progress_stream = (lambda project_id: pass# WARNING: Decompyle incomplete
)()
stop_whisk_generation = (lambda : try:
request_stop = request_stopclear_generation_service = clear_generation_serviceimport app.services.whisk_automation_servicerequest_stop()clear_generation_service()(jsonify({
'status': 'success',
'message': 'Generation stopped' }), 200)except Exception:
e = Nonelogger.error(f'''Stop generation failed: {e}''', exc_info = True)del eNoneNone = del e)()
get_whisk_log = (lambda : try:
get_whisk_log_file = get_whisk_log_fileimport app.services.whisk_automation_servicelog_file = get_whisk_log_file()contents = ''if os.path.exists(log_file):
f = open(log_file, 'r', encoding = 'utf-8')lines = f.readlines()contents = ''.join(lines[-200:])try:
None(None, None)with None:
if not None:
try:
try:
(jsonify({
'logFile': log_file,
'contents': contents }), 200)except Exception:
e = Nonelogger.error(f'''Failed to get log: {e}''')del eNoneNone = del e)()
get_project_batch_stats = (lambda project_id: try:
project = Project.query.get(project_id)if not project:
(jsonify({
'error': f'''Project not found: {project_id}''' }), 404)characters = None.query.filter_by(project_id = project_id).all()total_characters = len(characters)generated_characters = (lambda .0: pass# WARNING: Decompyle incomplete
)(characters())
        character_images = []
        projects_dir = get_projects_path()
        characters_dir = projects_dir / project_id / 'images' / 'characters'
        char_name_map = _build_project_character_name_map(project, characters)
        if characters_dir.exists():
            for img_path in characters_dir.iterdir():
                if img_path.is_file() and img_path.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp', '.gif'):
                    unique_id = _normalize_whisk_character_key(img_path.stem)
                    name = char_name_map.get(unique_id, unique_id)
                    if not unique_id:
                        character_images.append({
                            'uniqueId': None,
                            'name': name,
                            'filename': img_path.name,
                            'url': f'''/api/whisk/projects/{project_id}/character-image/{img_path.name}''' })
                        continue
                        scene_stats = {
                            'total': 0,
                            'completed': 0,
                            'failed': 0,
                            'pending': 0 }
                        if not project.video_settings:
                            video_settings = { }
                            scene_generation = video_settings.get('sceneGeneration', { })
                            scene_images = scene_generation.get('sceneImages', [])
                            if scene_images:
                                scene_stats['total'] = len(scene_images)
                                for scene in scene_images:
                                    status = scene.get('status', '')
                                    if status == 'success' and scene.get('imageDataUrl') or scene.get('imagePath'):
                                        continue
                                    if status == 'error':
                                        continue
                                    {
                                        'name': None,
                                        'nameKo': None } = sum
                                    settings = scene_generation.get('settings', { })
                                    if not settings.get('styleTemplateId'):
                                        template_id = settings.get('selectedStyleTemplateId')
                                        if template_id:
                                            template = ImagePromptTemplate.query.get(template_id)
                                            if template:
                                                style_template['name'] = template.name
                                                style_template['nameKo'] = template.name_ko
        return (jsonify({
            'characters': {
                'total': total_characters,
                'generated': generated_characters,
                'images': character_images },
            'scenes': scene_stats,
            'styleTemplate': style_template }), 200)
    except Exception:
        e = None
        logger.error(f'''Failed to get batch stats: {e}''', exc_info = True)
        del e
        return None
        None = 
        del e

)()
get_character_image = (lambda project_id, filename: send_file = send_fileimport flasktry:
Project.query.get_or_404(project_id)safe_filename = os.path.basename(filename)if safe_filename != filename:
(jsonify({
'error': 'Invalid filename' }), 400)projects_dir = None()image_path = projects_dir / project_id / 'images' / 'characters' / safe_filenameif not image_path.exists():
(jsonify({
'error': 'Image not found' }), 404)send_file(str(image_path))except Exception:
e = Nonelogger.error(f'''Failed to serve character image: {e}''', exc_info = True)del eNoneNone = del e)()
apply_characters = (lambda project_id: get_generation_service = get_generation_serviceimport app.services.whisk_automation_servicetry:
Project.query.get_or_404(project_id)projects_dir = get_projects_path()characters_dir = projects_dir / project_id / 'images' / 'characters'if not characters_dir.exists():
(jsonify({
'success': False,
'error': 'Characters folder not found' }), 404)image_paths = Nonefor img_path in characters_dir.iterdir():
if img_path.is_file() and img_path.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp', '.gif'):
image_paths.append(str(img_path.resolve()))if not image_paths:
(jsonify({
'success': False,
'error': 'No character images found' }), 404)None.info(f'''[APPLY_CHARS] Found {len(image_paths)} character images for project {project_id}''')service = get_generation_service()if not service or service.driver:
logger.info('[APPLY_CHARS] No active browser, attempting to open Whisk...')try:
result = service.start_generation_flow()if not result.get('success'):
(jsonify({
'success': False,
'error': 'Failed to open Whisk browser: ' + result.get('error', 'Unknown error') }), 400)None.info('[APPLY_CHARS] Browser opened successfully, proceeding with character application')try:
passexcept Exception:
e = Nonelogger.error(f'''[APPLY_CHARS] Failed to open browser: {e}''')try:
del eNoneNone = del etry:
result = service.apply_character_images(image_paths)(jsonify({
'success': result['success'],
'subjectApplied': result['subject_applied'],
'styleApplied': result['style_applied'],
'error': result.get('error') }), 200 if result['success'] else 400)except Exception:
e = Nonelogger.error(f'''Failed to apply characters: {e}''', exc_info = True)del eNoneNone = del e)()
apply_style = (lambda : get_generation_service = get_generation_serviceimport app.services.whisk_automation_serviceImagePromptTemplate = ImagePromptTemplateimport app.modelsimport ostry:
if not request.get_json():
data = { }template_id = data.get('templateId')if not template_id:
(jsonify({
'success': False,
'error': 'Template ID is required' }), 400)template = None.query.get(template_id)if not template:
(jsonify({
'success': False,
'error': 'Template not found' }), 404)if not None.sample_image_url:
(jsonify({
'success': False,
'error': 'Template has no sample image' }), 400)sample_url = None.sample_image_urlif sample_url.startswith('data:'):
import base64import tempfile(header, encoded) = sample_url.split(',', 1)mime_type = header.split(':')[1].split(';')[0]ext = mime_type.split('/')[1]if ext == 'jpeg':
ext = 'jpg'image_data = base64.b64decode(encoded)temp_file = tempfile.NamedTemporaryFile(suffix = f'''.{ext}''', delete = False)temp_file.write(image_data)temp_file.close()image_path = temp_file.namelogger.info(f'''[APPLY_STYLE] Saved base64 image to temp file: {image_path}''')elif sample_url.startswith('/static/'):
current_app = current_appimport flaskstatic_folder = current_app.static_folderrelative_path = sample_url.replace('/static/', '')image_path = os.path.join(static_folder, relative_path)if not os.path.exists(image_path):
(jsonify({
'success': False,
'error': f'''Style image not found: {relative_path}''' }), 404)None.info(f'''[APPLY_STYLE] Using static file: {image_path}''')elif sample_url.startswith('/api/style-samples/'):
get_user_style_samples_path = get_user_style_samples_pathimport app.config.pathsfilename = sample_url.replace('/api/style-samples/', '')safe_filename = os.path.basename(filename)samples_dir = get_user_style_samples_path()image_path = os.path.join(str(samples_dir), safe_filename)if not os.path.exists(image_path):
(jsonify({
'success': False,
'error': f'''Custom style image not found: {safe_filename}''' }), 404)None.info(f'''[APPLY_STYLE] Using custom style sample: {image_path}''')else:
(jsonify({
'success': False,
'error': 'Unsupported image URL format' }), 400)service = get_generation_service()if not service or service.driver:
(jsonify({
'success': False,
'error': 'Browser not open. Please start generation first.' }), 400)result = None.apply_style_image(image_path)(jsonify({
'success': result['success'],
'styleApplied': result['style_applied'],
'templateName': template.name,
'error': result.get('error') }), 200 if template.name_ko or result['success'] else 400)except Exception:
e = Nonelogger.error(f'''Failed to apply style: {e}''', exc_info = True)del eNoneNone = del e)()
open_characters_folder = (lambda project_id: try:
Project.query.get_or_404(project_id)projects_dir = get_projects_path()characters_dir = projects_dir / project_id / 'images' / 'characters'characters_dir.mkdir(parents = True, exist_ok = True)folder_path = str(characters_dir)logger.info(f'''Attempting to open characters folder: {folder_path}''')logger.info(f'''Folder exists: {os.path.exists(folder_path)}''')logger.info(f'''Platform: {sys.platform}''')if sys.platform == 'win32':
open_folder_foreground(folder_path)elif sys.platform == 'darwin':
subprocess.Popen([
'open',
folder_path])else:
subprocess.Popen([
'xdg-open',
folder_path])logger.info(f'''Successfully opened characters folder: {folder_path}''')(jsonify({
'status': 'success',
'folderPath': folder_path.replace('\\', '/') }), 200)except Exception:
e = Nonelogger.error(f'''Failed to open characters folder: {e}''', exc_info = True)del eNoneNone = del e)()
open_whisk_folder = (lambda project_id: try:
Project.query.get_or_404(project_id)projects_dir = get_projects_path()whisk_dir = projects_dir / project_id / 'whisk_images'whisk_dir.mkdir(parents = True, exist_ok = True)folder_path = str(whisk_dir)logger.info(f'''Attempting to open Whisk folder: {folder_path}''')if sys.platform == 'win32':
open_folder_foreground(folder_path)elif sys.platform == 'darwin':
subprocess.Popen([
'open',
folder_path])else:
subprocess.Popen([
'xdg-open',
folder_path])logger.info(f'''Successfully opened Whisk folder: {folder_path}''')(jsonify({
'status': 'success',
'folderPath': folder_path.replace('\\', '/') }), 200)except Exception:
e = Nonelogger.error(f'''Failed to open Whisk folder: {e}''', exc_info = True)del eNoneNone = del e)()
serve_whisk_image = (lambda project_id, filename: send_file = send_fileimport flaskimport mimetypesimport ostry:
Project.query.get_or_404(project_id)safe_filename = os.path.basename(filename)if safe_filename or safe_filename != filename:
(jsonify({
'error': 'Invalid filename' }), 400)projects_dir = None()image_path = projects_dir / project_id / 'whisk_images' / safe_filenameif not image_path.exists():
(jsonify({
'error': 'Image not found' }), 404)(mime_type, _) = None.guess_type(str(image_path))if not mime_type:
mime_type = 'image/png'send_file(str(image_path), mimetype = mime_type, as_attachment = False)except Exception:
e = Nonelogger.error(f'''Failed to serve whisk image: {e}''', exc_info = True)del eNoneNone = del e)()
apply_whisk_to_scene = (lambda project_id: request = requestimport flaskimport shutilimport os# WARNING: Decompyle incomplete
)()
analyze_scenes_for_whisk = (lambda project_id: pass# WARNING: Decompyle incomplete
)()
match_whisk_characters = (lambda project_id: pass# WARNING: Decompyle incomplete
)()

def _split_whisk_analysis(text = whisk_controller_bp.route('/api/whisk/projects/<project_id>/apply-to-scene', methods = [
    'POST'])):
    '''
    Whisk 분석 결과를 개별 캐릭터 설명으로 분리

    패턴:
    1. 빈 줄 2개 이상으로 구분된 단락
    2. "A digital illustration..." 등으로 시작하는 새 설명
    '''
    if not text:
        return []
    paragraphs = None.split('\\n\\s*\\n\\s*\\n+', text.strip())
    if len(paragraphs) == 1:
        paragraphs = re.split('\\n\\s*\\n', text.strip())
    result = []
    for p in paragraphs:
        cleaned = p.strip()
        if len(cleaned) >= 50:
            result.append(cleaned)
        if result and text.strip():
            result = [
                text.strip()]
    return result


def _build_character_summary_for_matching(characters = whisk_controller_bp.route('/api/whisk/projects/<project_id>/open-characters-folder', methods = [
    'POST'])):
    """
    캐릭터 정보를 AI 매칭용 요약으로 변환

    Returns:
        dict: { 'A': 'Character A (백무진): male, 60대, 마른 체형...', ... }
    """
    summaries = { }
    for char in characters:
        unique_id = char.get('uniqueId', '')
        name = char.get('name', 'Unknown')
        parts = [
            f'''Character {unique_id} ({name}):''']
        if char.get('gender'):
            parts.append(f'''gender={char['gender']}''')
        if char.get('ageRange'):
            parts.append(f'''age={char['ageRange']}''')
        if char.get('appearance'):
            parts.append(f'''appearance={char['appearance']}''')
        if char.get('clothing'):
            parts.append(f'''clothing={char['clothing']}''')
        if char.get('image_prompt_en'):
            parts.append(f'''profile={char['image_prompt_en'][:200]}''')
        summaries[unique_id] = ' '.join(parts)
        return summaries


def _match_description_with_characters(provider = whisk_controller_bp.route('/api/whisk/projects/<project_id>/character-image/<filename>', methods = [
    'GET']), whisk_description = whisk_controller_bp.route('/api/whisk/projects/<project_id>/apply-characters', methods = [
    'POST']), character_summaries = whisk_controller_bp.route('/api/whisk/apply-style', methods = [
    'POST']), characters = ('whisk_description', str, 'character_summaries', dict, 'characters', list, 'return', dict)):
    """
    Whisk 설명과 캐릭터 목록을 비교하여 가장 일치하는 캐릭터 찾기

    Returns:
        dict: {
            'characterId': 'D',
            'characterName': '흑풍',
            'confidence': 85,
            'reasoning': '...'
        }
    """
    char_list = (lambda .0: [ f'''- {summary}''' for summary in .0 ])(character_summaries.values()())
    prompt = f'''You are a character matching expert. Analyze the Whisk image description and find the BEST matching character from the list.\n\n## Whisk Image Description:\n{whisk_description}\n\n## Available Characters:\n{char_list}\n\n## Instructions:\n1. Compare physical features: gender, age, skin tone, hair style, body type\n2. Compare clothing and accessories\n3. Find the character that matches the MOST features\n4. If no character matches well, return "NONE"\n\n## Response Format (JSON only, no markdown):\n{{"characterId": "X", "characterName": "이름", "confidence": 0-100, "reasoning": "brief explanation in Korean"}}\n\nImportant:\n- characterId must be one of: {', '.join(character_summaries.keys())} or "NONE"\n- confidence: 90+ for strong match, 70-89 for good match, 50-69 for weak match, <50 for no match\n- If confidence < 50, set characterId to "NONE"\n'''
    
    try:
        response = provider.generate_text(prompt, model = 'gemini-2.5-flash')
        response_text = response.strip()
        if response_text.startswith('```'):
            response_text = re.sub('^```(?:json)?\\n?', '', response_text)
            response_text = re.sub('\\n?```$', '', response_text)
        import json
        result = json.loads(response_text)
        char_id = result.get('characterId', 'NONE')
        char_name = result.get('characterName', '')
        confidence = result.get('confidence', 0)
        reasoning = result.get('reasoning', '')
        if not char_id != 'NONE' and char_name:
            for char in characters:
                if char.get('uniqueId') == char_id:
                    char_name = char.get('name', '')
                    '\n'.join
                
                return {
                    'characterId': char_id,
                    'characterName': char_name,
                    'confidence': confidence,
                    'reasoning': reasoning }
                except Exception:
                    e = None
                    logger.error(f'''AI matching failed: {e}''')
                    del e
                    return None
                    None = 
                    del e



def _strip_style_keywords(text = whisk_controller_bp.route('/api/whisk/stop-generation', methods = [
    'POST'])):
