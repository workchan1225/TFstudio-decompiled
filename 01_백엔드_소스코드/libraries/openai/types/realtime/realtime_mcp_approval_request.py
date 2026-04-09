# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_mcp_approval_request.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeMcpApprovalRequest']

class RealtimeMcpApprovalRequest(BaseModel):
    type: Literal['mcp_approval_request'] = 'A Realtime item requesting human approval of a tool invocation.'
