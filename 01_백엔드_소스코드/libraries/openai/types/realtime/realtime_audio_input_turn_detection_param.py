# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_audio_input_turn_detection_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
__all__ = [
    'RealtimeAudioInputTurnDetectionParam',
    'ServerVad',
    'SemanticVad']

def ServerVad():
    '''ServerVad'''
    threshold: 'float' = '\n    Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.\n    '

ServerVad = <NODE:27>(ServerVad, 'ServerVad', TypedDict, total = False)

def SemanticVad():
    '''SemanticVad'''
    interrupt_response: 'bool' = '\n    Server-side semantic turn detection which uses a model to determine when the user has finished speaking.\n    '

SemanticVad = <NODE:27>(SemanticVad, 'SemanticVad', TypedDict, total = False)
RealtimeAudioInputTurnDetectionParam: 'TypeAlias' = Union[(ServerVad, SemanticVad)]
