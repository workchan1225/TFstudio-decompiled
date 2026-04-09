# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_audio_transcript_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseAudioTranscriptDeltaEvent']

class ResponseAudioTranscriptDeltaEvent(BaseModel):
    type: Literal['response.output_audio_transcript.delta'] = 'Returned when the model-generated transcription of audio output is updated.'
