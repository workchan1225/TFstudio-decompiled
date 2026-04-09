# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fine_tuning_job_cancelled_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FineTuningJobCancelledWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class FineTuningJobCancelledWebhookEvent(BaseModel):
    type: Literal['fine_tuning.job.cancelled'] = 'Sent when a fine-tuning job has been cancelled.'
    object: Optional[Literal['event']] = None
