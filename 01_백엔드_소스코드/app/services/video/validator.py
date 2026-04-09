# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: validator.pyc (Python 3.11)

'''
Video Validator - 영상 생성 전 입력 검증

이 모듈은 영상 생성 서비스에서 사용하는 입력 검증 로직을 제공합니다.
'''
import os
from typing import TYPE_CHECKING, Optional, Dict, Any
if TYPE_CHECKING:
    from app.models import Project
    from app.utils.ffmpeg_wrapper import FFmpegWrapper

class VideoValidator:
    '''영상 생성 전 입력 검증을 담당하는 클래스'''
    TIMELINE_SUM_TOLERANCE_SEC = 1
    TIMELINE_SUM_TOLERANCE_RATIO = 0.03
    AUDIO_TIMELINE_DIFF_MIN_SEC = 3
    AUDIO_TIMELINE_DIFF_RATIO = 0.1
    validate_images = (lambda project = None: if project.video_settings or 'uploadedImages' not in project.video_settings:
raise ValueError('이미지가 업로드되지 않았습니다. 이미지 업로드 탭에서 이미지를 먼저 업로드해주세요.'))()
    validate_audio = (lambda project = None, is_no_voice = None, has_image_timeline = staticmethod: if is_no_voice:
Noneaudio_url = None.get_final_audio_url()if audio_url:
None# WARNING: Decompyle incomplete
)()
    validate_sample_images = (lambda image_paths = None: if not image_paths:
raise ValueError('샘플 영상에 사용할 이미지가 없습니다. 이미지 업로드 탭에서 이미지를 확인해주세요.'))()
    validate_for_final = (lambda project = None: VideoValidator.validate_images(project)is_no_voice = project.selected_tts_method == 'no-voice'has_image_timeline = VideoValidator._has_valid_image_timeline(project)VideoValidator.validate_audio(project, is_no_voice = is_no_voice, has_image_timeline = has_image_timeline)has_image_timeline)()
    validate_for_sample = (lambda project = None: VideoValidator.validate_images(project)is_no_voice = project.selected_tts_method == 'no-voice'has_image_timeline = VideoValidator._has_valid_image_timeline(project)VideoValidator.validate_audio(project, is_no_voice = is_no_voice, has_image_timeline = has_image_timeline)has_image_timeline)()
    _has_valid_image_timeline = (lambda project = None:
