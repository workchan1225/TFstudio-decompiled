# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_cancelled_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BatchCancelledWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class BatchCancelledWebhookEvent(BaseModel):
    type: Literal['batch.cancelled'] = 'Sent when a batch API request has been cancelled.'
    object: Optional[Literal['event']] = None
