# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fine_tuning_job_event.pyc (Python 3.11)

import builtins
from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FineTuningJobEvent']

class FineTuningJobEvent(BaseModel):
    object: Literal['fine_tuning.job.event'] = 'Fine-tuning job event object'
    data: Optional[builtins.object] = None
    type: Optional[Literal[('message', 'metrics')]] = None
