# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_cancel_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCancelEvent']

class ResponseCancelEvent(BaseModel):
    type: Literal['response.cancel'] = 'ResponseCancelEvent'
    event_id: Optional[str] = None
    response_id: Optional[str] = None
