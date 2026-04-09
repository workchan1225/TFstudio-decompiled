# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_queued_event.pyc (Python 3.11)

from typing_extensions import Literal
from response import Response
from _models import BaseModel
__all__ = [
    'ResponseQueuedEvent']

class ResponseQueuedEvent(BaseModel):
    type: Literal['response.queued'] = 'Emitted when a response is queued and waiting to be processed.'
