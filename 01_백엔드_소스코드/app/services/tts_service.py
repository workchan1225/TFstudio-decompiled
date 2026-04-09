# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tts_service.pyc (Python 3.11)

'''
TTSService - TTS 생성 및 오디오 관리 서비스
'''
import sys
import subprocess
from pathlib import Path
from typing import Dict, Any
from sqlalchemy.orm.attributes import flag_modified
from app.models.project import Project
from app.utils.ffmpeg_utils import get_ffmpeg_executable
from app.utils.file_paths import ProjectPaths
from app.services.typecast_service import TypecastService
from app.utils.atomic_media_write import atomic_audio_output
from app.utils.file_naming import generate_audio_filename
from app.utils.script_text_cleaner import clean_script_for_subtitle
from app import db

class TTSService:
    '''
    TTS 생성 및 오디오 파일 관리 서비스

    책임:
    - Typecast TTS 생성
    - 오디오 파일 업로드 및 변환
    - 오디오 메타데이터 관리
    - TTS 설정 저장
    '''
    generate_tts_from_script = (lambda project = None, typecast_api_key = None, voice_settings = staticmethod: if not project.script:
raise ValueError('No script found')project_id = project.idtypecast_service = TypecastService(typecast_api_key)paths = ProjectPaths(project_id)paths.ensure_directories()audio_path = paths.audio_path('audio.mp3')voice_id = voice_settings.get('voiceId')speed = voice_settings.get('speed', 1)pitch = voice_settings.get('pitch', 0)volume = voice_settings.get('volume', 100)emotion = voice_settings.get('emotion', 'normal')emotion_intensity = voice_settings.get('emotionIntensity', 1)clean_text = clean_script_for_subtitle(project.script)result = typecast_service.generate_speech(text = clean_text, voice_id = voice_id, speed = speed, pitch = pitch, volume = volume, emotion = emotion, emotion_intensity = emotion_intensity, output_path = str(audio_path))if result['status'] != 'success':
error_msg = result.get('message', 'TTS 생성 실패')raise ValueError(error_msg)project.audio_url = paths.relative_path(audio_path)TTSService._save_tts_settings(project, voice_settings)TTSService._update_progress(project, has_tts = True)try:
db.session.commit()except Exception:
e = Nonedb.session.rollback()raise RuntimeError(f'''데이터베이스 저장 실패: {e}''')e = Nonedel e{
'status': 'success',
'audioUrl': str(audio_path) })()
    upload_audio_file = (lambda project = None, file = None: project_id = project.idif file or file.filename == '':
raise ValueError('No file selected')allowed_extensions = {
'm4a',
'mp3',
'mp4',
'ogg',
'wav',
'flac'}if '.' not in file.filename:
raise ValueError('File must have an extension')file_ext = file.filename.rsplit('.', 1)[1].lower().strip()if not file_ext:
raise ValueError('Invalid file extension')if file_ext not in allowed_extensions:
raise ValueError(f'''Unsupported file type: .{file_ext}. Allowed: {', '.join(allowed_extensions)}''')paths = ProjectPaths(project_id)paths.ensure_directories()if not project.title:
filename = generate_audio_filename(project_id, 'untitled', tts_method = 'local', extension = 'mp3')output_path = paths.audio_path(filename)if file_ext != 'mp3':
TTSService._convert_to_mp3(file, file_ext, output_path, paths)else:
atomic_output_path = atomic_audio_output(output_path)file.save(atomic_output_path)None(None, None)else:
with None:
if not None:
passrelative_audio_path = paths.relative_path(output_path)if not project.active_script_language:
active_language = '한국어'project.set_tts_audio_url_for_language('local-upload', relative_audio_path, active_language)project.set_selected_tts_method_for_language('local-upload', active_language)if active_language == '한국어':
project.audio_url = relative_audio_pathTTSService._update_progress(project, has_tts = True)try:
db.session.commit()except Exception:
e = Nonedb.session.rollback()raise RuntimeError(f'''데이터베이스 저장 실패: {e}''')e = Nonedel eaudio_url = f'''/data/{relative_audio_path}'''.replace('\\', '/')print(f'''[TTSService] Audio uploaded successfully: {audio_url} (lang={active_language})'''){
'success': True,
'audioUrl': audio_url,
'audio_url': audio_url,
'relativeAudioPath': relative_audio_path,
'activeScriptLanguage': active_language,
'selectedTtsMethod': 'local-upload',
'message': 'Audio uploaded successfully' })()
    _convert_to_mp3 = (lambda file = None, file_ext = None, output_path = staticmethod, paths = ('file', Any, 'file_ext', str, 'output_path', Path, 'paths', ProjectPaths): temp_path = paths.temp_path(f'''temp.{file_ext}''')file.save(str(temp_path))ffmpeg_path = get_ffmpeg_executable()# WARNING: Decompyle incomplete
)()
    _save_tts_settings = (lambda project = None, voice_settings = None: if not project.video_settings:
project.video_settings = { }settings = dict(project.video_settings) if project.video_settings else { }settings['voice'] = voice_settings.get('voiceId')settings['speed'] = voice_settings.get('speed', 1)settings['pitch'] = voice_settings.get('pitch', 0)settings['volume'] = voice_settings.get('volume', 100)settings['emotion'] = voice_settings.get('emotion', 'normal')settings['emotionIntensity'] = voice_settings.get('emotionIntensity', 1)project.video_settings = settingsflag_modified(project, 'video_settings'))()
    _update_progress = (lambda project = None, has_tts = None: if has_tts and project.mixed_audio_url:
import logginglogger = logging.getLogger(__name__)logger.info(f'''[TTSService] Invalidating mixed_audio_url due to TTS change: {project.mixed_audio_url}''')project.mixed_audio_url = Noneif not project.direct_progress:
project.direct_progress = { }progress = dict(project.direct_progress)progress['hasTTS'] = has_ttsif has_tts and progress.get('hasBGM'):
progress['hasBGM'] = Falseproject.direct_progress = progressflag_modified(project, 'direct_progress'))()
    select_tts_method = (lambda project = None, method = None: valid_methods = {
'qwen3',
'typecast',
'web-tts',
'edge-tts',
'no-voice',
'gemini-voice',
'google-voice',
'local-upload',
'gemini-native',
'speaker-merged'}if method not in valid_methods:
raise ValueError(f'''Invalid TTS method: {method}''')project.selected_tts_method = methodif method == 'no-voice':
project.audio_url = Noneprint('[TTSService] No-voice mode selected, clearing audio URLs')Noneif None == 'typecast':
if project.typecast_audio_url:
project.audio_url = project.typecast_audio_urlprint(f'''[TTSService] Set audio_url from typecast: {project.audio_url}''')else:
print('[TTSService] Typecast method selected but audio not yet generated')elif method == 'web-tts':
if project.web_tts_audio_url:
project.audio_url = project.web_tts_audio_urlprint(f'''[TTSService] Set audio_url from web-tts: {project.audio_url}''')else:
print('[TTSService] Web TTS method selected but audio not yet generated')elif method == 'local-upload':
if project.local_audio_url:
project.audio_url = project.local_audio_urlprint(f'''[TTSService] Set audio_url from local-upload: {project.audio_url}''')else:
print('[TTSService] Local upload method selected but audio not yet uploaded')elif method == 'google-voice':
if project.google_cloud_tts_audio_url:
project.audio_url = project.google_cloud_tts_audio_urlprint(f'''[TTSService] Set audio_url from google-voice: {project.audio_url}''')else:
print('[TTSService] Google Cloud TTS method selected but audio not yet generated')elif method == 'gemini-voice':
if project.gemini_tts_audio_url:
project.audio_url = project.gemini_tts_audio_urlprint(f'''[TTSService] Set audio_url from gemini-voice: {project.audio_url}''')else:
print('[TTSService] Gemini TTS method selected but audio not yet generated')elif method == 'speaker-merged':
if project.speaker_merged_audio_url:
project.audio_url = project.speaker_merged_audio_urlprint(f'''[TTSService] Set audio_url from speaker-merged: {project.audio_url}''')else:
print('[TTSService] Speaker-merged method selected but audio not yet generated')elif method == 'edge-tts':
if project.edge_tts_audio_url:
project.audio_url = project.edge_tts_audio_urlprint(f'''[TTSService] Set audio_url from edge-tts: {project.audio_url}''')else:
print('[TTSService] Edge TTS method selected but audio not yet generated')elif method == 'qwen3':
if project.qwen3_tts_audio_url:
project.audio_url = project.qwen3_tts_audio_urlprint(f'''[TTSService] Set audio_url from qwen3: {project.audio_url}''')else:
print('[TTSService] Qwen3 TTS method selected but audio not yet generated')elif method == 'gemini-native':
if project.gemini_native_tts_audio_url:
project.audio_url = project.gemini_native_tts_audio_urlprint(f'''[TTSService] Set audio_url from gemini-native: {project.audio_url}''')else:
print('[TTSService] Gemini Native TTS method selected but audio not yet generated')if project.subtitle_url:
print(f'''[TTSService] Subtitle already exists: {project.subtitle_url}''')None)()
