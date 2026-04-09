# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prompt_templates_controller.pyc (Python 3.11)

from flask import Blueprint, request, jsonify
from app import db
from app.models.prompt_template import PromptTemplate
from app.api.utils.error_handler import handle_api_errors
import uuid
prompt_templates_controller_bp = Blueprint('prompt_templates', __name__)
get_templates = (lambda : template_type = request.args.get('type')include_inactive = request.args.get('include_inactive', 'false').lower() == 'true'query = PromptTemplate.queryif template_type:
query = query.filter_by(type = template_type)if not include_inactive:
query = query.filter_by(is_active = True)templates = query.order_by(PromptTemplate.is_default.desc(), PromptTemplate.updated_at.desc()).all()('templates'({
(lambda .0: [ template.to_dict() for template in .0 ]): templates() }), 200)
)()
get_template = (lambda template_id: template = PromptTemplate.query.get(template_id)if not template:
(jsonify({
'error': 'Template not found' }), 404)(None(template.to_dict()), 200))()
create_template = (lambda : if not request.get_json():
data = { }if not data.get('type') and data.get('name') or data.get('systemPrompt'):
(jsonify({
'error': 'Missing required fields: type, name, systemPrompt' }), 400)if None['type'] not in ('topic', 'outline', 'script', 'image'):
(jsonify({
'error': 'Invalid type. Must be one of: topic, outline, script, image' }), 400)if None.get('isDefault', False):
PromptTemplate.query.filter_by(type = data['type'], is_default = True).update({
'is_default': False })template = PromptTemplate(id = str(uuid.uuid4()), type = data['type'], name = data['name'], description = data.get('description', ''), system_prompt = data['systemPrompt'], user_prompt_template = data.get('userPromptTemplate', ''), parameters = data.get('parameters', { }), is_default = data.get('isDefault', False), is_active = data.get('isActive', True))db.session.add(template)db.session.commit()(jsonify(template.to_dict()), 201))()()
update_template = (lambda template_id: template = PromptTemplate.query.get(template_id)if not template:
(jsonify({
'error': 'Template not found' }), 404)data = None.get_json()if not data.get('isDefault', False) and template.is_default:
PromptTemplate.query.filter_by(type = template.type, is_default = True).update({
'is_default': False })if 'name' in data:
template.name = data['name']if 'description' in data:
template.description = data['description']if 'systemPrompt' in data:
template.system_prompt = data['systemPrompt']if 'userPromptTemplate' in data:
template.user_prompt_template = data['userPromptTemplate']if 'parameters' in data:
template.parameters = data['parameters']if 'isDefault' in data:
template.is_default = data['isDefault']if 'isActive' in data:
template.is_active = data['isActive']db.session.commit()(jsonify(template.to_dict()), 200))()()
delete_template = (lambda template_id: template = PromptTemplate.query.get(template_id)if not template:
(jsonify({
'error': 'Template not found' }), 404)if None.is_default:
(jsonify({
'error': 'Cannot delete default template. Please set another template as default first.' }), 400)None.session.delete(template)db.session.commit()(jsonify({
'message': 'Template deleted successfully' }), 200))()()
duplicate_template = (lambda template_id: original = PromptTemplate.query.get(template_id)if not original:
(jsonify({
'error': 'Template not found' }), 404)duplicate = None(id = str(uuid.uuid4()), type = original.type, name = f'''{original.name} (복사본)''', description = original.description, system_prompt = original.system_prompt, user_prompt_template = original.user_prompt_template, parameters = original.parameters.copy() if original.parameters else { }, is_default = False, is_active = original.is_active)db.session.add(duplicate)db.session.commit()(jsonify(duplicate.to_dict()), 201))()()
set_default_template = (lambda template_id: template = PromptTemplate.query.get(template_id)if not template:
(jsonify({
'error': 'Template not found' }), 404)None.query.filter_by(type = template.type, is_default = True).update({
'is_default': False })template.is_default = Truedb.session.commit()(jsonify(template.to_dict()), 200))()()
get_default_template = (lambda template_type: if template_type not in ('topic', 'outline', 'script', 'image'):
(jsonify({
'error': 'Invalid type' }), 400)template = None.get_default_template(template_type)if not template:
(jsonify({
'error': f'''No default template found for type: {template_type}''' }), 404)(None(template.to_dict()), 200))()
get_active_templates = (lambda template_type: if template_type not in ('topic', 'outline', 'script', 'image'):
(jsonify({
'error': 'Invalid type' }), 400)templates = None.get_active_templates(template_type)('templates'({
(lambda .0: [ template.to_dict() for template in .0 ]): templates() }), 200)
)()
