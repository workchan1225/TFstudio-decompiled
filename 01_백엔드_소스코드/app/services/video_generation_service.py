# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: video_generation_service.pyc (Python 3.11)

'''
VideoGenerationService - 영상 생성 서비스
'''
import os
import shutil
import logging
import threading
import time
import re
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
from sqlalchemy.orm.attributes import flag_modified
logger = logging.getLogger(__name__)
from app.models.project import Project
from app.utils.file_paths import ProjectPaths, resolve_data_path
from app.utils.ffmpeg_wrapper import FFmpegWrapper, FFmpegStoppedError
from app.services.subtitle_service import SubtitleService
from app.services.image_composer_service import ImageComposerService
from app.services.progress_service import progress_service
from app.services.subtitle_runtime_style_resolver import calculate_runtime_position, get_orientation as get_runtime_orientation, resolve_runtime_subtitle_style, resolve_runtime_title_layer_style
from app.constants.subtitle_style_defaults import merge_with_defaults
from app.constants.title_layer_defaults import merge_title_layer_with_defaults
from app import db
from app.services.video import VideoValidator, get_image_effects_config, get_final_voice_url, filter_audio_tracks_by_duration, initialize_services

class TimelineMismatchError(Exception):
    pass
# WARNING: Decompyle incomplete

DEFAULT_IMAGE_DURATION = 3
MIN_IMAGE_DURATION = 0.1
BASE_LANDSCAPE_RESOLUTION = '1920x1080'

