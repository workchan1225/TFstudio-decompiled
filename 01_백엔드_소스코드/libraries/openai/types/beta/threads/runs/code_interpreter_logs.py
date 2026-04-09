# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: code_interpreter_logs.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'CodeInterpreterLogs']

class CodeInterpreterLogs(BaseModel):
    type: Literal['logs'] = 'Text output from the Code Interpreter tool call as part of a run step.'
    logs: Optional[str] = None
