# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_failed_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BatchFailedWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class BatchFailedWebhookEvent(BaseModel):
    type: Literal['batch.failed'] = 'Sent when a batch API request has failed.'
    object: Optional[Literal['event']] = None
