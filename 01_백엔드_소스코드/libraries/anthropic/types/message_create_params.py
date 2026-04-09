# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from model_param import ModelParam
from message_param import MessageParam
from metadata_param import MetadataParam
from text_block_param import TextBlockParam
from tool_union_param import ToolUnionParam
from tool_choice_param import ToolChoiceParam
from thinking_config_param import ThinkingConfigParam
from tool_choice_any_param import ToolChoiceAnyParam
from tool_choice_auto_param import ToolChoiceAutoParam
from tool_choice_tool_param import ToolChoiceToolParam
__all__ = [
    'MessageCreateParamsBase',
    'Metadata',
    'ToolChoice',
    'ToolChoiceToolChoiceAuto',
    'ToolChoiceToolChoiceAny',
    'ToolChoiceToolChoiceTool',
    'MessageCreateParamsNonStreaming',
    'MessageCreateParamsStreaming']

def MessageCreateParamsBase():
    '''MessageCreateParamsBase'''
    top_p: 'float' = 'MessageCreateParamsBase'

MessageCreateParamsBase = <NODE:27>(MessageCreateParamsBase, 'MessageCreateParamsBase', TypedDict, total = False)
Metadata: 'TypeAlias' = MetadataParam
ToolChoice: 'TypeAlias' = ToolChoiceParam
ToolChoiceToolChoiceAuto: 'TypeAlias' = ToolChoiceAutoParam
ToolChoiceToolChoiceAny: 'TypeAlias' = ToolChoiceAnyParam
ToolChoiceToolChoiceTool: 'TypeAlias' = ToolChoiceToolParam

def MessageCreateParamsNonStreaming():
    '''MessageCreateParamsNonStreaming'''
    stream: 'Literal[False]' = 'MessageCreateParamsNonStreaming'

MessageCreateParamsNonStreaming = <NODE:27>(MessageCreateParamsNonStreaming, 'MessageCreateParamsNonStreaming', MessageCreateParamsBase, total = False)

class MessageCreateParamsStreaming(MessageCreateParamsBase):
    stream: 'Required[Literal[True]]' = 'MessageCreateParamsStreaming'

MessageCreateParams = Union[(MessageCreateParamsNonStreaming, MessageCreateParamsStreaming)]
