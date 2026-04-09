# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vrew_export_service.pyc (Python 3.11)

'''
Vrew Export Service

TFstudio 프로젝트를 Vrew 형식(.vrew)으로 내보내기
Vrew v3.5.4 (포맷 버전 15) 호환
'''
import base64
import copy
import json
import logging
import os
import random
import re
import shutil
import string
import uuid
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from app.models.project import Project
from app.utils.file_paths import ProjectPaths
from app.config.paths import get_data_path, get_ffmpeg_path, get_ffprobe_path
from app.utils.script_text_cleaner import clean_line_for_tts

try:
    from app.utils.ffmpeg_wrapper import FFmpegWrapper
    HAS_FFMPEG = True
except ImportError:
    HAS_FFMPEG = False

logger = logging.getLogger(__name__)

class VrewExportService:
    '''TFstudio 프로젝트를 Vrew 형식으로 내보내기'''
    VREW_VERSION = 15
    FILE_VERSION = 1
    WORKFLOW_MODE_WITH_VOICE = 'with-voice'
    WORKFLOW_MODE_NO_VOICE = 'no-voice'
    WORKFLOW_MODE_VREW_SCRIPT_FIRST = 'vrew-script-first'
    VREW_IMAGE_MODE_SENTENCE = 'sentence'
    VREW_IMAGE_MODE_SCENE = 'scene'
    VREW_READABLE_CHARS_PER_SEC = 6.5
    VREW_MIN_SEGMENT_DURATION = 1.8
    VREW_READ_PAUSE_SECONDS = 0.25
    VREW_READ_PADDING_RATIO = 0.3
    VREW_FONT_SIZE_SCALE = 1.61111
    _resolve_workflow_mode = (lambda mode = None: if mode in {
VrewExportService.WORKFLOW_MODE_WITH_VOICE,
VrewExportService.WORKFLOW_MODE_NO_VOICE,
VrewExportService.WORKFLOW_MODE_VREW_SCRIPT_FIRST}:
modeNone.WORKFLOW_MODE_WITH_VOICE)()
    _resolve_vrew_image_mode = (lambda mode = None: if mode in {
VrewExportService.VREW_IMAGE_MODE_SENTENCE,
VrewExportService.VREW_IMAGE_MODE_SCENE}:
modeNone.VREW_IMAGE_MODE_SENTENCE)()
    export_to_vrew = (lambda project, include_images, orientation = None, exclude_tts = None, workflow_mode = staticmethod, enable_ken_burns = (True, None, False, None, False, None), vrew_image_mode = ('project', Project, 'include_images', bool, 'orientation', str, 'exclude_tts', bool, 'workflow_mode', Optional[str], 'enable_ken_burns', bool, 'vrew_image_mode', Optional[str], 'return', str): logger.info(f'''[VrewExport] Starting export for project: {project.id}''')# WARNING: Decompyle incomplete
)()
    _validate_segments_quality = (lambda segments = None: if not segments:
FalseMAX_SEGMENT_DURATION = Noneinvalid_count = 0for seg in segments:
if not seg.get('start', 0):
start = 0if not seg.get('end', 0):
end = 0duration = end - startif duration > MAX_SEGMENT_DURATION:
logger.warning(f'''[VrewExport] Segment too long: {duration:.2f}s (max: {MAX_SEGMENT_DURATION}s)''')Falseif None == 0 and end == 0:
invalid_count += 1if invalid_count > len(segments) * 0.5:
logger.warning(f'''[VrewExport] Too many invalid segments: {invalid_count}/{len(segments)}''')FalseNone)()
    _get_subtitle_segments = (lambda project = None: SubtitleManagementService = SubtitleManagementServiceimport app.services.subtitle_management_servicetry:
result = SubtitleManagementService.get_subtitles(project)segments = result.get('segments', [])source = result.get('source', 'unknown')if segments:
sanitized_segments = VrewExportService._sanitize_subtitle_segments_for_export(segments, log_prefix = '[VrewExport]')logger.info(f'''[VrewExport] Using subtitles from \'{source}\': {len(sanitized_segments)} segments''')sanitized_segmentsNone.warning('[VrewExport] No subtitles found from SubtitleManagementService')[]except Exception:
e = Nonelogger.error(f'''[VrewExport] Failed to get subtitles: {e}''')del eNoneNone = del e)()
    _sanitize_subtitle_segments_for_export = (lambda segments = None, log_prefix = None: if not segments:
[]sanitized_segments = Nonecleaned_count = 0emptied_count = 0for seg in segments:
if not isinstance(seg, dict):
continueif not seg.get('text', ''):
raw_text = str('')cleaned_text = clean_line_for_tts(raw_text)if cleaned_text != raw_text.strip():
cleaned_count += 1if not raw_text.strip() and cleaned_text:
emptied_count += 1updated_seg = dict(seg)updated_seg['text'] = cleaned_textsanitized_segments.append(updated_seg)logger.info(f'''{log_prefix} Sanitized subtitle texts: {cleaned_count}/{len(sanitized_segments)} modified, {emptied_count} emptied''')sanitized_segments)()
    _create_image_only_segments = (lambda images = None, duration_per_image = None: segments = []current_time = 0for i, img in enumerate(images):
segments.append({
'start': current_time,
'end': current_time + duration_per_image,
'text': '',
'lineIndex': i })current_time += duration_per_imagelogger.info(f'''[VrewExport] Created {len(segments)} image-only segments (total duration: {current_time}s)''')segments)()
    _convert_image_timeline_to_segments = (lambda timeline_segments = None: segments = []for seg in timeline_segments:
start_time = seg.get('startTime', 0)end_time = seg.get('endTime', start_time + 3)image_index = seg.get('imageIndex', 0)segments.append({
'start': start_time,
'end': end_time,
'text': '',
'lineIndex': image_index })segments.sort(key = (lambda x: x['start']))
        total_duration = segments[-1]['end'] if segments else 0
        logger.info(f'''[VrewExport] Converted imageTimeline to {len(segments)} segments (total duration: {total_duration}s)''')
        return segments
)()
    _split_text_by_max_chars = (lambda text = None, max_chars = None: pass# WARNING: Decompyle incomplete
)()
    _merge_units_to_target_count = (lambda units = None, target_count = None: normalized_units = units()if normalized_units or target_count <= 0:
[]if (lambda .0: pass# WARNING: Decompyle incomplete
)(normalized_units) <= target_count:
            return normalized_units
        base_count = None(normalized_units) // target_count
        remainder = len(normalized_units) % target_count
        merged = []
        cursor = 0
        for idx in range(target_count):
            take = base_count + 1 if idx < remainder else 0
            group = normalized_units[cursor:cursor + take]
            cursor += take
            merged.append(' '.join(group).strip())
            return merged()
)()
    _build_script_chunks_for_segment_count = (lambda project = None, segment_count = None: if segment_count <= 0:
[]if not None.get_active_script_for_subtitle():
if not project.script:
script_text = ''.strip()if not script_text:
[]normalized = None.replace('\r\n', '\n').replace('\r', '\n')lines = normalized.split('\n')()units = []for raw_line in lines:
cleaned_line = clean_line_for_tts(raw_line)cleaned_line = re.sub('\\s+', ' ', cleaned_line).strip()if not cleaned_line:
continuesentence_parts = re.split('(?<=[.!?。？！])\\s+', cleaned_line)for part in sentence_parts:
part = part.strip()if not part:
continueunits.extend(VrewExportService._split_text_by_max_chars(part, max_chars = 58))if not units:
units = VrewExportService._split_text_by_max_chars(re.sub('\\s+', ' ', script_text), max_chars = 58)if not units:
[](lambda .0: pass# WARNING: Decompyle incomplete
)._merge_units_to_target_count(units, segment_count)
)()
    _apply_script_chunks_to_segments = (lambda segments = None, chunks = None: if not segments:
[]if not None:
segmentsadjusted_chunks = Noneif len(chunks) > len(segments):
adjusted_chunks = VrewExportService._merge_units_to_target_count(chunks, len(segments))updated_segments = []for idx, segment in enumerate(segments):
updated = dict(segment)if idx < len(adjusted_chunks):
updated['text'] = adjusted_chunks[idx]updated_segments.append(updated)updated_segments)()
    _estimate_read_duration_for_text = (lambda text = None:
