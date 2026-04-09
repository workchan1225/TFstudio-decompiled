# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_response_status.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeResponseStatus',
    'Error']

class Error(BaseModel):
    code: Optional[str] = None
    type: Optional[str] = None


class RealtimeResponseStatus(BaseModel):
    error: Optional[Error] = None
    reason: Optional[Literal[('turn_detected', 'client_cancelled', 'max_output_tokens', 'content_filter')]] = None
    type: Optional[Literal[('completed', 'cancelled', 'incomplete', 'failed')]] = None
