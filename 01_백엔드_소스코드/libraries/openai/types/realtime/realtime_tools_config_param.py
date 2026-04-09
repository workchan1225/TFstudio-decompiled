# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_tools_config_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from realtime_function_tool_param import RealtimeFunctionToolParam
__all__ = [
    'RealtimeToolsConfigParam',
    'RealtimeToolsConfigUnionParam',
    'Mcp',
    'McpAllowedTools',
    'McpAllowedToolsMcpToolFilter',
    'McpRequireApproval',
    'McpRequireApprovalMcpToolApprovalFilter',
    'McpRequireApprovalMcpToolApprovalFilterAlways',
    'McpRequireApprovalMcpToolApprovalFilterNever']

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
RealtimeToolsConfigUnionParam: 'TypeAlias' = Union[(RealtimeFunctionToolParam, Mcp)]
RealtimeToolsConfigParam: 'TypeAlias' = List[RealtimeToolsConfigUnionParam]
