# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ffmpeg_wrapper.pyc (Python 3.11)

'''
FFmpeg 래퍼 유틸리티
영상, 오디오, 자막 처리를 위한 FFmpeg 명령어 래퍼
'''
import subprocess
import os
import random
import sys
import tempfile
import queue
import threading
import time
from collections import deque
from typing import Optional, List, Tuple, Callable, Dict, Any, cast
import logging
from app.utils.atomic_media_write import atomic_audio_output
from app.utils.ffmpeg_utils import get_ffmpeg_executable, probe_video_dimensions
ZOOM_FOCUS_POSITIONS = [
    'center',
    'top',
    'bottom',
    'left',
    'right',
    'top_left',
    'top_right',
    'bottom_left',
    'bottom_right']

try:
    from app.config import OPENCV_EFFECTS_ENGINE, OPENCV_MOTION_EFFECTS
except ImportError:
    OPENCV_EFFECTS_ENGINE = True
    OPENCV_MOTION_EFFECTS = {
        'pan',
        'rotate',
        'zoom_in',
        'zoom_out',
        'ken_burns'}


try:
    from app.config.zoom_motion_config import get_adjusted_zoom_params, LONG_SEGMENT_THRESHOLD, ZOOM_MIN
except ImportError:
    LONG_SEGMENT_THRESHOLD = 60
    ZOOM_MIN = 1
    
    def get_adjusted_zoom_params(duration, user_zoom_start, user_zoom_end, is_zoom_out = (1, 1.3, False)):
        return {
            'zoom_start': user_zoom_start,
            'zoom_end': user_zoom_end,
            'zoom_duration': duration,
            'hold_duration': 0,
            'is_long_segment': False }


logger = logging.getLogger(__name__)

class FFmpegStoppedError(RuntimeError):
    '''Raised when an FFmpeg process is intentionally stopped.'''
    pass


class FFmpegWrapper:
    '''FFmpeg 명령어 실행을 위한 래퍼 클래스'''
    
    def __init__(self = None, ffmpeg_path = None, project_id = None):
        '''
        Args:
            ffmpeg_path: FFmpeg 실행 파일 경로 (None이면 자동 탐색)
            project_id: 프로젝트 ID (프로세스 관리용)
        '''
        if ffmpeg_path and os.path.exists(ffmpeg_path):
            self.ffmpeg_path = ffmpeg_path
        else:
            self.ffmpeg_path = get_ffmpeg_executable()
        self.project_id = project_id
        self.current_process = None
        self._stop_requested = False
        self._nvenc_available = None
        self._temp_filter_scripts = []
        self._use_opencv_engine = OPENCV_EFFECTS_ENGINE

    _is_progress_line = (lambda line = None: pass# WARNING: Decompyle incomplete
)()
    _normalize_stderr = (lambda stderr = None: if not stderr:
''lines = None.replace('\r', '\n').split('\n')filtered = lines()' '.join(' '.join(filtered).split()))()
    _extract_meaningful_error = (lambda stderr = None: pass# WARNING: Decompyle incomplete
)()
    
    def _build_ffmpeg_failure_message(self = None, return_code = None, stderr = None):
