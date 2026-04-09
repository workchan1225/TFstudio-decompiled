# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function_tool_call_delta.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FunctionToolCallDelta',
    'Function']

class Function(BaseModel):
    '''The definition of the function that was called.'''
    arguments: Optional[str] = None
    name: Optional[str] = None
    output: Optional[str] = None


class FunctionToolCallDelta(BaseModel):
    type: Literal['function'] = 'FunctionToolCallDelta'
    id: Optional[str] = None
    function: Optional[Function] = None
