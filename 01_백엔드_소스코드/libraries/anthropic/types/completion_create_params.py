# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: completion_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict
from _types import SequenceNotStr
from _utils import PropertyInfo
from model_param import ModelParam
from metadata_param import MetadataParam
from anthropic_beta_param import AnthropicBetaParam
__all__ = [
    'CompletionRequestStreamingMetadata',
    'CompletionRequestNonStreamingMetadata',
    'CompletionRequestNonStreaming',
    'CompletionRequestStreaming',
    'CompletionCreateParamsBase',
    'Metadata',
    'CompletionCreateParamsNonStreaming',
    'CompletionCreateParamsStreaming']

def CompletionCreateParamsBase():
    '''CompletionCreateParamsBase'''
    betas: "Annotated[List[AnthropicBetaParam], PropertyInfo(alias='anthropic-beta')]" = 'CompletionCreateParamsBase'

CompletionCreateParamsBase = <NODE:27>(CompletionCreateParamsBase, 'CompletionCreateParamsBase', TypedDict, total = False)
Metadata: 'TypeAlias' = MetadataParam

def CompletionCreateParamsNonStreaming():
    '''CompletionCreateParamsNonStreaming'''
    stream: 'Literal[False]' = 'CompletionCreateParamsNonStreaming'

CompletionCreateParamsNonStreaming = <NODE:27>(CompletionCreateParamsNonStreaming, 'CompletionCreateParamsNonStreaming', CompletionCreateParamsBase, total = False)

class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: 'Required[Literal[True]]' = 'CompletionCreateParamsStreaming'

CompletionRequestStreamingMetadata = MetadataParam
CompletionRequestNonStreamingMetadata = MetadataParam
CompletionRequestNonStreaming = CompletionCreateParamsNonStreaming
CompletionRequestStreaming = CompletionCreateParamsStreaming
CompletionCreateParams = Union[(CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming)]
