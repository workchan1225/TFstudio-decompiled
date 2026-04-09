# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_mcp_tool_call_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from realtime_mcphttp_error_param import RealtimeMcphttpErrorParam
from realtime_mcp_protocol_error_param import RealtimeMcpProtocolErrorParam
from realtime_mcp_tool_execution_error_param import RealtimeMcpToolExecutionErrorParam
__all__ = [
    'RealtimeMcpToolCallParam',
    'Error']
Error: 'TypeAlias' = Union[(RealtimeMcpProtocolErrorParam, RealtimeMcpToolExecutionErrorParam, RealtimeMcphttpErrorParam)]

def RealtimeMcpToolCallParam():
    '''RealtimeMcpToolCallParam'''
    output: 'Optional[str]' = 'A Realtime item representing an invocation of a tool on an MCP server.'

RealtimeMcpToolCallParam = <NODE:27>(RealtimeMcpToolCallParam, 'RealtimeMcpToolCallParam', TypedDict, total = False)
