# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_transcription_session_audio_input.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
from audio_transcription import AudioTranscription
from noise_reduction_type import NoiseReductionType
from realtime_audio_formats import RealtimeAudioFormats
from realtime_transcription_session_audio_input_turn_detection import RealtimeTranscriptionSessionAudioInputTurnDetection
__all__ = [
    'RealtimeTranscriptionSessionAudioInput',
    'NoiseReduction']

class NoiseReduction(BaseModel):
    '''Configuration for input audio noise reduction.

    This can be set to `null` to turn off.
    Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.
    Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.
    '''
    type: Optional[NoiseReductionType] = None


class RealtimeTranscriptionSessionAudioInput(BaseModel):
    format: Optional[RealtimeAudioFormats] = None
    noise_reduction: Optional[NoiseReduction] = None
    transcription: Optional[AudioTranscription] = None
    turn_detection: Optional[RealtimeTranscriptionSessionAudioInputTurnDetection] = None
