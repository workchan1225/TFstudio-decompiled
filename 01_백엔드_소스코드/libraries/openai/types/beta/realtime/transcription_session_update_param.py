# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_session_update_param.pyc (Python 3.11)

from __future__ import annotations
from typing import List
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'TranscriptionSessionUpdateParam',
    'Session',
    'SessionClientSecret',
    'SessionClientSecretExpiresAt',
    'SessionInputAudioNoiseReduction',
    'SessionInputAudioTranscription',
    'SessionTurnDetection']

def SessionClientSecretExpiresAt():
    '''SessionClientSecretExpiresAt'''
    seconds: 'int' = 'SessionClientSecretExpiresAt'

SessionClientSecretExpiresAt = <NODE:27>(SessionClientSecretExpiresAt, 'SessionClientSecretExpiresAt', TypedDict, total = False)

def SessionClientSecret():
    '''SessionClientSecret'''
    expires_at: 'SessionClientSecretExpiresAt' = 'SessionClientSecret'

SessionClientSecret = <NODE:27>(SessionClientSecret, 'SessionClientSecret', TypedDict, total = False)

def SessionInputAudioNoiseReduction():
    '''SessionInputAudioNoiseReduction'''
    type: "Literal['near_field', 'far_field']" = 'SessionInputAudioNoiseReduction'

SessionInputAudioNoiseReduction = <NODE:27>(SessionInputAudioNoiseReduction, 'SessionInputAudioNoiseReduction', TypedDict, total = False)

def SessionInputAudioTranscription():
    '''SessionInputAudioTranscription'''
    prompt: 'str' = 'SessionInputAudioTranscription'

SessionInputAudioTranscription = <NODE:27>(SessionInputAudioTranscription, 'SessionInputAudioTranscription', TypedDict, total = False)

def SessionTurnDetection():
    '''SessionTurnDetection'''
    type: "Literal['server_vad', 'semantic_vad']" = 'SessionTurnDetection'

SessionTurnDetection = <NODE:27>(SessionTurnDetection, 'SessionTurnDetection', TypedDict, total = False)

def Session():
    '''Session'''
    turn_detection: 'SessionTurnDetection' = 'Session'

Session = <NODE:27>(Session, 'Session', TypedDict, total = False)

def TranscriptionSessionUpdateParam():
    '''TranscriptionSessionUpdateParam'''
    event_id: 'str' = 'TranscriptionSessionUpdateParam'

TranscriptionSessionUpdateParam = <NODE:27>(TranscriptionSessionUpdateParam, 'TranscriptionSessionUpdateParam', TypedDict, total = False)
