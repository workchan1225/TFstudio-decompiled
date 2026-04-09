# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_mcp_call_failed.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseMcpCallFailed']

class ResponseMcpCallFailed(BaseModel):
    type: Literal['response.mcp_call.failed'] = 'Returned when an MCP tool call has failed.'
