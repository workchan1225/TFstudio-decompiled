# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_session_update.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'TranscriptionSessionUpdate',
    'Session',
    'SessionClientSecret',
    'SessionClientSecretExpiresAt',
    'SessionInputAudioNoiseReduction',
    'SessionInputAudioTranscription',
    'SessionTurnDetection']

class SessionClientSecretExpiresAt(BaseModel):
    anchor: Optional[Literal['created_at']] = None
    seconds: Optional[int] = None


class SessionClientSecret(BaseModel):
    expires_at: Optional[SessionClientSecretExpiresAt] = None


class SessionInputAudioNoiseReduction(BaseModel):
    type: Optional[Literal[('near_field', 'far_field')]] = None


class SessionInputAudioTranscription(BaseModel):
    language: Optional[str] = None
    model: Optional[Literal[('gpt-4o-transcribe', 'gpt-4o-mini-transcribe', 'whisper-1')]] = None
    prompt: Optional[str] = None


class SessionTurnDetection(BaseModel):
    create_response: Optional[bool] = None
    eagerness: Optional[Literal[('low', 'medium', 'high', 'auto')]] = None
    interrupt_response: Optional[bool] = None
    prefix_padding_ms: Optional[int] = None
    silence_duration_ms: Optional[int] = None
    threshold: Optional[float] = None
    type: Optional[Literal[('server_vad', 'semantic_vad')]] = None


class Session(BaseModel):
    client_secret: Optional[SessionClientSecret] = None
    include: Optional[List[str]] = None
    input_audio_format: Optional[Literal[('pcm16', 'g711_ulaw', 'g711_alaw')]] = None
    input_audio_noise_reduction: Optional[SessionInputAudioNoiseReduction] = None
    input_audio_transcription: Optional[SessionInputAudioTranscription] = None
    modalities: Optional[List[Literal[('text', 'audio')]]] = None
    turn_detection: Optional[SessionTurnDetection] = None


class TranscriptionSessionUpdate(BaseModel):
    type: Literal['transcription_session.update'] = 'TranscriptionSessionUpdate'
    event_id: Optional[str] = None
