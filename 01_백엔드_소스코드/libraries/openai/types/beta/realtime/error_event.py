# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ErrorEvent',
    'Error']

class Error(BaseModel):
    type: str = 'Error'
    code: Optional[str] = None
    event_id: Optional[str] = None
    param: Optional[str] = None


class ErrorEvent(BaseModel):
    type: Literal['error'] = 'ErrorEvent'
