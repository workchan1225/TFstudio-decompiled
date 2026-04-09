# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_incomplete_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseIncompleteWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class ResponseIncompleteWebhookEvent(BaseModel):
    type: Literal['response.incomplete'] = 'Sent when a background response has been interrupted.'
    object: Optional[Literal['event']] = None
