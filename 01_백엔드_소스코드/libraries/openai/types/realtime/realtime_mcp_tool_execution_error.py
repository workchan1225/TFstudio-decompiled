# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_mcp_tool_execution_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeMcpToolExecutionError']

class RealtimeMcpToolExecutionError(BaseModel):
    type: Literal['tool_execution_error'] = 'RealtimeMcpToolExecutionError'
