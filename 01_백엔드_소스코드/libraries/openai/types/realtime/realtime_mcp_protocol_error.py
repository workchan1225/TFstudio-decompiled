# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_mcp_protocol_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeMcpProtocolError']

class RealtimeMcpProtocolError(BaseModel):
    type: Literal['protocol_error'] = 'RealtimeMcpProtocolError'
