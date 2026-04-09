# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from  import web_search_tool_param
from chat import ChatCompletionFunctionToolParam
from _types import SequenceNotStr
from custom_tool_param import CustomToolParam
from computer_tool_param import ComputerToolParam
from function_tool_param import FunctionToolParam
from web_search_tool_param import WebSearchToolParam
from apply_patch_tool_param import ApplyPatchToolParam
from file_search_tool_param import FileSearchToolParam
from function_shell_tool_param import FunctionShellToolParam
from web_search_preview_tool_param import WebSearchPreviewToolParam
__all__ = [
    'ToolParam',
    'Mcp',
    'McpAllowedTools',
    'McpAllowedToolsMcpToolFilter',
    'McpRequireApproval',
    'McpRequireApprovalMcpToolApprovalFilter',
    'McpRequireApprovalMcpToolApprovalFilterAlways',
    'McpRequireApprovalMcpToolApprovalFilterNever',
    'CodeInterpreter',
    'CodeInterpreterContainer',
    'CodeInterpreterContainerCodeInterpreterToolAuto',
    'ImageGeneration',
    'ImageGenerationInputImageMask',
    'LocalShell']
WebSearchTool = web_search_tool_param.WebSearchToolParam
WebSearchToolFilters = web_search_tool_param.Filters
WebSearchToolUserLocation = web_search_tool_param.UserLocation

def McpAllowedToolsMcpToolFilter():
    '''McpAllowedToolsMcpToolFilter'''
    tool_names: 'SequenceNotStr[str]' = 'A filter object to specify which tools are allowed.'

McpAllowedToolsMcpToolFilter = <NODE:27>(McpAllowedToolsMcpToolFilter, 'McpAllowedToolsMcpToolFilter', TypedDict, total = False)
McpAllowedTools: 'TypeAlias' = Union[(SequenceNotStr[str], McpAllowedToolsMcpToolFilter)]

def McpRequireApprovalMcpToolApprovalFilterAlways():
    '''McpRequireApprovalMcpToolApprovalFilterAlways'''
    tool_names: 'SequenceNotStr[str]' = 'A filter object to specify which tools are allowed.'

McpRequireApprovalMcpToolApprovalFilterAlways = <NODE:27>(McpRequireApprovalMcpToolApprovalFilterAlways, 'McpRequireApprovalMcpToolApprovalFilterAlways', TypedDict, total = False)

def McpRequireApprovalMcpToolApprovalFilterNever():
    '''McpRequireApprovalMcpToolApprovalFilterNever'''
    tool_names: 'SequenceNotStr[str]' = 'A filter object to specify which tools are allowed.'

McpRequireApprovalMcpToolApprovalFilterNever = <NODE:27>(McpRequireApprovalMcpToolApprovalFilterNever, 'McpRequireApprovalMcpToolApprovalFilterNever', TypedDict, total = False)

def McpRequireApprovalMcpToolApprovalFilter():
    '''McpRequireApprovalMcpToolApprovalFilter'''
    never: 'McpRequireApprovalMcpToolApprovalFilterNever' = "Specify which of the MCP server's tools require approval.\n\n    Can be\n    `always`, `never`, or a filter object associated with tools\n    that require approval.\n    "

McpRequireApprovalMcpToolApprovalFilter = <NODE:27>(McpRequireApprovalMcpToolApprovalFilter, 'McpRequireApprovalMcpToolApprovalFilter', TypedDict, total = False)
McpRequireApproval: 'TypeAlias' = Union[(McpRequireApprovalMcpToolApprovalFilter, Literal[('always', 'never')])]

def Mcp():
    '''Mcp'''
    server_url: 'str' = '\n    Give the model access to additional tools via remote Model Context Protocol\n    (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).\n    '

Mcp = <NODE:27>(Mcp, 'Mcp', TypedDict, total = False)

def CodeInterpreterContainerCodeInterpreterToolAuto():
    '''CodeInterpreterContainerCodeInterpreterToolAuto'''
    memory_limit: "Optional[Literal['1g', '4g', '16g', '64g']]" = 'Configuration for a code interpreter container.\n\n    Optionally specify the IDs of the files to run the code on.\n    '

CodeInterpreterContainerCodeInterpreterToolAuto = <NODE:27>(CodeInterpreterContainerCodeInterpreterToolAuto, 'CodeInterpreterContainerCodeInterpreterToolAuto', TypedDict, total = False)
CodeInterpreterContainer: 'TypeAlias' = Union[(str, CodeInterpreterContainerCodeInterpreterToolAuto)]

def CodeInterpreter():
    '''CodeInterpreter'''
    type: "Required[Literal['code_interpreter']]" = 'A tool that runs Python code to help generate a response to a prompt.'

CodeInterpreter = <NODE:27>(CodeInterpreter, 'CodeInterpreter', TypedDict, total = False)

def ImageGenerationInputImageMask():
    '''ImageGenerationInputImageMask'''
    image_url: 'str' = 'Optional mask for inpainting.\n\n    Contains `image_url`\n    (string, optional) and `file_id` (string, optional).\n    '

ImageGenerationInputImageMask = <NODE:27>(ImageGenerationInputImageMask, 'ImageGenerationInputImageMask', TypedDict, total = False)

def ImageGeneration():
    '''ImageGeneration'''
    size: "Literal['1024x1024', '1024x1536', '1536x1024', 'auto']" = 'A tool that generates images using the GPT image models.'

ImageGeneration = <NODE:27>(ImageGeneration, 'ImageGeneration', TypedDict, total = False)

def LocalShell():
    '''LocalShell'''
    type: "Required[Literal['local_shell']]" = 'A tool that allows the model to execute shell commands in a local environment.'

LocalShell = <NODE:27>(LocalShell, 'LocalShell', TypedDict, total = False)
ToolParam: 'TypeAlias' = Union[(FunctionToolParam, FileSearchToolParam, ComputerToolParam, WebSearchToolParam, Mcp, CodeInterpreter, ImageGeneration, LocalShell, FunctionShellToolParam, CustomToolParam, WebSearchPreviewToolParam, ApplyPatchToolParam)]
ParseableToolParam: 'TypeAlias' = Union[(ToolParam, ChatCompletionFunctionToolParam)]
