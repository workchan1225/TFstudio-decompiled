# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: capcut_export_service.pyc (Python 3.11)

'''
CapCut Export Service

TFstudio 프로젝트를 CapCut 형식으로 내보내기
CapCut 드래프트 폴더에 직접 생성하여 CapCut 앱에서 즉시 열 수 있음
'''
import base64
import json
import logging
import os
import re
import shutil
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from PIL import Image
from app.models.project import Project
from app.config.paths import get_data_path, get_ffprobe_path
from app.utils.script_text_cleaner import clean_line_for_tts
logger = logging.getLogger(__name__)

class CapCutExportService:
    '''TFstudio 프로젝트를 CapCut 형식으로 내보내기'''
    CAPCUT_VERSION = 360000
    APP_VERSION = '7.5.0'
    TIME_UNIT = 1000000
    IMAGEFIT_VALUE_MAP = {
        'cover': 0,
        'contain': 1,
        'fill': 2,
        'auto': -1 }
    WORKFLOW_MODE_WITH_VOICE = 'with-voice'
    WORKFLOW_MODE_NO_VOICE = 'no-voice'
    WORKFLOW_MODE_VREW_SCRIPT_FIRST = 'vrew-script-first'
    _resolve_workflow_mode = (lambda mode = None: if mode in {
CapCutExportService.WORKFLOW_MODE_WITH_VOICE,
CapCutExportService.WORKFLOW_MODE_NO_VOICE,
CapCutExportService.WORKFLOW_MODE_VREW_SCRIPT_FIRST}:
modeNone.WORKFLOW_MODE_WITH_VOICE)()
    _hex_to_rgb_float = (lambda hex_color = None:
