# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_clear_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'InputAudioBufferClearEvent']

class InputAudioBufferClearEvent(BaseModel):
    type: Literal['input_audio_buffer.clear'] = 'InputAudioBufferClearEvent'
    event_id: Optional[str] = None
