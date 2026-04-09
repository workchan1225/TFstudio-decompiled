# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session_update_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict
__all__ = [
    'SessionUpdateEventParam',
    'Session',
    'SessionClientSecret',
    'SessionClientSecretExpiresAfter',
    'SessionInputAudioNoiseReduction',
    'SessionInputAudioTranscription',
    'SessionTool',
    'SessionTracing',
    'SessionTracingTracingConfiguration',
    'SessionTurnDetection']

def SessionClientSecretExpiresAfter():
    '''SessionClientSecretExpiresAfter'''
    seconds: 'int' = 'SessionClientSecretExpiresAfter'

SessionClientSecretExpiresAfter = <NODE:27>(SessionClientSecretExpiresAfter, 'SessionClientSecretExpiresAfter', TypedDict, total = False)

def SessionClientSecret():
    '''SessionClientSecret'''
    expires_after: 'SessionClientSecretExpiresAfter' = 'SessionClientSecret'

SessionClientSecret = <NODE:27>(SessionClientSecret, 'SessionClientSecret', TypedDict, total = False)

def SessionInputAudioNoiseReduction():
    '''SessionInputAudioNoiseReduction'''
    type: "Literal['near_field', 'far_field']" = 'SessionInputAudioNoiseReduction'

SessionInputAudioNoiseReduction = <NODE:27>(SessionInputAudioNoiseReduction, 'SessionInputAudioNoiseReduction', TypedDict, total = False)

def SessionInputAudioTranscription():
    '''SessionInputAudioTranscription'''
    prompt: 'str' = 'SessionInputAudioTranscription'

SessionInputAudioTranscription = <NODE:27>(SessionInputAudioTranscription, 'SessionInputAudioTranscription', TypedDict, total = False)

def SessionTool():
    '''SessionTool'''
    type: "Literal['function']" = 'SessionTool'

SessionTool = <NODE:27>(SessionTool, 'SessionTool', TypedDict, total = False)

def SessionTracingTracingConfiguration():
    '''SessionTracingTracingConfiguration'''
    workflow_name: 'str' = 'SessionTracingTracingConfiguration'

SessionTracingTracingConfiguration = <NODE:27>(SessionTracingTracingConfiguration, 'SessionTracingTracingConfiguration', TypedDict, total = False)
SessionTracing: 'TypeAlias' = Union[(Literal['auto'], SessionTracingTracingConfiguration)]

def SessionTurnDetection():
    '''SessionTurnDetection'''
    type: "Literal['server_vad', 'semantic_vad']" = 'SessionTurnDetection'

SessionTurnDetection = <NODE:27>(SessionTurnDetection, 'SessionTurnDetection', TypedDict, total = False)

def Session():
    '''Session'''
    voice: "Union[str, Literal['alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse']]" = 'Session'

Session = <NODE:27>(Session, 'Session', TypedDict, total = False)

def SessionUpdateEventParam():
    '''SessionUpdateEventParam'''
    event_id: 'str' = 'SessionUpdateEventParam'

SessionUpdateEventParam = <NODE:27>(SessionUpdateEventParam, 'SessionUpdateEventParam', TypedDict, total = False)
