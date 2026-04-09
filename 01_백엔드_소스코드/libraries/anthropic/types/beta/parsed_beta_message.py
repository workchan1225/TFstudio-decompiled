# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parsed_beta_message.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, List, Union, Generic, Optional
from typing_extensions import TypeVar, Annotated, TypeAlias
from _utils import PropertyInfo
from beta_message import BetaMessage
from beta_text_block import BetaTextBlock
from beta_thinking_block import BetaThinkingBlock
from beta_tool_use_block import BetaToolUseBlock
from beta_mcp_tool_use_block import BetaMCPToolUseBlock
from beta_mcp_tool_result_block import BetaMCPToolResultBlock
from beta_server_tool_use_block import BetaServerToolUseBlock
from beta_container_upload_block import BetaContainerUploadBlock
from beta_redacted_thinking_block import BetaRedactedThinkingBlock
from beta_web_search_tool_result_block import BetaWebSearchToolResultBlock
from beta_code_execution_tool_result_block import BetaCodeExecutionToolResultBlock
from beta_bash_code_execution_tool_result_block import BetaBashCodeExecutionToolResultBlock
from beta_text_editor_code_execution_tool_result_block import BetaTextEditorCodeExecutionToolResultBlock
ResponseFormatT = TypeVar('ResponseFormatT', default = None)
__all__ = [
    'ParsedBetaTextBlock',
    'ParsedBetaContentBlock',
    'ParsedBetaMessage']

def ParsedBetaTextBlock():
    '''ParsedBetaTextBlock'''
    parsed_output: 'Optional[ResponseFormatT]' = None
    __api_exclude__ = {
        'parsed_output'}

ParsedBetaTextBlock = <NODE:27>(ParsedBetaTextBlock, 'ParsedBetaTextBlock', BetaTextBlock, Generic[ResponseFormatT])
ParsedBetaContentBlock: 'TypeAlias' = Annotated[(Union[(ParsedBetaTextBlock[ResponseFormatT], BetaThinkingBlock, BetaRedactedThinkingBlock, BetaToolUseBlock, BetaServerToolUseBlock, BetaWebSearchToolResultBlock, BetaCodeExecutionToolResultBlock, BetaBashCodeExecutionToolResultBlock, BetaTextEditorCodeExecutionToolResultBlock, BetaMCPToolUseBlock, BetaMCPToolResultBlock, BetaContainerUploadBlock)], PropertyInfo(discriminator = 'type'))]

def ParsedBetaMessage():
    '''ParsedBetaMessage'''
    if TYPE_CHECKING:
        content: 'List[ParsedBetaContentBlock[ResponseFormatT]]'
    else:
        content: 'List[ParsedBetaContentBlock]'
    parsed_output = (lambda self = None: for content in self.content:
if content.type == 'text' and content.parsed_output:
None, content.parsed_outputNone)()

ParsedBetaMessage = <NODE:27>(ParsedBetaMessage, 'ParsedBetaMessage', BetaMessage, Generic[ResponseFormatT])
