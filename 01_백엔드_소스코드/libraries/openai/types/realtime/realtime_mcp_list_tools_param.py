# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_mcp_list_tools_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'RealtimeMcpListToolsParam',
    'Tool']

def Tool():
    '''Tool'''
    description: 'Optional[str]' = 'A tool available on an MCP server.'

Tool = <NODE:27>(Tool, 'Tool', TypedDict, total = False)

def RealtimeMcpListToolsParam():
    '''RealtimeMcpListToolsParam'''
    id: 'str' = 'A Realtime item listing tools available on an MCP server.'

RealtimeMcpListToolsParam = <NODE:27>(RealtimeMcpListToolsParam, 'RealtimeMcpListToolsParam', TypedDict, total = False)
