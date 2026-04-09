# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: function_tool.pyc (Python 3.11)

from typing import Dict, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FunctionTool']

class FunctionTool(BaseModel):
    name: str = 'Defines a function in your own code the model can choose to call.\n\n    Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).\n    '
    parameters: Optional[Dict[(str, object)]] = None
    type: Literal['function'] = None
    description: Optional[str] = None
