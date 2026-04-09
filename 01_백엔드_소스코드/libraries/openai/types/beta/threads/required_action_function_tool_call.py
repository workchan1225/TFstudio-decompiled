# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: required_action_function_tool_call.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RequiredActionFunctionToolCall',
    'Function']

class Function(BaseModel):
    name: str = 'The function definition.'


class RequiredActionFunctionToolCall(BaseModel):
    type: Literal['function'] = 'Tool call objects'
