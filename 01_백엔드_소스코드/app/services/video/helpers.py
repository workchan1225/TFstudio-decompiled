# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

'''
Video Generation Helpers - 영상 생성 공통 유틸리티

generate_video와 generate_sample_video 간의 공통 로직을 추출한 헬퍼 함수들
'''
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
from app.models.project import Project
from app.utils.file_paths import ProjectPaths
from app.utils.ffmpeg_wrapper import FFmpegWrapper
from app.services.subtitle_service import SubtitleService
DEFAULT_IMAGE_EFFECTS: Dict[(str, Any)] = {
    'effect': 'static',
    'zoomLevel': 1.2,
    'panDirection': 'left_to_right',
    'speed': 'medium' }

def get_image_effects_config(project = None):
    """
    프로젝트에서 이미지 효과 설정을 로드합니다.

    우선순위:
    1. imageEffects (신규 설정)
    2. imagePosition (레거시 호환)
    3. 기본값 (static, zoomLevel=1.2, left_to_right, medium)

    Args:
        project: 프로젝트 객체

    Returns:
        이미지 효과 설정 딕셔너리

    Example:
        >>> effects = get_image_effects_config(project)
        >>> print(effects['effect'])  # 'static', 'zoom_in', 'pan', etc.
    """
    if not project.video_settings:
        video_settings = { }
        if not video_settings.get('imageEffects'):
            pass
    image_effects = video_settings.get('imagePosition', DEFAULT_IMAGE_EFFECTS.copy())
    return image_effects


def filter_audio_tracks_by_duration(bgm_tracks = None, sfx_tracks = None, max_duration = None):
    '''
    시간 기반으로 오디오 트랙을 필터링합니다.

    샘플 영상 생성 시, 지정된 최대 시간 내에서 시작하는 트랙만 포함합니다.
    enabled가 True이고, timing.startTime이 max_duration 미만인 트랙만 반환합니다.

    Args:
        bgm_tracks: BGM 트랙 목록
        sfx_tracks: SFX 트랙 목록
        max_duration: 최대 재생 시간 (초)

    Returns:
        Tuple[filtered_bgm_tracks, filtered_sfx_tracks]

    Example:
        >>> filtered_bgm, filtered_sfx = filter_audio_tracks_by_duration(
        ...     bgm_tracks, sfx_tracks, max_duration=10.0
        ... )
    '''
    pass
# WARNING: Decompyle incomplete


def get_final_voice_url(project = None):
