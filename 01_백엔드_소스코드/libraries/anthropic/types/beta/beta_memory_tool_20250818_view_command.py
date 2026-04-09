# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_memory_tool_20250818_view_command.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaMemoryTool20250818ViewCommand']

class BetaMemoryTool20250818ViewCommand(BaseModel):
    path: str = 'BetaMemoryTool20250818ViewCommand'
    view_range: Optional[List[int]] = None
