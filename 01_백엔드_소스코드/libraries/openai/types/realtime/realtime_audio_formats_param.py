# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_audio_formats_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict
__all__ = [
    'RealtimeAudioFormatsParam',
    'AudioPCM',
    'AudioPCMU',
    'AudioPCMA']

def AudioPCM():
    '''AudioPCM'''
    type: "Literal['audio/pcm']" = 'The PCM audio format. Only a 24kHz sample rate is supported.'

AudioPCM = <NODE:27>(AudioPCM, 'AudioPCM', TypedDict, total = False)

def AudioPCMU():
    '''AudioPCMU'''
    type: "Literal['audio/pcmu']" = 'The G.711 μ-law format.'

AudioPCMU = <NODE:27>(AudioPCMU, 'AudioPCMU', TypedDict, total = False)

def AudioPCMA():
    '''AudioPCMA'''
    type: "Literal['audio/pcma']" = 'The G.711 A-law format.'

AudioPCMA = <NODE:27>(AudioPCMA, 'AudioPCMA', TypedDict, total = False)
RealtimeAudioFormatsParam: 'TypeAlias' = Union[(AudioPCM, AudioPCMU, AudioPCMA)]
