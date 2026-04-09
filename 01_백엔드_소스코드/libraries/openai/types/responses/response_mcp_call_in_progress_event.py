# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_call_in_progress_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpCallInProgressEvent']

class ResponseMcpCallInProgressEvent(BaseModel):
    type: Literal['response.mcp_call.in_progress'] = 'Emitted when an MCP  tool call is in progress.'
