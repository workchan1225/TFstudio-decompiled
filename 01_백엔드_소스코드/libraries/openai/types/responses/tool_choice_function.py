# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_function.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ToolChoiceFunction']

class ToolChoiceFunction(BaseModel):
    type: Literal['function'] = 'Use this option to force the model to call a specific function.'
