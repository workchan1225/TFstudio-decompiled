# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_code_interpreter_call_in_progress_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCodeInterpreterCallInProgressEvent']

class ResponseCodeInterpreterCallInProgressEvent(BaseModel):
    type: Literal['response.code_interpreter_call.in_progress'] = 'Emitted when a code interpreter call is in progress.'
