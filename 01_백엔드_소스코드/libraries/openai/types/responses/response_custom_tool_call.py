# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_custom_tool_call.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCustomToolCall']

class ResponseCustomToolCall(BaseModel):
    type: Literal['custom_tool_call'] = 'A call to a custom tool created by the model.'
    id: Optional[str] = None
