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
    type: Literal['response.created'] = 'Returned when a new Response is created.\n\n    The first event of response creation,\n    where the response is in an initial state of `in_progress`.\n    '
