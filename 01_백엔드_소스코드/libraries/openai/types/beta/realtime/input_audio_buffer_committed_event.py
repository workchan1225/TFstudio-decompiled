# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_committed_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'InputAudioBufferCommittedEvent']

class InputAudioBufferCommittedEvent(BaseModel):
    type: Literal['input_audio_buffer.committed'] = 'InputAudioBufferCommittedEvent'
    previous_item_id: Optional[str] = None
