# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: local_upload_subtitle_strategy_service.pyc (Python 3.11)

import logging
from typing import Any, Callable, Dict, Optional
from app.models.project import Project
from app.services.local_upload_gemini25_sync_service import LocalUploadGemini25SyncService
from app.services.local_upload_stt_service import LocalUploadSTTService
logger = logging.getLogger(__name__)

class LocalUploadSubtitleStrategyService:
    '''로컬 업로드 자막 생성 전략 디스패처.'''
    DEFAULT_ENGINE = 'google'
    GEMINI25_ENGINE = 'gemini25'
    _GEMINI25_ALIASES = {
        'gemini-2.5',
        'gemini25-sync',
        'gemini-2.5-sync',
        'gemini25',
        'gemini_2_5'}
    resolve_engine = (lambda cls = None, stt_options = None: pass# WARNING: Decompyle incomplete
)()
    generate_subtitles = (lambda cls = None, project = None, stt_options = classmethod, progress_callback = (None, None, None), trace_id = ('project', Project, 'stt_options', Optional[Dict[(str, Any)]], 'progress_callback', Optional[Callable[([
        int,
        str], None)]], 'trace_id', Optional[str], 'return', Dict[(str, Any)]):
