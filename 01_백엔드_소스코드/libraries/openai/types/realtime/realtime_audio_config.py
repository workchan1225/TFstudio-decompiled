# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_audio_config.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
from realtime_audio_config_input import RealtimeAudioConfigInput
from realtime_audio_config_output import RealtimeAudioConfigOutput
__all__ = [
    'RealtimeAudioConfig']

class RealtimeAudioConfig(BaseModel):
    '''Configuration for input and output audio.'''
    input: Optional[RealtimeAudioConfigInput] = None
    output: Optional[RealtimeAudioConfigOutput] = None
