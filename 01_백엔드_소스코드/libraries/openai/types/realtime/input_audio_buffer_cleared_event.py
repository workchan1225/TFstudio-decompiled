# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_cleared_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'InputAudioBufferClearedEvent']

class InputAudioBufferClearedEvent(BaseModel):
    type: Literal['input_audio_buffer.cleared'] = '\n    Returned when the input audio buffer is cleared by the client with a\n    `input_audio_buffer.clear` event.\n    '
