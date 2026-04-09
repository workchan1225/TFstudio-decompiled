# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_completed_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BatchCompletedWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class BatchCompletedWebhookEvent(BaseModel):
    type: Literal['batch.completed'] = 'Sent when a batch API request has been completed.'
    object: Optional[Literal['event']] = None
