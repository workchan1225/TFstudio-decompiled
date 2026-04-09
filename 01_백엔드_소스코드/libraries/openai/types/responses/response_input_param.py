# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from easy_input_message_param import EasyInputMessageParam
from response_output_message_param import ResponseOutputMessageParam
from response_reasoning_item_param import ResponseReasoningItemParam
from response_custom_tool_call_param import ResponseCustomToolCallParam
from response_computer_tool_call_param import ResponseComputerToolCallParam
from response_function_tool_call_param import ResponseFunctionToolCallParam
from response_function_web_search_param import ResponseFunctionWebSearchParam
from response_compaction_item_param_param import ResponseCompactionItemParamParam
from response_file_search_tool_call_param import ResponseFileSearchToolCallParam
from response_custom_tool_call_output_param import ResponseCustomToolCallOutputParam
from response_code_interpreter_tool_call_param import ResponseCodeInterpreterToolCallParam
from response_input_message_content_list_param import ResponseInputMessageContentListParam
from response_function_call_output_item_list_param import ResponseFunctionCallOutputItemListParam
from response_function_shell_call_output_content_param import ResponseFunctionShellCallOutputContentParam
from response_computer_tool_call_output_screenshot_param import ResponseComputerToolCallOutputScreenshotParam
__all__ = [
    'ResponseInputParam',
    'ResponseInputItemParam',
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

def Message():
    '''Message'''
    type: "Literal['message']" = '\n    A message input to the model with a role indicating instruction following\n    hierarchy. Instructions given with the `developer` or `system` role take\n    precedence over instructions given with the `user` role.\n    '

Message = <NODE:27>(Message, 'Message', TypedDict, total = False)

def ComputerCallOutputAcknowledgedSafetyCheck():
    '''ComputerCallOutputAcknowledgedSafetyCheck'''
    message: 'Optional[str]' = 'A pending safety check for the computer call.'

ComputerCallOutputAcknowledgedSafetyCheck = <NODE:27>(ComputerCallOutputAcknowledgedSafetyCheck, 'ComputerCallOutputAcknowledgedSafetyCheck', TypedDict, total = False)

def ComputerCallOutput():
    '''ComputerCallOutput'''
    status: "Optional[Literal['in_progress', 'completed', 'incomplete']]" = 'The output of a computer tool call.'

ComputerCallOutput = <NODE:27>(ComputerCallOutput, 'ComputerCallOutput', TypedDict, total = False)

def FunctionCallOutput():
    '''FunctionCallOutput'''
    status: "Optional[Literal['in_progress', 'completed', 'incomplete']]" = 'The output of a function tool call.'

FunctionCallOutput = <NODE:27>(FunctionCallOutput, 'FunctionCallOutput', TypedDict, total = False)

def ImageGenerationCall():
    '''ImageGenerationCall'''
    type: "Required[Literal['image_generation_call']]" = 'An image generation request made by the model.'

ImageGenerationCall = <NODE:27>(ImageGenerationCall, 'ImageGenerationCall', TypedDict, total = False)

def LocalShellCallAction():
    '''LocalShellCallAction'''
    working_directory: 'Optional[str]' = 'Execute a shell command on the server.'

LocalShellCallAction = <NODE:27>(LocalShellCallAction, 'LocalShellCallAction', TypedDict, total = False)

def LocalShellCall():
    '''LocalShellCall'''
    type: "Required[Literal['local_shell_call']]" = 'A tool call to run a command on the local shell.'

LocalShellCall = <NODE:27>(LocalShellCall, 'LocalShellCall', TypedDict, total = False)

def LocalShellCallOutput():
    '''LocalShellCallOutput'''
    status: "Optional[Literal['in_progress', 'completed', 'incomplete']]" = 'The output of a local shell tool call.'

LocalShellCallOutput = <NODE:27>(LocalShellCallOutput, 'LocalShellCallOutput', TypedDict, total = False)

def ShellCallAction():
    '''ShellCallAction'''
    timeout_ms: 'Optional[int]' = 'The shell commands and limits that describe how to run the tool call.'

ShellCallAction = <NODE:27>(ShellCallAction, 'ShellCallAction', TypedDict, total = False)

def ShellCall():
    '''ShellCall'''
    status: "Optional[Literal['in_progress', 'completed', 'incomplete']]" = 'A tool representing a request to execute one or more shell commands.'

ShellCall = <NODE:27>(ShellCall, 'ShellCall', TypedDict, total = False)

def ShellCallOutput():
    '''ShellCallOutput'''
    max_output_length: 'Optional[int]' = 'The streamed output items emitted by a shell tool call.'

ShellCallOutput = <NODE:27>(ShellCallOutput, 'ShellCallOutput', TypedDict, total = False)

def ApplyPatchCallOperationCreateFile():
    '''ApplyPatchCallOperationCreateFile'''
    type: "Required[Literal['create_file']]" = 'Instruction for creating a new file via the apply_patch tool.'

ApplyPatchCallOperationCreateFile = <NODE:27>(ApplyPatchCallOperationCreateFile, 'ApplyPatchCallOperationCreateFile', TypedDict, total = False)

def ApplyPatchCallOperationDeleteFile():
    '''ApplyPatchCallOperationDeleteFile'''
    type: "Required[Literal['delete_file']]" = 'Instruction for deleting an existing file via the apply_patch tool.'

ApplyPatchCallOperationDeleteFile = <NODE:27>(ApplyPatchCallOperationDeleteFile, 'ApplyPatchCallOperationDeleteFile', TypedDict, total = False)

def ApplyPatchCallOperationUpdateFile():
    '''ApplyPatchCallOperationUpdateFile'''
    type: "Required[Literal['update_file']]" = 'Instruction for updating an existing file via the apply_patch tool.'

ApplyPatchCallOperationUpdateFile = <NODE:27>(ApplyPatchCallOperationUpdateFile, 'ApplyPatchCallOperationUpdateFile', TypedDict, total = False)
ApplyPatchCallOperation: 'TypeAlias' = Union[(ApplyPatchCallOperationCreateFile, ApplyPatchCallOperationDeleteFile, ApplyPatchCallOperationUpdateFile)]

def ApplyPatchCall():
    '''ApplyPatchCall'''
    id: 'Optional[str]' = '\n    A tool call representing a request to create, delete, or update files using diff patches.\n    '

ApplyPatchCall = <NODE:27>(ApplyPatchCall, 'ApplyPatchCall', TypedDict, total = False)

def ApplyPatchCallOutput():
    '''ApplyPatchCallOutput'''
    output: 'Optional[str]' = 'The streamed output emitted by an apply patch tool call.'

ApplyPatchCallOutput = <NODE:27>(ApplyPatchCallOutput, 'ApplyPatchCallOutput', TypedDict, total = False)

def McpListToolsTool():
    '''McpListToolsTool'''
    description: 'Optional[str]' = 'A tool available on an MCP server.'

McpListToolsTool = <NODE:27>(McpListToolsTool, 'McpListToolsTool', TypedDict, total = False)

def McpListTools():
    '''McpListTools'''
    error: 'Optional[str]' = 'A list of tools available on an MCP server.'

McpListTools = <NODE:27>(McpListTools, 'McpListTools', TypedDict, total = False)

def McpApprovalRequest():
    '''McpApprovalRequest'''
    type: "Required[Literal['mcp_approval_request']]" = 'A request for human approval of a tool invocation.'

McpApprovalRequest = <NODE:27>(McpApprovalRequest, 'McpApprovalRequest', TypedDict, total = False)

def McpApprovalResponse():
    '''McpApprovalResponse'''
    reason: 'Optional[str]' = 'A response to an MCP approval request.'

McpApprovalResponse = <NODE:27>(McpApprovalResponse, 'McpApprovalResponse', TypedDict, total = False)

def McpCall():
    '''McpCall'''
    status: "Literal['in_progress', 'completed', 'incomplete', 'calling', 'failed']" = 'An invocation of a tool on an MCP server.'

McpCall = <NODE:27>(McpCall, 'McpCall', TypedDict, total = False)

def ItemReference():
    '''ItemReference'''
    type: "Optional[Literal['item_reference']]" = 'An internal identifier for an item to reference.'

ItemReference = <NODE:27>(ItemReference, 'ItemReference', TypedDict, total = False)
ResponseInputItemParam: 'TypeAlias' = Union[(EasyInputMessageParam, Message, ResponseOutputMessageParam, ResponseFileSearchToolCallParam, ResponseComputerToolCallParam, ComputerCallOutput, ResponseFunctionWebSearchParam, ResponseFunctionToolCallParam, FunctionCallOutput, ResponseReasoningItemParam, ResponseCompactionItemParamParam, ImageGenerationCall, ResponseCodeInterpreterToolCallParam, LocalShellCall, LocalShellCallOutput, ShellCall, ShellCallOutput, ApplyPatchCall, ApplyPatchCallOutput, McpListTools, McpApprovalRequest, McpApprovalResponse, McpCall, ResponseCustomToolCallOutputParam, ResponseCustomToolCallParam, ItemReference)]
ResponseInputParam: 'TypeAlias' = List[ResponseInputItemParam]
