# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sync_service.pyc (Python 3.11)

'''
SyncService - Database/Filesystem Synchronization Service

프로젝트 데이터베이스 레코드와 파일시스템 간의 동기화를 담당합니다.
- 폴더가 없는 프로젝트는 DB에서 자동 제거
- 존재하지 않는 이미지 참조는 uploadedImages에서 자동 제거
'''
from pathlib import Path
from typing import Dict, List, Any, Tuple
import logging
import re
from sqlalchemy.orm.attributes import flag_modified
from app.models.project import Project, Media
from app.utils.file_paths import ProjectPaths
from app import db
logger = logging.getLogger(__name__)

class SyncService:
    '''
    프로젝트 데이터와 파일시스템 간의 동기화 서비스

    Responsibilities:
    - 프로젝트 폴더 존재 여부 검증
    - 이미지 파일 존재 여부 검증
    - 고아 데이터베이스 레코드 제거
    - 동기화 상태 리포트 제공
    '''
    validate_project_folder = (lambda project_id = None: try:
paths = ProjectPaths(project_id)paths.project_base.exists()except Exception:
e = Nonelogger.error(f'''[SyncService] Error validating project folder {project_id}: {e}''')e = Nonedel eFalsee = Nonedel e)()
    sync_project_images = (lambda project = None: if not project.video_settings:
{
'synced': False,
'reason': 'no_video_settings' }uploaded_images = None.video_settings.get('uploadedImages', [])if not uploaded_images:
{
'synced': False,
'reason': 'no_images' }paths = None(project.id)valid_images = []removed_count = 0removed_paths = []for img in uploaded_images:
img_path = img.get('path', '')if not img_path:
continuenormalized_path = img_path.replace('\\', '/')get_data_path = get_data_pathimport app.config.pathsdata_dir = get_data_path()if normalized_path.startswith('data/'):
relative_part = normalized_path[5:]full_path = data_dir / relative_partelif normalized_path.startswith('/data/'):
relative_part = normalized_path[6:]full_path = data_dir / relative_partelif normalized_path.startswith('projects/'):
full_path = data_dir / normalized_pathelse:
full_path = Path(img_path)if full_path.exists():
valid_images.append(img)continueremoved_count += 1removed_paths.append(img_path)logger.warning(f'''[SyncService] Removing missing image ref: {img_path} (checked: {full_path})''')if removed_count > 0:
settings = dict(project.video_settings)settings['uploadedImages'] = valid_imagesproject.video_settings = settingsflag_modified(project, 'video_settings'){
'synced': True,
'removed': removed_count,
'remaining': len(valid_images),
'removed_paths': removed_paths,
'project_id': project.id })()
    get_valid_projects = (lambda : projects = Project.query.order_by(Project.updated_at.desc()).all()valid_projects = []removed_count = 0removed_ids = []# WARNING: Decompyle incomplete
)()
    sync_single_project = (lambda project = None: if not SyncService.validate_project_folder(project.id):
{
'synced': False,
'reason': 'project_folder_missing',
'project_id': project.id }sync_result = None.sync_project_images(project)if sync_result.get('removed', 0) > 0:
try:
db.session.commit()logger.info(f'''[SyncService] Synced project {project.id}: removed {sync_result['removed']} missing images''')except Exception:
e = Nonelogger.error(f'''[SyncService] Error committing image sync: {e}''')db.session.rollback()del eNoneNone = del esync_result)()
    sync_orphaned_media = (lambda : existing_project_ids = Project.query.all()()all_media = Media.query.all()orphaned_count = 0missing_file_count = 0for media in all_media:
if media.project_id and media.project_id not in existing_project_ids:
logger.info(f'''[SyncService] Removing orphaned media: {media.file_name} (project: {media.project_id})''')db.session.delete(media)orphaned_count += 1continueif media.file_path:
paths = ProjectPaths(media.project_id) if media.project_id else Noneif paths:
normalized_path = media.file_path.replace('\\', '/')full_path = paths.data_dir / normalized_pathif not full_path.exists():
logger.info(f'''[SyncService] Removing missing file media: {media.file_name}''')db.session.delete(media)missing_file_count += 1if orphaned_count > 0 or missing_file_count > 0:
try:
db.session.commit()except Exception:
e = Nonelogger.error(f'''[SyncService] Error committing media cleanup: {e}''')db.session.rollback()e = Nonedel eexcept:
e = Nonedel e{
'orphaned_media_removed': orphaned_count,
'missing_file_media_removed': missing_file_count })()
    sync_all_projects = (lambda : projects = Project.query.all()removed_projects = []synced_images = []# WARNING: Decompyle incomplete
)()
    set_project_thumbnail_from_image = (lambda project = None, image_path = None: if not image_path:
Falsethumbnail = None.replace('\\', '/')if not thumbnail.startswith('/') and thumbnail.startswith('http'):
if thumbnail.startswith('data/'):
thumbnail = '/' + thumbnailelse:
thumbnail = '/data/' + thumbnailproject.thumbnail = thumbnailTrue)()
    get_sync_status = (lambda : import uuidget_projects_path = get_projects_pathimport app.config.pathsprojects_dir = get_projects_path()db_projects = Project.query.all()db_ids = db_projects()folder_ids = set()if projects_dir.exists():
for item in projects_dir.iterdir():
if item.is_dir() and item.name != 'temp':
uuid.UUID(item.name)folder_ids.add(item.name)continueexcept ValueError:
continueorphan_folders = folder_ids - db_idsorphan_db = db_ids - folder_ids{
'dbCount': len(db_ids),
'folderCount': len(folder_ids),
'inSync': len(orphan_db) == 0,
'orphanFolders': len(orphan_folders),
'orphanDb': len(orphan_db),
'message': '동기화됨' if (len(orphan_folders) == 0 or len(orphan_folders) == 0) and len(orphan_db) == 0 else f'''{len(orphan_folders)}개 복구 가능, {len(orphan_db)}개 정리 필요''' })()
    scan_and_recover_projects = (lambda :
