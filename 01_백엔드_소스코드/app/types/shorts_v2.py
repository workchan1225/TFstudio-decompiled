# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shorts_v2.pyc (Python 3.11)

'''
Shorts V2 Types - 문장 기반 쇼츠 생성 타입 정의

이 모듈은 Shorts V2 기능에 필요한 모든 데이터 타입을 정의합니다.
Project.shorts_data JSON 필드의 version: 2 스키마를 구현합니다.
'''
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Literal
from enum import Enum
import uuid

class ShortsV2JobStatus(Enum, str):
    '''렌더링 작업 상태'''
    QUEUED = 'queued'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    FAILED = 'failed'


class TransitionType(Enum, str):
    '''트랜지션 타입'''
    NONE = 'none'
    FADE = 'fade'
    SLIDE_LEFT = 'slide_left'
    SLIDE_RIGHT = 'slide_right'
    DISSOLVE = 'dissolve'


class ConversionMode(Enum, str):
    '''9:16 변환 모드'''
    CROP = 'crop'
    PADDING = 'padding'

SentenceIndex = <NODE:12>()
ClipInfo = <NODE:12>()
TransitionSettings = <NODE:12>()
SubtitleSplitSettings = <NODE:12>()
TitleOverlaySettings = <NODE:12>()
MediaLayoutSettings = <NODE:12>()
ThumbnailImageSettings = <NODE:12>()
ThumbnailTextSettings = <NODE:12>()
ThumbnailSettings = <NODE:12>()
DraftSettings = <NODE:12>()
ShortsV2Draft = <NODE:12>()
AIClipCategory = Literal[('hook', 'climax', 'thumbnail', 'insight')]
AIClipPlan = <NODE:12>()
ShortsV2AIPlan = <NODE:12>()
ShortsV2Output = <NODE:12>()
ShortsV2JobInfo = <NODE:12>()

class ShortsV2Constraints:
    '''쇼츠 V2 제약조건'''
    MIN_CLIP_DURATION = 5
    MAX_CLIP_DURATION = 60
    MAX_TOTAL_DURATION = 180
    DEFAULT_BITRATE = 15
    RESOLUTION_WIDTH = 1080
    RESOLUTION_HEIGHT = 1920
    DEFAULT_TRANSITION_DURATION = 0.4
