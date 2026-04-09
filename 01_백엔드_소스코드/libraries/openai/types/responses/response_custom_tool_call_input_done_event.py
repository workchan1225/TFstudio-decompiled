# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_custom_tool_call_input_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCustomToolCallInputDoneEvent']

class ResponseCustomToolCallInputDoneEvent(BaseModel):
    type: Literal['response.custom_tool_call_input.done'] = 'Event indicating that input for a custom tool call is complete.'
