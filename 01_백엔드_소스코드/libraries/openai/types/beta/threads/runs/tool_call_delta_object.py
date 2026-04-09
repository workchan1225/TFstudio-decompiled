# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_call_delta_object.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from tool_call_delta import ToolCallDelta
__all__ = [
    'ToolCallDeltaObject']

class ToolCallDeltaObject(BaseModel):
    type: Literal['tool_calls'] = 'Details of the tool call.'
    tool_calls: Optional[List[ToolCallDelta]] = None
