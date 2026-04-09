# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: media_controller.pyc (Python 3.11)

"""
Media Controller (Clean Architecture Version)

Handles media library operations: listing, filtering, uploading, syncing.
Replaces v1 media.py.

Registration in app/__init__.py:
    from app.api.controllers import media_controller_bp
    app.register_blueprint(media_controller_bp, url_prefix='/api/media')
"""
from flask import Blueprint, request, jsonify
from pathlib import Path
import logging
logger = logging.getLogger(__name__)
media_controller_bp = Blueprint('media', __name__)
get_media = (lambda : MediaService = MediaServiceimport app.services.media_servicetry:
project_id = request.args.get('projectId')media_type = request.args.get('mediaType', 'all')search = request.args.get('search')sort_by = request.args.get('sortBy', 'created_at')sort_order = request.args.get('sortOrder', 'desc')page = int(request.args.get('page', 1))per_page = int(request.args.get('perPage', 50))(media_list, total_count, stats) = MediaService.get_all_media(project_id = project_id, media_type = media_type, search = search, sort_by = sort_by, sort_order = sort_order, page = page, per_page = per_page)((lambda .0: [ m.to_dict() for m in .0 ])({
            'items': media_list(),
            'totalCount': total_count,
            'page': page,
            'perPage': per_page,
            'totalPages': (total_count + per_page - 1) // per_page,
            'stats': stats }), 200)
    except Exception:
        e = None
        logger.error(f'''Error getting media: {e}''')
        import traceback
        traceback.print_exc()
        del e
        return None
        None = 
        del e

)()
get_projects_with_media = (lambda : MediaService = MediaServiceimport app.services.media_servicetry:
projects = MediaService.get_projects_with_media()(jsonify({
'projects': projects }), 200)except Exception:
e = Nonelogger.error(f'''Error getting projects with media: {e}''')del eNoneNone = del e)()
get_media_stats = (lambda : MediaService = MediaServiceimport app.services.media_servicetry:
project_id = request.args.get('projectId')(_, _, stats) = MediaService.get_all_media(project_id = project_id, page = 1, per_page = 1)(jsonify(stats), 200)except Exception:
e = Nonelogger.error(f'''Error getting media stats: {e}''')del eNoneNone = del e)()
get_media_detail = (lambda media_id: try:
Media = Mediaimport app.models.projectmedia = Media.query.get(media_id)if not media:
(jsonify({
'error': 'Media not found' }), 404)(None(media.to_dict()), 200)except Exception:
e = Nonelogger.error(f'''Error getting media detail: {e}''')del eNoneNone = del e)()
update_media = (lambda media_id: MediaService = MediaServiceimport app.services.media_servicetry:
if not request.get_json():
data = { }media = MediaService.update_media(media_id, data)if not media:
(jsonify({
'error': 'Media not found' }), 404)(None(media.to_dict()), 200)except Exception:
e = Nonelogger.error(f'''Error updating media: {e}''')del eNoneNone = del e)()
delete_media = (lambda media_id: MediaService = MediaServiceimport app.services.media_servicetry:
delete_file = request.args.get('deleteFile', 'false').lower() == 'true'success = MediaService.delete_media(media_id, delete_file = delete_file)if not success:
(jsonify({
'error': 'Media not found' }), 404)Noneexcept Exception:
e = Nonelogger.error(f'''Error deleting media: {e}''')del eNoneNone = del e)()
get_sync_status = (lambda : MediaService = MediaServiceimport app.services.media_servicetry:
status = MediaService.check_sync_status()(jsonify(status), 200)except Exception:
e = Nonelogger.error(f'''Error checking sync status: {e}''')import tracebacktraceback.print_exc()del eNoneNone = del e)()
sync_all_media = (lambda : MediaService = MediaServiceimport app.services.media_servicetry:
results = MediaService.sync_all_projects()(jsonify({
'message': f'''{results['syncedCount']}개 추가, {results['cleanedCount']}개 정리됨''',
'syncedCount': results['syncedCount'],
'cleanedCount': results['cleanedCount'] }), 200)except Exception:
e = Nonelogger.error(f'''Error syncing all media: {e}''')import tracebacktraceback.print_exc()del eNoneNone = del e)()
sync_project_media = (lambda project_id: MediaService = MediaServiceimport app.services.media_servicetry:
synced_count = MediaService.sync_project_media(project_id)(jsonify({
'message': f'''{synced_count} media files synced''',
'syncedCount': synced_count,
'projectId': project_id }), 200)except Exception:
e = Nonelogger.error(f'''Error syncing project media: {e}''')del eNoneNone = del e)()
open_folder = (lambda : Path = Pathimport pathlibopen_folder_foreground = open_folder_foregroundimport app.utils.folder_utilsimport systry:
if not request.get_json():
data = { }file_path = data.get('filePath')is_absolute = data.get('isAbsolute', False)if not file_path:
(jsonify({
'error': 'filePath is required' }), 400)if None.platform == 'win32':
file_path = file_path.replace('/', '\\')if is_absolute:
full_path = Path(file_path)else:
get_data_path = get_data_pathimport app.config.pathsdata_dir = get_data_path()full_path = data_dir / file_pathtry:
full_path = full_path.resolve()try:
passexcept Exception:
try:
passtry:
if not full_path.exists():
if not full_path.suffix:
try:
full_path.mkdir(parents = True, exist_ok = True)logger.info(f'''[open-folder] Created missing folder: {full_path}''')try:
passexcept Exception:
mkdir_err = Nonelogger.warning(f'''[open-folder] Cannot create folder: {full_path} - {mkdir_err}''')try:
del mkdir_errNoneNone = del mkdir_errtry:
logger.warning(f'''[open-folder] File not found: {full_path}''')(jsonify({
'error': f'''File not found: {full_path}''' }), 404)try:
is_directory = full_path.is_dir()(jsonify({
'success': True,
'path': str(full_path) }), 200)except Exception:
e = Nonelogger.error(f'''Error opening folder: {e}''', exc_info = True)del eNoneNone = del e)()
upload_file = (lambda : import osimport uuidimport mimetypesdatetime = datetimeimport datetimedb = dbimport appMedia = Mediaimport app.models.projectMediaService = MediaServiceimport app.services.media_serviceif 'file' not in request.files:
(jsonify({
'error': 'No file provided' }), 400)file = None.files['file']if file.filename == '':
(jsonify({
'error': 'No file selected' }), 400)try:
media_type = MediaService.get_media_type(file.filename)if not media_type:
(jsonify({
'error': 'Unsupported file type' }), 400)get_data_path = get_data_pathimport app.config.pathsdata_dir = get_data_path()upload_dir = data_dir / 'media' / 'global'upload_dir.mkdir(parents = True, exist_ok = True)ext = Path(file.filename).suffixnew_filename = f'''{uuid.uuid4()}{ext}'''file_path = upload_dir / new_filenamerelative_path = f'''media/global/{new_filename}'''file.save(str(file_path))file_size = file_path.stat().st_sizemedia = Media(id = str(uuid.uuid4()), project_id = None, media_type = media_type, file_path = relative_path, file_name = file.filename, file_size = file_size, mime_type = mimetypes.guess_type(file.filename)[0], description = request.form.get('description'), tags = request.form.get('tags'), created_at = datetime.utcnow())if media_type == 'image':
try:
Image = Imageimport PILimg = Image.open(file_path)(media.width, media.height) = img.sizetry:
None(None, None)with None:
if not None:
try:
try:
try:
passexcept Exception:
try:
passtry:
db.session.add(media)db.session.commit()(jsonify(media.to_dict()), 201)except Exception:
e = Nonelogger.error(f'''Error uploading file: {e}''')import tracebacktraceback.print_exc()del eNoneNone = del e)()
overwrite_media_file = (lambda : import reSceneImageStorage = SceneImageStorageimport app.utils.image_storagetry:
if not request.get_json():
data = { }target_path = data.get('targetPath')image_data_url = data.get('imageDataUrl')if not target_path:
(jsonify({
'error': 'targetPath is required' }), 400)if not None:
(jsonify({
'error': 'imageDataUrl is required' }), 400)normalized_path = None.replace('\\', '/')if '..' in normalized_path:
logger.warning(f'''[Media Overwrite] Path traversal attempt blocked: {target_path}''')(jsonify({
'error': 'Invalid path' }), 400)if not None.startswith('projects/'):
(jsonify({
'error': 'Invalid targetPath format' }), 400)path_parts = None.split('/')if len(path_parts) < 2:
(jsonify({
'error': 'Invalid targetPath format' }), 400)project_id = None[1]if not re.match('^[a-f0-9-]{36}$', project_id, re.IGNORECASE):
logger.warning(f'''[Media Overwrite] Invalid project ID format: {project_id}''')(jsonify({
'error': 'Invalid project ID format' }), 400)storage = SceneImageStorage(project_id)success = storage.overwrite_media_file(normalized_path, image_data_url)if not success:
(jsonify({
'error': 'Failed to overwrite file' }), 500)(None({
'success': True,
'path': normalized_path }), 200)except Exception:
e = Nonelogger.error(f'''Error overwriting media file: {e}''', exc_info = True)del eNoneNone = del e)()
delete_media_file = (lambda : import retry:
if not request.get_json():
data = { }target_path = data.get('targetPath')if not target_path:
(jsonify({
'error': 'targetPath is required' }), 400)normalized_path = None.replace('\\', '/')if '..' in normalized_path:
(jsonify({
'error': 'Invalid path' }), 400)if not None.startswith('projects/'):
(jsonify({
'error': 'Invalid targetPath format' }), 400)path_parts = None.split('/')if len(path_parts) < 2:
(jsonify({
'error': 'Invalid targetPath format' }), 400)project_id = None[1]if not re.match('^[a-f0-9-]{36}$', project_id, re.IGNORECASE):
(jsonify({
'error': 'Invalid project ID format' }), 400)get_data_path = get_data_pathimport app.config.pathsfull_path = get_data_path() / normalized_pathtry:
resolved_path = full_path.resolve()data_dir_resolved = get_data_path().resolve()if not str(resolved_path).startswith(str(data_dir_resolved)):
(jsonify({
'error': 'Invalid path' }), 400)except Exception:
try:
try:
if not full_path.exists():
(jsonify({
'success': True,
'message': 'File already deleted' }), 200)None, (jsonify({
'error': 'Path resolution failed' }), 400).unlink()logger.info(f'''delete_media_file: deleted {normalized_path}''')(jsonify({
'success': True,
'path': normalized_path }), 200)except Exception:
logger.error(f'''Error deleting media file: {e}''', exc_info = True)del eNoneNone = del e)()
