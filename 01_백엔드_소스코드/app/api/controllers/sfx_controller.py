# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sfx_controller.pyc (Python 3.11)

"""
SFX Controller (Sound Effects)

효과음 업로드, 라이브러리 관리, 믹싱 API 컨트롤러

Registration in app/__init__.py:
    from app.api.controllers import sfx_controller_bp
    app.register_blueprint(sfx_controller_bp, url_prefix='/api/sfx')

Endpoints (14):
- POST /upload - 오디오 파일 업로드 + 분석 + 라이브러리 자동 저장
- POST /analyze-file - 오디오 파일 분석 (저장 없이)
- GET /categories - SFX 카테고리 목록
- POST /mix - SFX와 메인 오디오 믹싱
- POST /preview - SFX 미리듣기 생성
- GET /library - 라이브러리 항목 조회
- POST /library - 라이브러리에 SFX 추가
- DELETE /library/<item_id> - 라이브러리에서 제거
- PATCH /library/<item_id> - 라이브러리 항목 수정
- POST /library/<item_id>/favorite - 즐겨찾기 토글
- GET /library/stats - 라이브러리 통계
- POST /library/import - 프로젝트에서 라이브러리로 가져오기
- POST /save-project-sfx - 프로젝트 SFX 저장
- POST /save-mixed-audio - 믹싱 오디오 URL 저장
"""
from flask import Blueprint, request, jsonify
import logging
import os
import uuid
from werkzeug.utils import secure_filename
from app.models.project import Project
from app import db
sfx_controller_bp = Blueprint('sfx', __name__)
logger = logging.getLogger(__name__)
upload_sfx = (lambda : if 'file' not in request.files:
(jsonify({
'error': 'No file provided' }), 400)file = None.files['file']if file.filename == '':
(jsonify({
'error': 'No file selected' }), 400)try:
analyze_audio_file = analyze_audio_filevalidate_audio_file = validate_audio_fileimport app.utils.audio_analyzerget_sfx_library_path = get_sfx_library_pathimport app.config.pathsget_library_service = get_library_serviceimport app.services.sfx_library_servicefilename = secure_filename(file.filename)library_dir = str(get_sfx_library_path())os.makedirs(library_dir, exist_ok = True)file_id = str(uuid.uuid4())if not os.path.splitext(filename)[1].lower():
ext = '.wav'saved_filename = f'''{file_id}{ext}'''saved_path = os.path.join(library_dir, saved_filename)file.save(saved_path)(is_valid, error_msg) = validate_audio_file(saved_path)if not is_valid:
os.remove(saved_path)(jsonify({
'error': error_msg }), 400)analysis = analyze_audio_file(saved_path, original_filename = file.filename)if not request.form.get('name'):
name = analysis.get('suggested_name', 'Untitled SFX')if not request.form.get('category'):
category = analysis.get('suggested_category', 'action')description = request.form.get('description', '')tags_str = request.form.get('tags', '')tags = tags_str.split(',')() if tags_str else []auto_save = request.form.get('autoSave', 'true').lower() == 'true'item = Noneallow_duplicate = request.form.get('allowDuplicate', 'false').lower() == 'true'if auto_save:
library_service = get_library_service()result = library_service.add_to_library(source_path = saved_path, name = name, description = description, category = category, tags = tags, metadata = {
'duration': analysis.get('duration', 0),
'sample_rate': analysis.get('sample_rate', 44100),
'channels': analysis.get('channels', 2),
'recommended_volume': analysis.get('recommended_volume', 0.7),
'original_filename': filename }, allow_duplicate = allow_duplicate)if result.get('success'):
item = result.get('item')elif result.get('error') == 'duplicate':
os.remove(saved_path)(jsonify({
'success': False,
'error': 'duplicate',
'message': result.get('message', '이미 동일한 효과음이 존재합니다'),
'existingItem': result.get('existingItem') }), 409)try:
os.remove(saved_path)(jsonify({
'error': result.get('error', 'Failed to save to library') }), 500)try:
(jsonify({
'success': True,
'item': item,
'analysis': {
'duration': analysis.get('duration', 0),
'sample_rate': analysis.get('sample_rate', 44100),
'channels': analysis.get('channels', 2),
'format': analysis.get('format', 'unknown'),
'peak_volume': analysis.get('peak_volume', 0),
'mean_volume': analysis.get('mean_volume', -20),
'recommended_volume': analysis.get('recommended_volume', 0.7),
'suggested_name': analysis.get('suggested_name', ''),
'suggested_category': analysis.get('suggested_category', 'action'),
'file_size': analysis.get('file_size', 0) },
'savedPath': saved_path if not auto_save else None }), 200)except Exception:
e = Nonelogger.error(f'''[SFX] Upload error: {e}''')del eNoneNone = del e)()
analyze_file = (lambda : if 'file' not in request.files:
(jsonify({
'error': 'No file provided' }), 400)file = None.files['file']if file.filename == '':
(jsonify({
'error': 'No file selected' }), 400)try:
analyze_audio_file = analyze_audio_filevalidate_audio_file = validate_audio_fileimport app.utils.audio_analyzerget_temp_path = get_temp_pathimport app.config.pathstemp_dir = str(get_temp_path())os.makedirs(temp_dir, exist_ok = True)filename = secure_filename(file.filename)if not os.path.splitext(filename)[1].lower():
ext = '.wav'temp_path = os.path.join(temp_dir, f'''analyze_{uuid.uuid4()}{ext}''')file.save(temp_path)try:
(is_valid, error_msg) = validate_audio_file(temp_path)if not is_valid:
try:
if os.path.exists(temp_path):
os.remove(temp_path)(jsonify({
'error': error_msg }), 400)try:
analysis = analyze_audio_file(temp_path, original_filename = file.filename)try:
if os.path.exists(temp_path):
os.remove(temp_path)(jsonify({
'success': True,
'analysis': analysis }), 200)if os.path.exists(temp_path):
os.remove(temp_path)try:
passexcept Exception:
e = (jsonify({
'error': error_msg }), 400)logger.error(f'''[SFX] Analyze error: {e}''')del eNoneNone = del e)()
get_categories = (lambda : get_all_sfx_categories = get_all_sfx_categoriesimport app.utils.sfx_promptscategories = get_all_sfx_categories()(jsonify({
'categories': categories }), 200))()
mix_sfx = (lambda :
