# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_text_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseTextDeltaEvent']

class ResponseTextDeltaEvent(BaseModel):
    type: Literal['response.output_text.delta'] = 'Returned when the text value of an "output_text" content part is updated.'
