# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_controller.pyc (Python 3.11)

import logging
from flask import Blueprint, jsonify, request
from app.services.project_assistant_service import ProjectAssistantService
logger = logging.getLogger(__name__)
assistant_controller_bp = Blueprint('assistant', __name__)
chat_with_project_assistant = (lambda : try:
if not request.get_json(silent = True):
data = { }if not data.get('projectId') and str('').strip():
project_id = Noneif not data.get('scope') and str('').strip().lower():
scope = Nonemessages = data.get('messages')if not data.get('routeContext'):
route_context = { }if not data.get('projectContext'):
project_context = { }if not data.get('pageContext'):
page_context = { }if scope and scope not in ProjectAssistantService.SUPPORTED_SCOPES:
supported_scopes = ', '.join(sorted(ProjectAssistantService.SUPPORTED_SCOPES))(jsonify({
'error': f'''scope must be one of: {supported_scopes}''' }), 400)if not None(messages, list):
(jsonify({
'error': 'messages must be an array' }), 400)if not None and isinstance(route_context, dict):
(jsonify({
'error': 'routeContext must be an object' }), 400)if not None and isinstance(project_context, dict):
(jsonify({
'error': 'projectContext must be an object' }), 400)if not None and isinstance(page_context, dict):
(jsonify({
'error': 'pageContext must be an object' }), 400)response = None.chat(project_id = project_id, scope = scope, messages = messages, route_context = route_context, project_context = project_context, page_context = page_context)(jsonify(response), 200)except LookupError:
exc = Nonedel excNoneNone = del excexcept ValueError:
exc = Nonedel excNoneNone = del excexcept Exception:
exc = Nonelogger.exception('[AssistantController] Unexpected error: %s', exc)del excNoneNone = del exc)()
