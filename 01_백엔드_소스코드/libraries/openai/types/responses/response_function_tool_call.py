# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_tool_call.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFunctionToolCall']

class ResponseFunctionToolCall(BaseModel):
    type: Literal['function_call'] = 'A tool call to run a function.\n\n    See the\n    [function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.\n    '
    id: Optional[str] = None
    status: Optional[Literal[('in_progress', 'completed', 'incomplete')]] = None
