# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fine_tuning_job_failed_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FineTuningJobFailedWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class FineTuningJobFailedWebhookEvent(BaseModel):
    type: Literal['fine_tuning.job.failed'] = 'Sent when a fine-tuning job has failed.'
    object: Optional[Literal['event']] = None
