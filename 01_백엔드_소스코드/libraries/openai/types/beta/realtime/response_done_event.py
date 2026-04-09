# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from realtime_response import RealtimeResponse
__all__ = [
    'ResponseDoneEvent']

class ResponseDoneEvent(BaseModel):
    type: Literal['response.done'] = 'ResponseDoneEvent'
