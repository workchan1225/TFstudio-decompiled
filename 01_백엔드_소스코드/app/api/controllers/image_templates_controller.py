# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_templates_controller.pyc (Python 3.11)

'''
Image Templates API

이미지 프롬프트 템플릿 관리 API 엔드포인트
'''
from flask import Blueprint, request, jsonify
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from app.services.image_template_service import ImageTemplateService
from app.models.image_prompt_template import ImagePromptTemplate
from app.api.utils.error_handler import handle_api_errors
image_templates_controller_bp = Blueprint('image_templates', __name__)
get_templates = (lambda : try:
template_type = request.args.get('type')active_only = request.args.get('active_only', 'true').lower() == 'true'templates = ImageTemplateService.get_templates(template_type, active_only)jsonify({
'success': True,
'templates': templates })except Exception:
e = Noneimport tracebacktraceback.print_exc()del eNoneNone = del e)()
get_template = (lambda template_id: template = ImageTemplateService.get_template_by_id(template_id)if not template:
(jsonify({
'success': False,
'error': '템플릿을 찾을 수 없습니다.' }), 404)None({
'success': True,
'template': template }))()
create_template = (lambda : print(f'''[CreateTemplate] Received request, content_length={request.content_length}''')try:
data = request.get_json()except Exception:
e = Noneprint(f'''[CreateTemplate] Failed to parse JSON: {e}''')del eNoneNone = del eif not data:
print('[CreateTemplate] No JSON data received')(jsonify({
'success': False,
'error': 'JSON 데이터가 없습니다' }), 400)if None.get('sampleImageBase64'):
img_size = len(data['sampleImageBase64'])print(f'''[CreateTemplate] Base64 image size: {img_size / 1024:.1f}KB''')required_fields = [
'type',
'name',
'systemPrompt']for field in required_fields:
if not data.get(field):
None, (jsonify({
'success': False,
'error': f'''{field}는 필수 항목입니다.''' }), 400)if data['type'] not in valid_types:
(jsonify({
'success': False,
'error': f'''유효하지 않은 타입입니다. 가능한 값: {', '.join(valid_types)}''' }), 400)try:
ImageTemplateService.create_template(data) = [
'character',
'scene',
'style',
'non_character'](jsonify({
'success': True,
'template': template }), 201)except Exception:
e = Nonedel eNoneNone = del e)()()
update_template = (lambda template_id:
