# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: editor_controller.pyc (Python 3.11)

'''
Editor API Endpoints

Handles Pro Editor state management for video projects.
'''
from flask import Blueprint, request, jsonify
from app.services.editor.editor_service import EditorService
from app.services.editor.manim_service import ManimService
editor_controller_bp = Blueprint('editor', __name__)
get_editor_state = (lambda project_id = None: try:
state = EditorService.get_state(project_id)(jsonify(state), 200)except Exception:
e = Nonedel eNoneNone = del e)()
save_editor_state = (lambda project_id = None: try:
data = request.get_json()if not data:
(jsonify({
'error': 'No data provided' }), 400)(is_valid, error_msg) = None.validate_state(data)if not is_valid:
(jsonify({
'error': error_msg }), 400)result = None.save_state(project_id, data)(jsonify(result), 200)except Exception:
e = Nonedel eNoneNone = del e)()
clear_editor_state = (lambda project_id = None: try:
result = EditorService.clear_state(project_id)(jsonify(result), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_editor_summary = (lambda project_id = None: try:
summary = EditorService.get_project_summary(project_id)(jsonify(summary), 200)except Exception:
e = Nonedel eNoneNone = del e)()
render_video = (lambda project_id = None: try:
result = EditorService.render_video(project_id)(jsonify(result), 200)except ValueError:
e = Nonedel eNoneNone = del eexcept Exception:
e = Nonedel eNoneNone = del e)()
get_render_status = (lambda project_id = None: try:
status = EditorService.get_render_status(project_id)(jsonify(status), 200)except Exception:
e = Nonedel eNoneNone = del e)()
generate_manim = (lambda : try:
data = request.get_json()if not data:
(jsonify({
'error': 'No data provided' }), 400)template_type = None.get('template', 'text_motion')params = data.get('params', { })video_url = ManimService.generate_animation(template_type, params)duration_map = {
'text_motion': 3,
'math_graph': 4,
'circle_animation': 2.5 }duration = duration_map.get(template_type, 3)(jsonify({
'status': 'success',
'url': video_url,
'duration': duration }), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_manim_templates = (lambda : try:
templates = ManimService.get_available_templates()(jsonify(templates), 200)except Exception:
e = Nonedel eNoneNone = del e)()
