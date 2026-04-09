# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_shell_call_output_content.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'ResponseFunctionShellCallOutputContent',
    'Outcome',
    'OutcomeTimeout',
    'OutcomeExit']

class OutcomeTimeout(BaseModel):
    type: Literal['timeout'] = 'Indicates that the shell call exceeded its configured time limit.'


class OutcomeExit(BaseModel):
    type: Literal['exit'] = 'Indicates that the shell commands finished and returned an exit code.'

Outcome: TypeAlias = Annotated[(Union[(OutcomeTimeout, OutcomeExit)], PropertyInfo(discriminator = 'type'))]

class ResponseFunctionShellCallOutputContent(BaseModel):
    stdout: str = 'Captured stdout and stderr for a portion of a shell tool call output.'
