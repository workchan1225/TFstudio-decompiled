# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_completed_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCompletedWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class ResponseCompletedWebhookEvent(BaseModel):
    type: Literal['response.completed'] = 'Sent when a background response has been completed.'
    object: Optional[Literal['event']] = None
