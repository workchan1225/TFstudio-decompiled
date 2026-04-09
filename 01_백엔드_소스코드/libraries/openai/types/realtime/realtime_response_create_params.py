# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_response_create_params.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from shared.metadata import Metadata
from conversation_item import ConversationItem
from realtime_function_tool import RealtimeFunctionTool
from responses.response_prompt import ResponsePrompt
from responses.tool_choice_mcp import ToolChoiceMcp
from responses.tool_choice_options import ToolChoiceOptions
from responses.tool_choice_function import ToolChoiceFunction
from realtime_response_create_mcp_tool import RealtimeResponseCreateMcpTool
from realtime_response_create_audio_output import RealtimeResponseCreateAudioOutput
__all__ = [
    'RealtimeResponseCreateParams',
    'ToolChoice',
    'Tool']
ToolChoice: TypeAlias = Union[(ToolChoiceOptions, ToolChoiceFunction, ToolChoiceMcp)]
Tool: TypeAlias = Union[(RealtimeFunctionTool, RealtimeResponseCreateMcpTool)]

class RealtimeResponseCreateParams(BaseModel):
    '''Create a new Realtime response with these parameters'''
    audio: Optional[RealtimeResponseCreateAudioOutput] = None
    conversation: Union[(str, Literal[('auto', 'none')], None)] = None
    input: Optional[List[ConversationItem]] = None
    instructions: Optional[str] = None
    max_output_tokens: Union[(int, Literal['inf'], None)] = None
    metadata: Optional[Metadata] = None
    output_modalities: Optional[List[Literal[('text', 'audio')]]] = None
    prompt: Optional[ResponsePrompt] = None
    tool_choice: Optional[ToolChoice] = None
    tools: Optional[List[Tool]] = None
