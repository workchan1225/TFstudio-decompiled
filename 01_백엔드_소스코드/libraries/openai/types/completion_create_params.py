# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: completion_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict
from _types import SequenceNotStr
from chat.chat_completion_stream_options_param import ChatCompletionStreamOptionsParam
__all__ = [
    'CompletionCreateParamsBase',
    'CompletionCreateParamsNonStreaming',
    'CompletionCreateParamsStreaming']

def CompletionCreateParamsBase():
    '''CompletionCreateParamsBase'''
    user: 'str' = 'CompletionCreateParamsBase'

CompletionCreateParamsBase = <NODE:27>(CompletionCreateParamsBase, 'CompletionCreateParamsBase', TypedDict, total = False)

def CompletionCreateParamsNonStreaming():
    '''CompletionCreateParamsNonStreaming'''
    stream: 'Optional[Literal[False]]' = 'CompletionCreateParamsNonStreaming'

CompletionCreateParamsNonStreaming = <NODE:27>(CompletionCreateParamsNonStreaming, 'CompletionCreateParamsNonStreaming', CompletionCreateParamsBase, total = False)

class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: 'Required[Literal[True]]' = 'CompletionCreateParamsStreaming'

CompletionCreateParams = Union[(CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming)]
