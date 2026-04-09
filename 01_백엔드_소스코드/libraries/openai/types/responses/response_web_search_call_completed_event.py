# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_web_search_call_completed_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseWebSearchCallCompletedEvent']

class ResponseWebSearchCallCompletedEvent(BaseModel):
    type: Literal['response.web_search_call.completed'] = 'Emitted when a web search call is completed.'
