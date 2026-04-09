# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_mcp_list_tools.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeMcpListTools',
    'Tool']

class Tool(BaseModel):
    name: str = 'A tool available on an MCP server.'
    annotations: Optional[object] = None
    description: Optional[str] = None


class RealtimeMcpListTools(BaseModel):
    type: Literal['mcp_list_tools'] = 'A Realtime item listing tools available on an MCP server.'
    id: Optional[str] = None
