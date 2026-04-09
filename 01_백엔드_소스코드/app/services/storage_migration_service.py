# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: storage_migration_service.pyc (Python 3.11)

'''
Storage Migration Service
Handles data migration between storage paths
'''
import os
import shutil
import uuid
import logging
from pathlib import Path
from datetime import datetime
from typing import Literal
from app.config.paths import get_data_path
from app.config.runtime_config import set_migration_status, get_migration_status, clear_migration_status, set_pending_data_path, MigrationStatus
logger = logging.getLogger(__name__)
MIGRATION_FILES = [
    'device_uuid']
SKIP_DIRS = [
    'temp',
    'cache']

class StorageMigrationService:
    '''Service for migrating data between storage paths'''
    start_migration = (lambda source_path = None, target_path = None, mode = staticmethod: migration_id = str(uuid.uuid4())[:8](total_bytes, total_files) = StorageMigrationService._calculate_size(source_path)status = {
'migration_id': migration_id,
'source_path': source_path,
'target_path': target_path,
'mode': mode,
'status': 'pending',
'started_at': datetime.now().isoformat(),
'files_total': total_files,
'files_copied': 0,
'bytes_total': total_bytes,
'bytes_copied': 0 }set_migration_status(status)logger.info(f'''Migration {migration_id} started: {source_path} -> {target_path} ({mode})''')migration_id)()
    execute_migration = (lambda migration_id = None: status = get_migration_status()if status or status.get('migration_id') != migration_id:
logger.error(f'''Migration {migration_id} not found''')Falsesource = None(status['source_path'])target = Path(status['target_path'])mode = status.get('mode', 'copy')status['status'] = 'in_progress'set_migration_status(status)try:
target.mkdir(parents = True, exist_ok = True)files_copied = 0bytes_copied = 0for filename in MIGRATION_FILES:
src_file = source / filenameif src_file.exists():
dst_file = target / filenameif mode == 'copy':
shutil.copy2(src_file, dst_file)else:
shutil.move(src_file, dst_file)files_copied += 1bytes_copied += dst_file.stat().st_size if dst_file.exists() else 0logger.info(f'''Migrated file: {filename}''')for item in source.iterdir():
if item.is_dir():
dirname = item.nameif dirname in SKIP_DIRS:
logger.info(f'''Skipped directory: {dirname}''')continuesrc_dir = itemdst_dir = target / dirnamedst_dir.mkdir(parents = True, exist_ok = True)for root, dirs, files in os.walk(src_dir):
dirs[:] = dirs()rel_root = Path(root).relative_to(src_dir)dst_root = dst_dir / rel_rootdst_root.mkdir(parents = True, exist_ok = True)for file in files:
src_file = Path(root) / filedst_file = dst_root / filefiles_copied += 1bytes_copied += dst_file.stat().st_size if dst_file.exists() else 0if files_copied % 100 == 0:
status['files_copied'] = files_copiedstatus['bytes_copied'] = bytes_copiedset_migration_status(status)try:
continueexcept Exception:
e = Nonelogger.warning(f'''Failed to migrate {src_file}: {e}''')try:
e = Nonedel econtinuee = Nonedel etry:
continuelogger.info(f'''Migrated directory: {dirname}''')continueif item.is_file() and item.name not in MIGRATION_FILES:
dst_file = target / item.nameif mode == 'copy':
shutil.copy2(item, dst_file)else:
shutil.move(item, dst_file)files_copied += 1bytes_copied += dst_file.stat().st_size if dst_file.exists() else 0logger.info(f'''Migrated root file: {item.name}''')try:
continueexcept Exception:
e = Nonelogger.warning(f'''Failed to migrate {item}: {e}''')try:
e = Nonedel econtinuee = Nonedel etry:
continuestatus['status'] = 'completed'status['completed_at'] = datetime.now().isoformat()status['files_copied'] = files_copiedstatus['bytes_copied'] = bytes_copiedset_migration_status(status)set_pending_data_path(str(target))logger.info(f'''Migration {migration_id} completed: {files_copied} files, {bytes_copied} bytes''')Trueexcept Exception:
e = Nonelogger.error(f'''Migration {migration_id} failed: {e}''')status['status'] = 'failed'status['error'] = str(e)set_migration_status(status)e = Nonedel eFalsee = Nonedel e)()
    verify_migration = (lambda migration_id = None: status = get_migration_status()if status or status.get('migration_id') != migration_id:
Falseif None.get('status') != 'completed':
Falsetarget = None(status['target_path'])critical_items = [
target / 'database' / 'tfstudio.db',
target / 'device_uuid']for item in critical_items:
if not item.exists():
logger.warning(f'''Migration verification failed: {item} not found''')projects_dir = target / 'projects'if not projects_dir.exists():
projects_dir.mkdir(parents = True, exist_ok = True)True)()
    rollback_migration = (lambda migration_id = None: status = get_migration_status()if status or status.get('migration_id') != migration_id:
FalseNone()logger.info(f'''Migration {migration_id} rolled back''')True)()
    delete_source_data = (lambda source_path = None: source = Path(source_path)if not source.exists():
{
'success': False,
'error': '소스 경로가 존재하지 않습니다.',
'deleted_files': 0,
'deleted_bytes': 0 }source_str = None(source).lower()dangerous_patterns = [
'windows',
'system32',
'program files',
'programdata',
'$recycle.bin',
'recovery',
'users\\default']for pattern in dangerous_patterns:
if pattern in source_str and 'tfstudio' not in source_str:
None, {
'success': False,
'error': f'''시스템 폴더는 삭제할 수 없습니다: {source_path}''',
'deleted_files': 0,
'deleted_bytes': 0 }0 = 0try:
for item in source.iterdir():
if item.is_dir():
for root, dirs, files in os.walk(item):
for file in files:
filepath = Path(root) / filedeleted_bytes += filepath.stat().st_sizedeleted_files += 1except (OSError, IOError):
continueshutil.rmtree(item)logger.info(f'''Deleted directory: {item.name}''')deleted_bytes += item.stat().st_size if item.exists() else 0deleted_files += 1item.unlink()logger.info(f'''Deleted file: {item.name}''')try:
continueexcept Exception:
e = Nonelogger.warning(f'''Failed to delete {item}: {e}''')try:
e = Nonedel econtinuee = Nonedel etry:
logger.info(f'''Source data deleted: {deleted_files} files, {deleted_bytes} bytes'''){
'success': True,
'error': '',
'deleted_files': deleted_files,
'deleted_bytes': deleted_bytes }except Exception:
e = Nonelogger.error(f'''Error deleting source data: {e}''')del eNoneNone = del e)()
    _calculate_size = (lambda path = None: total_bytes = 0total_files = 0source = Path(path)if not source.exists():
(0, 0)for root, dirs, files in None.walk(source):
dirs[:] = dirs()for file in files:
filepath = Path(root) / filetotal_bytes += filepath.stat().st_sizetotal_files += 1except (OSError, IOError):
continue(total_bytes, total_files))()
    get_progress = (lambda migration_id = None: status = get_migration_status()if status or status.get('migration_id') != migration_id:
Nonefiles_total = None.get('files_total', 0)files_copied = status.get('files_copied', 0)bytes_total = status.get('bytes_total', 0)bytes_copied = status.get('bytes_copied', 0){
'migration_id': migration_id,
'status': status.get('status'),
'files_total': files_total,
'files_copied': files_copied,
'bytes_total': bytes_total,
'bytes_copied': bytes_copied,
'percent_files': round((files_copied / files_total) * 100, 1) if files_total > 0 else 0,
'percent_bytes': round((bytes_copied / bytes_total) * 100, 1) if bytes_total > 0 else 0,
'error': status.get('error') })()

storage_migration_service = StorageMigrationService()
