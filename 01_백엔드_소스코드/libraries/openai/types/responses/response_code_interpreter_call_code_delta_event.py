# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_code_interpreter_call_code_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCodeInterpreterCallCodeDeltaEvent']

class ResponseCodeInterpreterCallCodeDeltaEvent(BaseModel):
    type: Literal['response.code_interpreter_call_code.delta'] = 'Emitted when a partial code snippet is streamed by the code interpreter.'
