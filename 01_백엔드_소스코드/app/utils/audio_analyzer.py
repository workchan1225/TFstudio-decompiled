# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: audio_analyzer.pyc (Python 3.11)

'''
오디오 분석 유틸리티 모듈

업로드된 오디오 파일의 메타데이터를 자동으로 분석합니다.
- 오디오 길이, 샘플레이트, 채널 수
- 파일명에서 이름 및 카테고리 추측
- 볼륨 분석 및 추천
'''
import os
import re
import subprocess
import sys
import json
from pathlib import Path
from typing import Dict, Optional, Tuple
import logging
logger = logging.getLogger(__name__)

def _get_ffprobe_path():
    '''FFprobe 경로 반환'''
    get_ffprobe_path = get_ffprobe_path
    import app.config.paths
    return str(get_ffprobe_path())


def _get_hidden_run_kwargs(timeout = None):
    '''Windows GUI 환경에서 콘솔 창 없이 subprocess 실행 kwargs 반환.'''
    kwargs = {
        'capture_output': True,
        'text': True,
        'encoding': 'utf-8',
        'errors': 'replace',
        'timeout': timeout,
        'stdin': subprocess.DEVNULL }
    if sys.platform == 'win32':
        kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW
    return kwargs

CATEGORY_KEYWORDS = {
    'action': [
        'footstep',
        'step',
        'walk',
        'run',
        'door',
        'punch',
        'hit',
        'crash',
        'break',
        'slam',
        'knock',
        'kick',
        'fall',
        'jump',
        'click',
        'typing',
        '발소리',
        '문',
        '타격',
        '충돌',
        '넘어',
        '클릭'],
    'ambient': [
        'ambient',
        'background',
        'atmos',
        'room',
        'office',
        'city',
        'traffic',
        'crowd',
        'cafe',
        'restaurant',
        'indoor',
        'outdoor',
        '배경',
        '환경',
        '분위기',
        '실내',
        '실외',
        '거리'],
    'voice': [
        'voice',
        'vocal',
        'sigh',
        'laugh',
        'cry',
        'scream',
        'gasp',
        'whisper',
        'breath',
        'cough',
        'sneeze',
        '목소리',
        '한숨',
        '웃음',
        '울음',
        '비명',
        '속삭임'],
    'music': [
        'music',
        'stinger',
        'transition',
        'whoosh',
        'swoosh',
        'reveal',
        'tension',
        'suspense',
        'dramatic',
        'fanfare',
        'jingle',
        '음악',
        '전환',
        '긴장',
        '드라마틱'],
    'ui': [
        'ui',
        'button',
        'click',
        'beep',
        'notification',
        'alert',
        'pop',
        'ding',
        'chime',
        'error',
        'success',
        'complete',
        '알림',
        '버튼',
        '완료',
        '에러'],
    'nature': [
        'nature',
        'rain',
        'wind',
        'thunder',
        'bird',
        'water',
        'wave',
        'ocean',
        'fire',
        'forest',
        'river',
        'storm',
        '자연',
        '비',
        '바람',
        '천둥',
        '새',
        '물',
        '파도',
        '불'] }

def parse_filename(filename = None):
    '''
    파일명에서 이름과 카테고리를 추출

    Args:
        filename: 파일명 (예: "footsteps_running_01.wav")

    Returns:
        {
            \'suggested_name\': str,
            \'suggested_category\': str,
            \'original_filename\': str
        }
    '''
    name_without_ext = Path(filename).stem
    parts = re.split('[_\\-\\s]+', name_without_ext)
    cleaned_parts = []
    for part in parts:
        if not re.match('^(v?\\d+|[0-9]+)$', part.lower()):
            cleaned_parts.append(part)
    suggested_name = (lambda .0: pass# WARNING: Decompyle incomplete
)(cleaned_parts()) if cleaned_parts else name_without_ext
    suggested_category = 'action'
    filename_lower = filename.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in filename_lower:
                suggested_category = category
                ' '.join
            
            if suggested_category != 'action':
                ' '.join
            
            return {
                'suggested_name': suggested_name,
                'suggested_category': suggested_category,
                'original_filename': filename }


def analyze_audio_file(file_path = None, original_filename = None):
    """
    오디오 파일 메타데이터 분석

    Args:
        file_path: 오디오 파일 경로
        original_filename: 원본 파일명 (선택, 파일명 분석에 사용)

    Returns:
        {
            'duration': float,  # 초
            'sample_rate': int,
            'channels': int,
            'codec': str,
            'format': str,
            'bitrate': int,
            'peak_volume': float,  # dB
            'mean_volume': float,  # dB
            'recommended_volume': float,  # 0.0~1.0
            'suggested_name': str,
            'suggested_category': str,
            'file_size': int,  # bytes
        }
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'''Audio file not found: {file_path}''')
    result = {
        'duration': 0,
        'sample_rate': 44100,
        'channels': 2,
        'codec': 'unknown',
        'format': 'unknown',
        'bitrate': 0,
        'peak_volume': 0,
        'mean_volume': -20,
        'recommended_volume': 0.7,
        'file_size': os.path.getsize(file_path) }
# WARNING: Decompyle incomplete


def get_audio_duration(file_path = None):
    '''
    오디오 파일 길이만 빠르게 조회

    Args:
        file_path: 오디오 파일 경로

    Returns:
        길이 (초)
    '''
    pass
# WARNING: Decompyle incomplete


def validate_audio_file(file_path = None):
    '''
    오디오 파일 유효성 검사

    Args:
        file_path: 오디오 파일 경로

    Returns:
        (유효 여부, 에러 메시지)
    '''
    if not os.path.exists(file_path):
        return (False, 'File not found')
    file_size = None.path.getsize(file_path)
    if file_size > 314572800:
        return (False, 'File too large (max 300MB)')
    if None == 0:
        return (False, 'File is empty')
    ext = None(file_path).suffix.lower()
    allowed_extensions = [
        '.wav',
        '.mp3',
        '.ogg',
        '.flac',
        '.m4a',
        '.aac']
    if ext not in allowed_extensions:
        return (False, f'''Unsupported format. Allowed: {', '.join(allowed_extensions)}''')
    
    try:
        duration = get_audio_duration(file_path)
        if duration <= 0:
            return (False, 'Invalid audio file or cannot read duration')
        if None > 300:
            return (False, 'Audio too long (max 5 minutes)')
    except Exception:
        e = None
        del e
        return None
        None = 
        del e
        return (True, '')



def analyze_loudness(file_path = None):
    """
    LUFS 기반 음량 분석 (EBU R128)

    FFmpeg loudnorm 필터의 1-pass 분석을 사용하여
    오디오의 통합 음량(LUFS), True Peak, Loudness Range를 측정합니다.

    Args:
        file_path: 오디오 파일 경로

    Returns:
        {
            'input_i': float,       # Integrated loudness (LUFS)
            'input_tp': float,      # True peak (dBTP)
            'input_lra': float,     # Loudness range (LU)
            'input_thresh': float,  # Threshold (LUFS)
            'success': bool,        # 분석 성공 여부
            'error': str            # 에러 메시지 (실패 시)
        }
    """
    result = {
        'input_i': -23,
        'input_tp': -1,
        'input_lra': 7,
        'input_thresh': -33,
        'success': False,
        'error': None }
    if not os.path.exists(file_path):
        result['error'] = f'''File not found: {file_path}'''
        return result
# WARNING: Decompyle incomplete
