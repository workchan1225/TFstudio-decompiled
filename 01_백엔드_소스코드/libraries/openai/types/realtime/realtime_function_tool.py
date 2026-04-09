# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_function_tool.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeFunctionTool']

class RealtimeFunctionTool(BaseModel):
    description: Optional[str] = None
    name: Optional[str] = None
    parameters: Optional[object] = None
    type: Optional[Literal['function']] = None
