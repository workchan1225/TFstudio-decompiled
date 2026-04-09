# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run_step_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from run_step_delta import RunStepDelta
__all__ = [
    'RunStepDeltaEvent']

class RunStepDeltaEvent(BaseModel):
    object: Literal['thread.run.step.delta'] = 'Represents a run step delta i.e.\n\n    any changed fields on a run step during streaming.\n    '
