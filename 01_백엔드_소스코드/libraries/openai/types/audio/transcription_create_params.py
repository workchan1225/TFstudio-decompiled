# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import FileTypes, SequenceNotStr
from audio_model import AudioModel
from transcription_include import TranscriptionInclude
from audio_response_format import AudioResponseFormat
__all__ = [
    'TranscriptionCreateParamsBase',
    'ChunkingStrategy',
    'ChunkingStrategyVadConfig',
    'TranscriptionCreateParamsNonStreaming',
    'TranscriptionCreateParamsStreaming']

def TranscriptionCreateParamsBase():
    '''TranscriptionCreateParamsBase'''
    timestamp_granularities: "List[Literal['word', 'segment']]" = 'TranscriptionCreateParamsBase'

TranscriptionCreateParamsBase = <NODE:27>(TranscriptionCreateParamsBase, 'TranscriptionCreateParamsBase', TypedDict, total = False)

def ChunkingStrategyVadConfig():
    '''ChunkingStrategyVadConfig'''
    threshold: 'float' = 'ChunkingStrategyVadConfig'

ChunkingStrategyVadConfig = <NODE:27>(ChunkingStrategyVadConfig, 'ChunkingStrategyVadConfig', TypedDict, total = False)
ChunkingStrategy: 'TypeAlias' = Union[(Literal['auto'], ChunkingStrategyVadConfig)]

def TranscriptionCreateParamsNonStreaming():
    '''TranscriptionCreateParamsNonStreaming'''
    stream: 'Optional[Literal[False]]' = 'TranscriptionCreateParamsNonStreaming'

TranscriptionCreateParamsNonStreaming = <NODE:27>(TranscriptionCreateParamsNonStreaming, 'TranscriptionCreateParamsNonStreaming', TranscriptionCreateParamsBase, total = False)

class TranscriptionCreateParamsStreaming(TranscriptionCreateParamsBase):
    stream: 'Required[Literal[True]]' = 'TranscriptionCreateParamsStreaming'

TranscriptionCreateParams = Union[(TranscriptionCreateParamsNonStreaming, TranscriptionCreateParamsStreaming)]
