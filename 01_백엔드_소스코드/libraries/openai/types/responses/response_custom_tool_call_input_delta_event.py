# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_custom_tool_call_input_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCustomToolCallInputDeltaEvent']

class ResponseCustomToolCallInputDeltaEvent(BaseModel):
    type: Literal['response.custom_tool_call_input.delta'] = 'Event representing a delta (partial update) to the input of a custom tool call.'
