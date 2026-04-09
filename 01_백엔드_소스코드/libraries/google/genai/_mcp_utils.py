# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _mcp_utils.pyc (Python 3.11)

'''Utils for working with MCP tools.'''
from importlib.metadata import PackageNotFoundError, version
import typing
from typing import Any
from  import _common
from  import types
if typing.TYPE_CHECKING:
    from mcp.types import Tool as McpTool
    from mcp import ClientSession as McpClientSession
else:
    McpClientSession: typing.Type = Any
    McpTool: typing.Type = Any
    
    try:
        from mcp.types import Tool as McpTool
        from mcp import ClientSession as McpClientSession
    except ImportError:
        McpTool = None
        McpClientSession = None

    
    def mcp_to_gemini_tool(tool = None):
        '''Translates an MCP tool to a Google GenAI tool.'''
        pass
    # WARNING: Decompyle incomplete

    
    def mcp_to_gemini_tools(tools = None):
        '''Translates a list of MCP tools to a list of Google GenAI tools.'''
        return tools()

    
    def has_mcp_tool_usage(tools = None):
        '''Checks whether the list of tools contains any MCP tools or sessions.'''
        pass
    # WARNING: Decompyle incomplete

    
    def has_mcp_session_usage(tools = None):
        '''Checks whether the list of tools contains any MCP sessions.'''
        pass
    # WARNING: Decompyle incomplete

    
    def set_mcp_usage_header(headers = None):
        '''Sets the MCP version label in the Google API client header.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _filter_to_supported_schema(schema = None):
        '''Filters the schema to only include fields that are supported by JSONSchema.'''
        pass
    # WARNING: Decompyle incomplete

    return None
