# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_item.pyc (Python 3.11)

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from easy_input_message import EasyInputMessage
from response_output_message import ResponseOutputMessage
from response_reasoning_item import ResponseReasoningItem
from response_custom_tool_call import ResponseCustomToolCall
from response_computer_tool_call import ResponseComputerToolCall
from response_function_tool_call import ResponseFunctionToolCall
from response_function_web_search import ResponseFunctionWebSearch
from response_compaction_item_param import ResponseCompactionItemParam
from response_file_search_tool_call import ResponseFileSearchToolCall
from response_custom_tool_call_output import ResponseCustomToolCallOutput
from response_code_interpreter_tool_call import ResponseCodeInterpreterToolCall
from response_input_message_content_list import ResponseInputMessageContentList
from response_function_call_output_item_list import ResponseFunctionCallOutputItemList
from response_function_shell_call_output_content import ResponseFunctionShellCallOutputContent
from response_computer_tool_call_output_screenshot import ResponseComputerToolCallOutputScreenshot
__all__ = [
    'ResponseInputItem',
    'Message',
    'ComputerCallOutput',
    'ComputerCallOutputAcknowledgedSafetyCheck',
    'FunctionCallOutput',
    'ImageGenerationCall',
    'LocalShellCall',
    'LocalShellCallAction',
    'LocalShellCallOutput',
    'ShellCall',
    'ShellCallAction',
    'ShellCallOutput',
    'ApplyPatchCall',
    'ApplyPatchCallOperation',
    'ApplyPatchCallOperationCreateFile',
    'ApplyPatchCallOperationDeleteFile',
    'ApplyPatchCallOperationUpdateFile',
    'ApplyPatchCallOutput',
    'McpListTools',
    'McpListToolsTool',
    'McpApprovalRequest',
    'McpApprovalResponse',
    'McpCall',
    'ItemReference']

class Message(BaseModel):
    role: Literal[('user', 'system', 'developer')] = '\n    A message input to the model with a role indicating instruction following\n    hierarchy. Instructions given with the `developer` or `system` role take\n    precedence over instructions given with the `user` role.\n    '
    status: Optional[Literal[('in_progress', 'completed', 'incomplete')]] = None
    type: Optional[Literal['message']] = None


class ComputerCallOutputAcknowledgedSafetyCheck(BaseModel):
    id: str = 'A pending safety check for the computer call.'
    code: Optional[str] = None
    message: Optional[str] = None


class ComputerCallOutput(BaseModel):
    type: Literal['computer_call_output'] = 'The output of a computer tool call.'
    id: Optional[str] = None
    acknowledged_safety_checks: Optional[List[ComputerCallOutputAcknowledgedSafetyCheck]] = None
    status: Optional[Literal[('in_progress', 'completed', 'incomplete')]] = None


class FunctionCallOutput(BaseModel):
    type: Literal['function_call_output'] = 'The output of a function tool call.'
    id: Optional[str] = None
    status: Optional[Literal[('in_progress', 'completed', 'incomplete')]] = None


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


class ShellCallAction(BaseModel):
    commands: List[str] = 'The shell commands and limits that describe how to run the tool call.'
    max_output_length: Optional[int] = None
    timeout_ms: Optional[int] = None


class ShellCall(BaseModel):
    type: Literal['shell_call'] = 'A tool representing a request to execute one or more shell commands.'
    id: Optional[str] = None
    status: Optional[Literal[('in_progress', 'completed', 'incomplete')]] = None


class ShellCallOutput(BaseModel):
    type: Literal['shell_call_output'] = 'The streamed output items emitted by a shell tool call.'
    id: Optional[str] = None
    max_output_length: Optional[int] = None


class ApplyPatchCallOperationCreateFile(BaseModel):
    type: Literal['create_file'] = 'Instruction for creating a new file via the apply_patch tool.'


class ApplyPatchCallOperationDeleteFile(BaseModel):
    type: Literal['delete_file'] = 'Instruction for deleting an existing file via the apply_patch tool.'


class ApplyPatchCallOperationUpdateFile(BaseModel):
    type: Literal['update_file'] = 'Instruction for updating an existing file via the apply_patch tool.'

ApplyPatchCallOperation: TypeAlias = Annotated[(Union[(ApplyPatchCallOperationCreateFile, ApplyPatchCallOperationDeleteFile, ApplyPatchCallOperationUpdateFile)], PropertyInfo(discriminator = 'type'))]

class ApplyPatchCall(BaseModel):
    type: Literal['apply_patch_call'] = '\n    A tool call representing a request to create, delete, or update files using diff patches.\n    '
    id: Optional[str] = None


class ApplyPatchCallOutput(BaseModel):
    type: Literal['apply_patch_call_output'] = 'The streamed output emitted by an apply patch tool call.'
    id: Optional[str] = None
    output: Optional[str] = None


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
    id: Optional[str] = None
    reason: Optional[str] = None


class McpCall(BaseModel):
    type: Literal['mcp_call'] = 'An invocation of a tool on an MCP server.'
    approval_request_id: Optional[str] = None
    error: Optional[str] = None
    output: Optional[str] = None
    status: Optional[Literal[('in_progress', 'completed', 'incomplete', 'calling', 'failed')]] = None


class ItemReference(BaseModel):
    id: str = 'An internal identifier for an item to reference.'
    type: Optional[Literal['item_reference']] = None

ResponseInputItem: TypeAlias = Annotated[(Union[(EasyInputMessage, Message, ResponseOutputMessage, ResponseFileSearchToolCall, ResponseComputerToolCall, ComputerCallOutput, ResponseFunctionWebSearch, ResponseFunctionToolCall, FunctionCallOutput, ResponseReasoningItem, ResponseCompactionItemParam, ImageGenerationCall, ResponseCodeInterpreterToolCall, LocalShellCall, LocalShellCallOutput, ShellCall, ShellCallOutput, ApplyPatchCall, ApplyPatchCallOutput, McpListTools, McpApprovalRequest, McpApprovalResponse, McpCall, ResponseCustomToolCallOutput, ResponseCustomToolCall, ItemReference)], PropertyInfo(discriminator = 'type'))]
