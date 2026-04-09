# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_in_progress_event.pyc (Python 3.11)

from typing_extensions import Literal
from response import Response
from _models import BaseModel
__all__ = [
    'ResponseInProgressEvent']

class ResponseInProgressEvent(BaseModel):
    type: Literal['response.in_progress'] = 'Emitted when the response is in progress.'
