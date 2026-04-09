# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_session_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List
from typing_extensions import Literal, TypedDict
__all__ = [
    'TranscriptionSessionCreateParams',
    'ClientSecret',
    'ClientSecretExpiresAt',
    'InputAudioNoiseReduction',
    'InputAudioTranscription',
    'TurnDetection']

def TranscriptionSessionCreateParams():
    '''TranscriptionSessionCreateParams'''
    turn_detection: 'TurnDetection' = 'TranscriptionSessionCreateParams'

TranscriptionSessionCreateParams = <NODE:27>(TranscriptionSessionCreateParams, 'TranscriptionSessionCreateParams', TypedDict, total = False)

def ClientSecretExpiresAt():
    '''ClientSecretExpiresAt'''
    seconds: 'int' = 'ClientSecretExpiresAt'

ClientSecretExpiresAt = <NODE:27>(ClientSecretExpiresAt, 'ClientSecretExpiresAt', TypedDict, total = False)

def ClientSecret():
    '''ClientSecret'''
    expires_at: 'ClientSecretExpiresAt' = 'ClientSecret'

ClientSecret = <NODE:27>(ClientSecret, 'ClientSecret', TypedDict, total = False)

def InputAudioNoiseReduction():
    '''InputAudioNoiseReduction'''
    type: "Literal['near_field', 'far_field']" = 'InputAudioNoiseReduction'

InputAudioNoiseReduction = <NODE:27>(InputAudioNoiseReduction, 'InputAudioNoiseReduction', TypedDict, total = False)

def InputAudioTranscription():
    '''InputAudioTranscription'''
    prompt: 'str' = 'InputAudioTranscription'

InputAudioTranscription = <NODE:27>(InputAudioTranscription, 'InputAudioTranscription', TypedDict, total = False)

def TurnDetection():
    '''TurnDetection'''
    type: "Literal['server_vad', 'semantic_vad']" = 'TurnDetection'

TurnDetection = <NODE:27>(TurnDetection, 'TurnDetection', TypedDict, total = False)
