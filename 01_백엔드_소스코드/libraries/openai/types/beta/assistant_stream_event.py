# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_stream_event.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from thread import Thread
from _utils import PropertyInfo
from _models import BaseModel
from threads.run import Run
from threads.message import Message
from shared.error_object import ErrorObject
from threads.runs.run_step import RunStep
from threads.message_delta_event import MessageDeltaEvent
from threads.runs.run_step_delta_event import RunStepDeltaEvent
__all__ = [
    'AssistantStreamEvent',
    'ThreadCreated',
    'ThreadRunCreated',
    'ThreadRunQueued',
    'ThreadRunInProgress',
    'ThreadRunRequiresAction',
    'ThreadRunCompleted',
    'ThreadRunIncomplete',
    'ThreadRunFailed',
    'ThreadRunCancelling',
    'ThreadRunCancelled',
    'ThreadRunExpired',
    'ThreadRunStepCreated',
    'ThreadRunStepInProgress',
    'ThreadRunStepDelta',
    'ThreadRunStepCompleted',
    'ThreadRunStepFailed',
    'ThreadRunStepCancelled',
    'ThreadRunStepExpired',
    'ThreadMessageCreated',
    'ThreadMessageInProgress',
    'ThreadMessageDelta',
    'ThreadMessageCompleted',
    'ThreadMessageIncomplete',
    'ErrorEvent']

class ThreadCreated(BaseModel):
    event: Literal['thread.created'] = '\n    Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.\n    '
    enabled: Optional[bool] = None


class ThreadRunCreated(BaseModel):
    event: Literal['thread.run.created'] = '\n    Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.\n    '


class ThreadRunQueued(BaseModel):
    event: Literal['thread.run.queued'] = '\n    Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.\n    '


class ThreadRunInProgress(BaseModel):
    event: Literal['thread.run.in_progress'] = '\n    Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.\n    '


class ThreadRunRequiresAction(BaseModel):
    event: Literal['thread.run.requires_action'] = '\n    Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.\n    '


class ThreadRunCompleted(BaseModel):
    event: Literal['thread.run.completed'] = '\n    Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.\n    '


class ThreadRunIncomplete(BaseModel):
    event: Literal['thread.run.incomplete'] = '\n    Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.\n    '


class ThreadRunFailed(BaseModel):
    event: Literal['thread.run.failed'] = '\n    Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.\n    '


class ThreadRunCancelling(BaseModel):
    event: Literal['thread.run.cancelling'] = '\n    Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.\n    '


class ThreadRunCancelled(BaseModel):
    event: Literal['thread.run.cancelled'] = '\n    Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.\n    '


class ThreadRunExpired(BaseModel):
    event: Literal['thread.run.expired'] = '\n    Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.\n    '


class ThreadRunStepCreated(BaseModel):
    event: Literal['thread.run.step.created'] = '\n    Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.\n    '


class ThreadRunStepInProgress(BaseModel):
    event: Literal['thread.run.step.in_progress'] = '\n    Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.\n    '


class ThreadRunStepDelta(BaseModel):
    event: Literal['thread.run.step.delta'] = '\n    Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.\n    '


class ThreadRunStepCompleted(BaseModel):
    event: Literal['thread.run.step.completed'] = '\n    Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.\n    '


class ThreadRunStepFailed(BaseModel):
    event: Literal['thread.run.step.failed'] = '\n    Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.\n    '


class ThreadRunStepCancelled(BaseModel):
    event: Literal['thread.run.step.cancelled'] = '\n    Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.\n    '


class ThreadRunStepExpired(BaseModel):
    event: Literal['thread.run.step.expired'] = '\n    Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.\n    '


class ThreadMessageCreated(BaseModel):
    event: Literal['thread.message.created'] = '\n    Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.\n    '


class ThreadMessageInProgress(BaseModel):
    event: Literal['thread.message.in_progress'] = '\n    Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.\n    '


class ThreadMessageDelta(BaseModel):
    event: Literal['thread.message.delta'] = '\n    Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.\n    '


class ThreadMessageCompleted(BaseModel):
    event: Literal['thread.message.completed'] = '\n    Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.\n    '


class ThreadMessageIncomplete(BaseModel):
    event: Literal['thread.message.incomplete'] = '\n    Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.\n    '


class ErrorEvent(BaseModel):
    event: Literal['error'] = '\n    Occurs when an [error](https://platform.openai.com/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.\n    '

AssistantStreamEvent: TypeAlias = Annotated[(Union[(ThreadCreated, ThreadRunCreated, ThreadRunQueued, ThreadRunInProgress, ThreadRunRequiresAction, ThreadRunCompleted, ThreadRunIncomplete, ThreadRunFailed, ThreadRunCancelling, ThreadRunCancelled, ThreadRunExpired, ThreadRunStepCreated, ThreadRunStepInProgress, ThreadRunStepDelta, ThreadRunStepCompleted, ThreadRunStepFailed, ThreadRunStepCancelled, ThreadRunStepExpired, ThreadMessageCreated, ThreadMessageInProgress, ThreadMessageDelta, ThreadMessageCompleted, ThreadMessageIncomplete, ErrorEvent)], PropertyInfo(discriminator = 'event'))]
