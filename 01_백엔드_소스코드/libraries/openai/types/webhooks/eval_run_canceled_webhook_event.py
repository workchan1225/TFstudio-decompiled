# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eval_run_canceled_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'EvalRunCanceledWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class EvalRunCanceledWebhookEvent(BaseModel):
    type: Literal['eval.run.canceled'] = 'Sent when an eval run has been canceled.'
    object: Optional[Literal['event']] = None
