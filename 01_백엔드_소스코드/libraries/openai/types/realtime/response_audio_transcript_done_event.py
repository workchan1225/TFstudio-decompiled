# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_audio_transcript_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseAudioTranscriptDoneEvent']

class ResponseAudioTranscriptDoneEvent(BaseModel):
    type: Literal['response.output_audio_transcript.done'] = '\n    Returned when the model-generated transcription of audio output is done\n    streaming. Also emitted when a Response is interrupted, incomplete, or\n    cancelled.\n    '
