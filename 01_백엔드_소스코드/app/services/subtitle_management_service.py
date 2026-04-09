# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subtitle_management_service.pyc (Python 3.11)

'''
SubtitleManagementService - 자막 생성 및 관리 서비스
'''
import math
import os
import re
import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional, Callable, cast, Tuple, List
from sqlalchemy.orm.attributes import flag_modified
from app.models.project import Project
from app.utils.file_paths import ProjectPaths
from app.services.subtitle_service import SubtitleService
from app.utils.script_text_cleaner import clean_line_for_tts
from app import db
logger = logging.getLogger(__name__)
_QUOTE_PATTERN = re.compile('^["\\\'""]+|["\'""]+$')

def _validate_and_sort_segments(segments = None):
    '''세그먼트 검증, 정렬, 중복 제거

    Args:
        segments: 자막 세그먼트 리스트

    Returns:
        정렬되고 중복 제거된 세그먼트 리스트
    '''
    if not segments:
        return []
    for seg in None:
        seg['start'] = max(0, float(seg.get('start', 0)))
        seg['end'] = max(0, float(seg.get('end', 0)))
        if seg['end'] <= seg['start']:
            seg['end'] = seg['start'] + 0.5
        sorted_segments = sorted(segments, key = (lambda s: (s['start'], s['end'])))
        seen_ids = set()
        unique_segments = []
        for seg in sorted_segments:
            seg_id = seg.get('id', '')
            if seg_id and seg_id in seen_ids:
                logger.debug(f'''ID 중복 제거: {seg_id}''')
                continue
            if unique_segments:
                last = unique_segments[-1]
                is_time_overlap = abs(seg['start'] - last['start']) < 0.1
                is_same_text = seg.get('text', '') == last.get('text', '')
                if is_time_overlap and is_same_text:
                    logger.debug(f'''시간/텍스트 중복 제거: {seg.get('text', '')[:20]}...''')
                    continue
            unique_segments.append(seg)
            if seg_id:
                seen_ids.add(seg_id)
            for i, seg in enumerate(unique_segments):
                if seg.get('id') or str(seg.get('id', '')).startswith('segment-'):
                    seg['id'] = f'''segment-{i}'''
                removed_count = len(segments) - len(unique_segments)
                if removed_count > 0:
                    logger.info(f'''{removed_count}개 중복 세그먼트 제거됨''')
    return unique_segments


def _normalize_data_path(url = None):
    """
    URL에서 '/data/' 또는 'data/' 접두사를 제거하여 data_dir와 결합 시 중복 방지

    Args:
        url: 파일 URL (예: '/data/projects/.../file.srt' 또는 'data/projects/.../file.srt')

    Returns:
        접두사가 제거된 경로 (예: 'projects/.../file.srt')
    """
    if not url:
        return url
    clean = None.replace('\\', '/')
    if clean.startswith('/data/'):
        return clean[6:]
    if None.startswith('data/'):
        return clean[5:]
    return None.lstrip('/')

LOCAL_UPLOAD_SYNC_ENGINE_TO_LAYER_ID = {
    'google': 'local-upload-stt-google-layer',
    'gemini25': 'local-upload-stt-gemini25-layer' }
LOCAL_UPLOAD_LEGACY_LAYER_ID = 'local-upload-stt-layer'

def _normalize_local_upload_sync_engine(raw_engine = None):
    if not isinstance(raw_engine, str):
        return 'google'
    normalized = None.strip().lower()
    if normalized == 'gemini25':
        return 'gemini25'


def _get_local_upload_sync_engine(project = None, target_language = None):
