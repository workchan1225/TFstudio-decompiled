# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from tool_param import ToolParam
from response_includable import ResponseIncludable
from tool_choice_options import ToolChoiceOptions
from response_input_param import ResponseInputParam
from response_prompt_param import ResponsePromptParam
from tool_choice_mcp_param import ToolChoiceMcpParam
from shared_params.metadata import Metadata
from tool_choice_shell_param import ToolChoiceShellParam
from tool_choice_types_param import ToolChoiceTypesParam
from shared_params.reasoning import Reasoning
from tool_choice_custom_param import ToolChoiceCustomParam
from tool_choice_allowed_param import ToolChoiceAllowedParam
from response_text_config_param import ResponseTextConfigParam
from tool_choice_function_param import ToolChoiceFunctionParam
from response_conversation_param import ResponseConversationParam
from tool_choice_apply_patch_param import ToolChoiceApplyPatchParam
from shared_params.responses_model import ResponsesModel
__all__ = [
    'ResponseCreateParamsBase',
    'Conversation',
    'StreamOptions',
    'ToolChoice',
    'ResponseCreateParamsNonStreaming',
    'ResponseCreateParamsStreaming']

def ResponseCreateParamsBase():
    '''ResponseCreateParamsBase'''
    user: 'str' = 'ResponseCreateParamsBase'

ResponseCreateParamsBase = <NODE:27>(ResponseCreateParamsBase, 'ResponseCreateParamsBase', TypedDict, total = False)
Conversation: 'TypeAlias' = Union[(str, ResponseConversationParam)]

def StreamOptions():
    '''StreamOptions'''
    include_obfuscation: 'bool' = 'Options for streaming responses. Only set this when you set `stream: true`.'

StreamOptions = <NODE:27>(StreamOptions, 'StreamOptions', TypedDict, total = False)
ToolChoice: 'TypeAlias' = Union[(ToolChoiceOptions, ToolChoiceAllowedParam, ToolChoiceTypesParam, ToolChoiceFunctionParam, ToolChoiceMcpParam, ToolChoiceCustomParam, ToolChoiceApplyPatchParam, ToolChoiceShellParam)]

def ResponseCreateParamsNonStreaming():
    '''ResponseCreateParamsNonStreaming'''
    stream: 'Optional[Literal[False]]' = 'ResponseCreateParamsNonStreaming'

ResponseCreateParamsNonStreaming = <NODE:27>(ResponseCreateParamsNonStreaming, 'ResponseCreateParamsNonStreaming', ResponseCreateParamsBase, total = False)

class ResponseCreateParamsStreaming(ResponseCreateParamsBase):
    stream: 'Required[Literal[True]]' = 'ResponseCreateParamsStreaming'

ResponseCreateParams = Union[(ResponseCreateParamsNonStreaming, ResponseCreateParamsStreaming)]
