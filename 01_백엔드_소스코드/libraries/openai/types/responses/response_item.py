# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_item.pyc (Python 3.11)

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from response_output_message import ResponseOutputMessage
from response_computer_tool_call import ResponseComputerToolCall
from response_input_message_item import ResponseInputMessageItem
from response_function_web_search import ResponseFunctionWebSearch
from response_apply_patch_tool_call import ResponseApplyPatchToolCall
from response_file_search_tool_call import ResponseFileSearchToolCall
from response_function_tool_call_item import ResponseFunctionToolCallItem
from response_function_shell_tool_call import ResponseFunctionShellToolCall
from response_code_interpreter_tool_call import ResponseCodeInterpreterToolCall
from response_apply_patch_tool_call_output import ResponseApplyPatchToolCallOutput
from response_computer_tool_call_output_item import ResponseComputerToolCallOutputItem
from response_function_tool_call_output_item import ResponseFunctionToolCallOutputItem
from response_function_shell_tool_call_output import ResponseFunctionShellToolCallOutput
__all__ = [
    'ResponseItem',
    'ImageGenerationCall',
    'LocalShellCall',
    'LocalShellCallAction',
    'LocalShellCallOutput',
    'McpListTools',
    'McpListToolsTool',
    'McpApprovalRequest',
    'McpApprovalResponse',
    'McpCall']

class ImageGenerationCall(BaseModel):
    id: str = 'An image generation request made by the model.'
    type: Literal['image_generation_call'] = None


class LocalShellCallAction(BaseModel):
    type: Literal['exec'] = 'Execute a shell command on the server.'
    timeout_ms: Optional[int] = None
    user: Optional[str] = None
    working_directory: Optional[str] = None


class LocalShellCall(BaseModel):
    type: Literal['local_shell_call'] = 'A tool call to run a command on the local shell.'


class LocalShellCallOutput(BaseModel):
    type: Literal['local_shell_call_output'] = 'The output of a local shell tool call.'
    status: Optional[Literal[('in_progress', 'completed', 'incomplete')]] = None


class McpListToolsTool(BaseModel):
    name: str = 'A tool available on an MCP server.'
    annotations: Optional[object] = None
    description: Optional[str] = None


class McpListTools(BaseModel):
    type: Literal['mcp_list_tools'] = 'A list of tools available on an MCP server.'
    error: Optional[str] = None


class McpApprovalRequest(BaseModel):
    type: Literal['mcp_approval_request'] = 'A request for human approval of a tool invocation.'


class McpApprovalResponse(BaseModel):
    type: Literal['mcp_approval_response'] = 'A response to an MCP approval request.'
    reason: Optional[str] = None


class McpCall(BaseModel):
    type: Literal['mcp_call'] = 'An invocation of a tool on an MCP server.'
    approval_request_id: Optional[str] = None
    error: Optional[str] = None
    output: Optional[str] = None
    status: Optional[Literal[('in_progress', 'completed', 'incomplete', 'calling', 'failed')]] = None

ResponseItem: TypeAlias = Annotated[(Union[(ResponseInputMessageItem, ResponseOutputMessage, ResponseFileSearchToolCall, ResponseComputerToolCall, ResponseComputerToolCallOutputItem, ResponseFunctionWebSearch, ResponseFunctionToolCallItem, ResponseFunctionToolCallOutputItem, ImageGenerationCall, ResponseCodeInterpreterToolCall, LocalShellCall, LocalShellCallOutput, ResponseFunctionShellToolCall, ResponseFunctionShellToolCallOutput, ResponseApplyPatchToolCall, ResponseApplyPatchToolCallOutput, McpListTools, McpApprovalRequest, McpApprovalResponse, McpCall)], PropertyInfo(discriminator = 'type'))]
