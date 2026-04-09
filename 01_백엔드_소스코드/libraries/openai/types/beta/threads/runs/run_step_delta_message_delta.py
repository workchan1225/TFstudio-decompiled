# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run_step_delta_message_delta.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RunStepDeltaMessageDelta',
    'MessageCreation']

class MessageCreation(BaseModel):
    message_id: Optional[str] = None


class RunStepDeltaMessageDelta(BaseModel):
    type: Literal['message_creation'] = 'Details of the message creation by the run step.'
    message_creation: Optional[MessageCreation] = None
