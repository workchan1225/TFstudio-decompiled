# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_code_interpreter_call_completed_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCodeInterpreterCallCompletedEvent']

class ResponseCodeInterpreterCallCompletedEvent(BaseModel):
    type: Literal['response.code_interpreter_call.completed'] = 'Emitted when the code interpreter call is completed.'
