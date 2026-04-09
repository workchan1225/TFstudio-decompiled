# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_shell_tool_call.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFunctionShellToolCall',
    'Action']

class Action(BaseModel):
    commands: List[str] = 'The shell commands and limits that describe how to run the tool call.'
    max_output_length: Optional[int] = None
    timeout_ms: Optional[int] = None


class ResponseFunctionShellToolCall(BaseModel):
    type: Literal['shell_call'] = 'A tool call that executes one or more shell commands in a managed environment.'
    created_by: Optional[str] = None
