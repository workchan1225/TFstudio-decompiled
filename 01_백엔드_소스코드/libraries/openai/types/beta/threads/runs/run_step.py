# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run_step.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from shared.metadata import Metadata
from tool_calls_step_details import ToolCallsStepDetails
from message_creation_step_details import MessageCreationStepDetails
__all__ = [
    'RunStep',
    'LastError',
    'StepDetails',
    'Usage']

class LastError(BaseModel):
    message: str = 'The last error associated with this run step.\n\n    Will be `null` if there are no errors.\n    '

StepDetails: TypeAlias = Annotated[(Union[(MessageCreationStepDetails, ToolCallsStepDetails)], PropertyInfo(discriminator = 'type'))]

class Usage(BaseModel):
    total_tokens: int = "Usage statistics related to the run step.\n\n    This value will be `null` while the run step's status is `in_progress`.\n    "


class RunStep(BaseModel):
    assistant_id: str = 'Represents a step in execution of a run.'
    cancelled_at: Optional[int] = None
    created_at: int = None
    expired_at: Optional[int] = None
    failed_at: Optional[int] = None
    last_error: Optional[LastError] = None
    type: Literal[('message_creation', 'tool_calls')] = None
    usage: Optional[Usage] = None
