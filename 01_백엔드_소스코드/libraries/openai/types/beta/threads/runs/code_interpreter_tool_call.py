# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: code_interpreter_tool_call.pyc (Python 3.11)

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'CodeInterpreterToolCall',
    'CodeInterpreter',
    'CodeInterpreterOutput',
    'CodeInterpreterOutputLogs',
    'CodeInterpreterOutputImage',
    'CodeInterpreterOutputImageImage']

class CodeInterpreterOutputLogs(BaseModel):
    type: Literal['logs'] = 'Text output from the Code Interpreter tool call as part of a run step.'


class CodeInterpreterOutputImageImage(BaseModel):
    file_id: str = 'CodeInterpreterOutputImageImage'


class CodeInterpreterOutputImage(BaseModel):
    type: Literal['image'] = 'CodeInterpreterOutputImage'

CodeInterpreterOutput: TypeAlias = Annotated[(Union[(CodeInterpreterOutputLogs, CodeInterpreterOutputImage)], PropertyInfo(discriminator = 'type'))]

class CodeInterpreter(BaseModel):
    outputs: List[CodeInterpreterOutput] = 'The Code Interpreter tool call definition.'


class CodeInterpreterToolCall(BaseModel):
    type: Literal['code_interpreter'] = 'Details of the Code Interpreter tool call the run step was involved in.'
