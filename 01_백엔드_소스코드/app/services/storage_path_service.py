# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: storage_path_service.pyc (Python 3.11)

'''
Storage Path Service
Handles storage path configuration, validation, and space usage
'''
import os
import sqlite3
import shutil
import logging
from pathlib import Path
from typing import TypedDict
from app.config.paths import get_data_path, get_data_path_source, reset_data_path_cache
from app.config.runtime_config import get_configured_data_path, get_default_data_path, get_pending_data_path, set_pending_data_path, validate_data_path, get_migration_status, get_path_history, add_to_path_history
logger = logging.getLogger(__name__)

class SpaceInfo(TypedDict):
    percent_used: float = 'Disk space information'


class StoragePathInfo(TypedDict):
    pathHistory: list[str] = 'Storage path information'


class ValidationResult(TypedDict):
    spaceInfo: SpaceInfo | None = 'Path validation result'


class ApplyResult(TypedDict):
    hasExistingData: bool = 'Path apply result'


class StorageState(TypedDict):
    hasProjects: bool = 'Target path storage state.'


class StoragePathService:
    '''Service for managing storage path configuration'''
    get_current_path_info = (lambda : reset_data_path_cache()current_path = get_data_path()default_path = get_default_data_path()source = get_data_path_source()pending_path = get_pending_data_path()space_info = StoragePathService.get_space_usage(str(current_path))path_history = get_path_history(){
'currentPath': str(current_path).replace('\\', '/'),
'defaultPath': str(default_path).replace('\\', '/'),
'source': source,
'pendingPath': pending_path.replace('\\', '/') if pending_path else None,
'spaceInfo': space_info,
'pathHistory': path_history })()
    get_space_usage = (lambda path = None: pass# WARNING: Decompyle incomplete
)()
    get_data_size = (lambda : try:
data_path = get_data_path()total_size = 0for dirpath, dirnames, filenames in os.walk(data_path):
if 'temp' in dirpath:
continuefor filename in filenames:
filepath = os.path.join(dirpath, filename)total_size += os.path.getsize(filepath)try:
continueexcept (OSError, IOError):
try:
continuetry:
continuetotal_sizeexcept Exception:
e = Nonelogger.error(f'''Failed to calculate data size: {e}''')e = Nonedel e0e = Nonedel e)()
    validate_path = (lambda path = None: (is_valid, error) = validate_data_path(path)if not is_valid:
{
'valid': False,
'error': error,
'spaceInfo': None }space_info = None.get_space_usage(path)data_size = StoragePathService.get_data_size()required_space = data_size + 104857600if space_info['free'] < required_space:
{
'valid': False,
'error': f'''Not enough space. Required: {StoragePathService._format_size(required_space)}, Available: {StoragePathService._format_size(space_info['free'])}''',
'spaceInfo': space_info }{
'valid': None,
'error': '',
'spaceInfo': space_info })()
    apply_path = (lambda path = None: storage_migration_service = storage_migration_serviceimport app.services.storage_migration_servicevalidation = StoragePathService.validate_path(path)if not validation['valid']:
{
'success': False,
'error': validation['error'],
'restartRequired': False,
'hasExistingData': False }None()current_path = str(get_data_path()).replace('\\', '/')new_path = path.replace('\\', '/')if current_path == new_path:
{
'success': False,
'error': '현재 경로와 동일합니다.',
'restartRequired': False,
'hasExistingData': False }try:
target = Path(path)target.mkdir(parents = True, exist_ok = True)target_state = StoragePathService._get_tfstudio_data_state(target)has_existing_data = target_state['state'] == 'valid_existing'if has_existing_data:
logger.info(f'''Found existing TFstudio data at {path}, using as-is''')elif target_state['state'] == 'partial_existing':
logger.warning('Target path contains partial TFstudio data without a valid database; migrating current data into target: %s', path)else:
logger.info('Target path is empty, migrating current data: %s', path)migration_id = storage_migration_service.start_migration(current_path, new_path, mode = 'copy')migration_ok = storage_migration_service.execute_migration(migration_id)if not migration_ok or storage_migration_service.verify_migration(migration_id):
{
'success': False,
'error': '데이터 마이그레이션에 실패했습니다.',
'restartRequired': False,
'hasExistingData': False }None._ensure_essential_dirs(target)add_to_path_history(current_path)logger.info(f'''Added {current_path} to path history''')set_pending_data_path(path){
'success': True,
'error': '',
'restartRequired': True,
'hasExistingData': has_existing_data }except Exception:
e = Nonelogger.error(f'''Path configuration error: {e}''')del eNoneNone = del e)()
    get_migration_status_info = (lambda : get_migration_status())()
    delete_previous_path_data = (lambda previous_path = None: storage_migration_service = storage_migration_serviceimport app.services.storage_migration_servicecurrent_path = str(get_data_path()).replace('\\', '/')previous_path_normalized = previous_path.replace('\\', '/')if current_path == previous_path_normalized:
{
'success': False,
'error': '현재 사용 중인 경로는 삭제할 수 없습니다.',
'deleted_files': 0,
'deleted_bytes': 0 }default_path = None(get_default_data_path()).replace('\\', '/')if default_path == previous_path_normalized:
{
'success': False,
'error': '기본 저장 경로는 삭제할 수 없습니다.',
'deleted_files': 0,
'deleted_bytes': 0 }None.delete_source_data(previous_path))()
    _format_size = (lambda size_bytes = None: for unit in ('B', 'KB', 'MB', 'GB', 'TB'):
if size_bytes < 1024:
None, f'''{size_bytes:.1f} {unit}'''f'''{size_bytes:.1f} PB''')()
    _ensure_essential_dirs = (lambda path = None: essential_dirs = [
'database',
'projects',
'outputs',
'temp',
'cache']for dir_name in essential_dirs:
(path / dir_name).mkdir(parents = True, exist_ok = True)None)()
    _has_valid_database = (lambda path = None: db_path = path / 'database' / 'tfstudio.db'if not db_path.exists() or db_path.is_file():
Falseif None.stat().st_size <= 0:
Falseconnection = None# WARNING: Decompyle incomplete
)()
    _get_tfstudio_data_state = (lambda path = None:
