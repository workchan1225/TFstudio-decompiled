# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_refusal_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseRefusalDoneEvent']

class ResponseRefusalDoneEvent(BaseModel):
    type: Literal['response.refusal.done'] = 'Emitted when refusal text is finalized.'
