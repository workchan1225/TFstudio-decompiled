# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_response_create_audio_output.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal
from _models import BaseModel
from realtime_audio_formats import RealtimeAudioFormats
__all__ = [
    'RealtimeResponseCreateAudioOutput',
    'Output']

class Output(BaseModel):
    format: Optional[RealtimeAudioFormats] = None
    voice: Union[(str, Literal[('alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse', 'marin', 'cedar')], None)] = None


class RealtimeResponseCreateAudioOutput(BaseModel):
    '''Configuration for audio input and output.'''
    output: Optional[Output] = None
