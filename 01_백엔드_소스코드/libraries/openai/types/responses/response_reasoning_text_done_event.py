# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_reasoning_text_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseReasoningTextDoneEvent']

class ResponseReasoningTextDoneEvent(BaseModel):
    type: Literal['response.reasoning_text.done'] = 'Emitted when a reasoning text is completed.'
