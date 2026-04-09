# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_cancelled_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCancelledWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class ResponseCancelledWebhookEvent(BaseModel):
    type: Literal['response.cancelled'] = 'Sent when a background response has been cancelled.'
    object: Optional[Literal['event']] = None
