# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_mcp_approval_response.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeMcpApprovalResponse']

class RealtimeMcpApprovalResponse(BaseModel):
    type: Literal['mcp_approval_response'] = 'A Realtime item responding to an MCP approval request.'
    reason: Optional[str] = None
