# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_error.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'RealtimeError']

class RealtimeError(BaseModel):
    type: str = 'Details of the error.'
    code: Optional[str] = None
    event_id: Optional[str] = None
    param: Optional[str] = None
