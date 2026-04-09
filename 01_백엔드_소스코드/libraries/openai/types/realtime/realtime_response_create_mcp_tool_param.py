# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_response_create_mcp_tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
__all__ = [
    'RealtimeResponseCreateMcpToolParam',
    'AllowedTools',
    'AllowedToolsMcpToolFilter',
    'RequireApproval',
    'RequireApprovalMcpToolApprovalFilter',
    'RequireApprovalMcpToolApprovalFilterAlways',
    'RequireApprovalMcpToolApprovalFilterNever']

def AllowedToolsMcpToolFilter():
    '''AllowedToolsMcpToolFilter'''
    tool_names: 'SequenceNotStr[str]' = 'A filter object to specify which tools are allowed.'

AllowedToolsMcpToolFilter = <NODE:27>(AllowedToolsMcpToolFilter, 'AllowedToolsMcpToolFilter', TypedDict, total = False)
AllowedTools: 'TypeAlias' = Union[(SequenceNotStr[str], AllowedToolsMcpToolFilter)]

def RequireApprovalMcpToolApprovalFilterAlways():
    '''RequireApprovalMcpToolApprovalFilterAlways'''
    tool_names: 'SequenceNotStr[str]' = 'A filter object to specify which tools are allowed.'

RequireApprovalMcpToolApprovalFilterAlways = <NODE:27>(RequireApprovalMcpToolApprovalFilterAlways, 'RequireApprovalMcpToolApprovalFilterAlways', TypedDict, total = False)

def RequireApprovalMcpToolApprovalFilterNever():
    '''RequireApprovalMcpToolApprovalFilterNever'''
    tool_names: 'SequenceNotStr[str]' = 'A filter object to specify which tools are allowed.'

RequireApprovalMcpToolApprovalFilterNever = <NODE:27>(RequireApprovalMcpToolApprovalFilterNever, 'RequireApprovalMcpToolApprovalFilterNever', TypedDict, total = False)

def RequireApprovalMcpToolApprovalFilter():
    '''RequireApprovalMcpToolApprovalFilter'''
    never: 'RequireApprovalMcpToolApprovalFilterNever' = "Specify which of the MCP server's tools require approval.\n\n    Can be\n    `always`, `never`, or a filter object associated with tools\n    that require approval.\n    "

RequireApprovalMcpToolApprovalFilter = <NODE:27>(RequireApprovalMcpToolApprovalFilter, 'RequireApprovalMcpToolApprovalFilter', TypedDict, total = False)
RequireApproval: 'TypeAlias' = Union[(RequireApprovalMcpToolApprovalFilter, Literal[('always', 'never')])]

def RealtimeResponseCreateMcpToolParam():
    '''RealtimeResponseCreateMcpToolParam'''
    server_url: 'str' = '\n    Give the model access to additional tools via remote Model Context Protocol\n    (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).\n    '

RealtimeResponseCreateMcpToolParam = <NODE:27>(RealtimeResponseCreateMcpToolParam, 'RealtimeResponseCreateMcpToolParam', TypedDict, total = False)
