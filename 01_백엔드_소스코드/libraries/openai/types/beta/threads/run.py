# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from run_status import RunStatus
from assistant_tool import AssistantTool
from shared.metadata import Metadata
from assistant_tool_choice_option import AssistantToolChoiceOption
from assistant_response_format_option import AssistantResponseFormatOption
from required_action_function_tool_call import RequiredActionFunctionToolCall
__all__ = [
    'Run',
    'IncompleteDetails',
    'LastError',
    'RequiredAction',
    'RequiredActionSubmitToolOutputs',
    'TruncationStrategy',
    'Usage']

class IncompleteDetails(BaseModel):
    '''Details on why the run is incomplete.

    Will be `null` if the run is not incomplete.
    '''
    reason: Optional[Literal[('max_completion_tokens', 'max_prompt_tokens')]] = None


class LastError(BaseModel):
    message: str = 'The last error associated with this run. Will be `null` if there are no errors.'


class RequiredActionSubmitToolOutputs(BaseModel):
    tool_calls: List[RequiredActionFunctionToolCall] = 'Details on the tool outputs needed for this run to continue.'


class RequiredAction(BaseModel):
    type: Literal['submit_tool_outputs'] = 'Details on the action required to continue the run.\n\n    Will be `null` if no action is required.\n    '


class TruncationStrategy(BaseModel):
    type: Literal[('auto', 'last_messages')] = 'Controls for how a thread will be truncated prior to the run.\n\n    Use this to control the initial context window of the run.\n    '
    last_messages: Optional[int] = None


class Usage(BaseModel):
    total_tokens: int = 'Usage statistics related to the run.\n\n    This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).\n    '


class Run(BaseModel):
    assistant_id: str = '\n    Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).\n    '
    cancelled_at: Optional[int] = None
    created_at: int = None
    expires_at: Optional[int] = None
    failed_at: Optional[int] = None
    instructions: str = None
    last_error: Optional[LastError] = None
    max_completion_tokens: Optional[int] = None
    max_prompt_tokens: Optional[int] = None
    parallel_tool_calls: bool = None
    required_action: Optional[RequiredAction] = None
    response_format: Optional[AssistantResponseFormatOption] = None
    thread_id: str = None
    tools: List[AssistantTool] = None
    truncation_strategy: Optional[TruncationStrategy] = None
    usage: Optional[Usage] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
