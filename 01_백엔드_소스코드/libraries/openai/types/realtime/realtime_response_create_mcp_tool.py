# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_response_create_mcp_tool.pyc (Python 3.11)

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
__all__ = [
    'RealtimeResponseCreateMcpTool',
    'AllowedTools',
    'AllowedToolsMcpToolFilter',
    'RequireApproval',
    'RequireApprovalMcpToolApprovalFilter',
    'RequireApprovalMcpToolApprovalFilterAlways',
    'RequireApprovalMcpToolApprovalFilterNever']

class AllowedToolsMcpToolFilter(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None

AllowedTools: TypeAlias = Union[(List[str], AllowedToolsMcpToolFilter, None)]

class RequireApprovalMcpToolApprovalFilterAlways(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None


class RequireApprovalMcpToolApprovalFilterNever(BaseModel):
    '''A filter object to specify which tools are allowed.'''
    read_only: Optional[bool] = None
    tool_names: Optional[List[str]] = None


class RequireApprovalMcpToolApprovalFilter(BaseModel):
    """Specify which of the MCP server's tools require approval.

    Can be
    `always`, `never`, or a filter object associated with tools
    that require approval.
    """
    always: Optional[RequireApprovalMcpToolApprovalFilterAlways] = None
    never: Optional[RequireApprovalMcpToolApprovalFilterNever] = None

RequireApproval: TypeAlias = Union[(RequireApprovalMcpToolApprovalFilter, Literal[('always', 'never')], None)]

class RealtimeResponseCreateMcpTool(BaseModel):
    type: Literal['mcp'] = '\n    Give the model access to additional tools via remote Model Context Protocol\n    (MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).\n    '
    allowed_tools: Optional[AllowedTools] = None
    authorization: Optional[str] = None
    connector_id: Optional[Literal[('connector_dropbox', 'connector_gmail', 'connector_googlecalendar', 'connector_googledrive', 'connector_microsoftteams', 'connector_outlookcalendar', 'connector_outlookemail', 'connector_sharepoint')]] = None
    headers: Optional[Dict[(str, str)]] = None
    require_approval: Optional[RequireApproval] = None
    server_description: Optional[str] = None
    server_url: Optional[str] = None
