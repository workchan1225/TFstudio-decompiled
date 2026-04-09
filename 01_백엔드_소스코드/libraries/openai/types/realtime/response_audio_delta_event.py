# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_audio_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseAudioDeltaEvent']

class ResponseAudioDeltaEvent(BaseModel):
    type: Literal['response.output_audio.delta'] = 'Returned when the model-generated audio is updated.'
