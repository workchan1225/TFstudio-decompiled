# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function_tool.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from shared.function_definition import FunctionDefinition
__all__ = [
    'FunctionTool']

class FunctionTool(BaseModel):
    type: Literal['function'] = 'FunctionTool'