class VideoGenerationService:
    '''
    직접 제작 프로젝트의 최종 영상 생성 서비스

    책임:
    - 이미지/영상 소스로 최종 영상 생성
    - 오디오 병합
    - 자막 추가 (multi-layer 또는 legacy)
    - 영상 메타데이터 관리
    '''
    _start_progress_heartbeat = (lambda task_id = None, start_progress = None, end_progress = staticmethod, step = (1, 3), interval_sec = ('task_id', str, 'start_progress', float, 'end_progress', float, 'step', float, 'interval_sec', float, 'return', Tuple[(threading.Event, threading.Thread)]): pass# WARNING: Decompyle incomplete
)()
    _calculate_ffmpeg_watchdogs = (lambda total_duration = None: safe_duration = max(float(total_duration), 0)no_response_timeout = max(120, min(1800, int(safe_duration * 0.25) + 120))progress_stall_timeout = max(no_response_timeout * 2, min(3600, int(safe_duration * 0.5) + 240))(no_response_timeout, progress_stall_timeout))()
    generate_video = (lambda project, bitrate = None, orientation = None, image_fit = staticmethod, exclude_subtitle = ('landscape', 'cover', False, False), skip_timeline_validation = ('project', Project, 'bitrate', Any, 'orientation', str, 'image_fit', str, 'exclude_subtitle', bool, 'skip_timeline_validation', bool, 'return', Dict[(str, Any)]): pass# WARNING: Decompyle incomplete
)()
    generate_preview = (lambda project = None, orientation = None, image_fit = staticmethod, exclude_subtitle = ('landscape', 'cover', False): project_id = project.iddb.session.expire_all()db.session.refresh(project)logger.debug('[VideoGenerationService] ===== PREVIEW GENERATION START =====')has_image_timeline = VideoValidator.validate_for_final(project)is_no_voice = project.selected_tts_method == 'no-voice'if orientation == 'portrait':
preview_resolution = '540x960'else:
preview_resolution = '960x540'preview_bitrate = 5logger.debug(f'''[VideoGenerationService] Preview Resolution: {preview_resolution}''')logger.debug(f'''[VideoGenerationService] Preview Bitrate: {preview_bitrate} Mbps''')logger.debug('[VideoGenerationService] =====================================')(ffmpeg, subtitle_service, paths) = initialize_services(project_id)backend_dir = paths.backend_dirdata_dir = paths.data_dirpreflight = VideoValidator.validate_render_preflight(project = project, ffmpeg = ffmpeg, data_dir = str(data_dir), is_no_voice = is_no_voice, has_image_timeline = has_image_timeline)if not preflight.get('expected_duration') and preflight.get('audio_duration') and preflight.get('final_audio_url'):
logger.info('[VideoGenerationService] Preview preflight OK: segments=%s, timeline=%.3fs, audio=%.3fs, audioUrl=%s', preflight.get('segment_count'), float(0), float(0), 'None')(intro_img_paths, intro_img_durations, intro_img_meta, intro_offset_duration) = VideoGenerationService._get_intro_image_data(project, data_dir)(image_paths, durations, media_metadata) = VideoGenerationService._prepare_image_data(project, data_dir, has_image_timeline, intro_data = (intro_img_paths, intro_img_durations, intro_img_meta) if intro_img_paths else None)loop_short_videos = project.video_settings.get('loopShortVideos', True) if project.video_settings else True(preview_width, preview_height) = map(int, preview_resolution.split('x'))composer_temp_dir = Nonecomposer_layers = []if VideoGenerationService._has_composer_enabled(project):
composer_layers = VideoGenerationService._get_composer_layers(project)if composer_layers:
logger.debug(f'''[VideoGenerationService] Preview: Composer enabled, found {len(composer_layers)} layers - will apply via FFmpeg''')composer_temp_dir = paths.video_path('composer_temp_preview')os.makedirs(composer_temp_dir, exist_ok = True)image_effects = get_image_effects_config(project)apply_mode = image_effects.get('applyMode', 'batch')scene_effects = image_effects.get('sceneEffects', { }) if apply_mode == 'individual' else Nonepreview_filename = f'''preview_{orientation}_clean.mp4''' if exclude_subtitle else f'''preview_{orientation}.mp4'''preview_video = paths.video_path(preview_filename)temp_video = paths.video_path(f'''temp_preview_{orientation}.mp4''')temp_with_audio = paths.video_path(f'''temp_preview_{orientation}_audio.mp4''')try:
print(f'''[VideoGenerationService] PREVIEW: Creating video with {len(image_paths)} images''')print(f'''[VideoGenerationService] PREVIEW: Loop short videos: {loop_short_videos}''')print(f'''[VideoGenerationService] PREVIEW: Media metadata count: {len(media_metadata) if media_metadata else 0}''')if media_metadata:
for i, meta in enumerate(media_metadata):
print(f'''[VideoGenerationService] PREVIEW MetaData[{i}]: {meta}''')ffmpeg.create_video_with_image_effects(image_paths = image_paths, durations = durations, effect_settings = image_effects, output_path = str(temp_video), resolution = preview_resolution, bitrate = preview_bitrate, image_fit = image_fit, per_scene_effects = scene_effects, media_metadata = media_metadata, loop_short_videos = loop_short_videos, prefer_opencv_engine = False)actual_preview_duration = ffmpeg.get_video_duration(str(temp_video))total_duration = sum(durations)preview_drift = total_duration - actual_preview_durationlogger.info(f'''[VideoGen] Preview duration: expected={total_duration:.3f}s, actual={actual_preview_duration:.3f}s, drift={preview_drift:.3f}s''')if not project.bgm_tracks and project.sfx_tracks:
(enabled_bgm, enabled_sfx) = filter_audio_tracks_by_duration([], [], total_duration)if is_no_voice:
logger.debug('[VideoGenerationService] Preview: No-voice mode')if enabled_bgm or enabled_sfx:
if not project.video_settings:
video_settings = { }bgm_sequence_loop = video_settings.get('bgmSequenceLoop', True)ffmpeg.add_multiple_audio_tracks_to_video(video_path = str(temp_video), voice_path = None, bgm_tracks = enabled_bgm, sfx_tracks = enabled_sfx, output_path = str(temp_with_audio), total_duration = total_duration, data_dir = str(data_dir), bgm_sequence_loop = bgm_sequence_loop, enforce_duration = True)else:
logger.debug('[VideoGenerationService] Preview: Adding multi-track audio')final_voice_url = get_final_voice_url(project)final_voice_url = VideoGenerationService._prepend_intro_tts(project, final_voice_url, ffmpeg, paths, data_dir)if not project.video_settings:
video_settings_dict = { }bgm_sequence_loop = video_settings_dict.get('bgmSequenceLoop', True)ffmpeg.add_multiple_audio_tracks_to_video(video_path = str(temp_video), voice_path = final_voice_url, bgm_tracks = enabled_bgm, sfx_tracks = enabled_sfx, output_path = str(temp_with_audio), total_duration = total_duration, data_dir = str(data_dir), bgm_sequence_loop = bgm_sequence_loop, enforce_duration = True)temp_with_subtitle = paths.video_path(f'''temp_preview_{orientation}_subtitle.mp4''')(preview_width, preview_height) = map(int, preview_resolution.split('x'))if exclude_subtitle and VideoGenerationService._has_subtitle_data(project):
logger.debug('[VideoGenerationService] Preview: Adding subtitles')scale_factor = preview_width / 1920 if orientation == 'landscape' else preview_width / 1080temp_ass_path = VideoGenerationService._generate_subtitle_ass(project = project, subtitle_service = subtitle_service, paths = paths, video_width = preview_width, video_height = preview_height, orientation = orientation, is_preview = True, scale_factor = scale_factor)if temp_ass_path:
if intro_offset_duration > 0:
temp_ass_path = VideoGenerationService._offset_ass_subtitles(temp_ass_path, intro_offset_duration)if abs(preview_drift) > 0.05:
temp_ass_path = VideoGenerationService._rescale_ass_subtitles(temp_ass_path, expected_duration = total_duration + intro_offset_duration, actual_duration = actual_preview_duration + intro_offset_duration, intro_offset = intro_offset_duration)ffmpeg.add_ass_subtitle_to_video(video_path = str(temp_with_audio), ass_subtitle_path = temp_ass_path, output_path = str(temp_with_subtitle))try:
os.remove(temp_ass_path)try:
passexcept Exception:
e = Nonelogger.warning(f'''Failed to remove temp ASS file: {e}''')try:
e = Nonedel ee = Nonedel etry:
temp_with_subtitle = temp_with_audiotemp_with_subtitle = temp_with_audiologo_settings = VideoGenerationService._get_logo_settings(project, orientation)logo_added = Falseif logo_settings and logo_settings.get('enabled') and logo_settings.get('filePath'):
logo_path = resolve_data_path(data_dir, logo_settings['filePath'])if os.path.exists(logo_path):
logger.debug('[VideoGenerationService] Preview: Adding logo overlay')ffmpeg.add_logo_overlay(video_path = str(temp_with_subtitle), logo_path = logo_path, output_path = str(preview_video), position_x = logo_settings.get('positionX', 90), position_y = logo_settings.get('positionY', 90), size_percent = logo_settings.get('size', 20), opacity = logo_settings.get('opacity', 100))logo_added = Trueelif temp_with_subtitle != temp_with_audio:
shutil.copy2(str(temp_with_subtitle), str(preview_video))else:
shutil.copy2(str(temp_with_audio), str(preview_video))temp_with_composer = paths.video_path(f'''temp_preview_composer_{orientation}.mp4''')has_composer_overlay = Falseif composer_layers:
logger.debug('[VideoGenerationService] Preview: Preparing composer layers for FFmpeg')canvas_settings = project.video_settings.get('composerCanvas', { })source_width = canvas_settings.get('width', 1920)source_height = canvas_settings.get('height', 1080)ffmpeg_layers = VideoGenerationService._prepare_composer_layers_for_ffmpeg(project_id = project_id, composer_layers = composer_layers, temp_dir = Path(composer_temp_dir), data_dir = str(data_dir), source_width = source_width, source_height = source_height, target_width = preview_width, target_height = preview_height)if ffmpeg_layers:
if logo_added and preview_video.exists():
composer_input = str(preview_video)else:
composer_input = str(temp_with_subtitle)if not os.path.exists(composer_input):
composer_input = str(temp_with_audio)logger.debug(f'''[VideoGenerationService] Preview: Applying {len(ffmpeg_layers)} composer layers via FFmpeg''')try:
ffmpeg.add_timed_image_overlays(video_path = composer_input, output_path = str(temp_with_composer), layers = ffmpeg_layers, canvas_width = preview_width, canvas_height = preview_height)if temp_with_composer.exists():
has_composer_overlay = Truelogger.debug('[VideoGenerationService] Preview: Composer layers applied successfully')else:
logger.debug('[VideoGenerationService] Preview: Warning - Composer output not created')try:
passexcept Exception:
e = Nonelogger.debug(f'''[VideoGenerationService] Preview: Failed to apply composer layers: {e}''')try:
e = Nonedel ee = Nonedel etry:
overlay_settings = image_effects.get('overlays', [])overlay_apply_mode = image_effects.get('overlayApplyMode', 'global')dialogue_overlays = image_effects.get('dialogueOverlays', { })active_overlays = overlay_settings()if has_composer_overlay and temp_with_composer.exists():
overlay_input = str(temp_with_composer)elif logo_added and preview_video.exists():
overlay_input = str(preview_video)elif temp_with_subtitle != temp_with_audio:
overlay_input = str(temp_with_subtitle)else:
overlay_input = str(temp_with_audio)logger.debug(f'''[VideoGenerationService] Preview: Overlay input: {overlay_input} (logo_added={logo_added})''')if not os.path.exists(overlay_input):
logger.debug(f'''[VideoGenerationService] Preview: Warning: Overlay input file not found: {overlay_input}''')overlay_input = str(temp_with_audio)logger.debug(f'''[VideoGenerationService] Preview: Falling back to: {overlay_input}''')same_file = os.path.normpath(overlay_input) == os.path.normpath(str(preview_video))temp_with_overlays = paths.video_path(f'''temp_preview_{orientation}_overlays.mp4''')if overlay_apply_mode == 'individual' and dialogue_overlays:
logger.debug('[VideoGenerationService] Preview: Using individual dialogue overlays mode')timed_overlays = VideoGenerationService._build_timed_overlays(project = project, dialogue_overlays = dialogue_overlays)if timed_overlays:
logger.debug(f'''[VideoGenerationService] Preview: Applying {len(timed_overlays)} timed overlay segments''')try:
ffmpeg.apply_timed_atmosphere_overlays(video_path = overlay_input, output_path = str(temp_with_overlays), timed_overlays = timed_overlays)if temp_with_overlays.exists():
if preview_video.exists():
os.remove(str(preview_video))shutil.move(str(temp_with_overlays), str(preview_video))logger.debug('[VideoGenerationService] Preview: Timed overlays applied')else:
logger.debug('[VideoGenerationService] Preview: Timed overlay output not created')if same_file and preview_video.exists() and os.path.exists(overlay_input):
shutil.copy2(overlay_input, str(preview_video))try:
passexcept Exception:
overlay_error = Nonelogger.debug(f'''[VideoGenerationService] Preview: ERROR: Failed to apply timed overlays: {overlay_error}''')if same_file and preview_video.exists() and os.path.exists(overlay_input):
shutil.copy2(overlay_input, str(preview_video))if temp_with_overlays.exists():
os.remove(str(temp_with_overlays))try:
overlay_error = Nonedel overlay_erroroverlay_error = Nonedel overlay_errortry:
logger.debug('[VideoGenerationService] Preview: No valid timed overlays')if same_file and preview_video.exists() and os.path.exists(overlay_input):
shutil.copy2(overlay_input, str(preview_video))elif active_overlays:
logger.debug(f'''[VideoGenerationService] Preview: Applying {len(active_overlays)} atmosphere overlays (global mode)''')try:
ffmpeg.apply_atmosphere_overlays(video_path = overlay_input, output_path = str(temp_with_overlays), overlays = active_overlays)if temp_with_overlays.exists():
if preview_video.exists():
os.remove(str(preview_video))shutil.move(str(temp_with_overlays), str(preview_video))logger.debug('[VideoGenerationService] Preview: Atmosphere overlays applied')else:
logger.debug('[VideoGenerationService] Preview: Overlay output not created')if same_file and preview_video.exists() and os.path.exists(overlay_input):
shutil.copy2(overlay_input, str(preview_video))try:
passexcept Exception:
overlay_error = Nonelogger.debug(f'''[VideoGenerationService] Preview: ERROR: Failed to apply overlays: {overlay_error}''')if same_file and preview_video.exists() and os.path.exists(overlay_input):
shutil.copy2(overlay_input, str(preview_video))if temp_with_overlays.exists():
os.remove(str(temp_with_overlays))try:
overlay_error = Nonedel overlay_erroroverlay_error = Nonedel overlay_errortry:
if same_file and preview_video.exists() and os.path.exists(overlay_input):
shutil.copy2(overlay_input, str(preview_video))temp_files_to_clean = [
temp_video,
temp_with_audio]if temp_with_subtitle != temp_with_audio:
temp_files_to_clean.append(temp_with_subtitle)if has_composer_overlay and temp_with_composer.exists():
temp_files_to_clean.append(temp_with_composer)for temp_file in temp_files_to_clean:
if os.path.exists(str(temp_file)):
os.remove(str(temp_file))try:
continueexcept Exception:
e = Nonelogger.warning(f'''Failed to remove temp file {temp_file}: {e}''')try:
e = Nonedel econtinuee = Nonedel etry:
continueif composer_temp_dir and os.path.exists(composer_temp_dir):
try:
shutil.rmtree(composer_temp_dir, ignore_errors = True)try:
passexcept Exception:
e = Nonelogger.warning(f'''Failed to remove composer temp dir: {e}''')try:
e = Nonedel ee = Nonedel etry:
logger.debug('[VideoGenerationService] ===== PREVIEW GENERATION SUCCESS =====')relative_path = paths.relative_path(preview_video).replace('\\', '/')preview_url = f'''/data/{relative_path}'''{
'status': 'success',
'previewUrl': preview_url }except Exception:
e = Nonefor temp_file in (temp_video, temp_with_audio):
if os.path.exists(str(temp_file)):
os.remove(str(temp_file))continueexcept Exception:
cleanup_err = Nonelogger.warning(f'''Failed to remove temp file {temp_file}: {cleanup_err}''')cleanup_err = Nonedel cleanup_errcontinuecleanup_err = Nonedel cleanup_errif composer_temp_dir and os.path.exists(composer_temp_dir):
shutil.rmtree(composer_temp_dir, ignore_errors = True)else:
except Exception:
cleanup_err = Nonelogger.warning(f'''Failed to remove composer temp dir: {cleanup_err}''')cleanup_err = Nonedel cleanup_errexcept:
cleanup_err = Nonedel cleanup_errraise e = Nonedel e)()
    _merge_consecutive_overlays = (lambda timed_overlays = None: if timed_overlays or len(timed_overlays) < 2:
timed_overlays
def overlays_equal(overlays1 = None, overlays2 = None):
'''두 오버레이 리스트가 동일한지 비교'''
pass# WARNING: Decompyle incomplete
merged = []current = timed_overlays[0].copy()current['overlays'] = list(current['overlays'])for next_seg in timed_overlays[1:]:
is_continuous = next_seg['start_time'] - current['end_time'] < 0.1is_same_overlay = overlays_equal(current['overlays'], next_seg['overlays'])if is_continuous and is_same_overlay:
current['end_time'] = next_seg['end_time']logger.debug(f'''[VideoGenerationService] Merged overlay segment: {current['start_time']:.2f}s - {current['end_time']:.2f}s''')continuemerged.append(current)current = next_seg.copy()current['overlays'] = list(current['overlays'])merged.append(current)logger.debug(f'''[VideoGenerationService] Merged {len(timed_overlays)} segments into {len(merged)} segments''')merged)()
    _resolve_target_language_and_method = (lambda project = None:
