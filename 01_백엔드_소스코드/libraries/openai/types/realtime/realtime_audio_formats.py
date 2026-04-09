# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_audio_formats.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'RealtimeAudioFormats',
    'AudioPCM',
    'AudioPCMU',
    'AudioPCMA']

class AudioPCM(BaseModel):
    '''The PCM audio format. Only a 24kHz sample rate is supported.'''
    rate: Optional[Literal[24000]] = None
    type: Optional[Literal['audio/pcm']] = None


class AudioPCMU(BaseModel):
    '''The G.711 μ-law format.'''
    type: Optional[Literal['audio/pcmu']] = None


class AudioPCMA(BaseModel):
    '''The G.711 A-law format.'''
    type: Optional[Literal['audio/pcma']] = None

RealtimeAudioFormats: TypeAlias = Annotated[(Union[(AudioPCM, AudioPCMU, AudioPCMA)], PropertyInfo(discriminator = 'type'))]
