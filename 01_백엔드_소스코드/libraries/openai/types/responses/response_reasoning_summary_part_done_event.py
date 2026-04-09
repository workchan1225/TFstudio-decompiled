# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_reasoning_summary_part_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseReasoningSummaryPartDoneEvent',
    'Part']

class Part(BaseModel):
    type: Literal['summary_text'] = 'The completed summary part.'


class ResponseReasoningSummaryPartDoneEvent(BaseModel):
    type: Literal['response.reasoning_summary_part.done'] = 'Emitted when a reasoning summary part is completed.'
