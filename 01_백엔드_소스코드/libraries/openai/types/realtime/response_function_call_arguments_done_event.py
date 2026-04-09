# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_call_arguments_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFunctionCallArgumentsDoneEvent']

class ResponseFunctionCallArgumentsDoneEvent(BaseModel):
    type: Literal['response.function_call_arguments.done'] = '\n    Returned when the model-generated function call arguments are done streaming.\n    Also emitted when a Response is interrupted, incomplete, or cancelled.\n    '
