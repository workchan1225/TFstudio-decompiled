# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subtitle_presets_controller.pyc (Python 3.11)

'''자막 스타일 프리셋 API - 프로젝트 독립적 CRUD'''
import logging
from flask import Blueprint, request, jsonify
from app import db
from app.models.subtitle_style_preset import SubtitleStylePreset
logger = logging.getLogger(__name__)
subtitle_presets_controller_bp = Blueprint('subtitle_presets', __name__)
get_all_presets = (lambda : try:
presets = SubtitleStylePreset.query.order_by(SubtitleStylePreset.name).all()((lambda .0: [ preset.to_dict() for preset in .0 ])(presets()), 200)
    except Exception:
        e = None
        logger.error(f'''Failed to get all presets: {e}''')
        del e
        return None
        None = 
        del e

)()
get_preset = (lambda preset_id: try:
preset = SubtitleStylePreset.query.get(preset_id)if not preset:
(jsonify({
'error': 'Preset not found' }), 404)(None(preset.to_dict()), 200)except Exception:
e = Nonelogger.error(f'''Failed to get preset {preset_id}: {e}''')del eNoneNone = del e)()
create_preset = (lambda : try:
data = request.jsonif not data or data.get('name'):
(jsonify({
'error': 'Name is required' }), 400)existing = None.query.filter_by(name = data['name']).first()if existing:
(jsonify({
'error': f'''Preset with name "{data['name']}" already exists''' }), 409)preset = None.from_dict(data)db.session.add(preset)db.session.commit()(jsonify(preset.to_dict()), 201)except Exception:
e = Nonedb.session.rollback()logger.error(f'''Failed to create preset: {e}''')del eNoneNone = del e)()
update_preset = (lambda preset_id: try:
preset = SubtitleStylePreset.query.get(preset_id)if not preset:
(jsonify({
'error': 'Preset not found' }), 404)data = None.jsonif not data:
(jsonify({
'error': 'No data provided' }), 400)if None in data and data['name'] != preset.name:
existing = SubtitleStylePreset.query.filter_by(name = data['name']).first()if existing:
(jsonify({
'error': f'''Preset with name "{data['name']}" already exists''' }), 409)None.update_from_dict(data)db.session.commit()(jsonify(preset.to_dict()), 200)except Exception:
e = Nonedb.session.rollback()logger.error(f'''Failed to update preset {preset_id}: {e}''')del eNoneNone = del e)()
delete_preset = (lambda preset_id: try:
preset = SubtitleStylePreset.query.get(preset_id)if not preset:
(jsonify({
'error': 'Preset not found' }), 404)preset_name = None.namedb.session.delete(preset)db.session.commit()(jsonify({
'message': f'''Preset "{preset_name}" deleted successfully''' }), 200)except Exception:
e = Nonedb.session.rollback()logger.error(f'''Failed to delete preset {preset_id}: {e}''')del eNoneNone = del e)()
