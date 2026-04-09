# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_shell_tool_call_output.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'ResponseFunctionShellToolCallOutput',
    'Output',
    'OutputOutcome',
    'OutputOutcomeTimeout',
    'OutputOutcomeExit']

class OutputOutcomeTimeout(BaseModel):
    type: Literal['timeout'] = 'Indicates that the shell call exceeded its configured time limit.'


class OutputOutcomeExit(BaseModel):
    type: Literal['exit'] = 'Indicates that the shell commands finished and returned an exit code.'

OutputOutcome: TypeAlias = Annotated[(Union[(OutputOutcomeTimeout, OutputOutcomeExit)], PropertyInfo(discriminator = 'type'))]

class Output(BaseModel):
    stdout: str = 'The content of a shell call output.'
    created_by: Optional[str] = None


class ResponseFunctionShellToolCallOutput(BaseModel):
    call_id: str = 'The output of a shell tool call.'
    type: Literal['shell_call_output'] = None
    created_by: Optional[str] = None
