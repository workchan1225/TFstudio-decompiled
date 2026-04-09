# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_call_completed.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpCallCompleted']

class ResponseMcpCallCompleted(BaseModel):
    type: Literal['response.mcp_call.completed'] = 'Returned when an MCP tool call has completed successfully.'
