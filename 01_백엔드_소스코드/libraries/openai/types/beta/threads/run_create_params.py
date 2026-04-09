# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from shared.chat_model import ChatModel
from assistant_tool_param import AssistantToolParam
from runs.run_step_include import RunStepInclude
from shared_params.metadata import Metadata
from shared.reasoning_effort import ReasoningEffort
from message_content_part_param import MessageContentPartParam
from code_interpreter_tool_param import CodeInterpreterToolParam
from assistant_tool_choice_option_param import AssistantToolChoiceOptionParam
from assistant_response_format_option_param import AssistantResponseFormatOptionParam
__all__ = [
    'RunCreateParamsBase',
    'AdditionalMessage',
    'AdditionalMessageAttachment',
    'AdditionalMessageAttachmentTool',
    'AdditionalMessageAttachmentToolFileSearch',
    'TruncationStrategy',
    'RunCreateParamsNonStreaming',
    'RunCreateParamsStreaming']

def RunCreateParamsBase():
    '''RunCreateParamsBase'''
    truncation_strategy: 'Optional[TruncationStrategy]' = 'RunCreateParamsBase'

RunCreateParamsBase = <NODE:27>(RunCreateParamsBase, 'RunCreateParamsBase', TypedDict, total = False)

def AdditionalMessageAttachmentToolFileSearch():
    '''AdditionalMessageAttachmentToolFileSearch'''
    type: "Required[Literal['file_search']]" = 'AdditionalMessageAttachmentToolFileSearch'

AdditionalMessageAttachmentToolFileSearch = <NODE:27>(AdditionalMessageAttachmentToolFileSearch, 'AdditionalMessageAttachmentToolFileSearch', TypedDict, total = False)
AdditionalMessageAttachmentTool: 'TypeAlias' = Union[(CodeInterpreterToolParam, AdditionalMessageAttachmentToolFileSearch)]

def AdditionalMessageAttachment():
    '''AdditionalMessageAttachment'''
    tools: 'Iterable[AdditionalMessageAttachmentTool]' = 'AdditionalMessageAttachment'

AdditionalMessageAttachment = <NODE:27>(AdditionalMessageAttachment, 'AdditionalMessageAttachment', TypedDict, total = False)

def AdditionalMessage():
    '''AdditionalMessage'''
    metadata: 'Optional[Metadata]' = 'AdditionalMessage'

AdditionalMessage = <NODE:27>(AdditionalMessage, 'AdditionalMessage', TypedDict, total = False)

def TruncationStrategy():
    '''TruncationStrategy'''
    last_messages: 'Optional[int]' = 'Controls for how a thread will be truncated prior to the run.\n\n    Use this to control the initial context window of the run.\n    '

TruncationStrategy = <NODE:27>(TruncationStrategy, 'TruncationStrategy', TypedDict, total = False)

def RunCreateParamsNonStreaming():
    '''RunCreateParamsNonStreaming'''
    stream: 'Optional[Literal[False]]' = 'RunCreateParamsNonStreaming'

RunCreateParamsNonStreaming = <NODE:27>(RunCreateParamsNonStreaming, 'RunCreateParamsNonStreaming', RunCreateParamsBase, total = False)

class RunCreateParamsStreaming(RunCreateParamsBase):
    stream: 'Required[Literal[True]]' = 'RunCreateParamsStreaming'

RunCreateParams = Union[(RunCreateParamsNonStreaming, RunCreateParamsStreaming)]
