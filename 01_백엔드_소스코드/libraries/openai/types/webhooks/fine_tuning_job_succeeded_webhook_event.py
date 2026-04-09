# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fine_tuning_job_succeeded_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FineTuningJobSucceededWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class FineTuningJobSucceededWebhookEvent(BaseModel):
    type: Literal['fine_tuning.job.succeeded'] = 'Sent when a fine-tuning job has succeeded.'
    object: Optional[Literal['event']] = None
