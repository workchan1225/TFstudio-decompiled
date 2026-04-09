# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_audio_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ResponseInputAudioParam',
    'InputAudio']

def InputAudio():
    '''InputAudio'''
    format: "Required[Literal['mp3', 'wav']]" = 'InputAudio'

InputAudio = <NODE:27>(InputAudio, 'InputAudio', TypedDict, total = False)

def ResponseInputAudioParam():
    '''ResponseInputAudioParam'''
    type: "Required[Literal['input_audio']]" = 'An audio input to the model.'

ResponseInputAudioParam = <NODE:27>(ResponseInputAudioParam, 'ResponseInputAudioParam', TypedDict, total = False)
