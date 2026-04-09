# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_service.pyc (Python 3.11)

'''
ImageService - 이미지 및 비디오 업로드 관리 서비스
'''
import json
import re
import shutil
import time
from pathlib import Path
from typing import List, Dict, Any
from sqlalchemy.orm.attributes import flag_modified
from app.models.project import Project
from app.utils.file_paths import ProjectPaths
from app.utils.uploaded_media_metadata import normalize_uploaded_media_binding_metadata, normalize_uploaded_media_source_metadata
from app import db
DEFAULT_IMAGE_DURATION = 3
MIN_IMAGE_DURATION = 0.1

class ImageService:
    '''
    이미지 및 비디오 미디어 업로드 관리 서비스

    책임:
    - 파일 업로드 및 저장
    - 썸네일 처리
    - 미디어 메타데이터 관리
    - 파일 시스템 정리
    '''
    upload_media_files = (lambda project, files = None, thumbnails = None, durations = staticmethod, types = (None,), source_metadata = ('project', Project, 'files', List[Any], 'thumbnails', List[Any], 'durations', List[float], 'types', List[str], 'source_metadata', List[Dict[(str, Any)]] | None, 'return', Dict[(str, Any)]): project_id = project.iduploaded_media = []saved_files = []print(f'''[ImageService] Received {len(files)} files and {len(thumbnails)} thumbnails''')print(f'''[ImageService] Durations: {durations}''')print(f'''[ImageService] Types: {types}''')source_metadata = source_metadata if isinstance(source_metadata, list) else []paths = ProjectPaths(project_id)try:
paths.ensure_directories()except OSError:
e = Noneraise RuntimeError(f'''디렉토리 생성 실패: {e}''')e = Nonedel eif not project.video_settings:
project.video_settings = { }settings = dict(project.video_settings) if project.video_settings else { }existing_images = settings.get('uploadedImages', [])start_index = len(existing_images)try:
for i, file in enumerate(files):
if file.filename:
media_type = types[i] if i < len(types) else 'image'file_ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''timestamp = int(time.time() * 1000)file_index = start_index + ioriginal_name = Path(file.filename).nameoriginal_stem = Path(original_name).stemchapter_scene_match = re.match('^(ch\\d+_\\d+)(?:_|$)', original_stem, re.IGNORECASE)chapter_scene_prefix = chapter_scene_match.group(1).lower() if chapter_scene_match else Noneif chapter_scene_prefix:
filename = f'''{chapter_scene_prefix}_{timestamp}_{file_index}.{file_ext}'''else:
filename = f'''{timestamp}_{file_index}.{file_ext}'''file_path = paths.image_path(filename)file.save(str(file_path))saved_files.append(file_path)print(f'''[ImageService] Saved file {i}: {file_path}''')try:
passexcept (OSError, IOError):
e = Noneraise RuntimeError(f'''파일 저장 실패 ({file.filename}): {e}''')e = Nonedel etry:
default_duration = 5 if media_type == 'video' else DEFAULT_IMAGE_DURATIONfrontend_duration = durations[i] if i < len(durations) else default_durationrelative_path_str = paths.relative_path(file_path)print(f'''[ImageService] Saved path: absolute={file_path}, relative={relative_path_str}''')media_info = {
'path': relative_path_str,
'duration': duration,
'type': media_type,
'order': file_index }media_info.update(normalize_uploaded_media_source_metadata(source_metadata[i] if i < len(source_metadata) and isinstance(source_metadata[i], dict) else { }, relative_path_str))media_info.update(normalize_uploaded_media_binding_metadata(source_metadata[i] if i < len(source_metadata) and isinstance(source_metadata[i], dict) else { }))if media_type == 'video' and i < len(thumbnails):
thumbnail_file = thumbnails[i]if thumbnail_file.filename:
thumbnail_path = paths.image_path(f'''{timestamp}_{file_index}_thumbnail.jpg''')thumbnail_file.save(str(thumbnail_path))saved_files.append(thumbnail_path)media_info['thumbnailPath'] = paths.relative_path(thumbnail_path)print(f'''[ImageService] Saved thumbnail {i}: {thumbnail_path}''')try:
passexcept (OSError, IOError):
e = Noneprint(f'''[ImageService] WARNING: 썸네일 저장 실패 (무시됨): {e}''')try:
e = Nonedel ee = Nonedel etry:
uploaded_media.append(media_info)continueexcept RuntimeError:
ImageService._cleanup_saved_files(saved_files)raise all_images = existing_images + uploaded_mediasettings['uploadedImages'] = all_imagesproject.video_settings = settingsflag_modified(project, 'video_settings')ImageService._invalidate_image_timeline(project)ImageService._update_progress(project, has_images = len(all_images) > 0)if start_index == 0 and uploaded_media:
SyncService = SyncServiceimport app.services.sync_servicefirst_path = uploaded_media[0]['path']SyncService.set_project_thumbnail_from_image(project, first_path)print(f'''[ImageService] Auto-set thumbnail for project {project_id}: {first_path}''')try:
db.session.commit()except Exception:
e = Nonedb.session.rollback()ImageService._cleanup_saved_files(saved_files)raise RuntimeError(f'''데이터베이스 저장 실패: {e}''')e = Nonedel e{
'status': (lambda .0: [ img['path'] for img in .0 ]),
            'imagePaths': uploaded_media(),
            'totalCount': len(all_images) }
)()
    _cleanup_saved_files = (lambda saved_files = None: for file_path in saved_files:
if file_path.exists():
file_path.unlink()print(f'''[ImageService] Cleaned up: {file_path}''')except Exception:
e = Noneprint(f'''[ImageService] WARNING: 파일 정리 실패 ({file_path}): {e}''')e = Nonedel econtinuee = Nonedel eNone)()
    clear_all_media = (lambda project = None: project_id = project.idprint(f'''[ImageService] Clearing all media for project: {project_id}''')deleted_count = 0failed_count = 0if project.video_settings and project.video_settings.get('uploadedImages'):
uploaded_media = project.video_settings.get('uploadedImages', [])print(f'''[ImageService] Deleting {len(uploaded_media)} media files individually''')paths = ProjectPaths(project_id)for media in uploaded_media:
for key in ('path', 'thumbnailPath'):
target_path = media.get(key) if isinstance(media, dict) else Noneif not target_path:
continueabs_path = Path(target_path)if not abs_path.is_absolute():
abs_path = paths.data_dir / target_pathif abs_path.exists() and abs_path.is_file():
abs_path.unlink()deleted_count += 1print(f'''[ImageService] Deleted file: {abs_path}''')except PermissionError:
failed_count += 1print(f'''[ImageService] WARNING: Failed to delete locked file: {target_path}''')continueexcept Exception:
e = Nonefailed_count += 1print(f'''[ImageService] WARNING: Failed to delete {target_path}: {e}''')e = Nonedel econtinuee = Nonedel eprint(f'''[ImageService] Deleted {deleted_count} files, {failed_count} failed''')try:
paths = ProjectPaths(project_id)images_dir = paths.images_dir()if images_dir.exists() and images_dir.is_dir():
for f in images_dir.iterdir():
if f.is_file() and f.suffix.lower() in ImageService.SUPPORTED_IMAGE_EXTENSIONS and ImageService.AI_SCENE_IMAGE_PATTERN.match(f.name):
f.unlink()deleted_count += 1try:
continueexcept Exception:
e = Noneprint(f'''[ImageService] WARNING: Failed to delete unregistered file {f.name}: {e}''')try:
e = Nonedel econtinuee = Nonedel etry:
continueexcept Exception:
e = Noneprint(f'''[ImageService] WARNING: Failed to scan images dir for cleanup: {e}''')e = Nonedel eexcept:
e = Nonedel eif not project.video_settings:
project.video_settings = { }settings = dict(project.video_settings) if project.video_settings else { }settings['uploadedImages'] = []project.video_settings = settingsflag_modified(project, 'video_settings')ImageService._invalidate_image_timeline(project)ImageService._update_progress(project, has_images = False, has_image_sync = False)try:
db.session.commit()except Exception:
e = Nonedb.session.rollback()raise RuntimeError(f'''데이터베이스 저장 실패: {e}''')e = Nonedel e{
'status': 'success',
'message': 'Images cleared successfully' })()
    clear_images_only = (lambda project = None: project_id = project.idprint(f'''[ImageService] Clearing image-only media for project: {project_id}''')if not project.video_settings:
project.video_settings = { }settings = dict(project.video_settings) if project.video_settings else { }uploaded_media = settings.get('uploadedImages', [])if not uploaded_media:
{
'status': 'success',
'message': 'No media to clear',
'removedImageCount': 0,
'keptVideoCount': 0,
'totalCount': 0 }kept_media = Noneremoved_images = []for item in uploaded_media:
media_type = item.get('type', 'image')if media_type == 'video':
kept_media.append(item)continueremoved_images.append(item)print(f'''[ImageService] Removing {len(removed_images)} image items, keeping {len(kept_media)} videos''')paths = ProjectPaths(project_id)for media in removed_images:
for key in ('path', 'thumbnailPath'):
target_path = media.get(key)if not target_path:
continueabs_path = Path(target_path)if not abs_path.is_absolute():
abs_path = paths.data_dir / target_pathif abs_path.exists() and abs_path.is_file():
abs_path.unlink()print(f'''[ImageService] Deleted {key}: {abs_path}''')except Exception:
e = Noneprint(f'''[ImageService] WARNING: Failed to delete {key} ({target_path}): {e}''')e = Nonedel econtinuee = Nonedel eif project.thumbnail and removed_images:
thumbnail_relative = project.thumbnailif thumbnail_relative.startswith('/data/'):
thumbnail_relative = thumbnail_relative[6:]elif thumbnail_relative.startswith('data/'):
thumbnail_relative = thumbnail_relative[5:]removed_paths = removed_images()for removed_path in removed_paths:
if removed_path:
if removed_path == thumbnail_relative or thumbnail_relative.endswith(removed_path):
print(f'''[ImageService] Clearing thumbnail reference (deleted image): {project.thumbnail}''')project.thumbnail = None(lambda .0: pass# WARNING: Decompyle incomplete
)
                                
                                for idx, item in enumerate(kept_media):
                                    item['order'] = idx
                                    settings['uploadedImages'] = kept_media
                                    project.video_settings = settings
                                    flag_modified(project, 'video_settings')
                                    ImageService._invalidate_image_timeline(project)
                                    ImageService._update_progress(project, has_images = len(kept_media) > 0, has_image_sync = False)
                                    
                                    try:
                                        db.session.commit()
                                    except Exception:
                                        e = None
                                        db.session.rollback()
                                        raise RuntimeError(f'''데이터베이스 저장 실패: {e}''')
                                        e = None
                                        del e

                                    return {
                                        'status': 'success',
                                        'message': 'Image media cleared successfully',
                                        'removedImageCount': len(removed_images),
                                        'keptVideoCount': len(kept_media),
                                        'totalCount': len(kept_media) }
)()
    update_media_list = (lambda project = None, new_images = None: pass# WARNING: Decompyle incomplete
)()
    _invalidate_image_timeline = (lambda project = None: if project.video_settings or 'imageTimeline' in project.video_settings:
settings = dict(project.video_settings)del settings['imageTimeline']project.video_settings = settingsflag_modified(project, 'video_settings')print('[ImageService] Invalidated image timeline')NoneNone)()
    _update_progress = (lambda project = None, has_images = None, has_image_sync = staticmethod: if not project.direct_progress:
project.direct_progress = { }progress = dict(project.direct_progress)# WARNING: Decompyle incomplete
)()
    update_image_effects = (lambda project = None, effect = None, zoom_level = staticmethod, pan_direction = ('static', 1.2, 'left_to_right', 'medium'), speed = ('project', Project, 'effect', str, 'zoom_level', float, 'pan_direction', str, 'speed', str, 'return', Dict[(str, Any)]): effect_settings = {
'effect': effect,
'zoomStart': 1,
'zoomEnd': zoom_level,
'panDirection': pan_direction,
'speed': speed }ImageService.update_image_effects_v2(project, effect_settings))()
    update_image_effects_v2 = (lambda project = None, effect_settings = None: if not project.video_settings:
project.video_settings = { }settings = dict(project.video_settings) if project.video_settings else { }settings['imageEffects'] = effect_settingssettings['imagePosition'] = effect_settingsproject.video_settings = settingsflag_modified(project, 'video_settings')ImageService._update_progress(project, has_image_sync = True)try:
db.session.commit()except Exception:
e = Nonedb.session.rollback()raise RuntimeError(f'''데이터베이스 저장 실패: {e}''')e = Nonedel e{
'status': 'success',
'imageEffects': effect_settings })()
    update_image_timeline = (lambda project = None, mode = None, fixed_duration = staticmethod, total_video_duration = ('equal', None, None, None), segments = ('project', Project, 'mode', str, 'fixed_duration', float, 'total_video_duration', float, 'segments', list, 'return', Dict[(str, Any)]): if not project.video_settings:
project.video_settings = { }settings = dict(project.video_settings) if project.video_settings else { }if not segments:
settings['imageTimeline'] = {
'mode': mode,
'fixedDuration': fixed_duration,
'totalVideoDuration': total_video_duration,
'segments': [] }project.video_settings = settingsflag_modified(project, 'video_settings')ImageService._update_progress(project, has_image_sync = True)try:
db.session.commit()except Exception:
e = total_video_durationdb.session.rollback()raise RuntimeError(f'''데이터베이스 저장 실패: {e}''')e = Nonedel e{
'status': 'success',
'imageTimeline': settings['imageTimeline'] })()
    get_image_timeline = (lambda project = None: if project.video_settings or 'imageTimeline' not in project.video_settings:
{
'imageTimeline': None }{
None: project.video_settings['imageTimeline'] })()
    rename_media_by_order = (lambda project = None, chapter_scene_map = None: get_data_path = get_data_pathimport app.config.pathsproject_id = project.idprint(f'''[ImageService] Renaming media by order for project: {project_id}''')if not project.video_settings:
{
'status': 'error',
'message': 'No video settings' }settings = dict(project.video_settings) if None.video_settings else { }uploaded_media = settings.get('uploadedImages', [])if not uploaded_media:
{
'status': 'success',
'message': 'No media to rename',
'renamedCount': 0 }data_dir = get_data_path()paths = ProjectPaths(project_id)images_dir = paths.images_dir()if not chapter_scene_map:
chapter_scene_map = []media_count = len(uploaded_media)scenes_per_chapter = max(1, min(3, (media_count + 1) // 2))current_chapter = 1scene_in_chapter = 1for i in range(media_count):
chapter_scene_map.append({
'chapter': current_chapter,
'scene': scene_in_chapter })scene_in_chapter += 1if scene_in_chapter > scenes_per_chapter:
scene_in_chapter = 1current_chapter += 1renamed_count = 0updated_media = []temp_renames = []for idx, media in enumerate(uploaded_media):
old_path = media.get('path', '')media_type = media.get('type', 'image')if media_type == 'video':
print(f'''[ImageService] Skipping video (keeping original name): {old_path}''')updated_item = dict(media)updated_item['order'] = idxupdated_media.append(updated_item)continueif not old_path:
updated_media.append(media)continueold_full_path = data_dir / old_pathif not old_full_path.exists():
print(f'''[ImageService] File not found: {old_full_path}''')updated_media.append(media)continueext = old_full_path.suffixtemp_filename = f'''_temp_rename_{idx}_{time.time_ns()}{ext}'''temp_path = images_dir / temp_filenameshutil.move(str(old_full_path), str(temp_path))temp_renames.append({
'idx': idx,
'media': media,
'temp_path': temp_path,
'ext': ext })except Exception:
e = Noneprint(f'''[ImageService] Error moving to temp: {e}''')updated_media.append(media)e = Nonedel econtinuee = Nonedel efor item in temp_renames:
idx = item['idx']media = item['media']temp_path = item['temp_path']ext = item['ext']timestamp = int(time.time() * 1000)new_filename = f'''ch{ch}_{sc}_{timestamp}{ext}'''new_path = images_dir / new_filenameshutil.move(str(temp_path), str(new_path))relative_path = str(new_path.relative_to(data_dir)).replace('\\', '/')updated_item = dict(media)updated_item['path'] = relative_pathupdated_item['order'] = idxupdated_media.append(updated_item)renamed_count += 1print(f'''[ImageService] Renamed: {media.get('path')} -> {relative_path}''')except Exception:
e = Noneprint(f'''[ImageService] Error renaming: {e}''')updated_media.append(media)e = Nonedel econtinuee = Nonedel esettings['uploadedImages'] = updated_mediaproject.video_settings = dict(settings)flag_modified(project, 'video_settings')try:
db.session.commit()except Exception:
e = Nonedb.session.rollback()raise RuntimeError(f'''데이터베이스 저장 실패: {e}''')e = Nonedel eprint(f'''[ImageService] Renamed {renamed_count} files'''){
'status': 'success',
'renamedCount': renamed_count,
'totalCount': len(uploaded_media) })()
    AI_SCENE_IMAGE_PATTERN = re.compile('^ch\\d+_(?:sc)?\\d+', re.IGNORECASE)
    SUPPORTED_IMAGE_EXTENSIONS = {
        '.jpg',
        '.png',
        '.jpeg',
        '.webp'}
    scan_ai_generated_images = (lambda project_id = None: paths = ProjectPaths(project_id)images_dir = paths.images_dir()if not images_dir.exists() or images_dir.is_dir():
[]result = Nonefor f in sorted(images_dir.iterdir()):
if not f.is_file():
continueif f.suffix.lower() not in ImageService.SUPPORTED_IMAGE_EXTENSIONS:
continueif not ImageService.AI_SCENE_IMAGE_PATTERN.match(f.name):
continuerel_path = f'''projects/{project_id}/images/{f.name}'''item = {
'path': rel_path,
'type': 'image',
'fileName': f.name }item.update(normalize_uploaded_media_source_metadata({ }, rel_path))result.append(item)result)()
    scan_flow_output_images = (lambda project_id = None: paths = ProjectPaths(project_id)flow_output_dir = paths.images_dir() / 'flow_output'if not flow_output_dir.exists() or flow_output_dir.is_dir():
[]result = Nonefiles = (lambda .0: pass# WARNING: Decompyle incomplete
)(flow_output_dir.rglob('*')(), key = (lambda file_path: file_path.name))
        for file_path in files:
            if file_path.suffix.lower() not in ImageService.SUPPORTED_IMAGE_EXTENSIONS:
                continue
            item = {
                'path': paths.relative_path(file_path),
                'type': 'image',
                'fileName': file_path.name }
            item.update(normalize_uploaded_media_source_metadata({ }, item['path']))
            result.append(item)
            return result
)()
