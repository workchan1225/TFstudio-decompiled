# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_response_create_audio_output_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, TypedDict
from realtime_audio_formats_param import RealtimeAudioFormatsParam
__all__ = [
    'RealtimeResponseCreateAudioOutputParam',
    'Output']

def Output():
    '''Output'''
    voice: "Union[str, Literal['alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse', 'marin', 'cedar']]" = 'Output'

Output = <NODE:27>(Output, 'Output', TypedDict, total = False)

def RealtimeResponseCreateAudioOutputParam():
    '''RealtimeResponseCreateAudioOutputParam'''
    output: 'Output' = 'Configuration for audio input and output.'

RealtimeResponseCreateAudioOutputParam = <NODE:27>(RealtimeResponseCreateAudioOutputParam, 'RealtimeResponseCreateAudioOutputParam', TypedDict, total = False)
