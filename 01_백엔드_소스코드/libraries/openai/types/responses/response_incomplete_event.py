# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_incomplete_event.pyc (Python 3.11)

from typing_extensions import Literal
from response import Response
from _models import BaseModel
__all__ = [
    'ResponseIncompleteEvent']

class ResponseIncompleteEvent(BaseModel):
    type: Literal['response.incomplete'] = 'An event that is emitted when a response finishes as incomplete.'
