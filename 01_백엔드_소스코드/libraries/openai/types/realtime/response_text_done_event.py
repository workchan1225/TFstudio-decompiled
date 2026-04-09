# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_text_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseTextDoneEvent']

class ResponseTextDoneEvent(BaseModel):
    type: Literal['response.output_text.done'] = 'Returned when the text value of an "output_text" content part is done streaming.\n\n    Also\n    emitted when a Response is interrupted, incomplete, or cancelled.\n    '
