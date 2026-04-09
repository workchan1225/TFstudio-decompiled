# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_transcription_session_create_request.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from realtime_transcription_session_audio import RealtimeTranscriptionSessionAudio
__all__ = [
    'RealtimeTranscriptionSessionCreateRequest']

class RealtimeTranscriptionSessionCreateRequest(BaseModel):
    type: Literal['transcription'] = 'Realtime transcription session object configuration.'
    audio: Optional[RealtimeTranscriptionSessionAudio] = None
    include: Optional[List[Literal['item.input_audio_transcription.logprobs']]] = None
