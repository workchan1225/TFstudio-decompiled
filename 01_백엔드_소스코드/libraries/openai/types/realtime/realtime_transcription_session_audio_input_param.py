# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_transcription_session_audio_input_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import TypedDict
from noise_reduction_type import NoiseReductionType
from audio_transcription_param import AudioTranscriptionParam
from realtime_audio_formats_param import RealtimeAudioFormatsParam
from realtime_transcription_session_audio_input_turn_detection_param import RealtimeTranscriptionSessionAudioInputTurnDetectionParam
__all__ = [
    'RealtimeTranscriptionSessionAudioInputParam',
    'NoiseReduction']

def NoiseReduction():
    '''NoiseReduction'''
    type: 'NoiseReductionType' = 'Configuration for input audio noise reduction.\n\n    This can be set to `null` to turn off.\n    Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.\n    Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.\n    '

NoiseReduction = <NODE:27>(NoiseReduction, 'NoiseReduction', TypedDict, total = False)

def RealtimeTranscriptionSessionAudioInputParam():
    '''RealtimeTranscriptionSessionAudioInputParam'''
    turn_detection: 'Optional[RealtimeTranscriptionSessionAudioInputTurnDetectionParam]' = 'RealtimeTranscriptionSessionAudioInputParam'

RealtimeTranscriptionSessionAudioInputParam = <NODE:27>(RealtimeTranscriptionSessionAudioInputParam, 'RealtimeTranscriptionSessionAudioInputParam', TypedDict, total = False)
