# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shorts_controller.pyc (Python 3.11)

"""
Shorts Controller

YouTube Shorts 생성 관련 API 컨트롤러

Registration in app/__init__.py:
    from app.api.controllers import shorts_controller_bp
    app.register_blueprint(shorts_controller_bp, url_prefix='/api/projects')

Endpoints:
- POST /<project_id>/shorts/analyze - 자막 분석하여 하이라이트 추출
- POST /<project_id>/shorts/generate - 쇼츠 영상 생성
- GET /<project_id>/shorts - 생성된 쇼츠 목록 조회
- GET /<project_id>/shorts/status - 생성 진행 상황 조회
- DELETE /<project_id>/shorts/<shorts_id> - 쇼츠 삭제
- POST /<project_id>/shorts/save - 쇼츠 데이터 저장
"""
from flask import Blueprint, request, jsonify
import logging
import threading
import time
import uuid
from datetime import datetime
from typing import Optional
from app.models.project import Project
from app import db
from app.services.google_auth_service import is_google_ai_configured, get_google_configuration_error_message
shorts_controller_bp = Blueprint('shorts', __name__)
logger = logging.getLogger(__name__)
_generation_progress = { }
_generation_progress_timestamps = { }
_generation_progress_lock = threading.Lock()
_GENERATION_PROGRESS_TTL_SECONDS = 1800
_GENERATION_PROGRESS_MAX_ENTRIES = 500

def _cleanup_generation_progress(now = None):
    pass
# WARNING: Decompyle incomplete


def _set_generation_progress(task_id = None, payload = None):
    _generation_progress_lock
    _cleanup_generation_progress()
    _generation_progress[task_id] = payload
    _generation_progress_timestamps[task_id] = time.time()
    None(None, None)
    return None
    with None:
        if not None:
            pass


def _update_generation_progress(task_id = None, updates = None):
    _generation_progress_lock
    existing = _generation_progress.get(task_id)
# WARNING: Decompyle incomplete


def _get_generation_progress(task_id = None):
    _generation_progress_lock
    _cleanup_generation_progress()
    payload = _generation_progress.get(task_id)
# WARNING: Decompyle incomplete

