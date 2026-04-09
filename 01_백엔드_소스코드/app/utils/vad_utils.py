# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vad_utils.pyc (Python 3.11)

'''
Voice Activity Detection (VAD) 유틸리티

silero-vad를 사용하여 음성 구간을 감지하고,
긴 오디오를 무음 경계에서 스마트하게 분할합니다.

주요 기능:
- 음성 구간 감지 (Voice Activity Detection)
- 무음 경계 기반 스마트 청크 분할
- 청크 오버랩 처리
'''
import os
import sys
import logging
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import subprocess
import tempfile
from app.utils.ffmpeg_utils import get_ffmpeg_executable, get_ffprobe_executable
logger = logging.getLogger(__name__)
_vad_model = None
_vad_utils = None

def log_debug(msg = None):
    '''디버그 로깅'''
    print(f'''[VAD] {msg}''')
    logger.info(msg)


def get_vad_model():
    '''
    Silero VAD 모델 로드 (캐싱됨)

    Returns:
        tuple: (model, utils) - VAD 모델과 유틸리티 함수
    '''
    pass
# WARNING: Decompyle incomplete


def read_audio_ffmpeg(audio_path = None, sample_rate = None):
    '''
    FFmpeg를 사용하여 오디오를 로드하고 torch tensor로 변환

    torchaudio 2.9+에서 torchcodec 의존성 문제를 우회합니다.

    Args:
        audio_path: 오디오 파일 경로
        sample_rate: 목표 샘플링 레이트

    Returns:
        torch.Tensor: 오디오 파형 (1D)
    '''
    import torch
    import numpy as np
    ffmpeg_exe = get_ffmpeg_executable()
    cmd = [
        ffmpeg_exe,
        '-y',
        '-i',
        audio_path,
        '-ar',
        str(sample_rate),
        '-ac',
        '1',
        '-f',
        's16le',
        '-acodec',
        'pcm_s16le',
        'pipe:1']
    run_kwargs = {
        'capture_output': True,
        'stdin': subprocess.DEVNULL }
    if sys.platform == 'win32':
        run_kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW
# WARNING: Decompyle incomplete


def detect_speech_timestamps(audio_path = None, sample_rate = None, min_speech_duration_ms = None, min_silence_duration_ms = (16000, 250, 300, 0.5), threshold = ('audio_path', str, 'sample_rate', int, 'min_speech_duration_ms', int, 'min_silence_duration_ms', int, 'threshold', float, 'return', List[Dict])):
    """
    오디오에서 음성 구간 감지

    Args:
        audio_path: 오디오 파일 경로
        sample_rate: 샘플링 레이트 (기본 16000)
        min_speech_duration_ms: 최소 음성 지속 시간 (ms)
        min_silence_duration_ms: 최소 무음 지속 시간 (ms)
        threshold: VAD 임계값 (0.0-1.0)

    Returns:
        [{'start': float, 'end': float}, ...] 음성 구간 리스트 (초 단위)
    """
    
    try:
        import torch
        (model, utils) = get_vad_model()
        (get_speech_timestamps, save_audio, read_audio, VADIterator, collect_chunks) = utils
        log_debug(f'''Detecting speech in: {audio_path}''')
        
        try:
            wav = read_audio_ffmpeg(audio_path, sample_rate = sample_rate)
            log_debug(f'''Audio loaded via FFmpeg: {len(wav)} samples ({len(wav) / sample_rate:.1f}s)''')
            
            try:
                pass
            except Exception:
                ffmpeg_err = None
                log_debug(f'''FFmpeg audio load failed, trying torchaudio: {ffmpeg_err}''')
                wav = read_audio(audio_path, sampling_rate = sample_rate)
                
                try:
                    ffmpeg_err = None
                    del ffmpeg_err
                ffmpeg_err = None
                del ffmpeg_err
                try:
                    speech_timestamps = get_speech_timestamps(wav, model, sampling_rate = sample_rate, min_speech_duration_ms = min_speech_duration_ms, min_silence_duration_ms = min_silence_duration_ms, threshold = threshold, return_seconds = True)
                    log_debug(f'''Detected {len(speech_timestamps)} speech segments''')
                    result = []
                    for ts in speech_timestamps:
                        result.append({
                            'start': float(ts['start']),
                            'end': float(ts['end']) })
                        return result
                        except ImportError:
                            log_debug('VAD not available, returning empty timestamps')
                            return 
                        except Exception:
                            log_debug(f'''Speech detection failed: {e}''')
                            import traceback = None
                            traceback.print_exc()
                            del e
                            return None
                            None = 
                            del e






def find_silence_boundaries(speech_timestamps = None, audio_duration = None, min_silence_gap = None):
    '''
    음성 구간 사이의 무음 경계 찾기

    Args:
        speech_timestamps: 음성 구간 리스트
        audio_duration: 전체 오디오 길이 (초)
        min_silence_gap: 최소 무음 간격 (초)

    Returns:
        무음 경계 시간 리스트 (초)
    '''
    if not speech_timestamps:
        return []
    boundaries = None
    if speech_timestamps[0]['start'] >= min_silence_gap:
        boundaries.append(speech_timestamps[0]['start'] / 2)
    for i in range(len(speech_timestamps) - 1):
        current_end = speech_timestamps[i]['end']
        next_start = speech_timestamps[i + 1]['start']
        gap = next_start - current_end
        if gap >= min_silence_gap:
            boundary = current_end + gap / 2
            boundaries.append(boundary)
        if audio_duration - speech_timestamps[-1]['end'] >= min_silence_gap:
            boundaries.append(speech_timestamps[-1]['end'] + min_silence_gap / 2)
    log_debug(f'''Found {len(boundaries)} silence boundaries''')
    return boundaries


