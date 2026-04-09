# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parsed_response.pyc (Python 3.11)

from typing import TYPE_CHECKING, List, Union, Generic, TypeVar, Optional
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from response import Response
from _models import GenericModel
from response_output_item import McpCall, McpListTools, LocalShellCall, McpApprovalRequest, ImageGenerationCall, LocalShellCallAction
from response_output_text import ResponseOutputText
from response_output_message import ResponseOutputMessage
from response_output_refusal import ResponseOutputRefusal
from response_reasoning_item import ResponseReasoningItem
from response_compaction_item import ResponseCompactionItem
from response_custom_tool_call import ResponseCustomToolCall
from response_computer_tool_call import ResponseComputerToolCall
from response_function_tool_call import ResponseFunctionToolCall
from response_function_web_search import ResponseFunctionWebSearch
from response_apply_patch_tool_call import ResponseApplyPatchToolCall
from response_file_search_tool_call import ResponseFileSearchToolCall
from response_function_shell_tool_call import ResponseFunctionShellToolCall
from response_code_interpreter_tool_call import ResponseCodeInterpreterToolCall
from response_apply_patch_tool_call_output import ResponseApplyPatchToolCallOutput
from response_function_shell_tool_call_output import ResponseFunctionShellToolCallOutput
__all__ = [
    'ParsedResponse',
    'ParsedResponseOutputMessage',
    'ParsedResponseOutputText']
ContentType = TypeVar('ContentType')

def ParsedResponseOutputText():
    '''ParsedResponseOutputText'''
    parsed: Optional[ContentType] = None

ParsedResponseOutputText = <NODE:27>(ParsedResponseOutputText, 'ParsedResponseOutputText', ResponseOutputText, GenericModel, Generic[ContentType])
ParsedContent: TypeAlias = Annotated[(Union[(ParsedResponseOutputText[ContentType], ResponseOutputRefusal)], PropertyInfo(discriminator = 'type'))]

def ParsedResponseOutputMessage():
    '''ParsedResponseOutputMessage'''
    if TYPE_CHECKING:
        content: List[ParsedContent[ContentType]]
        return None
    content: None[ParsedContent]

ParsedResponseOutputMessage = <NODE:27>(ParsedResponseOutputMessage, 'ParsedResponseOutputMessage', ResponseOutputMessage, GenericModel, Generic[ContentType])

class ParsedResponseFunctionToolCall(ResponseFunctionToolCall):
    parsed_arguments: object = None
    __api_exclude__ = {
        'parsed_arguments'}

ParsedResponseOutputItem: TypeAlias = Annotated[(Union[(ParsedResponseOutputMessage[ContentType], ParsedResponseFunctionToolCall, ResponseFileSearchToolCall, ResponseFunctionWebSearch, ResponseComputerToolCall, ResponseReasoningItem, McpCall, McpApprovalRequest, ImageGenerationCall, LocalShellCall, LocalShellCallAction, McpListTools, ResponseCodeInterpreterToolCall, ResponseCustomToolCall, ResponseCompactionItem, ResponseFunctionShellToolCall, ResponseFunctionShellToolCallOutput, ResponseApplyPatchToolCall, ResponseApplyPatchToolCallOutput)], PropertyInfo(discriminator = 'type'))]

def ParsedResponse():
    '''ParsedResponse'''
    if TYPE_CHECKING:
        output: List[ParsedResponseOutputItem[ContentType]]
    else:
        output: List[ParsedResponseOutputItem]
    output_parsed = (lambda self = None: for output in self.output:
if output.type == 'message':
for content in output.content:
if content.type == 'output_text' and content.parsed:
None, None, content.parsedNone)()

ParsedResponse = <NODE:27>(ParsedResponse, 'ParsedResponse', Response, GenericModel, Generic[ContentType])
