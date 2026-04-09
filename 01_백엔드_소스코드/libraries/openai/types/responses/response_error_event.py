# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_error_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseErrorEvent']

class ResponseErrorEvent(BaseModel):
    '''Emitted when an error occurs.'''
    message: str = None
    type: Literal['error'] = None
