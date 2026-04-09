# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_response_create_params_param.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, TypeAlias, TypedDict
from shared_params.metadata import Metadata
from conversation_item_param import ConversationItemParam
from realtime_function_tool_param import RealtimeFunctionToolParam
from responses.tool_choice_options import ToolChoiceOptions
from responses.response_prompt_param import ResponsePromptParam
from responses.tool_choice_mcp_param import ToolChoiceMcpParam
from responses.tool_choice_function_param import ToolChoiceFunctionParam
from realtime_response_create_mcp_tool_param import RealtimeResponseCreateMcpToolParam
from realtime_response_create_audio_output_param import RealtimeResponseCreateAudioOutputParam
__all__ = [
    'RealtimeResponseCreateParamsParam',
    'ToolChoice',
    'Tool']
ToolChoice: 'TypeAlias' = Union[(ToolChoiceOptions, ToolChoiceFunctionParam, ToolChoiceMcpParam)]
Tool: 'TypeAlias' = Union[(RealtimeFunctionToolParam, RealtimeResponseCreateMcpToolParam)]

def RealtimeResponseCreateParamsParam():
    '''RealtimeResponseCreateParamsParam'''
    tools: 'Iterable[Tool]' = 'Create a new Realtime response with these parameters'

RealtimeResponseCreateParamsParam = <NODE:27>(RealtimeResponseCreateParamsParam, 'RealtimeResponseCreateParamsParam', TypedDict, total = False)
