# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_error_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from realtime_error import RealtimeError
__all__ = [
    'RealtimeErrorEvent']

class RealtimeErrorEvent(BaseModel):
    type: Literal['error'] = '\n    Returned when an error occurs, which could be a client problem or a server\n    problem. Most errors are recoverable and the session will stay open, we\n    recommend to implementors to monitor and log error messages by default.\n    '
