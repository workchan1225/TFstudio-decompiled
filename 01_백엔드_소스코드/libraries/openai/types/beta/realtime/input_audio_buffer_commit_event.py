# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_commit_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'InputAudioBufferCommitEvent']

class InputAudioBufferCommitEvent(BaseModel):
    type: Literal['input_audio_buffer.commit'] = 'InputAudioBufferCommitEvent'
    event_id: Optional[str] = None
