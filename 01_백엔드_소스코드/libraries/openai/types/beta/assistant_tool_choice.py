# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_tool_choice.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from assistant_tool_choice_function import AssistantToolChoiceFunction
__all__ = [
    'AssistantToolChoice']

class AssistantToolChoice(BaseModel):
    type: Literal[('function', 'code_interpreter', 'file_search')] = 'Specifies a tool the model should use.\n\n    Use to force the model to call a specific tool.\n    '
    function: Optional[AssistantToolChoiceFunction] = None
