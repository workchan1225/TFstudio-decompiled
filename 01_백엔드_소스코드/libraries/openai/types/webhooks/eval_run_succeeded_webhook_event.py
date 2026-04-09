# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eval_run_succeeded_webhook_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'EvalRunSucceededWebhookEvent',
    'Data']

class Data(BaseModel):
    id: str = 'Event data payload.'


class EvalRunSucceededWebhookEvent(BaseModel):
    type: Literal['eval.run.succeeded'] = 'Sent when an eval run has succeeded.'
    object: Optional[Literal['event']] = None
