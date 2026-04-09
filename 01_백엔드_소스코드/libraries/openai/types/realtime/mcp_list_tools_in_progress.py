# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mcp_list_tools_in_progress.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'McpListToolsInProgress']

class McpListToolsInProgress(BaseModel):
    type: Literal['mcp_list_tools.in_progress'] = 'Returned when listing MCP tools is in progress for an item.'
