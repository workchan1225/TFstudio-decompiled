# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_session.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'TranscriptionSession',
    'ClientSecret',
    'InputAudioTranscription',
    'TurnDetection']

class ClientSecret(BaseModel):
    value: str = 'ClientSecret'


class InputAudioTranscription(BaseModel):
    language: Optional[str] = None
    model: Optional[Literal[('gpt-4o-transcribe', 'gpt-4o-mini-transcribe', 'whisper-1')]] = None
    prompt: Optional[str] = None


class TurnDetection(BaseModel):
    prefix_padding_ms: Optional[int] = None
    silence_duration_ms: Optional[int] = None
    threshold: Optional[float] = None
    type: Optional[str] = None


class TranscriptionSession(BaseModel):
    client_secret: ClientSecret = 'TranscriptionSession'
    input_audio_format: Optional[str] = None
    input_audio_transcription: Optional[InputAudioTranscription] = None
    modalities: Optional[List[Literal[('text', 'audio')]]] = None
    turn_detection: Optional[TurnDetection] = None
