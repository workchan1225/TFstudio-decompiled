# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: overlay_controller.pyc (Python 3.11)

'''
Overlay API Controller
오버레이 관련 API 엔드포인트
'''
import logging
from flask import Blueprint, request, jsonify, send_file
from app.services.overlay_library_service import get_overlay_library_service
logger = logging.getLogger(__name__)
overlay_controller_bp = Blueprint('overlay', __name__)
list_overlays = (lambda : try:
type_filter = request.args.get('type')service = get_overlay_library_service()overlays = service.list_overlays(type_filter = type_filter)jsonify({
'success': True,
'data': overlays,
'count': len(overlays) })except Exception:
e = Nonelogger.error(f'''Failed to list overlays: {e}''')del eNoneNone = del e)()
get_overlay = (lambda overlay_id: try:
service = get_overlay_library_service()overlay = service.get_overlay(overlay_id)if not overlay:
(jsonify({
'success': False,
'error': f'''Overlay not found: {overlay_id}''' }), 404)None({
'success': True,
'data': overlay })except Exception:
e = Nonelogger.error(f'''Failed to get overlay {overlay_id}: {e}''')del eNoneNone = del e)()
add_overlay = (lambda : try:
if 'file' not in request.files:
(jsonify({
'success': False,
'error': 'No file provided' }), 400)file = None.files['file']name = request.form.get('name', 'Custom Overlay')overlay_type = request.form.get('type', 'custom')blend_mode = request.form.get('blendMode', 'screen')opacity = float(request.form.get('opacity', 0.5))tags_str = request.form.get('tags', '')tags = tags_str.split(',')()import tempfileimport ostmp = tempfile.NamedTemporaryFile(delete = False, suffix = os.path.splitext(file.filename)[1])file.save(tmp.name)tmp_path = tmp.nametry:
None(None, None)with None:
if not (lambda .0: pass# WARNING: Decompyle incomplete
):
                
                try:
                    
                    try:
                        
                        try:
                            service = get_overlay_library_service()
                            overlay = service.add_overlay(file_path = tmp_path, name = name, overlay_type = overlay_type, blend_mode = blend_mode, opacity = opacity, tags = tags)
                            
                            try:
                                if os.path.exists(tmp_path):
                                    os.unlink(tmp_path)
                                    return (jsonify({
                                        'success': True,
                                        'data': overlay }), 201)
                                if os.path.exists(tmp_path):
                                    os.unlink(tmp_path)
                                
                                try:
                                    pass
                                except ValueError:
                                    e = None
                                    del e
                                    return None
                                    None = 
                                    del e
                                    except Exception:
                                        e = None
                                        logger.error(f'''Failed to add overlay: {e}''')
                                        del e
                                        return None
                                        None = 
                                        del e







)()
delete_overlay = (lambda overlay_id: try:
service = get_overlay_library_service()success = service.delete_overlay(overlay_id)if not success:
(jsonify({
'success': False,
'error': 'Failed to delete overlay (may be builtin or not found)' }), 400)None({
'success': True,
'message': f'''Overlay {overlay_id} deleted''' })except Exception:
e = Nonelogger.error(f'''Failed to delete overlay {overlay_id}: {e}''')del eNoneNone = del e)()
get_overlay_file = (lambda overlay_id: try:
service = get_overlay_library_service()file_path = service.get_overlay_file_path(overlay_id)if not file_path or file_path.exists():
(jsonify({
'success': False,
'error': f'''Overlay file not found: {overlay_id}''' }), 404)ext = None.suffix.lower()mime_types = {
'.webm': 'video/webm',
'.mp4': 'video/mp4',
'.gif': 'image/gif' }mimetype = mime_types.get(ext, 'application/octet-stream')send_file(file_path, mimetype = mimetype)except Exception:
e = Nonelogger.error(f'''Failed to get overlay file {overlay_id}: {e}''')del eNoneNone = del e)()
