# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bgm_controller.pyc (Python 3.11)

'''
BGM Controller (Clean Architecture Version)

Handles BGM upload, management, and mixing for projects.
Replaces v1 bgm.py.

Registration in app/__init__.py:
    from app.api.controllers import bgm_controller_bp
    app.register_blueprint(bgm_controller_bp)

Endpoints (6):
- POST /api/projects/<project_id>/bgm/upload - Upload BGM track
- GET /api/projects/<project_id>/bgm - Get project BGM tracks
- PUT /api/projects/<project_id>/bgm/<track_id> - Update BGM track
- DELETE /api/projects/<project_id>/bgm/<track_id> - Delete BGM track
- POST /api/projects/<project_id>/bgm/mix - Mix BGM with audio
- PUT /api/projects/<project_id>/bgm/reorder - Reorder BGM tracks
'''
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import logging
from pathlib import Path
from app.models.project import Project
from app import db
from app.services.bgm_service import BGMService
logger = logging.getLogger(__name__)
bgm_controller_bp = Blueprint('bgm', __name__)
ALLOWED_EXTENSIONS = {
    'aac',
    'm4a',
    'mp3',
    'ogg',
    'wav',
    'flac'}

def allowed_file(filename):
    if '.' in filename:
        pass
    return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

upload_bgm = (lambda project_id: project = Project.query.get_or_404(project_id)if 'file' not in request.files:
(jsonify({
'error': 'No file provided' }), 400)file = None.files['file']if file.filename == '':
(jsonify({
'error': 'No file selected' }), 400)if not None(file.filename):
(jsonify({
'error': f'''Invalid file type. Allowed: {', '.join(ALLOWED_EXTENSIONS)}''' }), 400)try:
bgm_service = BGMService(project_id)bgm_service.load_tracks_from_db(project)track_name = request.form.get('name', file.filename)track = bgm_service.upload_bgm_file(file, track_name)bgm_service.save_tracks_to_db(project)logger.info(f'''BGM uploaded for project {project_id}: {track['name']}''')(jsonify({
'status': 'success',
'track': track }), 200)except Exception:
e = Nonelogger.error(f'''BGM upload failed: {e}''', exc_info = True)del eNoneNone = del e)()
list_bgm_tracks = (lambda project_id: project = Project.query.get_or_404(project_id)(jsonify({
'tracks': BGMService.normalize_tracks(project.bgm_tracks) }), 200))()
update_bgm_track = (lambda project_id, track_id: project = Project.query.get_or_404(project_id)data = request.jsontry:
bgm_service = BGMService(project_id)bgm_service.load_tracks_from_db(project)updated_track = bgm_service.update_track(track_id, data)if not updated_track:
(jsonify({
'error': 'Track not found' }), 404)None.save_tracks_to_db(project)if project.mixed_audio_url:
logger.info('Invalidating mixed_audio_url after BGM update')project.mixed_audio_url = Nonedb.session.commit()(jsonify({
'status': 'success',
'track': updated_track }), 200)except Exception:
e = Nonelogger.error(f'''BGM update failed: {e}''', exc_info = True)del eNoneNone = del e)()
delete_bgm_track = (lambda project_id, track_id: project = Project.query.get_or_404(project_id)try:
bgm_service = BGMService(project_id)bgm_service.load_tracks_from_db(project)success = bgm_service.delete_track(track_id)if not success:
(jsonify({
'error': 'Track not found' }), 404)None.save_tracks_to_db(project)if project.mixed_audio_url:
logger.info('Invalidating mixed_audio_url after BGM deletion')project.mixed_audio_url = Nonedb.session.commit()(jsonify({
'status': 'success' }), 200)except Exception:
e = Nonelogger.error(f'''BGM delete failed: {e}''', exc_info = True)del eNoneNone = del e)()
mix_bgm_with_audio = (lambda project_id: project = Project.query.get_or_404(project_id)logger.info(f'''[BGM Mix] DEPRECATED endpoint called for project {project_id}''')logger.info('[BGM Mix] BGM mixing now happens at video generation time')if not project.bgm_tracks:
bgm_tracks = []enabled_tracks = bgm_tracks()if enabled_tracks:
if not project.direct_progress:
project.direct_progress = { }project.direct_progress['hasBGM'] = Truedb.session.commit()logger.info(f'''[BGM Mix] hasBGM flag set (enabled tracks: {len(enabled_tracks)})''')(jsonify({
'status': 'success',
'message': 'BGM 설정이 저장되었습니다. 영상 생성 시 자동으로 믹싱됩니다.',
'mixedAudioUrl': None }), 200))()
reorder_bgm_tracks = (lambda project_id: project = Project.query.get_or_404(project_id)data = request.jsontrack_ids = data.get('trackIds', [])try:
bgm_service = BGMService(project_id)bgm_service.load_tracks_from_db(project)bgm_service.reorder_tracks(track_ids)bgm_service.save_tracks_to_db(project)(jsonify({
'status': 'success',
'tracks': bgm_service.tracks }), 200)except Exception:
e = Nonelogger.error(f'''BGM reorder failed: {e}''', exc_info = True)del eNoneNone = del e)()
