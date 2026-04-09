# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_transcription_session_audio.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
from realtime_transcription_session_audio_input import RealtimeTranscriptionSessionAudioInput
__all__ = [
    'RealtimeTranscriptionSessionAudio']

class RealtimeTranscriptionSessionAudio(BaseModel):
    '''Configuration for input and output audio.'''
    input: Optional[RealtimeTranscriptionSessionAudioInput] = None