def smart_chunk_audio(audio_path = None, max_chunk_duration = None, min_chunk_duration = None, overlap_duration = (50, 10, 0.5, 0.5), min_silence_gap = ('audio_path', str, 'max_chunk_duration', float, 'min_chunk_duration', float, 'overlap_duration', float, 'min_silence_gap', float, 'return', List[Dict])):
    """
    VAD 기반 스마트 오디오 청크 분할

    음성 구간을 분석하여 무음 경계에서만 분할합니다.
    이를 통해 말 중간에서 잘리는 문제를 방지합니다.

    Args:
        audio_path: 오디오 파일 경로
        max_chunk_duration: 최대 청크 길이 (초)
        min_chunk_duration: 최소 청크 길이 (초)
        overlap_duration: 청크 간 오버랩 (초)
        min_silence_gap: 최소 무음 간격 (초)

    Returns:
        [{'start': float, 'end': float, 'has_overlap': bool}, ...]
    """
    log_debug(f'''Smart chunking audio: {audio_path}''')
    log_debug(f'''  max_chunk: {max_chunk_duration}s, min_chunk: {min_chunk_duration}s''')
    audio_duration = get_audio_duration(audio_path)
    if audio_duration <= 0:
        log_debug('Could not determine audio duration')
        return []
    None(f'''  audio_duration: {audio_duration:.1f}s''')
    if audio_duration <= max_chunk_duration:
        log_debug('Audio shorter than max_chunk, no splitting needed')
        return [
            {
                'start': 0,
                'end': audio_duration,
                'has_overlap': False }]
    speech_timestamps = None(audio_path)
    if not speech_timestamps:
        log_debug('VAD failed, falling back to fixed chunking')
        return fixed_chunk_audio(audio_path, max_chunk_duration, overlap_duration)
    silence_boundaries = None(speech_timestamps, audio_duration, min_silence_gap)
    chunks = []
    current_start = 0
# WARNING: Decompyle incomplete


def fixed_chunk_audio(audio_path = None, chunk_duration = None, overlap_duration = None):
    """
    고정 길이 청크 분할 (VAD 폴백용)

    Args:
        audio_path: 오디오 파일 경로
        chunk_duration: 청크 길이 (초)
        overlap_duration: 청크 간 오버랩 (초)

    Returns:
        [{'start': float, 'end': float, 'has_overlap': bool}, ...]
    """
    audio_duration = get_audio_duration(audio_path)
    if audio_duration <= 0:
        return []
    chunks = None
    current_start = 0
# WARNING: Decompyle incomplete


def get_audio_duration(audio_path = None):
    '''
    오디오 파일 길이 확인 (초)

    Args:
        audio_path: 오디오 파일 경로

    Returns:
        오디오 길이 (초), 실패 시 0.0
    '''
    pass
# WARNING: Decompyle incomplete


def extract_chunk_audio(audio_path, start_time = None, end_time = None, output_path = None, add_silence_padding = (0, 16000), sample_rate = ('audio_path', str, 'start_time', float, 'end_time', float, 'output_path', str, 'add_silence_padding', float, 'sample_rate', int, 'return', bool)):
    '''
    오디오에서 청크 추출

    Args:
        audio_path: 원본 오디오 경로
        start_time: 시작 시간 (초)
        end_time: 종료 시간 (초)
        output_path: 출력 파일 경로
        add_silence_padding: 시작에 추가할 무음 (초)
        sample_rate: 샘플링 레이트

    Returns:
        성공 여부
    '''
    duration = end_time - start_time
# WARNING: Decompyle incomplete


def merge_overlapping_segments(segments = None, overlap_threshold = None):
    """
    오버랩된 세그먼트 병합

    청크 경계에서 중복된 세그먼트를 제거합니다.

    Args:
        segments: 세그먼트 리스트 [{'start': float, 'end': float, 'text': str}, ...]
        overlap_threshold: 중복 판단 임계값 (초)

    Returns:
        병합된 세그먼트 리스트
    """
    if not segments:
        return []
    sorted_segments = None(segments, key = (lambda x: x['start']))
    merged = []
    for seg in sorted_segments:
        if not merged:
            merged.append(seg.copy())
            continue
        last = merged[-1]
        overlap = last['end'] - seg['start']
        if overlap > overlap_threshold:
            if len(seg.get('text', '')) > len(last.get('text', '')):
                merged[-1] = seg.copy()
            continue
        if overlap > 0:
            merged[-1]['end'] = seg['start'] - 0.05
            merged.append(seg.copy())
            continue
        merged.append(seg.copy())
        log_debug(f'''Merged {len(segments)} -> {len(merged)} segments''')
        return merged


def test_vad(audio_path = None):
    '''VAD 테스트'''
    log_debug(f'''Testing VAD on: {audio_path}''')
    duration = get_audio_duration(audio_path)
    log_debug(f'''Audio duration: {duration:.1f}s''')
    speech_ts = detect_speech_timestamps(audio_path)
    log_debug(f'''Speech segments: {len(speech_ts)}''')
    for i, ts in enumerate(speech_ts[:10]):
        log_debug(f'''  {i + 1}. {ts['start']:.2f}s - {ts['end']:.2f}s''')
        chunks = smart_chunk_audio(audio_path)
        log_debug(f'''Smart chunks: {len(chunks)}''')
        return {
            'duration': duration,
            'speech_segments': len(speech_ts),
            'chunks': len(chunks) }
