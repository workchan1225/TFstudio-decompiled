# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_audio_config_input_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import TypedDict
from noise_reduction_type import NoiseReductionType
from audio_transcription_param import AudioTranscriptionParam
from realtime_audio_formats_param import RealtimeAudioFormatsParam
from realtime_audio_input_turn_detection_param import RealtimeAudioInputTurnDetectionParam
__all__ = [
    'RealtimeAudioConfigInputParam',
    'NoiseReduction']

def NoiseReduction():
    '''NoiseReduction'''
    type: 'NoiseReductionType' = 'Configuration for input audio noise reduction.\n\n    This can be set to `null` to turn off.\n    Noise reduction filters audio added to the input audio buffer before it is sent to VAD and the model.\n    Filtering the audio can improve VAD and turn detection accuracy (reducing false positives) and model performance by improving perception of the input audio.\n    '

NoiseReduction = <NODE:27>(NoiseReduction, 'NoiseReduction', TypedDict, total = False)

def RealtimeAudioConfigInputParam():
    '''RealtimeAudioConfigInputParam'''
    turn_detection: 'Optional[RealtimeAudioInputTurnDetectionParam]' = 'RealtimeAudioConfigInputParam'

RealtimeAudioConfigInputParam = <NODE:27>(RealtimeAudioConfigInputParam, 'RealtimeAudioConfigInputParam', TypedDict, total = False)
