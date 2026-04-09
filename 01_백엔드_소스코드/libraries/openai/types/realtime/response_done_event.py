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
    type: Literal['response.done'] = 'Returned when a Response is done streaming.\n\n    Always emitted, no matter the\n    final state. The Response object included in the `response.done` event will\n    include all output Items in the Response but will omit the raw audio data.\n\n    Clients should check the `status` field of the Response to determine if it was successful\n    (`completed`) or if there was another outcome: `cancelled`, `failed`, or `incomplete`.\n\n    A response will contain all output items that were generated during the response, excluding\n    any audio content.\n    '
