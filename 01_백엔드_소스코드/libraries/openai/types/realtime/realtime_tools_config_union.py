# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_tools_config_union.pyc (Python 3.11)

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from realtime_function_tool import RealtimeFunctionTool
__all__ = [
    'RealtimeToolsConfigUnion',
    'Mcp',
    'McpAllowedTools',
    'McpAllowedToolsMcpToolFilter',
    'McpRequireApproval',
    'McpRequireApprovalMcpToolApprovalFilter',
    'McpRequireApprovalMcpToolApprovalFilterAlways',
    'McpRequireApprovalMcpToolApprovalFilterNever']

class McpAllowedToolsMcpToolFilter(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None

McpAllowedTools: TypeAlias = Union[(List[str], McpAllowedToolsMcpToolFilter, None)]

class McpRequireApprovalMcpToolApprovalFilterAlways(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None


class McpRequireApprovalMcpToolApprovalFilterNever(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None


class McpRequireApprovalMcpToolApprovalFilter(BaseModel):
    """Specify which of the MCP server's tools require approval.

    Can be
    `always`, `never`, or a filter object associated with tools
    that require approval.
    """
    always: Optional[McpRequireApprovalMcpToolApprovalFilterAlways] = None
    never: Optional[McpRequireApprovalMcpToolApprovalFilterNever] = None

McpRequireApproval: TypeAlias = Union[(McpRequireApprovalMcpToolApprovalFilter, Literal[('always', 'never')], None)]

class Mcp(BaseModel):
    type: Literal['mcp'] = '\n    Give the model access to additional tools via remote Model Context Protocol\n    (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).\n    '
    allowed_tools: Optional[McpAllowedTools] = None
    authorization: Optional[str] = None
    connector_id: Optional[Literal[('connector_dropbox', 'connector_gmail', 'connector_googlecalendar', 'connector_googledrive', 'connector_microsoftteams', 'connector_outlookcalendar', 'connector_outlookemail', 'connector_sharepoint')]] = None
    headers: Optional[Dict[(str, str)]] = None
    require_approval: Optional[McpRequireApproval] = None
    server_description: Optional[str] = None
    server_url: Optional[str] = None

RealtimeToolsConfigUnion: TypeAlias = Annotated[(Union[(RealtimeFunctionTool, Mcp)], PropertyInfo(discriminator = 'type'))]
