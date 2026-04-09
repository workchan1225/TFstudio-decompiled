# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_reasoning_summary_text_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseReasoningSummaryTextDoneEvent']

class ResponseReasoningSummaryTextDoneEvent(BaseModel):
    type: Literal['response.reasoning_summary_text.done'] = 'Emitted when a reasoning summary text is completed.'
