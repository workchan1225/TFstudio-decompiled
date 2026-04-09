# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: srt_mp4_export_service.pyc (Python 3.11)

"""
SRT + MP4 Export Service

TFstudio 프로젝트를 SRT 자막 파일 + MP4 영상(자막 없음)으로 내보내기
- SRT (UTF-8 BOM) - 범용 자막 형식
- MP4 - 이미지 + 오디오만 (자막 미포함)

Vrew 워크플로우:
1. Vrew에서 MP4 영상 불러오기
2. 자막 패널 > '파일에서 자막 가져오기'로 SRT 불러오기
"""
import logging
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from app.models.project import Project
from app.utils.file_paths import ProjectPaths, resolve_data_path
from app.config.paths import get_data_path, get_ffmpeg_path
logger = logging.getLogger(__name__)

class SrtMp4ExportService:
    '''TFstudio 프로젝트를 SRT + MP4 형식으로 내보내기 (자막 미포함 영상)'''
    export = (lambda project = None, orientation = None, export_srt = staticmethod, export_mp4 = ('horizontal', True, True): pass# WARNING: Decompyle incomplete
)()
    _get_subtitle_segments = (lambda project = None: if not project.video_settings:
video_settings = { }if not project.active_script_language:
target_language = '한국어'if not project.get_selected_tts_method_for_language(target_language):
if not project.selected_tts_method:
selected_method = 'unknown'uses_trimmed = project.is_using_trimmed_audio(target_language, selected_method)logger.info(f'''[SrtMp4Export] Getting subtitles, usesTrimmedAudio={uses_trimmed}''')segments = []source = 'unknown'if uses_trimmed:
adjusted_layers = Nonesilence_variant = project.get_silence_variant(target_language, selected_method)if isinstance(silence_variant, dict):
variant_layers = silence_variant.get('adjusted_subtitle_layers')if isinstance(variant_layers, list) and variant_layers:
adjusted_layers = variant_layersadjusted_by_language = video_settings.get('adjusted_subtitle_layers_by_language', { })if adjusted_layers and isinstance(adjusted_by_language, dict) and target_language in adjusted_by_language:
adjusted_layers = adjusted_by_language.get(target_language)if not adjusted_layers:
adjusted_layers = video_settings.get('adjusted_subtitle_layers', [])if adjusted_layers:
segments = SrtMp4ExportService._extract_segments_from_layers(adjusted_layers, project, target_language)source = 'adjusted_subtitle_layers (무음 제거 버전)'if not segments:
subtitle_layers = Noneif project.subtitle_layers_by_language and isinstance(project.subtitle_layers_by_language, dict):
subtitle_layers = project.subtitle_layers_by_language.get(target_language)if not subtitle_layers:
subtitle_layers = project.subtitle_layersif subtitle_layers:
segments = SrtMp4ExportService._extract_segments_from_layers(subtitle_layers, project, target_language)source = 'subtitle_layers (원본 버전)'if segments:
logger.info(f'''[SrtMp4Export] Using subtitles from \'{source}\': {len(segments)} segments''')segmentsNone.warning('[SrtMp4Export] No subtitles found')[])()
    _extract_segments_from_layers = (lambda layers = None, project = None, target_language = staticmethod: segments = []voice_type_to_layer_id = {
'chirp3-hd': 'chirp3hd-tts-layer',
'neural2': 'google-tts-layer',
'edge': 'edge-tts-layer',
'edge-tts': 'edge-tts-layer',
'elevenlabs': 'elevenlabs-tts-layer',
'web': 'web-tts-layer' }selected_method = project.get_selected_tts_method_for_language(target_language)if selected_method == 'speaker-merged':
active_layer_id = 'speaker-tts-layer'elif selected_method == 'elevenlabs':
active_layer_id = 'elevenlabs-tts-layer'else:
primary_voice_type = Nonespeaker_data = project.get_speaker_tts_data_for_language(target_language)if speaker_data:
primary_voice_type = speaker_data.get('primaryVoiceType')active_layer_id = voice_type_to_layer_id.get(primary_voice_type) if primary_voice_type else Noneif active_layer_id:
for layer in layers:
if not isinstance(layer, dict) or layer.get('segments'):
continueif layer.get('id', '') == active_layer_id:
for seg in layer.get('segments', []):
segments.append({
'start': seg.get('start', 0),
'end': seg.get('end', 0),
'text': seg.get('text', ''),
'speaker': seg.get('speaker', '') })if not segments:
for layer in layers:
if not isinstance(layer, dict) or layer.get('segments'):
continueif not layer.get('visible', True):
continuefor seg in layer.get('segments', []):
segments.append({
'start': seg.get('start', 0),
'end': seg.get('end', 0),
'text': seg.get('text', ''),
'speaker': seg.get('speaker', '') })segments)()
    _get_intro_duration = (lambda project = None: try:
if not project.video_settings:
video_settings = { }if isinstance(video_settings, str):
import jsonvideo_settings = json.loads(video_settings)intro_data = video_settings.get('introData')if not intro_data and isinstance(intro_data, dict) or intro_data.get('enabled'):
0None(intro_data.get('duration', 0))except Exception:
0)()
    _prepend_intro_images = (lambda project = None, data_dir = None, images_info = staticmethod: pass# WARNING: Decompyle incomplete
)()
    _get_images_timeline = (lambda project = None, data_dir = None, orientation = staticmethod: if not project.video_settings:
video_settings = { }uploaded_images = video_settings.get('uploadedImages', [])image_timeline = video_settings.get('imageTimeline', { })timeline_segments = image_timeline.get('segments', [])if not uploaded_images or timeline_segments:
SrtMp4ExportService._get_scene_based_images(project, data_dir, orientation)images_info = Nonefor seg in timeline_segments:
img_idx = seg.get('imageIndex', 0)if  <= 0, img_idx or 0, img_idx < len(uploaded_images):
passif not img_info.get('url'):
img_info.get('path', '') = uploaded_images[img_idx]if not img_url:
continueimg_path = SrtMp4ExportService._resolve_media_path(img_url, data_dir)if img_path.exists():
images_info.append({
'path': str(img_path),
'start_time': seg.get('startTime', 0),
'end_time': seg.get('endTime', 0),
'duration': seg.get('duration', seg.get('endTime', 0) - seg.get('startTime', 0)) })images_info)()
    _get_scene_based_images = (lambda project = None, data_dir = None, orientation = staticmethod: if not project.scenes:
[]segments = None._get_subtitle_segments(project)scene_timings = { }# WARNING: Decompyle incomplete
)()
    _generate_srt = (lambda segments = None, srt_format = None: use_period = srt_format == 'capcut'srt_lines = []entry_index = 1for seg in segments:
text = seg.get('text', '').strip()if not text:
continuestart_sec = seg.get('start', 0)end_sec = seg.get('end', 0)srt_lines.append(str(entry_index))start_tc = SrtMp4ExportService._seconds_to_srt_timecode(start_sec, use_period)end_tc = SrtMp4ExportService._seconds_to_srt_timecode(end_sec, use_period)srt_lines.append(f'''{start_tc} --> {end_tc}''')srt_lines.append(text)srt_lines.append('')entry_index += 1'\n'.join(srt_lines))()
    _seconds_to_srt_timecode = (lambda seconds = None, use_period = None: hours = int(seconds // 3600)minutes = int((seconds % 3600) // 60)secs = int(seconds % 60)millis = int((seconds % 1) * 1000)separator = '.' if use_period else ','f'''{hours:02d}:{minutes:02d}:{secs:02d}{separator}{millis:03d}''')()
    _generate_mp4 = (lambda images_info = None, audio_path = None, output_path = staticmethod, orientation = ('images_info', List[Dict], 'audio_path', Path, 'output_path', Path, 'orientation', str, 'return', None): FFmpegWrapper = FFmpegWrapperimport app.utils.ffmpeg_wrapperif orientation == 'vertical':
(width, height) = (1080, 1920)else:
(width, height) = (1920, 1080)ffmpeg = FFmpegWrapper()audio_duration = ffmpeg.get_video_duration(str(audio_path))if not len(images_info) == 1 or images_info:
single_image = images_info[0]['path'] if images_info else Noneif single_image:
SrtMp4ExportService._generate_single_image_mp4(image_path = single_image, audio_path = audio_path, output_path = output_path, duration = audio_duration, width = width, height = height)NoneNone._generate_multi_image_mp4(images_info = images_info, audio_path = audio_path, output_path = output_path, audio_duration = audio_duration, width = width, height = height))()
    _generate_single_image_mp4 = (lambda image_path, audio_path, output_path = None, duration = None, width = staticmethod, height = ('image_path', str, 'audio_path', Path, 'output_path', Path, 'duration', float, 'width', int, 'height', int, 'return', None): ffmpeg_exe = str(get_ffmpeg_path())video_extensions = {
'.avi',
'.m4v',
'.mkv',
'.mov',
'.webm',
'.mp4'}file_ext = Path(image_path).suffix.lower()is_video = file_ext in video_extensionslogger.info(f'''[SrtMp4Export] Single media: path={image_path}, ext={file_ext}, is_video={is_video}''')if is_video:
cmd = [
ffmpeg_exe,
'-y',
'-stream_loop',
'-1',
'-i',
image_path,
'-i',
str(audio_path),
'-c:v',
'libx264',
'-c:a',
'aac',
'-b:a',
'192k',
'-pix_fmt',
'yuv420p',
'-vf',
f'''scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2''',
'-shortest',
'-t',
str(duration),
str(output_path)]else:
cmd = [
ffmpeg_exe,
'-y',
'-loop',
'1',
'-i',
image_path,
'-i',
str(audio_path),
'-c:v',
'libx264',
'-tune',
'stillimage',
'-c:a',
'aac',
'-b:a',
'192k',
'-pix_fmt',
'yuv420p',
'-vf',
f'''scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2''',
'-shortest',
'-t',
str(duration),
str(output_path)]logger.info(f'''[SrtMp4Export] Running FFmpeg: {' '.join(cmd)}''')run_kwargs = {
'capture_output': True,
'text': True,
'encoding': 'utf-8',
'errors': 'replace',
'stdin': subprocess.DEVNULL }if sys.platform == 'win32':
run_kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW# WARNING: Decompyle incomplete
)()
    _generate_multi_image_mp4 = (lambda images_info, audio_path, output_path = None, audio_duration = None, width = staticmethod, height = ('images_info', List[Dict], 'audio_path', Path, 'output_path', Path, 'audio_duration', float, 'width', int, 'height', int, 'return', None): ffmpeg_exe = str(get_ffmpeg_path())temp_dir = output_path.parent / 'temp_concat'temp_dir.mkdir(exist_ok = True)# WARNING: Decompyle incomplete
)()
    _resolve_media_path = (lambda url = None, data_dir = None: url = url.replace('\\', '/')if url.startswith('/api/media/'):
relative_path = url.replace('/api/media/', '')data_dir / relative_pathif None.startswith('/data/'):
relative_path = url.replace('/data/', '')data_dir / relative_pathif None.startswith('data/'):
relative_path = url.replace('data/', '')data_dir / relative_pathif None.startswith('projects/'):
data_dir / urlif None(url).is_absolute():
Path(url)None / url)()
