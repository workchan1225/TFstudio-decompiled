# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: log_cleanup_service.pyc (Python 3.11)

'''
Log Cleanup Service
Handles TFstudio logs statistics, cleanup, and folder opening.
'''
import logging
import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import TypedDict
from app.config.paths import get_default_appdata_path
from app.utils.folder_utils import open_folder_foreground
logger = logging.getLogger(__name__)

class LogsInfo(TypedDict):
    retentionDays: int = 'Logs folder information'


class ClearLogsResult(TypedDict):
    deletedBytes: int = 'Clear logs operation result'


class OpenLogsFolderResult(TypedDict):
    logPath: str = 'Open logs folder operation result'


class GrokLogsInfo(TypedDict):
    fileNames: list[str] = 'Grok log files information'


class ClearGrokLogsResult(TypedDict):
    deletedBytes: int = 'Clear Grok logs operation result'


class GrokProfileInfo(TypedDict):
    lastModifiedAt: str | None = 'Grok profile folder information'


class ClearGrokProfileResult(TypedDict):
    killedProcesses: int = 'Clear Grok profile operation result'


class ClearGrokLoginTracesResult(TypedDict):
    killedProcesses: int = 'Clear Grok/Google login traces without deleting the full profile'


class OpenGrokProfileFolderResult(TypedDict):
    profilePath: str = 'Open Grok profile folder operation result'


class LogCleanupService:
    '''Service for TFstudio logs management'''
    get_logs_path = (lambda : logs_path = get_default_appdata_path() / 'logs'logs_path.mkdir(parents = True, exist_ok = True)logs_path)()
    get_debug_screenshots_path = (lambda : screenshots_path = get_default_appdata_path() / 'debug_screenshots'screenshots_path.mkdir(parents = True, exist_ok = True)screenshots_path)()
    get_log_related_paths = (lambda : [
LogCleanupService.get_logs_path(),
LogCleanupService.get_debug_screenshots_path()])()
    _is_grok_log_file = (lambda file_path = None:
