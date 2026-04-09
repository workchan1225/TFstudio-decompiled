# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_code_interpreter_call_interpreting_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCodeInterpreterCallInterpretingEvent']

class ResponseCodeInterpreterCallInterpretingEvent(BaseModel):
    type: Literal['response.code_interpreter_call.interpreting'] = 'Emitted when the code interpreter is actively interpreting the code snippet.'
