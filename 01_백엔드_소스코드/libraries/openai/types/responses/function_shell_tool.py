# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function_shell_tool.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FunctionShellTool']

class FunctionShellTool(BaseModel):
    type: Literal['shell'] = 'A tool that allows the model to execute shell commands.'
