# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_created_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from realtime_response import RealtimeResponse
__all__ = [
    'ResponseCreatedEvent']

class ResponseCreatedEvent(BaseModel):
    type: Literal['response.created'] = 'ResponseCreatedEvent'
