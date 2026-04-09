# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: media_service.pyc (Python 3.11)

'''
미디어 관리 서비스

프로젝트별 또는 전역 미디어 파일을 관리합니다.
- 미디어 파일 조회 (필터링, 검색, 정렬)
- 미디어 메타데이터 추출
- 기존 프로젝트 미디어 동기화
'''
import os
import sys
import uuid
import mimetypes
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set
from PIL import Image
import subprocess
import json
from app import db
from app.models.project import Media, Project
from app.utils.file_paths import resolve_data_path
from app.utils.ffmpeg_utils import probe_media_duration, probe_video_dimensions
from sqlalchemy import or_, and_, func

class MediaService:
    '''미디어 관리 서비스'''
    SUPPORTED_IMAGE_EXTENSIONS = {
        '.bmp',
        '.gif',
        '.jpg',
        '.png',
        '.jpeg',
        '.webp'}
    SUPPORTED_VIDEO_EXTENSIONS = {
        '.avi',
        '.mkv',
        '.mov',
        '.mp4',
        '.webm'}
    SUPPORTED_AUDIO_EXTENSIONS = {
        '.m4a',
        '.mp3',
        '.ogg',
        '.wav',
        '.flac'}
    SUPPORTED_SUBTITLE_EXTENSIONS = {
        '.ass',
        '.srt',
        '.vtt'}
    get_media_type = (lambda file_path = None: ext = Path(file_path).suffix.lower()if ext in MediaService.SUPPORTED_IMAGE_EXTENSIONS:
'image'if None in MediaService.SUPPORTED_VIDEO_EXTENSIONS:
'video'if None in MediaService.SUPPORTED_AUDIO_EXTENSIONS:
'audio'if None in MediaService.SUPPORTED_SUBTITLE_EXTENSIONS:
'subtitle')()
    get_all_media = (lambda project_id, media_type, search = None, sort_by = None, sort_order = staticmethod, page = (None, None, None, 'created_at', 'desc', 1, 50), per_page = ('project_id', Optional[str], 'media_type', Optional[str], 'search', Optional[str], 'sort_by', str, 'sort_order', str, 'page', int, 'per_page', int, 'return', Tuple[(List[Media], int, Dict[(str, Any)])]): query = Media.queryif project_id:
if project_id == 'global':
query = query.filter(Media.project_id.is_(None))else:
query = query.filter(Media.project_id == project_id)if media_type and media_type != 'all':
query = query.filter(Media.media_type == media_type)if search:
search_pattern = f'''%{search}%'''query = query.filter(or_(Media.file_name.ilike(search_pattern), Media.description.ilike(search_pattern), func.json_extract(Media.tags, '$').like(search_pattern)))total_count = query.count()sort_column = getattr(Media, sort_by, Media.created_at)if sort_order == 'desc':
query = query.order_by(sort_column.desc())else:
query = query.order_by(sort_column.asc())offset = (page - 1) * per_pagemedia_list = query.offset(offset).limit(per_page).all()stats = MediaService._calculate_stats(project_id)(media_list, total_count, stats))()
    _calculate_stats = (lambda project_id = None:
