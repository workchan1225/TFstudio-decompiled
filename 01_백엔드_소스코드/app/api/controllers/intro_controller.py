# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intro_controller.pyc (Python 3.11)

'''
Intro Controller - 인트로 생성 API 엔드포인트

POST /api/intro/generate           - 인트로 전체 생성
POST /api/intro/generate-hook      - 후킹 텍스트만 생성
POST /api/intro/extract-highlights - 하이라이트 장면 추출
POST /api/intro/generate-tts       - 인트로 TTS 생성
POST /api/intro/replace-image      - 개별 인트로 이미지 교체
POST /api/intro/update-video       - Grok 비디오 경로 업데이트
GET  /api/intro/templates          - 템플릿 목록
POST /api/intro/save               - 인트로 데이터 저장
GET  /api/intro/<project_id>       - 인트로 데이터 조회
'''
from flask import Blueprint, jsonify, request
intro_controller_bp = Blueprint('intro', __name__, url_prefix = '/api/intro')
generate_auto_intro = (lambda : data = request.get_json()if not data:
(jsonify({
'error': '요청 데이터가 없습니다.' }), 400)project_id = None.get('projectId')if not project_id:
(jsonify({
'error': 'projectId가 필요합니다.' }), 400)scene_image_count = None.get('sceneImageCount', 3)if not  <= 1, scene_image_count or 1, scene_image_count <= 10:
pass(jsonify({
'error': 'sceneImageCount는 1~10 사이여야 합니다.' }), 400)intro_servicefrom app.services.intro import intro_serviceif result.get('success'):
jsonify(result)(None(result), 500))()
generate_intro = (lambda : data = request.get_json()if not data:
(jsonify({
'error': '요청 데이터가 없습니다.' }), 400)project_id = None.get('projectId')if not project_id:
(jsonify({
'error': 'projectId가 필요합니다.' }), 400)intro_service = intro_serviceimport app.services.introresult = intro_service.generate_full_intro(project_id = project_id, scenes = data.get('scenes', []), intro_type = data.get('introType', 'highlight_question'), template_id = data.get('templateId'), hook_text = data.get('hookText'), source_scene_id = data.get('sourceSceneId'), duration = data.get('duration', 8), effect = data.get('effect', 'fast_zoom'), generate_tts = data.get('generateTts', False))if result.get('success'):
jsonify(result)(None(result), 500))()
generate_hook_text = (lambda : data = request.get_json()if not data:
(jsonify({
'error': '요청 데이터가 없습니다.' }), 400)narration_text = None.get('narrationText', '')if not narration_text:
(jsonify({
'error': 'narrationText가 필요합니다.' }), 400)intro_service = intro_serviceimport app.services.introresult = intro_service.generate_hook_text(narration_text = narration_text, intro_type = data.get('introType', 'highlight_question'))# WARNING: Decompyle incomplete
)()
extract_highlights = (lambda : data = request.get_json()if not data:
(jsonify({
'error': '요청 데이터가 없습니다.' }), 400)scenes = None.get('scenes', [])if not scenes:
(jsonify({
'error': 'scenes가 필요합니다.' }), 400)intro_service = intro_serviceimport app.services.introhighlights = intro_service.extract_highlights(scenes)jsonify({
'success': True,
'highlights': highlights }))()
generate_intro_tts = (lambda : data = request.get_json()if not data:
(jsonify({
'error': '요청 데이터가 없습니다.' }), 400)text = None.get('text', '')project_id = data.get('projectId', '')if not text or project_id:
(jsonify({
'error': 'text와 projectId가 필요합니다.' }), 400)intro_service = intro_serviceimport app.services.introresult = intro_service.generate_intro_tts(text = text, project_id = project_id, settings = data.get('ttsSettings'))jsonify(result))()
get_templates = (lambda : INTRO_TEMPLATES = INTRO_TEMPLATESimport app.services.introintro_type = request.args.get('type')if intro_type:
get_templates_by_type = get_templates_by_typeimport app.services.introtemplates = get_templates_by_type(intro_type)else:
templates = INTRO_TEMPLATESjsonify({
'success': True,
'templates': templates }))()
replace_intro_image = (lambda : data = request.get_json()if not data:
(jsonify({
'error': '요청 데이터가 없습니다.' }), 400)project_id = None.get('projectId')index = data.get('index')image_data_url = data.get('imageDataUrl', '')if not project_id:
(jsonify({
'error': 'projectId가 필요합니다.' }), 400)# WARNING: Decompyle incomplete
)()
update_intro_video = (lambda : data = request.get_json()if not data:
(jsonify({
'error': '요청 데이터가 없습니다.' }), 400)project_id = None.get('projectId')intro_index = data.get('introIndex')video_path = data.get('videoPath', '')if not project_id:
(jsonify({
'error': 'projectId가 필요합니다.' }), 400)# WARNING: Decompyle incomplete
)()
save_intro_data = (lambda : data = request.get_json()if not data:
(jsonify({
'error': '요청 데이터가 없습니다.' }), 400)project_id = None.get('projectId')intro_data = data.get('introData')# WARNING: Decompyle incomplete
)()
get_intro_data = (lambda project_id: intro_service = intro_serviceimport app.services.introresult = intro_service.get_intro_data(project_id)if result.get('success'):
jsonify(result)(None(result), 404))()
get_project_tts_settings = (lambda project_id: Project = Projectimport app.models.projectIntroTTSService = IntroTTSServiceimport app.services.intro.intro_tts_serviceproject = Project.query.get(project_id)if not project:
(jsonify({
'success': False,
'error': '프로젝트를 찾을 수 없습니다.' }), 404)settings = None.extract_project_tts_settings(project)jsonify({
'success': True,
'ttsSettings': settings.to_dict() }))()
