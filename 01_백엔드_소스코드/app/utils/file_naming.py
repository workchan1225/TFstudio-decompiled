# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_naming.pyc (Python 3.11)

'''
파일명 생성 유틸리티

프로젝트 제목을 기반으로 안전한 파일명을 생성합니다.
'''
import re
import unicodedata
import time
from pathlib import Path

def sanitize_filename(filename = None, max_length = None):
    '''
    파일명을 URL 안전하게 변환 (영문/숫자/하이픈/언더스코어만 허용)

    Args:
        filename: 원본 파일명
        max_length: 최대 길이 (기본 50자)

    Returns:
        안전한 파일명 (영문/숫자/하이픈/언더스코어만)
    '''
    filename = unicodedata.normalize('NFC', filename)
    filename = filename.replace(' ', '_')
    filename = re.sub('[^a-zA-Z0-9_-]', '', filename)
    filename = re.sub('_+', '_', filename)
    filename = filename.strip('_')
    if len(filename) > max_length:
        filename = filename[:max_length].rstrip('_')
    if not filename:
        filename = 'untitled'
    return filename


def generate_audio_filename(project_id = None, project_title = None, tts_method = None, extension = ('audio', 'mp3')):
    '''
    오디오 파일명 생성 (고정 파일명으로 덮어쓰기)

    Args:
        project_id: 프로젝트 ID
        project_title: 프로젝트 제목
        tts_method: TTS 방식 (\'typecast\', \'webtts\', \'local\', \'audio\', \'google\', \'edge_tts\' 등)
        extension: 파일 확장자

    Returns:
        파일명 (예: "my_project_edge_tts_abc123.mp3")

    Note:
        - 타임스탬프 없이 고정 파일명 사용 (재생성 시 덮어쓰기)
        - 브라우저 캐시 방지는 URL 쿼리 파라미터로 처리 (audio.mp3?t=timestamp)
    '''
    safe_title = sanitize_filename(project_title, max_length = 30)
    short_id = project_id[:8]
    return f'''{safe_title}_{tts_method}_{short_id}.{extension}'''


def generate_subtitle_filename(project_id = None, project_title = None, extension = None):
    '''
    자막 파일명 생성

    Args:
        project_id: 프로젝트 ID
        project_title: 프로젝트 제목
        extension: 파일 확장자 (srt, ass)

    Returns:
        파일명 (예: "my_project_subtitle_abc123.srt")
    '''
    safe_title = sanitize_filename(project_title, max_length = 30)
    short_id = project_id[:8]
    return f'''{safe_title}_subtitle_{short_id}.{extension}'''


def generate_video_filename(project_id = None, project_title = None, suffix = None, extension = ('final', 'mp4')):
    '''
    영상 파일명 생성

    Args:
        project_id: 프로젝트 ID
        project_title: 프로젝트 제목
        suffix: 파일명 접미사 (final, temp 등)
        extension: 파일 확장자

    Returns:
        파일명 (예: "my_project_final_abc123.mp4")
    '''
    safe_title = sanitize_filename(project_title, max_length = 30)
    short_id = project_id[:8]
    return f'''{safe_title}_{suffix}_{short_id}.{extension}'''


def generate_script_filename(project_id = None, project_title = None):
    '''
    스크립트 파일명 생성

    Args:
        project_id: 프로젝트 ID
        project_title: 프로젝트 제목

    Returns:
        파일명 (예: "my_project_script_abc123.txt")
    '''
    safe_title = sanitize_filename(project_title, max_length = 30)
    short_id = project_id[:8]
    return f'''{safe_title}_script_{short_id}.txt'''
