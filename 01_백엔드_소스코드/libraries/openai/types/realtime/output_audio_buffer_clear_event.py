# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: output_audio_buffer_clear_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'OutputAudioBufferClearEvent']

class OutputAudioBufferClearEvent(BaseModel):
    type: Literal['output_audio_buffer.clear'] = '**WebRTC/SIP Only:** Emit to cut off the current audio response.\n\n    This will trigger the server to\n    stop generating audio and emit a `output_audio_buffer.cleared` event. This\n    event should be preceded by a `response.cancel` client event to stop the\n    generation of the current response.\n    [Learn more](https://platform.openai.com/docs/guides/realtime-conversations#client-and-server-events-for-audio-in-webrtc).\n    '
    event_id: Optional[str] = None
