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
    type: Literal['input_audio_buffer.committed'] = '\n    Returned when an input audio buffer is committed, either by the client or\n    automatically in server VAD mode. The `item_id` property is the ID of the user\n    message item that will be created, thus a `conversation.item.created` event\n    will also be sent to the client.\n    '
    previous_item_id: Optional[str] = None
