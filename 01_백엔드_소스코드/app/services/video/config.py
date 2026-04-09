# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

'''
Video Configuration Builder

Project 객체에서 영상 생성에 필요한 모든 설정을 추출하는 빌더 클래스.
불변 VideoConfig 객체를 생성하여 영상 생성 파이프라인에 전달.
'''
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional
import json
from app.models.project import Project
from types import VideoMode, Orientation, ImageFit, Resolution, BitrateConfig, ImageEffectConfig, DEFAULT_BITRATE_MBPS, orientation_from_string, image_fit_from_string
from helpers import get_image_effects_config
LogoSettings = <NODE:12>()
SubtitleStyle = <NODE:12>()
VideoConfig = <NODE:12>()

class VideoConfigBuilder:
    """
    VideoConfig 빌더.

    Project 객체에서 영상 생성에 필요한 모든 설정을 추출하고,
    빌더 패턴으로 추가 옵션을 설정한 후 VideoConfig 객체를 생성.

    Usage:
        config = VideoConfigBuilder(project, data_dir) \\
            .with_mode(VideoMode.FINAL) \\
            .with_orientation('landscape') \\
            .with_bitrate(20) \\
            .build()
    """
    
    def __init__(self = None, project = None, data_dir = None):
