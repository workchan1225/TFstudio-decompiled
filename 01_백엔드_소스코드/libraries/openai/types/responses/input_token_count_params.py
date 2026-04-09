# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_token_count_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, TypeAlias, TypedDict
from tool_param import ToolParam
from tool_choice_options import ToolChoiceOptions
from tool_choice_mcp_param import ToolChoiceMcpParam
from tool_choice_shell_param import ToolChoiceShellParam
from tool_choice_types_param import ToolChoiceTypesParam
from shared_params.reasoning import Reasoning
from tool_choice_custom_param import ToolChoiceCustomParam
from response_input_item_param import ResponseInputItemParam
from tool_choice_allowed_param import ToolChoiceAllowedParam
from tool_choice_function_param import ToolChoiceFunctionParam
from response_conversation_param import ResponseConversationParam
from tool_choice_apply_patch_param import ToolChoiceApplyPatchParam
from response_format_text_config_param import ResponseFormatTextConfigParam
__all__ = [
    'InputTokenCountParams',
    'Conversation',
    'Text',
    'ToolChoice']

def InputTokenCountParams():
    '''InputTokenCountParams'''
    truncation: "Literal['auto', 'disabled']" = 'InputTokenCountParams'

InputTokenCountParams = <NODE:27>(InputTokenCountParams, 'InputTokenCountParams', TypedDict, total = False)
Conversation: 'TypeAlias' = Union[(str, ResponseConversationParam)]

def Text():
    '''Text'''
    verbosity: "Optional[Literal['low', 'medium', 'high']]" = 'Configuration options for a text response from the model.\n\n    Can be plain\n    text or structured JSON data. Learn more:\n    - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)\n    - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)\n    '

Text = <NODE:27>(Text, 'Text', TypedDict, total = False)
ToolChoice: 'TypeAlias' = Union[(ToolChoiceOptions, ToolChoiceAllowedParam, ToolChoiceTypesParam, ToolChoiceFunctionParam, ToolChoiceMcpParam, ToolChoiceCustomParam, ToolChoiceApplyPatchParam, ToolChoiceShellParam)]
