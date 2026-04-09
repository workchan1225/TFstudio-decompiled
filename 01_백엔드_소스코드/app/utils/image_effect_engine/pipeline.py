# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pipeline.pyc (Python 3.11)

'''
FFmpeg 파이프라인

OpenCV로 생성한 프레임을 stdin pipe로 FFmpeg에 전달하여
GPU 가속(NVENC) 또는 CPU(libx264)로 인코딩
'''
import subprocess
import sys
import os
import logging
from typing import Optional
import numpy as np
from app.utils.ffmpeg_utils import get_ffmpeg_executable, get_ffprobe_executable, get_subprocess_kwargs

def _get_ffmpeg_path_safe():
    '''FFmpeg 경로를 안전하게 가져오기 (EXE 환경 호환)'''
    return get_ffmpeg_executable()

logger = logging.getLogger(__name__)

def validate_video_file(video_path = None, ffprobe_path = None):
    '''
    비디오 파일이 유효한지 검증 (moov atom 포함 여부)

    Args:
        video_path: 비디오 파일 경로
        ffprobe_path: FFprobe 실행 파일 경로 (None이면 자동 탐색)

    Returns:
        True: 유효한 비디오 파일
        False: 손상되거나 불완전한 파일
    '''
    if not os.path.exists(video_path):
        return False
    if None.path.getsize(video_path) == 0:
        return False
# WARNING: Decompyle incomplete


class FFmpegPipeline:
    '''
    FFmpeg stdin pipe를 통한 스트리밍 인코딩

    메모리 효율:
    - 프레임을 한 장씩 생성하고 즉시 FFmpeg로 전송
    - 전체 영상을 메모리에 유지하지 않음
    '''
    
    def __init__(self, output_path, width, height, fps = None, encoder = None, quality = None, ffmpeg_path = (30, 'auto', 23, None, 0), expected_frames = ('output_path', str, 'width', int, 'height', int, 'fps', int, 'encoder', str, 'quality', int, 'ffmpeg_path', Optional[str], 'expected_frames', int)):
