# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: code_interpreter_tool_call_delta.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from code_interpreter_logs import CodeInterpreterLogs
from code_interpreter_output_image import CodeInterpreterOutputImage
__all__ = [
    'CodeInterpreterToolCallDelta',
    'CodeInterpreter',
    'CodeInterpreterOutput']
CodeInterpreterOutput: TypeAlias = Annotated[(Union[(CodeInterpreterLogs, CodeInterpreterOutputImage)], PropertyInfo(discriminator = 'type'))]

class CodeInterpreter(BaseModel):
    '''The Code Interpreter tool call definition.'''
    input: Optional[str] = None
    outputs: Optional[List[CodeInterpreterOutput]] = None


class CodeInterpreterToolCallDelta(BaseModel):
    type: Literal['code_interpreter'] = 'Details of the Code Interpreter tool call the run step was involved in.'
    id: Optional[str] = None
    code_interpreter: Optional[CodeInterpreter] = None
