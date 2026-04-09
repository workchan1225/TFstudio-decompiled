# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_expired_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BatchExpiredWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class BatchExpiredWebhookEvent(BaseModel):
    type: Literal['batch.expired'] = 'Sent when a batch API request has expired.'
    object: Optional[Literal['event']] = None
