# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_code_interpreter_call_code_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCodeInterpreterCallCodeDoneEvent']

class ResponseCodeInterpreterCallCodeDoneEvent(BaseModel):
    type: Literal['response.code_interpreter_call_code.done'] = 'Emitted when the code snippet is finalized by the code interpreter.'
