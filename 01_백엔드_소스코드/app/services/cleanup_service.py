# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cleanup_service.pyc (Python 3.11)

import os
import shutil
from pathlib import Path
import logging
from app.utils.file_paths import ProjectPaths
logger = logging.getLogger(__name__)

class CleanupService:
    cleanup_project_files = (lambda project_id: deleted_files = []errors = []try:
paths = ProjectPaths(project_id)project_folder = paths.project_baseif project_folder.exists():
shutil.rmtree(project_folder)deleted_files.append(str(project_folder))logger.info(f'''Deleted project folder: {project_folder}''')else:
logger.warning(f'''Project folder not found: {project_folder}''')except Exception:
e = Noneerrors.append(f'''Failed to delete project folder: {e}''')logger.error(f'''Failed to delete project folder for {project_id}: {e}''')e = Nonedel eexcept:
e = Nonedel elogger.info(f'''Deleted {len(deleted_files)} files/folders for project {project_id}''')if errors:
logger.warning(f'''Errors during cleanup ({len(errors)} errors): {errors}'''){
'deleted': deleted_files,
'errors': errors })()
