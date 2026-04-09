# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: media_preparer.pyc (Python 3.11)

'''
Media Preparer - 미디어 준비 모듈

영상 생성에 필요한 미디어(이미지/비디오)를 준비하는 클래스.
타임라인 기반 또는 원본 순서 기반으로 미디어 목록을 구성하고,
전체 영상 또는 샘플 영상용으로 미디어를 준비함.
'''
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, TYPE_CHECKING
import logging
import os
from app.utils.file_paths import resolve_data_path
from types import MediaItem, MediaType, DEFAULT_IMAGE_DURATION, MIN_IMAGE_DURATION
if TYPE_CHECKING:
    from app.models.project import Project
logger = logging.getLogger(__name__)

class PrepareMode(Enum, str):
    '''미디어 준비 모드'''
    FULL = 'full'
    SAMPLE = 'sample'

PrepareOptions = <NODE:12>()
PreparedMedia = <NODE:12>()

class MediaPreparer:
    '''
    미디어 준비 클래스.

    영상 생성에 필요한 미디어 목록을 준비하는 역할.
    타임라인 기반 또는 원본 순서 기반으로 미디어를 구성.

    Usage:
        # 전체 영상용
        result = MediaPreparer.prepare_for_full_video(project, data_dir, has_timeline=True)

        # 샘플 영상용
        result = MediaPreparer.prepare_for_sample_video(project, data_dir, limit=3)

        # 레거시 포맷으로 변환
        paths, durations, metadata = MediaPreparer.to_legacy_format(result)
    '''
    prepare_for_full_video = (lambda cls = None, project = None, data_dir = classmethod, has_timeline = (True,): options = PrepareOptions.for_full_video(use_timeline = has_timeline)cls._prepare(project, data_dir, options))()
    prepare_for_sample_video = (lambda cls, project = None, data_dir = None, limit = classmethod, max_duration = (3, 30, True), has_timeline = ('project', 'Project', 'data_dir', Path, 'limit', int, 'max_duration', float, 'has_timeline', bool, 'return', PreparedMedia): options = PrepareOptions.for_sample_video(limit = limit, max_duration = max_duration, use_timeline = has_timeline)cls._prepare(project, data_dir, options))()
    to_legacy_format = (lambda prepared = None: paths = []durations = []metadata = []for item in prepared.items:
paths.append(item.path)durations.append(item.duration)metadata.append(item.to_metadata())(paths, durations, metadata))()
    _prepare = (lambda cls = None, project = None, data_dir = classmethod, options = ('project', 'Project', 'data_dir', Path, 'options', PrepareOptions, 'return', PreparedMedia): if not project.video_settings:
video_settings = { }uploaded_images = video_settings.get('uploadedImages', [])if not uploaded_images:
logger.warning('업로드된 이미지가 없습니다.')PreparedMedia()if None.use_timeline:
result = cls._prepare_from_timeline(project, data_dir, uploaded_images, options)else:
result = cls._prepare_from_original_order(project, data_dir, uploaded_images, options)result = cls._prepend_intro_scene(project, data_dir, result)if options.mode == PrepareMode.SAMPLE:
result = cls._apply_sample_limits(result, options)if options.scale_duration and options.scale_factor != 1:
result = cls._apply_duration_scaling(result, options.scale_factor)logger.info(f'''미디어 준비 완료: {result.count}개 항목, 총 {result.total_duration:.2f}초 (소스: {result.source})''')result)()
    _prepare_from_timeline = (lambda cls, project = None, data_dir = None, uploaded_images = classmethod, options = ('project', 'Project', 'data_dir', Path, 'uploaded_images', List[Dict[(str, Any)]], 'options', PrepareOptions, 'return', PreparedMedia): if not project.video_settings:
video_settings = { }timeline = video_settings.get('imageTimeline', { })segments = timeline.get('segments', [])if not segments:
logger.info('타임라인 세그먼트가 없어 원본 순서로 폴백합니다.')cls._prepare_from_original_order(project, data_dir, uploaded_images, options)items = Nonetotal_duration = 0image_count = 0video_count = 0for segment in segments:
image_index = segment.get('imageIndex')duration = segment.get('duration', options.default_duration)if not cls._validate_image_index(image_index, uploaded_images):
logger.warning(f'''유효하지 않은 이미지 인덱스: {image_index}''')continueimage_data = uploaded_images[image_index]file_path = cls._resolve_file_path(image_data, data_dir)if not cls._validate_file_exists(file_path):
logger.warning(f'''파일이 존재하지 않습니다: {file_path}''')continueduration = cls._validate_duration(duration, options)media_type = cls._detect_media_type(file_path, image_data)original_duration = float(image_data.get('duration', 0)) if media_type == MediaType.VIDEO else 0item = MediaItem(path = file_path, duration = duration, media_type = media_type, original_duration = original_duration)items.append(item)total_duration += durationif media_type == MediaType.IMAGE:
image_count += 1continuevideo_count += 1PreparedMedia(items = items, total_duration = total_duration, image_count = image_count, video_count = video_count, source = 'timeline'))()
    _prepare_from_original_order = (lambda cls, project = None, data_dir = None, uploaded_images = classmethod, options = ('project', 'Project', 'data_dir', Path, 'uploaded_images', List[Dict[(str, Any)]], 'options', PrepareOptions, 'return', PreparedMedia): items = []total_duration = 0image_count = 0video_count = 0for image_data in uploaded_images:
file_path = cls._resolve_file_path(image_data, data_dir)if not cls._validate_file_exists(file_path):
logger.warning(f'''파일이 존재하지 않습니다: {file_path}''')continueduration = float(image_data.get('duration', options.default_duration))duration = cls._validate_duration(duration, options)media_type = cls._detect_media_type(file_path, image_data)original_duration = float(image_data.get('duration', 0)) if media_type == MediaType.VIDEO else 0item = MediaItem(path = file_path, duration = duration, media_type = media_type, original_duration = original_duration)items.append(item)total_duration += durationif media_type == MediaType.IMAGE:
image_count += 1continuevideo_count += 1PreparedMedia(items = items, total_duration = total_duration, image_count = image_count, video_count = video_count, source = 'original'))()
    _validate_image_index = (lambda index = None, uploaded_images = None: pass# WARNING: Decompyle incomplete
)()
    _validate_file_exists = (lambda file_path = None: if not file_path:
FalseNone.path.exists(file_path))()
    _validate_duration = (lambda duration = None, options = None: pass# WARNING: Decompyle incomplete
)()
    _resolve_file_path = (lambda image_data = None, data_dir = None:
