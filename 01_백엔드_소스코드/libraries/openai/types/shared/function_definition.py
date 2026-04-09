# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function_definition.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
from function_parameters import FunctionParameters
__all__ = [
    'FunctionDefinition']

class FunctionDefinition(BaseModel):
    name: str = 'FunctionDefinition'
    description: Optional[str] = None
    parameters: Optional[FunctionParameters] = None
    strict: Optional[bool] = None
