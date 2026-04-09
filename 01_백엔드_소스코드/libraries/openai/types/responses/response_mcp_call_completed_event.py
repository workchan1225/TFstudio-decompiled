# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_call_completed_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpCallCompletedEvent']

class ResponseMcpCallCompletedEvent(BaseModel):
    type: Literal['response.mcp_call.completed'] = 'Emitted when an MCP  tool call has completed successfully.'
