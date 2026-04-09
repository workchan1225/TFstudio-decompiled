# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run_step_delta.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from tool_call_delta_object import ToolCallDeltaObject
from run_step_delta_message_delta import RunStepDeltaMessageDelta
__all__ = [
    'RunStepDelta',
    'StepDetails']
StepDetails: TypeAlias = Annotated[(Union[(RunStepDeltaMessageDelta, ToolCallDeltaObject)], PropertyInfo(discriminator = 'type'))]

class RunStepDelta(BaseModel):
    '''The delta containing the fields that have changed on the run step.'''
    step_details: Optional[StepDetails] = None
