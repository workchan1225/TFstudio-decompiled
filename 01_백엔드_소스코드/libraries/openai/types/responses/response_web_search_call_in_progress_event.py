# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_web_search_call_in_progress_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseWebSearchCallInProgressEvent']

class ResponseWebSearchCallInProgressEvent(BaseModel):
    type: Literal['response.web_search_call.in_progress'] = 'Emitted when a web search call is initiated.'
