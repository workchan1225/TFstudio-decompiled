# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_mcp.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ToolChoiceMcp']

class ToolChoiceMcp(BaseModel):
    type: Literal['mcp'] = '\n    Use this option to force the model to call a specific tool on a remote MCP server.\n    '
    name: Optional[str] = None
