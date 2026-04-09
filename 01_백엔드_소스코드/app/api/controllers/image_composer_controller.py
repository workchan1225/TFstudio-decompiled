# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_composer_controller.pyc (Python 3.11)

'''
Image Composer API Controller
이미지 컴포지터 관련 API 엔드포인트
- 컴포지션 저장/로드
- 프레임 미리보기
- 영상 렌더링
'''
import logging
from flask import Blueprint, request, jsonify
from app.services.image_composer_service import ImageComposerService
logger = logging.getLogger(__name__)
image_composer_bp = Blueprint('image_composer', __name__)
save_composition = (lambda project_id = None: try:
data = request.get_json()if data or 'composition' not in data:
(jsonify({
'success': False,
'error': 'No composition data provided' }), 400)composition = None['composition']sync_segments = data.get('syncSegments')apply_to_video = data.get('applyToVideo', True)service = ImageComposerService(project_id)result = service.save_composition(composition, sync_segments, apply_to_video)if apply_to_video:
jsonify({
'success': True,
'compositionId': result.get('id'),
'savedAt': result.get('savedAt'),
'appliedToVideo': sync_segments is not None })except Exception:
e = result.get('savedAt')logger.error(f'''Failed to save composition for project {project_id}: {e}''')del eNoneNone = del e)()
load_composition = (lambda project_id = None: try:
service = ImageComposerService(project_id)composition = service.load_composition()jsonify({
'success': True,
'exists': composition is not None,
'composition': composition })except Exception:
e = Nonelogger.error(f'''Failed to load composition for project {project_id}: {e}''')del eNoneNone = del e)()
preview_frame = (lambda project_id = None: try:
data = request.get_json()if data or 'composition' not in data:
(jsonify({
'success': False,
'error': 'No composition data provided' }), 400)composition = None['composition']frame_time = data.get('frameTime', 0)service = ImageComposerService(project_id)image_data_url = service.render_preview_frame(composition, frame_time)jsonify({
'success': True,
'imageDataUrl': image_data_url })except Exception:
e = Nonelogger.error(f'''Failed to generate preview for project {project_id}: {e}''')del eNoneNone = del e)()
render_composition = (lambda project_id = None: try:
data = request.get_json()if data or 'composition' not in data:
(jsonify({
'success': False,
'error': 'No composition data provided' }), 400)composition = None['composition']export_settings = data.get('exportSettings', { })service = ImageComposerService(project_id)result = service.render_video(composition, export_settings)jsonify({
'success': True,
'outputPath': result.get('outputPath'),
'outputUrl': result.get('outputUrl') })except Exception:
e = Nonelogger.error(f'''Failed to render composition for project {project_id}: {e}''')del eNoneNone = del e)()
list_assets = (lambda project_id = None: try:
service = ImageComposerService(project_id)assets = service.list_assets()jsonify({
'success': True,
'assets': assets,
'count': len(assets) })except Exception:
e = Nonelogger.error(f'''Failed to list assets for project {project_id}: {e}''')del eNoneNone = del e)()
