# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eval_run_failed_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'EvalRunFailedWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class EvalRunFailedWebhookEvent(BaseModel):
    type: Literal['eval.run.failed'] = 'Sent when an eval run has failed.'
    object: Optional[Literal['event']] = None
