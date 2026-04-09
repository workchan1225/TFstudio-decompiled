# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _adapters.pyc (Python 3.11)

import typing
from _mcp_utils import mcp_to_gemini_tools
from types import FunctionCall, Tool
if typing.TYPE_CHECKING:
    from mcp import types as mcp_types
    from mcp import ClientSession

class McpToGenAiToolAdapter:
    '''Adapter for working with MCP tools in a GenAI client.'''
    
    def __init__(self = None, session = None, list_tools_result = None):
        self._mcp_session = session
        self._list_tools_result = list_tools_result

    
    async def call_tool(self = None, function_call = None):
        '''Calls a function on the MCP server.'''
        pass
    # WARNING: Decompyle incomplete

    tools = (lambda self = None: mcp_to_gemini_tools(self._list_tools_result.tools))()
