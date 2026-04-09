# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_failed_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFailedWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class ResponseFailedWebhookEvent(BaseModel):
    type: Literal['response.failed'] = 'Sent when a background response has failed.'
    object: Optional[Literal['event']] = None
