# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: code_interpreter_tool.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'CodeInterpreterTool']

class CodeInterpreterTool(BaseModel):
    type: Literal['code_interpreter'] = 'CodeInterpreterTool'
