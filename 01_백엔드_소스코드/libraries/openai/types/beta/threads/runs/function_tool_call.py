# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function_tool_call.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FunctionToolCall',
    'Function']

class Function(BaseModel):
    name: str = 'The definition of the function that was called.'
    output: Optional[str] = None


class FunctionToolCall(BaseModel):
    type: Literal['function'] = 'FunctionToolCall'
