# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mcp_list_tools_failed.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'McpListToolsFailed']

class McpListToolsFailed(BaseModel):
    type: Literal['mcp_list_tools.failed'] = 'Returned when listing MCP tools has failed for an item.'
