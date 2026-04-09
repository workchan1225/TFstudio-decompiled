# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_reasoning_text_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseReasoningTextDeltaEvent']

class ResponseReasoningTextDeltaEvent(BaseModel):
    type: Literal['response.reasoning_text.delta'] = 'Emitted when a delta is added to a reasoning text.'
