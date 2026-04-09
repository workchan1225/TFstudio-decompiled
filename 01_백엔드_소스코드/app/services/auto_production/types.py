# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

'''
Auto Production - Type Definitions
'''
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class AutoProductionPhase(Enum, str):
    PROJECT_SETUP = 'project_setup'
    SCRIPT_SAVE = 'script_save'
    TTS_GENERATION = 'tts_generation'
    SUBTITLE_GENERATION = 'subtitle_generation'
    IMAGE_GENERATION = 'image_generation'
    VIDEO_RENDER = 'video_render'

PHASE_WEIGHTS = {
    AutoProductionPhase.VIDEO_RENDER: 15,
    AutoProductionPhase.IMAGE_GENERATION: 35,
    AutoProductionPhase.SUBTITLE_GENERATION: 10,
    AutoProductionPhase.TTS_GENERATION: 35,
    AutoProductionPhase.SCRIPT_SAVE: 3,
    AutoProductionPhase.PROJECT_SETUP: 2 }
SceneData = <NODE:12>()
TTSSettings = <NODE:12>()
SubtitleSettings = <NODE:12>()
ImageSettings = <NODE:12>()
AutoProductionConfig = <NODE:12>()
