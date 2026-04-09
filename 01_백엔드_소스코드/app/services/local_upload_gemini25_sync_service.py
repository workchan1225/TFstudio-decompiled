# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: local_upload_gemini25_sync_service.pyc (Python 3.11)

import json
import logging
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
from sqlalchemy.orm.attributes import flag_modified
from app import db
from app.config.paths import get_data_path
from app.models.project import Project
from app.services.google_stt_service import GoogleSTTService, STTModel
from app.services.local_upload_stt_service import LocalUploadSTTService, _normalize_data_path
from app.services.subtitle_management_service import SubtitleManagementService
from app.utils.audio_silence_utils import get_audio_duration
from app.utils.file_paths import ProjectPaths
from app.utils.script_text_cleaner import clean_script_for_subtitle
from app.utils.sequence_alignment import STTWord, align_script_with_stt, enforce_minimum_segment_duration, validate_and_fix_segment_overlaps
from app.utils.stt_phrase_hints import extract_and_merge_hints
logger = logging.getLogger(__name__)

class LocalUploadGemini25SyncService:
    '''Gemini 2.5 동기화 패턴 기반 로컬 업로드 자막 생성 서비스.'''
    LOCAL_UPLOAD_STT_LAYER_ID = 'local-upload-stt-gemini25-layer'
    LEGACY_LOCAL_UPLOAD_STT_LAYER_ID = 'local-upload-stt-layer'
    SYNC_ENGINE = 'gemini25'
    VALID_MODELS = {
        STTModel.VIDEO,
        STTModel.LATEST_LONG,
        STTModel.LATEST_SHORT,
        STTModel.DEFAULT}
    LANGUAGE_MAP = {
        '한국어': 'ko',
        '영어': 'en',
        '일본어': 'ja',
        '중국어': 'zh' }
    generate_subtitles = (lambda project = None, stt_options = None, progress_callback = staticmethod, trace_id = (None, None, None): pass# WARNING: Decompyle incomplete
)()
    _get_script_for_sync = (lambda project = None:
