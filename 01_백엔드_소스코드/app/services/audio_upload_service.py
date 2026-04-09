# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: audio_upload_service.pyc (Python 3.11)

'''
AudioUploadService - 오디오 파일 업로드 서비스 (Voice, BGM)
'''
import sys
import subprocess
from pathlib import Path
from typing import Dict, Any
from werkzeug.datastructures import FileStorage
from app.models.project import Project
from app.utils.file_paths import ProjectPaths
from app.utils.ffmpeg_utils import get_ffmpeg_executable
from app.utils.atomic_media_write import atomic_audio_output
from app import db

class AudioUploadService:
    '''
    오디오 파일 업로드 서비스

    책임:
    - Voice 파일 업로드 및 변환
    - BGM 파일 업로드 및 변환
    - MP3 형식으로 통일 (FFmpeg 사용)
    '''
    ALLOWED_EXTENSIONS = {
        'm4a',
        'mp3',
        'ogg',
        'wav',
        'flac'}
    upload_audio = (lambda project = None, file = None, audio_type = staticmethod: AudioUploadService._validate_file(file)file_ext = file.filename.rsplit('.', 1)[1].lower().strip()if file_ext not in AudioUploadService.ALLOWED_EXTENSIONS:
raise ValueError(f'''Unsupported file type: .{file_ext}''')paths = ProjectPaths(project.id)paths.ensure_directories()output_filename = f'''{audio_type}.mp3'''output_path = paths.audio_path(output_filename)if file_ext != 'mp3':
audio_url = AudioUploadService._convert_to_mp3(file, file_ext, output_path, paths, audio_type)else:
atomic_output_path = atomic_audio_output(output_path)file.save(atomic_output_path)None(None, None)with None:
if not None:
passaudio_url = paths.relative_path(output_path)db.session.commit(){
'audio_url': audio_url,
'message': f'''{'음성' if audio_type == 'voice' else '배경음악'} 파일이 업로드되었습니다''' })()
    _validate_file = (lambda file = None: if not file:
raise ValueError('No file provided')if file.filename == '':
raise ValueError('No file selected')if '.' not in file.filename:
raise ValueError('File must have an extension'))()
    _convert_to_mp3 = (lambda file, file_ext = None, output_path = None, paths = staticmethod, audio_type = ('file', FileStorage, 'file_ext', str, 'output_path', Path, 'paths', ProjectPaths, 'audio_type', str, 'return', str): temp_path = paths.temp_path(f'''temp_{audio_type}.{file_ext}''')file.save(str(temp_path))ffmpeg_path = get_ffmpeg_executable()run_kwargs = {
'check': True,
'stdin': subprocess.DEVNULL }if sys.platform == 'win32':
run_kwargs['creationflags'] = subprocess.CREATE_NO_WINDOWatomic_output_path = atomic_audio_output(output_path)# WARNING: Decompyle incomplete
)()
