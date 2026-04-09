# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_code_interpreter_tool_call.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'ResponseCodeInterpreterToolCall',
    'Output',
    'OutputLogs',
    'OutputImage']

class OutputLogs(BaseModel):
    type: Literal['logs'] = 'The logs output from the code interpreter.'


class OutputImage(BaseModel):
    url: str = 'The image output from the code interpreter.'

Output: TypeAlias = Annotated[(Union[(OutputLogs, OutputImage)], PropertyInfo(discriminator = 'type'))]

class ResponseCodeInterpreterToolCall(BaseModel):
    id: str = 'A tool call to run code.'
    container_id: str = None
    type: Literal['code_interpreter_call'] = None
