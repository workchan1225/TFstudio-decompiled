# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_completed_event.pyc (Python 3.11)

from typing_extensions import Literal
from response import Response
from _models import BaseModel
__all__ = [
    'ResponseCompletedEvent']

class ResponseCompletedEvent(BaseModel):
    type: Literal['response.completed'] = 'Emitted when the model response is complete.'
