# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_reasoning_summary_part_added_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseReasoningSummaryPartAddedEvent',
    'Part']

class Part(BaseModel):
    type: Literal['summary_text'] = 'The summary part that was added.'


class ResponseReasoningSummaryPartAddedEvent(BaseModel):
    type: Literal['response.reasoning_summary_part.added'] = 'Emitted when a new reasoning summary part is added.'
