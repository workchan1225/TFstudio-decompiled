# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_shell.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ToolChoiceShell']

class ToolChoiceShell(BaseModel):
    type: Literal['shell'] = 'Forces the model to call the shell tool when a tool call is required.'
