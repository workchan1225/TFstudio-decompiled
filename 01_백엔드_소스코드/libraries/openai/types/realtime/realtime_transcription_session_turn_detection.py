# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_transcription_session_turn_detection.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'RealtimeTranscriptionSessionTurnDetection']

class RealtimeTranscriptionSessionTurnDetection(BaseModel):
    '''Configuration for turn detection.

    Can be set to `null` to turn off. Server
    VAD means that the model will detect the start and end of speech based on
    audio volume and respond at the end of user speech.
    '''
    prefix_padding_ms: Optional[int] = None
    silence_duration_ms: Optional[int] = None
    threshold: Optional[float] = None
    type: Optional[str] = None
