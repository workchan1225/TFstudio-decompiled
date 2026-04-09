# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bgm_service.pyc (Python 3.11)

'''
BGM Service
Handles BGM file management, audio processing, and mixing
'''
import os
import sys
import uuid
import logging
import subprocess
from pathlib import Path
from typing import List, Dict, Optional
from werkzeug.datastructures import FileStorage
from app.utils.file_paths import ProjectPaths, resolve_data_path
from app.utils.ffmpeg_utils import probe_media_duration
from app.utils.ffmpeg_wrapper import FFmpegWrapper
from app import db
logger = logging.getLogger(__name__)

class BGMService:
    '''BGM management and audio mixing service'''
    DEFAULT_SETTINGS = {
        'volume': 0.15,
        'loop': True,
        'fadeIn': 0,
        'fadeOut': 0,
        'startOffset': 0,
        'trimStart': 0,
        'trimEnd': 0 }
    get_track_file_url = (lambda track = None:
