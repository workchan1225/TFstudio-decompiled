# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: session_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict
__all__ = [
    'SessionCreateParams',
    'ClientSecret',
    'ClientSecretExpiresAfter',
    'InputAudioNoiseReduction',
    'InputAudioTranscription',
    'Tool',
    'Tracing',
    'TracingTracingConfiguration',
    'TurnDetection']

def SessionCreateParams():
    '''SessionCreateParams'''
    voice: "Union[str, Literal['alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse']]" = 'SessionCreateParams'

SessionCreateParams = <NODE:27>(SessionCreateParams, 'SessionCreateParams', TypedDict, total = False)

def ClientSecretExpiresAfter():
    '''ClientSecretExpiresAfter'''
    seconds: 'int' = 'ClientSecretExpiresAfter'

ClientSecretExpiresAfter = <NODE:27>(ClientSecretExpiresAfter, 'ClientSecretExpiresAfter', TypedDict, total = False)

def ClientSecret():
    '''ClientSecret'''
    expires_after: 'ClientSecretExpiresAfter' = 'ClientSecret'

ClientSecret = <NODE:27>(ClientSecret, 'ClientSecret', TypedDict, total = False)

def InputAudioNoiseReduction():
    '''InputAudioNoiseReduction'''
    type: "Literal['near_field', 'far_field']" = 'InputAudioNoiseReduction'

InputAudioNoiseReduction = <NODE:27>(InputAudioNoiseReduction, 'InputAudioNoiseReduction', TypedDict, total = False)

def InputAudioTranscription():
    '''InputAudioTranscription'''
    prompt: 'str' = 'InputAudioTranscription'

InputAudioTranscription = <NODE:27>(InputAudioTranscription, 'InputAudioTranscription', TypedDict, total = False)

def Tool():
    '''Tool'''
    type: "Literal['function']" = 'Tool'

Tool = <NODE:27>(Tool, 'Tool', TypedDict, total = False)

def TracingTracingConfiguration():
    '''TracingTracingConfiguration'''
    workflow_name: 'str' = 'TracingTracingConfiguration'

TracingTracingConfiguration = <NODE:27>(TracingTracingConfiguration, 'TracingTracingConfiguration', TypedDict, total = False)
Tracing: 'TypeAlias' = Union[(Literal['auto'], TracingTracingConfiguration)]

def TurnDetection():
    '''TurnDetection'''
    type: "Literal['server_vad', 'semantic_vad']" = 'TurnDetection'

TurnDetection = <NODE:27>(TurnDetection, 'TurnDetection', TypedDict, total = False)
