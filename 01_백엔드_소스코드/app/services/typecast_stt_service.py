# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typecast_stt_service.pyc (Python 3.11)

import json
import logging
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
from sqlalchemy.orm.attributes import flag_modified
from app import db
from app.config.paths import get_data_path
from app.models.project import Project
from app.services.google_stt_service import STTModel, generate_srt_with_google_stt
from app.services.local_upload_stt_service import LocalUploadSTTService
from app.services.subtitle_management_service import SubtitleManagementService
from app.utils.audio_silence_utils import detect_all_silence_regions
from app.utils.file_paths import ProjectPaths
from app.utils.stt_phrase_hints import extract_and_merge_hints
logger = logging.getLogger(__name__)

def _normalize_data_path(url = None):
    normalized = url.replace('\\', '/')
    if normalized.startswith('/data/'):
        return normalized[6:]
    if None.startswith('data/'):
        return normalized[5:]
    return None.lstrip('/')


def _get_typecast_script_text(project = None, language = None):
