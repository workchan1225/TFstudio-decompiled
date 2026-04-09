# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_failed_event.pyc (Python 3.11)

from typing_extensions import Literal
from response import Response
from _models import BaseModel
__all__ = [
    'ResponseFailedEvent']

class ResponseFailedEvent(BaseModel):
    type: Literal['response.failed'] = 'An event that is emitted when a response fails.'
