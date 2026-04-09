# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_transcription_session_create_response.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from audio_transcription import AudioTranscription
from noise_reduction_type import NoiseReductionType
from realtime_audio_formats import RealtimeAudioFormats
from realtime_transcription_session_turn_detection import RealtimeTranscriptionSessionTurnDetection
__all__ = [
    'RealtimeTranscriptionSessionCreateResponse',
    'Audio',
    'AudioInput',
    'AudioInputNoiseReduction']

class AudioInputNoiseReduction(BaseModel):
    '''Configuration for input audio noise reduction.'''
    type: Optional[NoiseReductionType] = None


class AudioInput(BaseModel):
    format: Optional[RealtimeAudioFormats] = None
    noise_reduction: Optional[AudioInputNoiseReduction] = None
    transcription: Optional[AudioTranscription] = None
    turn_detection: Optional[RealtimeTranscriptionSessionTurnDetection] = None


class Audio(BaseModel):
    '''Configuration for input audio for the session.'''
    input: Optional[AudioInput] = None


class RealtimeTranscriptionSessionCreateResponse(BaseModel):
    type: Literal['transcription'] = 'A Realtime transcription session configuration object.'
    audio: Optional[Audio] = None
    expires_at: Optional[int] = None
    include: Optional[List[Literal['item.input_audio_transcription.logprobs']]] = None
