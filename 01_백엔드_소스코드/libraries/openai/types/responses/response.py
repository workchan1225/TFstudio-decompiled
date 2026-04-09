# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias
from tool import Tool
from _models import BaseModel
from response_error import ResponseError
from response_usage import ResponseUsage
from response_prompt import ResponsePrompt
from response_status import ResponseStatus
from tool_choice_mcp import ToolChoiceMcp
from shared.metadata import Metadata
from shared.reasoning import Reasoning
from tool_choice_shell import ToolChoiceShell
from tool_choice_types import ToolChoiceTypes
from tool_choice_custom import ToolChoiceCustom
from response_input_item import ResponseInputItem
from tool_choice_allowed import ToolChoiceAllowed
from tool_choice_options import ToolChoiceOptions
from response_output_item import ResponseOutputItem
from response_text_config import ResponseTextConfig
from tool_choice_function import ToolChoiceFunction
from shared.responses_model import ResponsesModel
from tool_choice_apply_patch import ToolChoiceApplyPatch
__all__ = [
    'Response',
    'IncompleteDetails',
    'ToolChoice',
    'Conversation']

class IncompleteDetails(BaseModel):
    '''Details about why the response is incomplete.'''
    reason: Optional[Literal[('max_output_tokens', 'content_filter')]] = None

ToolChoice: TypeAlias = Union[(ToolChoiceOptions, ToolChoiceAllowed, ToolChoiceTypes, ToolChoiceFunction, ToolChoiceMcp, ToolChoiceCustom, ToolChoiceApplyPatch, ToolChoiceShell)]

class Conversation(BaseModel):
    id: str = 'The conversation that this response belongs to.\n\n    Input items and output items from this response are automatically added to this conversation.\n    '


class Response(BaseModel):
    created_at: float = 'Response'
    error: Optional[ResponseError] = None
    incomplete_details: Optional[IncompleteDetails] = None
    instructions: Union[(str, List[ResponseInputItem], None)] = None
    parallel_tool_calls: bool = None
    tools: List[Tool] = None
    top_p: Optional[float] = None
    background: Optional[bool] = None
    conversation: Optional[Conversation] = None
    max_output_tokens: Optional[int] = None
    max_tool_calls: Optional[int] = None
    previous_response_id: Optional[str] = None
    prompt: Optional[ResponsePrompt] = None
    prompt_cache_key: Optional[str] = None
    prompt_cache_retention: Optional[Literal[('in-memory', '24h')]] = None
    reasoning: Optional[Reasoning] = None
    safety_identifier: Optional[str] = None
    service_tier: Optional[Literal[('auto', 'default', 'flex', 'scale', 'priority')]] = None
    status: Optional[ResponseStatus] = None
    text: Optional[ResponseTextConfig] = None
    top_logprobs: Optional[int] = None
    truncation: Optional[Literal[('auto', 'disabled')]] = None
    usage: Optional[ResponseUsage] = None
    user: Optional[str] = None
    output_text = (lambda self = None: texts = []for output in self.output:
if output.type == 'message':
for content in output.content:
if content.type == 'output_text':
texts.append(content.text)''.join(texts))()
