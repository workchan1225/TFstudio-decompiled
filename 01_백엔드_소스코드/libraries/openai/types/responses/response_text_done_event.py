# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_text_done_event.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseTextDoneEvent',
    'Logprob',
    'LogprobTopLogprob']

class LogprobTopLogprob(BaseModel):
    token: Optional[str] = None
    logprob: Optional[float] = None


class Logprob(BaseModel):
    logprob: float = '\n    A logprob is the logarithmic probability that the model assigns to producing\n    a particular token at a given position in the sequence. Less-negative (higher)\n    logprob values indicate greater model confidence in that token choice.\n    '
    top_logprobs: Optional[List[LogprobTopLogprob]] = None


class ResponseTextDoneEvent(BaseModel):
    type: Literal['response.output_text.done'] = 'Emitted when text content is finalized.'