analyze_highlights = (lambda project_id = None: logger.info(f'''[ShortsController] analyze_highlights called for project {project_id}''')project = Project.query.get(project_id)if not project:
logger.error(f'''[ShortsController] Project not found: {project_id}''')(jsonify({
'error': 'Project not found',
'error_code': 'PROJECT_NOT_FOUND' }), 404)if not None.video_url:
logger.warning(f'''[ShortsController] No video found for project {project_id}''')(jsonify({
'error': '원본 영상이 없습니다. 먼저 영상 생성 탭에서 영상을 생성해주세요.',
'error_code': 'VIDEO_NOT_FOUND' }), 400)task_id = Nonetry:
ShortsAnalyzerService = ShortsAnalyzerServiceimport app.services.shorts_analyzer_serviceSettings = Settingsimport app.models.settingssettings = Settings.get_or_create()if not is_google_ai_configured(settings = settings):
logger.error('[ShortsController] Google AI is not configured')(jsonify({
'error': get_google_configuration_error_message(settings = settings),
'error_code': 'API_KEY_MISSING' }), 400)if not None.get_json():
data = { }min_duration = data.get('min_duration', 15)max_duration = data.get('max_duration', 60)count = data.get('count', 3)criteria = data.get('criteria', [
'emotional',
'key_dialogue',
'climax'])custom_prompt = data.get('custom_prompt', '')logger.info(f'''[ShortsController] Analysis params: count={count}, min={min_duration}, max={max_duration}, criteria={criteria}, custom_prompt={custom_prompt[:50] if custom_prompt else 'None'}''')subtitles = ShortsAnalyzerService.get_subtitles_from_project(project)if not subtitles:
logger.warning(f'''[ShortsController] No subtitles found for project {project_id}''')(jsonify({
'error': '자막을 찾을 수 없습니다. 먼저 자막 생성 탭에서 자막을 생성해주세요.',
'error_code': 'SUBTITLES_NOT_FOUND' }), 400)None.info(f'''[ShortsController] Found {len(subtitles)} subtitles''')result = ShortsAnalyzerService.analyze_highlights(subtitles = subtitles, min_duration = min_duration, max_duration = max_duration, count = count, criteria = criteria, custom_prompt = custom_prompt)if not project.shorts_data:
shorts_data = { }shorts_data['analysis_result'] = {
'highlights': result['highlights'],
'total_duration': result['total_duration'],
'subtitle_count': result['subtitle_count'],
'analyzed_at': datetime.now().isoformat(),
'settings': {
'min_duration': min_duration,
'max_duration': max_duration,
'count': count,
'criteria': criteria,
'custom_prompt': custom_prompt } }project.shorts_data = shorts_datadb.session.commit()logger.info(f'''[ShortsController] Analysis completed: {len(result['highlights'])} highlights found''')jsonify({
'success': True,
'highlights': result['highlights'],
'total_duration': result['total_duration'],
'subtitle_count': result['subtitle_count'] })except ValueError:
e = Nonelogger.error(f'''[ShortsController] Validation error: {e}''')del eNoneNone = del eexcept Exception:
e = Nonelogger.error(f'''[ShortsController] Unexpected error: {e}''', exc_info = True)del eNoneNone = del e)()
generate_shorts = (lambda project_id = None: pass# WARNING: Decompyle incomplete
)()
get_generation_status = (lambda project_id = None: task_id = request.args.get('task_id')if not task_id:
(jsonify({
'error': 'task_id is required' }), 400)task_status = None(task_id)# WARNING: Decompyle incomplete
)()
get_shorts_list = (lambda project_id = None: project = Project.query.get(project_id)if not project:
(jsonify({
'error': 'Project not found' }), 404)try:
ShortsGeneratorService = ShortsGeneratorServiceimport app.services.shorts_generator_servicegenerator = ShortsGeneratorService(project)file_shorts = generator.get_all_shorts()if not project.shorts_data:
shorts_data = { }db_shorts = shorts_data.get('generated_shorts', [])jsonify({
'success': True,
'shorts': file_shorts,
'analysis_result': shorts_data.get('analysis_result') })except Exception:
e = Nonelogger.error(f'''Error in get_shorts_list: {e}''')del eNoneNone = del e)()
delete_shorts = (lambda project_id = None, shorts_id = None: pass# WARNING: Decompyle incomplete
)()
save_shorts_data = (lambda project_id = None: project = Project.query.get(project_id)if not project:
(jsonify({
'error': 'Project not found' }), 404)try:
if not request.get_json():
data = { }if not project.shorts_data:
shorts_data = { }shorts_data.update({
'selected_clips': data.get('selected_clips', []),
'settings': data.get('settings', { }),
'updated_at': datetime.now().isoformat() })if 'analysis_result' in data:
shorts_data['analysis_result'] = data['analysis_result']project.shorts_data = shorts_datadb.session.commit()jsonify({
'success': True })except Exception:
e = Nonelogger.error(f'''Error in save_shorts_data: {e}''')del eNoneNone = del e)()
add_manual_clip = (lambda project_id = None: project = Project.query.get(project_id)if not project:
(jsonify({
'error': 'Project not found' }), 404)try:
if not request.get_json():
data = { }start_seconds = data.get('start_seconds', 0)end_seconds = data.get('end_seconds', 30)if end_seconds <= start_seconds:
(jsonify({
'error': '종료 시간은 시작 시간보다 커야 합니다.' }), 400)duration = None - start_secondsif duration < 5:
(jsonify({
'error': '클립 길이는 최소 5초 이상이어야 합니다.' }), 400)if None > 60:
(jsonify({
'error': '클립 길이는 최대 60초까지 가능합니다.' }), 400)clip = {
'id': f'''{uuid.uuid4().hex[:8]}''',
'start_seconds': start_seconds,
'end_seconds': end_seconds,
'start_time': _seconds_to_time(start_seconds),
'end_time': _seconds_to_time(end_seconds),
'duration': duration,
'type': 'manual',
'score': 1,
'reason': '수동 추가',
'transcript': '' }if not project.shorts_data:
shorts_data = { }selected_clips = shorts_data.get('selected_clips', [])selected_clips.append(clip)shorts_data['selected_clips'] = selected_clipsproject.shorts_data = shorts_datadb.session.commit()jsonify({
'success': True,
'clip': clip })except Exception:
e = Nonelogger.error(f'''Error in add_manual_clip: {e}''')del eNoneNone = del e)()

def _seconds_to_time(seconds = None):
    '''초를 HH:MM:SS 형식으로 변환'''
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f'''{hours:02d}:{minutes:02d}:{secs:02d}'''
