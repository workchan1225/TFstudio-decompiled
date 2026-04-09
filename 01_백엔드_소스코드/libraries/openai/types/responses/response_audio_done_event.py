# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_audio_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseAudioDoneEvent']

class ResponseAudioDoneEvent(BaseModel):
    type: Literal['response.audio.done'] = 'Emitted when the audio response is complete.'
