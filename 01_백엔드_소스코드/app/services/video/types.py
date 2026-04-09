# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

'''
Video Generation Types

영상 생성 서비스에서 사용하는 타입 정의.
모든 타입은 불변 데이터 구조로 정의됨.
'''
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple

class VideoMode(Enum, str):
    '''영상 생성 모드'''
    SAMPLE = 'sample'
    FINAL = 'final'


class Orientation(Enum, str):
    '''영상 방향'''
    LANDSCAPE = 'landscape'
    PORTRAIT = 'portrait'


class ImageFit(Enum, str):
    '''이미지 맞춤 방식'''
    COVER = 'cover'
    CONTAIN = 'contain'
    STRETCH = 'stretch'


class MediaType(Enum, str):
    '''미디어 타입'''
    IMAGE = 'image'
    VIDEO = 'video'


class EffectType(Enum, str):
    '''이미지 효과 타입'''
    STATIC = 'static'
    ZOOM_IN = 'zoom_in'
    ZOOM_OUT = 'zoom_out'
    PAN = 'pan'
    KEN_BURNS = 'ken_burns'


class PanDirection(Enum, str):
    '''패닝 방향'''
    LEFT_TO_RIGHT = 'left_to_right'
    RIGHT_TO_LEFT = 'right_to_left'
    TOP_TO_BOTTOM = 'top_to_bottom'
    BOTTOM_TO_TOP = 'bottom_to_top'


class EffectSpeed(Enum, str):
    '''효과 속도'''
    SLOW = 'slow'
    MEDIUM = 'medium'
    FAST = 'fast'


class ApplyMode(Enum, str):
    '''효과 적용 모드'''
    BATCH = 'batch'
    INDIVIDUAL = 'individual'

Resolution = <NODE:12>()
BitrateConfig = <NODE:12>()
MediaItem = <NODE:12>()
AudioTrack = <NODE:12>()
AudioConfig = <NODE:12>()
SceneEffect = <NODE:12>()
ImageEffectConfig = <NODE:12>()
DEFAULT_IMAGE_DURATION: float = 3
MIN_IMAGE_DURATION: float = 0.1
BASE_LANDSCAPE_WIDTH: int = 1920
BASE_LANDSCAPE_HEIGHT: int = 1080
DEFAULT_BITRATE_MBPS: int = 20

def orientation_from_string(orientation = dataclass):
    """
    문자열에서 Orientation 열거형으로 변환.

    Args:
        orientation: 'landscape' 또는 'portrait'

    Returns:
        Orientation 열거형 값
    """
    
    try:
        return Orientation(orientation.lower())
    except ValueError:
        return 



def image_fit_from_string(image_fit = dataclass(frozen = True)):
    """
    문자열에서 ImageFit 열거형으로 변환.

    Args:
        image_fit: 'cover', 'contain', 또는 'stretch'

    Returns:
        ImageFit 열거형 값
    """
    
    try:
        return ImageFit(image_fit.lower())
    except ValueError:
        return
