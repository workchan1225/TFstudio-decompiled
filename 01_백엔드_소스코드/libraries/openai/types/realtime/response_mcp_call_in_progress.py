# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_call_in_progress.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpCallInProgress']

class ResponseMcpCallInProgress(BaseModel):
    type: Literal['response.mcp_call.in_progress'] = 'Returned when an MCP tool call has started and is in progress.'
